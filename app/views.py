from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from . models import *
import random
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from django.core.files.storage import default_storage
from django.contrib.auth import get_user_model
from django.core.files import File
from django.core.paginator import Paginator
import os
from . forms import *
from django.core.exceptions import ValidationError
from datetime import datetime
import re
from django.http import Http404

# Create your views here.

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@tkrcet\.com$'
    if re.match(pattern, email):
        return True
    else:
        return False

def index(request):
    events = college_event_model.objects.all().order_by('-id')
    return render(request, 'index.html', {'events':events})

def adminDashboard(request):
    rec_stu_reg = CustomStudent.objects.filter(user_type='student') \
                                   .order_by('-id')[:5]
    total_stu = CustomStudent.objects.filter(user_type='student').count()
    total_fac = CustomFaculty.objects.filter(user_type='faculty').count()
    total_courses = CustomStudent.objects.values('course').distinct().count()
    return render(request, 'adminDashboard.html', {'rec_stu_reg':rec_stu_reg, 'total_stu':total_stu, 'total_fac':total_fac, 'total_courses':total_courses})

def admin_login(request):
    if request.method == 'POST':
        managerName = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=managerName, password=password)

        if user is not None:
            if user.is_superuser:
                request.session['login'] = 'admin'
                login(request, user)
                return redirect('adminDashboard')
    return render(request, 'admin_login.html')

def logout_user(request):
    logout(request)
    request.session.flush()
    return redirect('index')


