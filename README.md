# TKR VIDYASAARATHI

## ABSTRACT

The **College Management System** is a role-based web application developed to streamline and digitize core academic workflows for educational institutions. Built using **Django** as the backend framework with **HTML, CSS, and JavaScript** on the frontend, the system provides tailored functionalities for three main roles: **Admin, Faculty, and Students**. The Admin module enables secure login and allows management of academic years, semesters, faculties, and user accounts. The Faculty module supports uploading and managing academic resources including syllabus content, course materials, previous year question papers in PDF format, and important questions. The Student module allows users to register via email authentication and access all relevant academic content such as syllabus, study materials, and exam-related resources. This centralized system minimizes manual workload and ensures secure, efficient, and user-friendly access to learning content, promoting better communication and improving academic planning.

**Keywords:** College Management System, Django, Role-Based Access, Syllabus Management, Academic Resources, E-Learning, Web Application, Python, Faculty Portal, Student Dashboard.

---

## 1. INTRODUCTION

### 1.1 Motivation

The motivation is to address the inefficiencies and challenges of traditional academic operations (manual record-keeping, paper-based distribution, and fragmented communication). The system aims to provide a centralized, role-based platform that streamlines academic workflows, improves collaboration, and enhances access to educational resources, offering a scalable solution that adapts to the evolving needs of educational institutions.

### 1.4 Proposed System

The proposed system is a centralized, web-based platform built with **Django** (backend) and **HTML, CSS, and JavaScript** (frontend). It implements **Role-Based Access Control (RBAC)** for Admin, Faculty, and Student users, ensuring secure and relevant access to features. Key automations include managing academic years, semesters, faculty records, and providing streamlined communication for timely updates.

---

## 2. SYSTEM ARCHITECTURE

The project follows a modular, role-based design implemented using **Django's Model-View-Template (MVT) architecture**.

### Architecture Diagram

<img width="940" height="612" alt="image" src="https://github.com/user-attachments/assets/1a006111-3a20-486a-952c-610ee75cd711" />


---

## 3. IMPLEMENTATION & KEY FUNCTIONS

The system is divided into three main functional modules: Admin, Faculty, and Student.

### 3.1 Admin Module

* **Login:** Secure access to the admin dashboard.
* **Add/Manage:** Academic Years, Semesters, Faculties, and User accounts.
* **View Users:** Monitor registered student accounts.
* **Logout:** Securely exit the admin panel.

### 3.2 Faculty Module

* **Login:** Authenticated access to the faculty panel.
* **Add/Manage Syllabus:** Upload or update syllabus content (title, description, topic, video).
* **Add/Manage Course Material:** Upload notes, presentations, and reference documents.
* **Add/Manage Previous Question Papers (PDF):** Upload and manage past exam papers.
* **Add/Manage Important Questions:** Provide key questions for exams or revision.
* **View Users:** View student details for academic coordination.
* **Logout:** End session securely.

### 3.3 Student/User Module

* **Register (E-mail Auth):** Sign up with email verification.
* **Login:** Access the student dashboard after authentication.
* **Select Branch/Year:** Choose academic stream and set current year for filtered content.
* **View Academic Content:** Access Syllabus (including topics and videos), Course Material, Previous Question Papers (PDF), and Important Questions.
* **Logout:** Securely log out of the student portal.

### 3.4 Method of Implementation

* **Backend Framework:** Django (Python 3.6+).
* **Frontend Technologies:** HTML, CSS, JavaScript, **Bootstrap**.
* **Database:** **SQLite** (integrated through Django ORM).
* **IDE Used:** Visual Studio Code.
* **Deployment:** Windows 10 (Development OS).

---

## 4. USAGE & CREDENTIALS

* **Admin Login:**
    * **Username:** `admin`
    * **Password:** `admin`
* **Faculty Login:** Accounts must be created by the Admin.
* **Student Login:** Students can register via the registration page.

---

## 5. OUTPUT SCREENS (Screenshots)

This section details the primary user interfaces for each role.

### Screen 1: Home Page
**Description:** The initial landing page of the website.
<img width="936" height="438" alt="image" src="https://github.com/user-attachments/assets/d75055a8-65ff-404c-afc2-147f2179b390" />

### Screen 2: Student Register Page
**Description:** Allows students to sign up with their name, email, and password.
<img width="588" height="271" alt="image" src="https://github.com/user-attachments/assets/c47025f3-85d4-4021-8461-4b7745bd5d01" />

### Screen 3: Student Login
**Description:** Allows students to access their personalized dashboard.
<img width="600" height="279" alt="image" src="https://github.com/user-attachments/assets/a58c1cd0-4b1c-4300-861a-8ac0f3c509a9" />

### Screen 4: Student Dashboard
**Description:** Provides students with easy access to academic resources, organized by branch and year.
<img width="587" height="274" alt="image" src="https://github.com/user-attachments/assets/8b1f0a44-e8a9-4c0a-9933-18c70e219ba0" />

### Screen 5: View Profile
**Description:** Students can view their personal and academic information.
<img width="580" height="277" alt="image" src="https://github.com/user-attachments/assets/05f6067f-9975-4c2e-a289-3a410a36d496" />

### Screen 6: View Courses
**Description:** Students can browse and access the list of courses.
<img width="587" height="274" alt="image" src="https://github.com/user-attachments/assets/c8ef3613-f91d-4ed4-9ac3-f31881269477" />

### Screen 7: View Syllabus
**Description:** Students can access and download the syllabus for their courses.
<img width="864" height="435" alt="image" src="https://github.com/user-attachments/assets/352b5236-52e8-4cf6-90ef-26cbda22279a" />

