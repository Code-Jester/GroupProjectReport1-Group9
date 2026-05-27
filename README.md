# WorkforceConnect - Group 9

**Project theme:** Theme 2 - Economic Strategy and Workforce  
**Assessment:** Assessment 4 - Group Project Report 2

## Team Members

| Name | Student Number |
|---|---|
| Brandon | S389937 |
| Cahaya | S387346 |
| Chanveasna | S377961 |
| Kevin | S385480 |

## Overview

WorkforceConnect is a Django web application for workforce and employment planning. The system manages workers, employers, job opportunities, training programs, and job applications in one structured application. This project continues from Assessment 2 and has been extended for Assessment 4 with authentication, login/logout, a service layer, custom exception handling, API access, and automated tests.

The goal of the application is to support the economic strategy and workforce theme by connecting workers, skills, employers, jobs, and training pathways. The design focuses on clear object-oriented models, reusable Django views, and business logic that is separated from the presentation layer.

## Assessment 4 Feature Updates

The project has been extended with the following Assessment 4 requirements:

- **Authentication:** Django authentication is enabled using login and logout pages.
- **Login/Logout:** Users can log in and log out through the web interface.
- **Service Layer:** The job application process is handled in `workforce/services.py` instead of placing all business logic directly in views.
- **Custom Exceptions:** Application-specific errors are defined in `workforce/exceptions.py` for clearer error handling.
- **Tests:** The test suite checks meaningful job application behaviour, including successful applications, duplicate applications, closed jobs, and users without worker profiles.
- **API:** An authenticated REST API endpoint is available for open job opportunities.
- **Admin CRUD:** Django admin supports create, read, update, and delete operations for core workforce records.
- **Templates:** User-facing pages display workers, employers, jobs, training programs, applications, login/logout status, and system overview information.

## Main Features

- View worker records and worker skill information
- View employer records
- View job opportunities and job details
- View training programs
- Apply for jobs as an authenticated worker
- Prevent duplicate job applications
- Prevent applications to closed job opportunities
- View logged-in worker applications
- Manage data through Django admin
- Access open job data through an authenticated API endpoint

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- HTML
- CSS

## Project Structure

```text
GroupProjectReport1-Group9/
├── ADR.md
├── Group Contract.md
├── Project Plan.md
├── README.md
├── requirements.txt
├── supplementary_materials/
│   ├── Class-diagram.png
│   ├── Code_review.md
│   ├── ERD-diagram.png
│   └── ERD.md
└── workforceconnect/
    ├── manage.py
    ├── db.sqlite3
    ├── config/
    │   ├── settings.py
    │   └── urls.py
    └── workforce/
        ├── admin.py
        ├── api.py
        ├── exceptions.py
        ├── models.py
        ├── services.py
        ├── tests.py
        ├── urls.py
        ├── views.py
        ├── migrations/
        ├── static/
        └── templates/
```

## Requirements

To run this project, you need:

- Python 3.12, 3.13, or 3.14
- Django 6.0.4
- Django REST Framework
- Other packages listed in `requirements.txt`

## Setup Instructions

### 1. Clone or open the repository

Open the project folder in VS Code:

```powershell
cd C:\Users\LOQ\Downloads\GroupProjectReport1-Group9
```

### 2. Create a virtual environment

For Windows PowerShell:

```powershell
py -3.13 -m venv .venv
```

If Python 3.14 is installed instead, use:

```powershell
py -3.14 -m venv .venv
```

### 3. Activate the virtual environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

For Git Bash:

```bash
source .venv/Scripts/activate
```

### 4. Install the required packages

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install djangorestframework
```

### 5. Go to the Django project folder

```powershell
cd workforceconnect
```

### 6. Apply migrations

```powershell
python manage.py migrate
```

### 7. Create an admin user

```powershell
python manage.py createsuperuser
```

### 8. Run the development server

```powershell
python manage.py runserver
```

Open the project in your browser:

```text
http://127.0.0.1:8000/
```

## Authentication Notes

The application uses Django's built-in `User` model. Worker and Employer records can be linked to a user account through one-to-one relationships. This allows the system to connect logged-in users with their worker or employer profile.

The job application feature requires a logged-in user. A user must also have a linked Worker profile before applying for a job. If the user does not have a Worker profile, the service layer raises a custom exception and the view displays a clear message.

## Service Layer Notes

The main business workflow is located in:

```text
workforce/services.py
```

The `apply_for_job()` service is responsible for:

- checking that the user has a Worker profile
- checking that the selected job exists
- checking that the job is open
- preventing duplicate applications
- creating the application inside an atomic transaction

This keeps business rules out of the view layer and makes the logic easier to test.

## Exception Handling Notes

Custom exceptions are located in:

```text
workforce/exceptions.py
```

The project uses custom exceptions for:

- `WorkerProfileRequired`
- `JobClosed`
- `DuplicateApplication`

These exceptions make the application workflow easier to understand because each error represents a specific business rule.

## Testing

Run the test suite from the `workforceconnect` directory:

```powershell
python manage.py test
```

Current tests focus on the job application workflow because it is the highest-risk feature added in Assessment 4. The tests verify that:

- a valid worker can successfully create a pending application
- a worker cannot apply for the same job twice
- a worker cannot apply for a closed job
- a user without a Worker profile cannot apply for a job

The testing strategy is documented in `ADR.md`.

## Assessment 4 Documentation

This repository includes the required Assessment 4 documentation:

- `ADR.md` - updated Architectural Decision Record
- `README.md` - updated project documentation and run instructions
- `Project Plan.md` - project planning document
- `Group Contract.md` - group contract document
- `requirements.txt` - dependency list
- `supplementary_materials/` - ERD, class diagram, and supporting materials

## AI Tool Usage

AI tools were used to support coding, documentation, and review. The team still reviewed the generated suggestions and made architectural decisions based on the assessment requirements. The ADR records explain the reasoning behind authentication, service layer, exception handling, testing, and API choices.
