# Project Plan – Assessment 4 Group Project Report 2

## Project Overview

WorkforceConnect is a Django web application for the **Economic Strategy and Workforce** theme. The project supports workforce planning by organising workers, employers, job opportunities, training programs, skills, and job applications in one structured system.

This Assessment 4 version continues from Assessment 2. The application has been extended from a basic workforce information system into a more mature Django application with authentication, login/logout flow, permission boundaries, a service layer, custom exception handling, API support, and testing.

## Team Members

- Brandon – S389937
- Cahaya – S387346
- Chanveasna – S377961
- Kevin – S385480

## Target Users

The system is designed for two main user groups.

### Workers / Youth Workers

Workers use the system to:

- Explore available job opportunities
- View required skills for jobs
- Access training programs
- Apply for suitable job opportunities
- Track their own job applications after logging in

### Employers

Employers use the system to:

- View worker information
- Identify skill gaps
- Manage job opportunities through the system
- Match job requirements with worker skills
- Support workforce planning through organised data

## Project Evolution from Assessment 2

In Assessment 2, the project focused on the core Django structure, models, model relationships, class-based views, Django admin, templates, and architectural documentation.

For Assessment 4, the project has been extended with:

- Django authentication and login/logout support
- User-linked Worker and Employer profiles
- A service layer for business logic
- Custom exception classes for predictable error handling
- Permission boundaries for pages and API access
- REST API support for job opportunity data
- Test cases for important business behaviour
- Updated ADR, README, project plan, contract, and supplementary materials

## Assessment 4 Scope

The scope of this assessment is to improve the existing Django application by adding stronger architecture and more realistic user functionality.

| Area | Planned / Implemented Work | Main File References |
|---|---|---|
| Authentication | Add login/logout support and connect Django users to Worker and Employer profiles | `workforce/urls.py`, `workforce/models.py`, `templates/workforce/login.html` |
| Permission Boundaries | Restrict job application and application list pages to logged-in users | `workforce/views.py`, `workforce/api.py` |
| Service Layer | Move job application logic out of views into a dedicated service function | `workforce/services.py` |
| Exception Handling | Use custom exceptions for worker profile, closed job, and duplicate application problems | `workforce/exceptions.py`, `workforce/views.py` |
| Testing | Test meaningful business behaviour such as applying successfully, duplicate applications, closed jobs, and users without worker profiles | `workforce/tests.py` |
| API | Add a protected API endpoint for open job opportunities | `workforce/api.py`, `workforce/urls.py` |
| Admin CRUD | Continue using Django admin for managing core database records | `workforce/admin.py` |
| Templates | Improve user interface pages for jobs, workers, training programs, applications, and authentication | `workforce/templates/` |
| ADR Update | Record new decisions for authentication, service layer, exceptions, testing, API, and AI-supported development | `ADR.md` |
| README Update | Update setup instructions, project features, requirements, and running instructions | `README.md` |
| Supplementary Materials | Update ERD and class diagram to reflect authentication and service layer changes | `supplementary_materials/` |

## Development Strategy

The group will continue using the same GitHub repository from Assessment 2 so that commit history shows ongoing development. Each feature should be committed in small, clear commits so the team can explain the development process during the viva.

### Stage 1 – Review Existing Assessment 2 Codebase

- Check existing models, relationships, views, templates, and admin setup
- Confirm that the existing app still runs before adding new features
- Identify which Assessment 2 ADR entries need to be kept, updated, or superseded

### Stage 2 – Add Authentication and User Profiles

- Use Django's built-in authentication system
- Add login and logout routes
- Link `User` accounts to `Worker` and `Employer` profiles
- Use authentication to separate public browsing from user-specific actions

### Stage 3 – Add Service Layer

- Move important business logic into `services.py`
- Keep views focused on HTTP request and response handling
- Use the service layer for job application workflow logic
- Make the code easier to test and explain during the walkthrough

### Stage 4 – Add Exception Handling

- Create custom exceptions in `exceptions.py`
- Handle predictable business errors clearly in views
- Provide user-friendly feedback for duplicate applications, closed jobs, or missing worker profiles
- Keep error-handling logic consistent across the application

### Stage 5 – Add Testing

- Write tests for important behaviour, not only simple object creation
- Test the job application service because it connects models, rules, and exceptions
- Check permission-related behaviour where users must be logged in
- Avoid tests that only repeat the implementation without proving useful behaviour

### Stage 6 – Update Documentation and Supplementary Materials

- Update `ADR.md` with new design decisions
- Update `README.md` with current setup and run instructions
- Update `Project Plan.md` and `Group Contract.md`
- Update ERD and class diagrams to include authentication and the service layer
- Prepare notes for the live code walkthrough and viva

