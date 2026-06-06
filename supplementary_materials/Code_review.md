# Code Review Notes – Assessment 4

## Project
**WorkforceConnect – Theme 2: Economic Strategy & Workforce**

## Team Members
- Brandon – S389937
- Cahaya – S387346
- Chanveasna – S377961
- Kevin – S385480

## Purpose
This document records the supplementary code review notes for the Assessment 4 version of the Django application. The review focused on whether the updated project matched the Assessment 4 project plan and whether the code, diagrams, and documentation explained the system clearly for submission and viva preparation.

The Assessment 4 version extends the earlier Assessment 2 project by adding authentication, user-linked Worker and Employer profiles, permission boundaries, a service layer, custom exception handling, API support, and meaningful tests.

## Review Areas
The team reviewed the following areas:
- Django authentication and login/logout flow
- User-linked Worker and Employer profiles
- Permission boundaries for user-specific pages and API access
- Service-layer structure for job application logic
- Custom exceptions for predictable business errors
- Job opportunity API behaviour
- Test coverage for important business rules
- Admin CRUD support for core records
- Template navigation and page usability
- Updated ADR, README, project plan, ERD, and class diagram

## Review Notes

### 1. Authentication Review
The group reviewed the login and logout flow and confirmed that Django's built-in authentication system is the correct choice for this project. Using Django authentication avoids creating a custom password system and allows the application to check whether a user is logged in before allowing user-specific actions.

The review also confirmed that Worker and Employer profiles should be connected to Django user accounts. This makes it possible to separate general public browsing from actions that belong to a specific logged-in user, such as applying for a job or viewing an application list.

### 2. Permission Boundary Review
The group reviewed which pages should be public and which pages should be protected. Public browsing can include general information, job lists, training programs, and basic workforce information. Actions connected to a specific user, such as submitting a job application or viewing personal applications, should require login.

The team agreed that permission boundaries should be handled consistently in views and API code. This reduces the risk of users accessing pages or data they should not access.

### 3. Service Layer Review
The application workflow for applying to a job was reviewed and moved into a service-layer function in `workforce/services.py`. This is an improvement because views should mainly handle HTTP requests and responses, while the service layer handles business rules.

The service layer makes the code easier to test because the application logic can be checked without relying only on page loading. It also makes the viva explanation clearer because the group can point to one place where the job application rules are handled.

### 4. Exception Handling Review
The group reviewed the predictable errors that can happen during the job application process. These include:
- a logged-in user does not have a Worker profile
- a Worker tries to apply for a closed job
- a Worker tries to apply for the same job more than once

Custom exceptions in `workforce/exceptions.py` make these cases clearer than using generic errors. They also make it easier for views to show user-friendly feedback and easier for tests to check the correct behaviour.

### 5. API Review
The job opportunity API was reviewed to make sure it supports Assessment 4 requirements. The API should focus on open job opportunity data and should be protected so that only authenticated users can access it.

The API helps show that the project is not only template-based but also has structured data access that could support future frontend or integration work.

### 6. Testing Review
The group agreed that tests should focus on behaviour that matters, not only simple object creation. The most important test cases are:
- a logged-in Worker can apply for an open job
- a Worker cannot apply for the same job twice
- a Worker cannot apply for a closed job
- a logged-in user without a Worker profile cannot apply for a job
- application-list access is limited to authenticated users
- API access requires authentication
- model relationships connect Workers, Skills, Jobs, Employers, and Applications correctly

These tests are stronger because they check the actual rules of the system and help prove that the Assessment 4 features work as intended.

### 7. Admin and Template Review
The Django admin setup was reviewed to make sure the main database records can still be managed easily. This is useful for creating sample workers, employers, jobs, skills, training programs, and applications during development and testing.

The templates were also reviewed for navigation and clarity. The pages should be easy to move through and should support the main target users: workers/youth workers and employers.

### 8. Documentation and Diagram Review
The supplementary ERD and class diagram were updated to show the Assessment 4 changes. The diagrams now include the Django authentication user relationship and show the service layer, custom exceptions, protected views, API support, and tests.

The documentation review also focused on making sure the ADR, README, project plan, and supplementary materials tell the same story as the code. This is important because markers may compare the documentation with the repository during assessment.

### 9. AI-Assisted Development Review
AI tools may be used to support planning, wording, debugging, and code structure suggestions. However, the group must review and understand all final code before submission. The team should be ready to explain which suggestions were adapted and why the final decisions fit the project.

## Improvements Made After Review
- Updated the supplementary ERD to include Django Auth User and user-linked Worker and Employer profiles.
- Updated the ERD notes to explain authentication, job applications, protected API access, and service-layer business rules.
- Updated the class diagram to show the connection between models, service layer, exceptions, views/API, and tests.
- Updated the code review notes to reflect Assessment 4 instead of only Assessment 2.
- Added clearer review points for permission boundaries, testing, API support, and viva preparation.

## Remaining Final Checks Before Submission
- Run the Django application locally.
- Run the test suite using Django's test command.
- Check that login, logout, protected pages, and application workflow work correctly.
- Check that the API endpoint requires authentication.
- Confirm that the README setup instructions match the actual project.
- Confirm that ADR file references match real files in the repository.
- Confirm that every team member can explain their own contribution and the main Assessment 4 features.

## Reflection
The code review process helped the team move the project from a basic Django data system into a more complete web application. The most important improvement is that the project now has clearer separation of responsibilities: models store data, views handle web requests, services handle business logic, exceptions describe expected business errors, and tests check the rules that matter. This makes the project easier to explain, maintain, and assess during the live code walkthrough.
