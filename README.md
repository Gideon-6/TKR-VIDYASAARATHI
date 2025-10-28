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

| Screen No. | Description | Image |
| :---: | :--- | :---: |
| **1** | **Home Page:** The initial landing page of the website. |  |
<img width="940" height="440" alt="image" src="https://github.com/user-attachments/assets/d24f3899-1122-47b3-bd95-144ab6d0d9ff" />
| **2** | **Student Register Page:** Allows students to sign up with their name, email, and password. |  |
<img width="940" height="434" alt="image" src="https://github.com/user-attachments/assets/84831eec-6a1c-48fa-85ff-fcc418bc8c52" />
| **3** | **Student Login:** Allows students to access their personalized dashboard. |  |
<img width="940" height="433" alt="image" src="https://github.com/user-attachments/assets/a792680f-8932-4928-b9ca-5f788145d34a" />
| **4** | **Student Dashboard:** Provides students with easy access to academic resources, organized by branch and year. |  |
<img width="940" height="438" alt="image" src="https://github.com/user-attachments/assets/85ef0758-c25e-4a9b-b78f-69718a3233ed" />
| **5** | **View Profile:** Students can view their personal and academic information. |  |
<img width="940" height="437" alt="image" src="https://github.com/user-attachments/assets/9dfefdc2-e3a4-4edc-b7c5-b74a6ab9b1d9" />
| **6** | **View Courses:** Students can browse and access the list of courses. |  |
<img width="940" height="434" alt="image" src="https://github.com/user-attachments/assets/35980c0a-b919-453b-91be-931d1a9730e1" />
| **7** | **View Syllabus:** Students can access and download the syllabus for their courses. |  |
| **8** | **Unit Preview:** Allows students to preview course units, learning objectives, and associated resources. |  |
<img width="940" height="434" alt="image" src="https://github.com/user-attachments/assets/8f3fe084-1105-47c5-98d3-5d35cedd253a" />
<img width="940" height="435" alt="image" src="https://github.com/user-attachments/assets/13fc3b2f-6a7d-4fa9-ad36-3777b83fb22e" />
| **9** | **Faculty Login:** Faculty members securely log in to access their dashboard. |  |
<img width="940" height="469" alt="image" src="https://github.com/user-attachments/assets/9828aedf-56cb-46ed-8387-58b198309489" />
| **10** | **Faculty Dashboard:** Allows faculty to manage and upload course materials, syllabi, and academic resources. |  |
<img width="940" height="434" alt="image" src="https://github.com/user-attachments/assets/c933d941-fcda-4957-aa03-36d79cc8f172" />
| **11** | **View Syllabus:** Faculty members can upload, update, and manage the syllabus for their courses, including topics, descriptions, and related resources for students.|  |
<img width="940" height="438" alt="image" src="https://github.com/user-attachments/assets/d73fd5f0-b85d-48b2-aa56-37709618824d" />
| **12** | **Add Syllabus:** Faculty can upload new syllabi providing details such as course title, description, and topics. |  |
<img width="940" height="432" alt="image" src="https://github.com/user-attachments/assets/0d05a8a8-6778-44a3-a116-27d4f3c1b04b" />
| **13** | **Add Topics and PDFs:** Faculty members can add individual topics to the syllabus and upload related PDFs. |  |
<img width="940" height="436" alt="image" src="https://github.com/user-attachments/assets/766c48e4-39f9-443e-afb3-da149bfa0614" />
| **14** | **Add Question Papers:** Faculty can upload previous year question papers in PDF format. |  |
<img width="940" height="433" alt="image" src="https://github.com/user-attachments/assets/fe2ca4bd-a32d-4195-81ef-73b32ba0a362" />
| **15** | **View Students:** Faculty can view a list of registered students, including their details such as name, academic year, and branch, to manage and track their academic progress. |  |
<img width="940" height="433" alt="image" src="https://github.com/user-attachments/assets/e038d2bf-530a-44f1-a518-94e3cc403d21" />
| **16** | **Admin Login Page:** Administrators securely log in to access the admin dashboard. |  |
<img width="940" height="437" alt="image" src="https://github.com/user-attachments/assets/5f054b3b-998f-4e68-a663-380743ae0971" />
| **17** | **Admin Dashboard:** Administrators can manage academic structures such as years, semesters, and faculty records, as well as monitor and control user accounts (students and faculty), ensuring efficient academic operations. |  |
<img width="940" height="434" alt="image" src="https://github.com/user-attachments/assets/65e08f00-e4b6-42a2-bd91-fcbc9c0dde19" />
| **18** | **Add Faculty:** Administrators can add new faculty members by entering their details. |  |
<img width="940" height="435" alt="image" src="https://github.com/user-attachments/assets/a4a1ac25-87a4-437b-a15d-a5725d12158b" />
| **19** | **Add Academic Year:** Administrators define and add new academic years, specifying start/end dates and semesters. |  |
<img width="940" height="436" alt="image" src="https://github.com/user-attachments/assets/1c6a9b55-d1d3-4296-9aff-763e2e754ccf" />
| **20** | **Add College Events:** Administrators can create and manage college events (name, date, time, description). |  |
<img width="940" height="434" alt="image" src="https://github.com/user-attachments/assets/0f7c5fdf-2f56-4b44-b28d-a148b44da4c7" />
| **21** | **View Students:** Administrators can view the list of registered students, along with their details such as name, academic year, branch, and enrollment status, to manage and track student progress. |  |
<img width="940" height="434" alt="image" src="https://github.com/user-attachments/assets/6be52c68-4bee-4264-aa75-5e3012ae9127" />
| **22** | **View Faculty:** Administrators can view the list of registered faculty members, along with their details such as name, department, courses taught, and contact information, to manage faculty records effectively. |  |
<img width="940" height="435" alt="image" src="https://github.com/user-attachments/assets/63d2cbf3-a6b3-4266-98fb-a431a1a48cd1" />
| **23** | **View Events:** Administrators can view a list of upcoming and past college events, including details like event name, date, time, and description, to track and manage event schedules.|  |
<img width="940" height="435" alt="image" src="https://github.com/user-attachments/assets/0be13f3e-c65c-4446-968e-db7bdc3fb05a" />
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