## Responsibility Plan

The project is completed as a group, and all members are expected to understand the overall system. The table below shows the planned responsibility areas. The GitHub commit history should be used as the final evidence of contribution.

| Team Member | Main Responsibility Area |
|---|---|
| Brandon | Authentication flow, login/logout checking, and related template support |
| Cahaya | Service layer, exception handling, README/ADR/project documentation updates |
| Chanveasna | User interface templates, navigation flow, and application page usability |
| Kevin | Testing, API checking, admin CRUD review, and supplementary materials |

All members should also help review the final repository before submission.

## AI-Assisted Development Plan

AI tools may be used as semi-assisted development support. The group can use AI to help with:

- Generating possible code structures
- Comparing implementation options
- Improving documentation wording
- Planning tests and edge cases
- Debugging errors during development

However, the team is responsible for reviewing and understanding the final code. AI suggestions should be adapted to the project context instead of being accepted blindly. The final ADR should explain why each major architectural decision was chosen.

## Testing Strategy

The test suite should focus on behaviour that matters to the project. The most important testing areas are:

- A logged-in worker can apply for an open job
- A worker cannot apply for the same job twice
- A worker cannot apply for a closed job
- A logged-in user without a worker profile cannot apply for a job
- Application list access is limited to authenticated users
- API access requires authentication
- Model relationships work correctly between workers, skills, jobs, employers, and applications

The group will prioritise tests for business rules and permission boundaries because these are more meaningful than tests that only check whether a page loads.

## Risk Management

| Risk | Impact | Response |
|---|---|---|
| Python or Django version mismatch | The app may not run on another laptop | Keep `requirements.txt` updated and document setup steps clearly in `README.md` |
| Authentication errors | Users may access pages they should not access | Use `LoginRequiredMixin` and test permission boundaries |
| Business logic becomes repeated in views | Code becomes harder to maintain and test | Move important workflows into `services.py` |
| AI-generated code is not understood | Team may struggle during the viva | Review each AI suggestion and document decisions in ADR |
| Tests are too shallow | Testing marks may be reduced | Focus tests on real behaviour, service rules, and permission boundaries |
| Documentation does not match code | Marker may find inconsistencies | Check README, ADR, project plan, and code references before submission |

## Updated Group Contract

The group contract from the previous assessment is continued, with the following Assessment 4 updates:

- All members must understand the major features added in Assessment 4.
- Each member is responsible for explaining their own contribution during the live walkthrough.
- Communication will continue through Microsoft Teams and in-person discussion when possible.
- Members should commit their own work to GitHub so contribution history is visible.
- AI tools can be used for support, but the group must review and understand the final code.
- Before submission, the group will check that the app runs, documentation is updated, and all required files are included.

## Assessment 4 Submission Checklist

### Repository and Application

- [x] Same GitHub repository from Assessment 2 is used
- [x] Commit history shows continued development
- [x] Django application runs successfully
- [x] Authentication and login/logout are included
- [x] Service layer is included
- [x] Custom exception handling is included
- [x] Permission boundaries are included
- [x] API endpoint is included and protected
- [x] Admin CRUD functionality is available
- [x] Templates are working and easy to navigate

### Documentation

- [x] `ADR.md` is updated for Assessment 4
- [x] Superseded Assessment 2 decisions are marked where needed
- [x] `README.md` is updated with current setup and run instructions
- [x] `Project Plan.md` is updated
- [x] `Group Contract.md` is updated or contract update is included in this plan
- [x] AI usage is described responsibly and honestly
- [x] Code references in ADR match real project files

### Testing

- [x] Test suite is included
- [x] Tests cover meaningful business behaviour
- [x] Tests cover service layer logic
- [x] Tests cover exception cases
- [x] Tests cover authentication or permission boundaries where possible
- [x] Tests can be run using Django's test command

### Supplementary Materials

- [x] Updated ERD is included
- [x] Updated class diagram is included
- [x] Diagrams reflect authentication and service layer changes
- [x] Supporting planning or review notes are included

### Final Check Before Submission

- [x] Run the project locally
- [x] Run the test suite
- [x] Check all Markdown files display correctly on GitHub
- [x] Check repository is accessible to the marker
- [x] Check all team members are ready for the live code walkthrough
- [x] Submit the GitHub repository URL through Learnline

## Viva Preparation Notes

During the live code walkthrough, the group should be ready to explain:

- How authentication works in the application
- Why a service layer was added
- How custom exceptions improve error handling
- What the tests verify and why those tests were selected
- How the updated ADR shows the design evolution from Assessment 2 to Assessment 4
- How AI tools were used as support while the team still reviewed final decisions