### Screen 8: Unit Preview
**Description:** Allows students to preview course units, learning objectives, and associated resources.
<img width="566" height="271" alt="image" src="https://github.com/user-attachments/assets/6fc030ce-2e4d-4818-9d9f-ecb2330810a3" />
<img width="601" height="181" alt="image" src="https://github.com/user-attachments/assets/4e923fa1-b6fe-44fb-b65f-dc29aa204af6" />

### Screen 9: Faculty Login
**Description:** Faculty members securely log in to access their dashboard.
<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/41820f3a-0144-4dfc-aa16-74bd5d7de2a5" />

### Screen 10: Faculty Dashboard
**Description:** Allows faculty to manage and upload course materials, syllabi, and academic resources.
<img width="586" height="271" alt="image" src="https://github.com/user-attachments/assets/f8be617f-0183-4fc5-8496-dd852b9a1db6" />

### Screen 11: View Syllabus
**Description:** Faculty members can upload, update, and manage the syllabus for their courses, including topics, descriptions, and related resources for students.
<img width="600" height="279" alt="image" src="https://github.com/user-attachments/assets/805fb6c3-4c1e-4eec-b087-250ee6c55781" />

### Screen 12: Add Syllabus
**Description:** Faculty can upload new syllabi providing details such as course title, description, and topics.
<img width="566" height="270" alt="image" src="https://github.com/user-attachments/assets/425be66a-ed59-446e-8d64-b696b684c5a9" />

### Screen 13: Add Topics and PDFs
**Description:** Faculty members can add individual topics to the syllabus and upload related PDFs.
<img width="554" height="278" alt="image" src="https://github.com/user-attachments/assets/b00d7724-bd12-4afe-b5b0-a7a73d46d6dc" />

### Screen 14: Add Question Papers
**Description:** Faculty can upload previous year question papers in PDF format.
<img width="587" height="266" alt="image" src="https://github.com/user-attachments/assets/7339c36f-705a-46ac-b24b-50d881caa8ed" />

### Screen 15: View Students
**Description:** Faculty can view a list of registered students, including their details such as name, academic year, and branch, to manage and track their academic progress.
<img width="601" height="271" alt="image" src="https://github.com/user-attachments/assets/70b60a65-087d-48ba-b7bc-bd876971d05b" />

### Screen 16: Admin Login Page
**Description:** Administrators securely log in to access the admin dashboard.
<img width="601" height="279" alt="image" src="https://github.com/user-attachments/assets/0a367e06-42e6-4ea3-824f-0d55671b9e02" />

### Screen 17: Admin Dashboard
**Description:** Administrators can manage academic structures such as years, semesters, and faculty records, as well as monitor and control user accounts (students and faculty), ensuring efficient academic operations.
<img width="601" height="277" alt="image" src="https://github.com/user-attachments/assets/56ffc88c-9d39-4958-b09b-1d5b5d0cc9b1" />

### Screen 18: Add Faculty
**Description:** Administrators can add new faculty members by entering their details.
<img width="587" height="272" alt="image" src="https://github.com/user-attachments/assets/e2d6fa70-a7a7-480f-8d37-5f2e1d1f2101" />

### Screen 19: Add Academic Year
**Description:** Administrators define and add new academic years, specifying start/end dates and semesters.
<img width="601" height="278" alt="image" src="https://github.com/user-attachments/assets/8e656ca4-388f-4e2c-812a-27d2490deffd" />

### Screen 20: Add College Events
**Description:** Administrators can create and manage college events (name, date, time, description).
<img width="587" height="271" alt="image" src="https://github.com/user-attachments/assets/efe7d6fc-6379-4a06-930d-89036b3ff446" />

### Screen 21: View Students
**Description:** Administrators can view the list of registered students, along with their details such as name, academic year, branch, and enrollment status, to manage and track student progress.
<img width="601" height="277" alt="image" src="https://github.com/user-attachments/assets/4a28a45a-b113-4248-8f4f-6c7cdba60420" />

### Screen 22: View Faculty
**Description:** Administrators can view the list of registered faculty members, along with their details such as name, department, courses taught, and contact information, to manage faculty records effectively.
<img width="587" height="272" alt="image" src="https://github.com/user-attachments/assets/3edfc638-9ef0-4bd2-8bdb-cb3d5bdea38b" />


### Screen 23: View Events
**Description:** Administrators can view a list of upcoming and past college events, including details like event name, date, time, and description, to track and manage event schedules.
<img width="587" height="272" alt="image" src="https://github.com/user-attachments/assets/bf469957-07b1-4ee5-8911-cf54ae3e7f33" />
---

## 6. CONCLUSION & FUTURE ENHANCEMENT

### Conclusion

The College Management System provides a comprehensive, efficient, and scalable solution, successfully integrating all modules and meeting all functional and non-functional requirements. The system performed efficiently with secure login, data integrity, and an intuitive interface, satisfying all user acceptance criteria.

### Future Enhancement

Future enhancements include integrating an **online examination system** for automatic grading, **performance tracking and analytics** (dashboards for grades/attendance), and deeper **LMS integration**. Additional features could be a **real-time notification system**, a dedicated **mobile application**, an **AI-powered chatbot** for queries, and advanced attendance tracking.

---

## 7. PROJECT AUTHORS

This project was submitted in partial fulfillment of the requirements for the award of the degree of **Bachelor of Technology in CSE (Data Science)**.

* Avula Uday Kiran
* G. Akhiranandan
* B. Gideon Joy
* A. Mahad

Under the guidance of **J. Srividya, Asst. Professor**.
