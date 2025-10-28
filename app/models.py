from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator


# Create your models here.

class CustomFaculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, default='faculty')
    phone = models.CharField(max_length=15, blank=True)
    department = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.user.username} ({self.title})"
    
    class Meta:
        db_table = 'CustomFaculty'

class CustomStudent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, default='student')
    phone_number = models.CharField(max_length=15, null=True)
    student_image = models.ImageField(upload_to='profile/')
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=10, null=True)
    course = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'CustomStudent'

class academic_year(models.Model):
    academic_years = models.CharField(max_length=10, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    additional_notes = models.TextField(null=True)

    class Meta:
        db_table = 'academic_year'

class Course(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, verbose_name="Course Title")
    title_code = models.CharField(max_length=20, verbose_name="Course Code")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    academic_year = models.CharField(max_length=10, null=True)
    semester = models.CharField(max_length=10, null=True)
    unit = models.IntegerField(null=True)
    unit_title = models.CharField(max_length=20, null=True)
    description = models.TextField(null=True)
    resources = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=50, null=True)
    

    class Meta:
        ordering = ['title_code']
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        db_table = 'Course'

    def __str__(self):
        return f"{self.code} - {self.title}"
    
class upload_units(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = RichTextField(null=True, blank=True)
    pdf = models.FileField(upload_to='pdf_files', validators=[FileExtensionValidator(allowed_extensions=['pdf'])],null=True)

    class Meta:
        db_table = 'upload_units'

class previous_question_papers(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    question_paper_subject = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    pdf = models.FileField(upload_to='previous_question_papers', validators=[FileExtensionValidator(allowed_extensions=['pdf'])],null=True)
    academic_year = models.CharField(max_length=20, null=True)
    semmester = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'previous_question_papers'

class college_event_model(models.Model):
    event_name = models.CharField(max_length=50, null=True)
    event_date = models.DateField(null=True)
    event_time = models.TimeField(null=True)
    category = models.CharField(max_length=50, null=True)
    descritpion = models.TextField(null=True)
    organizer_name = models.CharField(max_length=50, null=True)
    contact_mail = models.EmailField(null=True)

    class Meta:
        db_table = 'college_event_model'

    