def student_reg(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        course = request.POST.get('course')
        terms = request.POST.get('terms')
        student_image = request.FILES.get('studentImage')

        # Basic validations
        if not validate_email(email):
            print('invalid email')
            messages.error(request, 'enter valid email')
            return redirect('student_reg')
             
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('student_reg')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('student_reg')
        
        if not student_image:
            messages.error(request, 'Please upload your student image.')
            return redirect('student_reg')

        # Temporarily save the uploaded image file
        image_path = f"temp_images/{student_image.name}"
        saved_image_path = default_storage.save(image_path, student_image)

        # Store all non-binary data in session
        otp = str(random.randint(100000, 999999))
        request.session['student_reg_data'] = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': phone,
            'password': password,
            'dob': dob,
            'gender': gender,
            'course': course,
        }
        request.session['otp'] = otp
        request.session['student_image_path'] = saved_image_path

        # Send OTP
        try:
            send_mail(
                'Your Student Registration OTP',
                f'Your OTP for registration is: {otp}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )
            messages.success(request, 'OTP sent to your email.')
            return redirect('verify_student_otp')
        except Exception as e:
            print("Email sending failed:", e)
            messages.error(request, 'Failed to send OTP. Please try again.')
            return redirect('student_reg')
    
    return render(request, 'student_reg.html')

def student_log(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        print('-----------------', user)
        if user and user.customstudent.user_type == 'student':
            login(request, user)
            request.session['login'] = 'student'
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('student_log')
    return render(request, 'student_login.html')

def faculty_log(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        print('-----------------', user)
        if user and user.is_staff:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('faculty_log')
    return render(request, 'faculty_login.html')

def add_faculty(request):
    if request.method == 'POST':
        # Built-in User model fields
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = email.split('@')[0]

        # CustomFaculty model fields
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        title = request.POST.get('title')
        subject = request.POST.get('subject')

        # Create user
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff = True
        )

        # Create faculty profile
        CustomFaculty.objects.create(
            user=user,
            phone=phone,
            department=department,
            title=title,
            subject=subject
        )

        messages.success(request, "Faculty account created successfully.")
        return redirect('adminDashboard')  # Redirect to login page
    return render(request, 'add_faculty.html')

def dashboard(request):
    login = request.session.get('login')
    events = college_event_model.objects.all().order_by('-id')
    return render(request, 'dashboard.html', {'login':login, 'events':events})


User = get_user_model()

def verify_student_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        session_otp = request.session.get('otp')
        data = request.session.get('student_reg_data')
        image_path = request.session.get('student_image_path')

        if not data or not session_otp:
            messages.error(request, 'Session expired. Please register again.')
            return redirect('student_reg')

        if entered_otp != session_otp:
            messages.error(request, 'Invalid OTP')
            return redirect('verify_student_otp')

        if not image_path or not default_storage.exists(image_path):
            messages.error(request, 'Image not found. Please re-register.')
            return redirect('student_reg')

        try:
            # Create user
            user = User.objects.create_user(
                username=data['email'],
                email=data['email'],
                password=data['password'],
                first_name=data['first_name'],
                last_name=data['last_name']
            )

            # Read saved image
            with default_storage.open(image_path, 'rb') as f:
                image_file = File(f, name=os.path.basename(image_path))

                # Create student record with correct field names
                CustomStudent.objects.create(
                    user=user,
                    phone_number=data.get('phone'),  # Correct field name
                    dob=data.get('dob'),             # Must match model field
                    gender=data.get('gender'),
                    course=data.get('course'),
                    student_image=image_file
                )

            # Clean session and temp file
            request.session.pop('student_reg_data', None)
            request.session.pop('otp', None)
            request.session.pop('student_image_path', None)
            default_storage.delete(image_path)

            messages.success(request, 'Account created successfully.')
            return redirect('student_log')

        except Exception as e:
            import traceback
            traceback.print_exc()
            messages.error(request, f'Registration failed: {str(e)}')
            return redirect('student_reg')

    return render(request, 'verify_otp.html')

@login_required(login_url='student_log')
def view_profile_student(request):
    login = request.session.get('login')
    user = request.user

    try:
        student = CustomStudent.objects.get(user=user)
        image_url = student.student_image.url if student.student_image else None
    except CustomStudent.DoesNotExist:
        student = None
        image_url = None

    return render(request, 'student_view_profile.html', {
        'login': login,
        'get_user': user,
        'student': student,
        'image_url': image_url
    })

@login_required(login_url='faculty_log')
def add_syllabus(request):
    user = request.user
    faculty = CustomFaculty.objects.get(user=user)
    get_years = academic_year.objects.all()
    if request.method == 'POST':
        course_title = request.POST.get('course_title')
        course_code = request.POST.get('course_code')
        academic_year_ = request.POST.get('academic_year')
        semester = request.POST.get('semester')

        units = []
        i = 1

        while f'unit_title_{i}' in request.POST:
            units.append({
                'title': request.POST.get(f'unit_title_{i}'),
                'description': request.POST.get(f'unit_description_{i}'),
                'resources': request.POST.get(f'unit_resources_{i}')
            })
            i += 1

        for index,unit in enumerate(units):
            Course.objects.create(
                uploaded_by=request.user,
                title=course_title,
                academic_year=academic_year_,
                semester=semester,
                unit=index+1,
                unit_title=unit['title'],
                description=unit['description'],
                resources=unit['resources'],
                title_code = course_code,
                subject=faculty.subject
            )
        messages.success(request, 'Course syllabus added successfully')
        return redirect('add_syllabus')

    return render(request, 'add_syllabus.html', {'get_years':get_years})

@login_required(login_url='admin_login')
def add_academic_year(request):
    get_years = academic_year.objects.all()
    if request.method == 'POST':
        yearName = request.POST.get('yearName')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        notes = request.POST.get('notes')

        academic_year.objects.create(
            academic_years=yearName,
            start_date=startDate,
            end_date=endDate,
            additional_notes=notes,
        )

        messages.success(request, 'Accademic year added successfully')
        return redirect('add_academic_year')
    
    return render(request, 'add_academic_year.html', {'get_years':get_years})

@login_required(login_url='faculty_log')
def view_course(request):
    get_years = academic_year.objects.all()
    get_units = Course.objects.filter(uploaded_by=request.user).order_by('id') 

    paginator = Paginator(get_units, 6)
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)  

    return render(request, 'view_all_syllabus.html', {
        'page_obj': page_obj,
        'get_years':get_years,
        'get_units':get_units
    })

@login_required(login_url='faculty_log')
def remove_units(request, id):
    get_unit = Course.objects.get(id=id)
    get_unit.delete()
    messages.success(request, 'Unit removed successfully')
    return redirect('view_course')

@login_required(login_url='faculty_log')
def add_unit_content(request, id):

    course = get_object_or_404(Course, id=id)

    check_unit = upload_units.objects.filter(course_id=id).exists()
    
    if check_unit:
        messages.error(request, 'Your are already added unit content')
        return redirect('view_course')

    if course.uploaded_by != request.user:
        messages.error(request, "You are not authorized to add units to this course.")
        return redirect('view_course') 

    if request.method == 'POST':
        form = UploadUnitsForm(request.POST, request.FILES)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.course_id = course 
            unit.save()
            messages.success(request, "Unit content uploaded successfully.")
            return redirect('view_course')  
    else:
        form = UploadUnitsForm()

    return render(request, 'add_unit_content.html', {'form': form, 'course': course, 'id':id})

@login_required(login_url='faculty_log')
def preview_unit(request, unit_id):
    try:
        unit = get_object_or_404(upload_units, course_id=unit_id)
    except Http404:
        return render(request, 'not_found.html')

    if unit.course_id.uploaded_by != request.user:
        messages.error(request, "You are not authorized to preview this unit.")
        return redirect('view_course') 
    pdf_url = unit.pdf.url if unit.pdf else None
    print('fdssddf',pdf_url)
    return render(request, 'unit_preview.html', {'unit': unit, 'pdf_url':pdf_url})

@login_required(login_url='faculty_log')
def add_question_papers(request):
    get_faculty_subjects = Course.objects.filter(
        uploaded_by=request.user
    ).values('title', 'title_code', 'academic_year', 'semester').distinct()
    return render(request, 'view_faculty_subject.html', {'get_faculty_subjects':get_faculty_subjects})


@login_required(login_url='faculty_log')
def add_question_papers_1(request, title):
    get_academic_year = academic_year.objects.all()
    get_subject_details = Course.objects.filter(title=title).first()
    if request.method == 'POST':

        title = request.POST.get('title')
        year = request.POST.get('year')
        semester = request.POST.get('semester')
        pdf = request.FILES.get('pdf')
        
        
        if pdf.size > 20 * 1024 * 1024:  # 10MB
            messages.error(request, 'File size exceeds the maximum limit of 10MB.')
            return render('add_question_papers')

        if not pdf.name.endswith('.pdf'):
            messages.error(request, 'Invalid file type. Only PDF files are allowed.')
            return render('add_question_papers')

        try:

            question_paper = previous_question_papers(
                uploaded_by=request.user,
                question_paper_subject=get_subject_details,
                pdf=pdf,
                academic_year=get_subject_details.academic_year,
                semmester=get_subject_details.semester
            )
            question_paper.save()
            messages.success(request, 'Question papers added successfully')
            return redirect('add_question_papers')
            
        except ValidationError as e:
            messages.error(request, f'{str(e)}')
            return redirect('add_question_papers')
    return render(request, 'add_pdf.html', {'title':title, 'years':get_academic_year})

@login_required(login_url='faculty_log')
def view_students(request):
    student_list = User.objects.filter(customstudent__user_type='student')
    if request.method == 'POST':
        query = request.POST.get('search_query')
        student_list = User.objects.filter(customstudent__user_type='student', first_name__icontains=query)

        paginator = Paginator(student_list, 6)  
        page_number = request.GET.get('page')  
        page_obj = paginator.get_page(page_number)
        return render(request, 'view_students.html', {'page_obj':page_obj})

    paginator = Paginator(student_list, 6)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)
    return render(request, 'view_students.html', {'page_obj':page_obj})

@login_required(login_url='student_log')
def view_course_student(request):
    login = request.session.get('login')
    get_student = request.user
    get_courses = CustomFaculty.objects.filter(department__icontains=get_student.customstudent.course)
    print(get_courses)
    get_academic_years = list(Course.objects.values_list('academic_year', flat=True))
    distinct_academic_years = list(set(get_academic_years))
    print('-----------', get_academic_years)
    get_syllabus = []

    if request.method == 'POST':
        year = request.POST.get('academic_year')
        sem = request.POST.get('semester')

        distinct_uploaded_by_ids = Course.objects.filter(
            academic_year=year, 
            semester=sem
        ).values('uploaded_by').distinct()

        uploaded_by_ids = [entry['uploaded_by'] for entry in distinct_uploaded_by_ids]

        print('yyyyyyyyyyyyyyyyyyy', uploaded_by_ids)

        faculty = CustomFaculty.objects.filter(user__in=uploaded_by_ids)
        print('ddddddddddddddd', faculty)

        paginator = Paginator(faculty, 6)  
        page_number = request.GET.get('page')  
        page_obj = paginator.get_page(page_number)

        return render(request, 'view_course_student.html', {'page_obj': page_obj, 'get_syllabus': get_syllabus, 'get_academic_years':distinct_academic_years, 'login':login})

    for course in get_courses:
        course_syllabus = Course.objects.filter(uploaded_by=course.user)
        for units in course_syllabus:
            get_syllabus.append(units)

    paginator = Paginator(get_courses, 6)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)

    return render(request, 'view_course_student.html', {'page_obj': page_obj, 'get_academic_years':distinct_academic_years, 'login':login})

@login_required(login_url='student_log')
def view_syllabus_student(request, user_id, subject):
    login = request.session.get('login')
    get_units = Course.objects.filter(uploaded_by=user_id, subject__icontains=subject).order_by('id') 

    paginator = Paginator(get_units, 6)
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number) 

    return render(request, 'view_syllabus_student.html', {'page_obj':page_obj, 'login':login}) 

@login_required(login_url='faculty_log')
def preview_unit_student(request, unit_id):
    login = request.session.get('login')
    try:
        unit = get_object_or_404(upload_units, course_id=unit_id)
    except Http404:
        return render(request, 'not_found.html')
    get_pdfs = previous_question_papers.objects.filter(question_paper_subject=unit_id)
    pdf_url = unit.pdf.url if unit.pdf else None
    print('fdssddf',pdf_url)
    return render(request, 'preview_unit_student.html', {'unit': unit, 'pdf_url':pdf_url, 'login':login, 'get_pdfs':get_pdfs})

@login_required(login_url='admin_login')
def view_all_students(request):
    students_list = CustomStudent.objects.all()
    paginator = Paginator(students_list, 10) 
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'view_all_student.html', {
        'students': page_obj,
        'page_obj': page_obj,
        'is_paginated': paginator.num_pages > 1
    })

@login_required(login_url='admin_login')
def view_all_faculty(request):
    faculty_list = CustomFaculty.objects.all()
    paginator = Paginator(faculty_list, 10) 
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'view_all_faculty.html', {
        'faculty': page_obj,
        'page_obj': page_obj,
        'is_paginated': paginator.num_pages > 1
    })

@login_required(login_url='admin_login')
def add_events(request):
    if request.method == "POST":
        eventName = request.POST.get('eventName')
        eventDate = request.POST.get('eventDate')
        eventTime = request.POST.get('eventTime')
        eventCategory = request.POST.get('eventCategory')
        eventDescription = request.POST.get('eventDescription')
        organizerName = request.POST.get('organizerName')
        contactEmail = request.POST.get('contactEmail')

        college_event_model.objects.create(
            event_name=eventName,
            event_date=eventDate,
            event_time=eventTime,
            category=eventCategory,
            descritpion=eventDescription,
            organizer_name=organizerName,
            contact_mail=contactEmail
        )

        messages.success(request, 'Event added successfully')
        return redirect('add_events')
    return render(request, 'add_events.html')

@login_required(login_url='admin_login')
def view_events(request):
    events_list = college_event_model.objects.order_by('event_date')
    paginator = Paginator(events_list, 6)  # 6 events per page (2 rows of 3 cards)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'view_events.html', {'page_obj': page_obj})

@login_required(login_url='admin_login')
def remove_event(request, id):
    get_event =  college_event_model.objects.get(id=id)
    get_event.delete()
    messages.success(request, 'Event removed successfully')
    return redirect('view_events')

def forgot_pass(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            otp = random.randint(000000, 999999)
            request.session['otp'] = otp
            request.session['email'] = email
            subject = 'Reset password OTP'
            message = f'''
                       You'r reset password OTP
                       OTP:{otp}
                       Don't share to any one

                       PayGuard Team
                        '''
            from_mail = settings.EMAIL_HOST_USER
            send_mail(subject, message, from_mail, [email], fail_silently=False )

            return redirect('reset_pass')
        else:
            messages.error(request, 'User mail not exists')
            return redirect('index')
    return render(request, 'forgot_pass.html')

def reset_pass(request):
    if request.method == 'POST':

        otp1 = request.POST.get('otp1')
        otp2 = request.POST.get('otp2')
        otp3 = request.POST.get('otp3')
        otp4 = request.POST.get('otp4')
        otp5 = request.POST.get('otp5')
        otp6 = request.POST.get('otp6')

        entered_otp = str(otp1+otp2+otp3+otp4+otp5+otp6)
        session_otp = str(request.session.get('otp', ''))
        email = request.session.get('email', '')
        
        if entered_otp == session_otp:
            return redirect('setPass')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
            return redirect('reset_pass')
    
    return render(request, 'reset_pass.html')

def setPass(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        get_email = request.session.get('email')
        if new_password == confirm_password:
            user = User.objects.get(email=get_email)
            user.set_password(new_password)
            user.save()
            request.session.pop('otp', None)
            request.session.pop('email', None)
            messages.success(request, 'Password changed successfully')
            return redirect('setPass')
        else:
            messages.success(request, 'Password not matched')
    return render(request, 'setPass.html')

@login_required(login_url='admin_login')
def delete_student(request, id):
    get_student = User.objects.get(id=id)
    get_student.delete()
    messages.success(request, 'Student removed successfully')

    return redirect('view_all_students')

@login_required(login_url='admin_login')
def delete_faculty(request, id):
    get_faculty = User.objects.get(id=id)
    get_faculty.delete()
    messages.success(request, 'Faculty removed successfully')

    return redirect('view_all_faculty')

@login_required(login_url='admin_login')
def delete_academic_year(request, id):
    get_year = academic_year.objects.get(id=id)
    get_year.delete()

    messages.success(request, 'Academic year removed successfully')
    return redirect('add_academic_year')






