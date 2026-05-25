# Architectural Decision Records

This ADR is a living document for WorkforceConnect. It continues the design decisions from Assessment 2 and records the new architectural decisions made for Assessment 4. The main evolution in Assessment 4 is that the project moved from a basic data-management application into a more structured Django application with authentication, a service layer, exception handling, API access, and testing.

---

## ADR 1: Use a separate WorkerSkill model for Worker-Skill relationships

### Status
Accepted - carried forward from Assessment 2

### Context
The system stores worker information and worker skills. A worker can have many skills, and one skill can belong to many workers. The project also needs to record extra information about each worker's skill, such as the proficiency level.

### Alternatives considered
1. Use a direct `ManyToManyField` between `Worker` and `Skill`
   - Pros: simple and fast to implement
   - Cons: cannot store extra relationship information such as proficiency level

2. Store skills as text inside the `Worker` model
   - Pros: very easy to set up
   - Cons: poor database design, difficult to query, and not scalable

3. Use a separate `WorkerSkill` model
   - Pros: supports extra fields, more flexible, and better for future expansion
   - Cons: requires more code and slightly more complex queries

### Decision
We decided to use a separate `WorkerSkill` model with foreign key links to `Worker` and `Skill`.

### Code reference
- `workforceconnect/workforce/models.py`

### Consequences
This decision makes the system more flexible and better organised. It allows the project to store proficiency levels for each worker's skill, which is important for workforce planning and future job matching.

---

## ADR 2: Use Django admin for initial and ongoing data management

### Status
Accepted - carried forward from Assessment 2 and extended in Assessment 4

### Context
During development, the project needed a quick and reliable way to add, edit, delete, and test data for workers, employers, jobs, training programs, skills, and applications.

### Alternatives considered
1. Build custom CRUD pages for every model from the beginning
   - Pros: more suitable for end users
   - Cons: slower to develop and more repetitive for a student project

2. Use Django admin for CRUD management
   - Pros: built-in, fast, reliable, and useful for testing data relationships
   - Cons: less customised than a purpose-built front-end interface

### Decision
We decided to use Django admin for CRUD data management. This decision is still used in Assessment 4 because admin remains useful for managing users, worker profiles, employer profiles, jobs, skills, training programs, and applications.

### Code reference
- `workforceconnect/workforce/admin.py`
- `workforceconnect/config/urls.py`

### Consequences
This helped the team develop faster and test the database structure without building unnecessary custom CRUD screens. The trade-off is that some management actions are still done through the admin interface rather than the normal user interface.

---

## ADR 3: Use class-based views for standard pages

### Status
Accepted - carried forward from Assessment 2

### Context
The project requires several common pages such as worker lists, worker details, employer lists, job lists, job details, training lists, and application lists. The team needed to decide whether these pages should be built with function-based views or class-based views.

### Alternatives considered
1. Use function-based views
   - Pros: simple and clear for beginners
   - Cons: repetitive for common list and detail pages

2. Use class-based views
   - Pros: reusable, cleaner for standard pages, and follows Django conventions
   - Cons: can be harder to understand at first

### Decision
We decided to use Django class-based views for standard list and detail pages.

### Code reference
- `workforceconnect/workforce/views.py`
- `workforceconnect/workforce/urls.py`

### Consequences
This reduced repeated code and made the views more organised. It also supports object-oriented methodology because each view class has a clear responsibility.

---

## ADR 4: Keep Employer and Worker as separate models

### Status
Accepted - carried forward from Assessment 2 and extended by ADR 7

### Context
The system includes both workers and employers, but they represent different real-world roles. Workers are people looking for employment opportunities, while employers are organisations offering jobs.

### Alternatives considered
1. Use one combined profile model for both workers and employers
   - Pros: fewer models
   - Cons: mixed responsibilities and unclear design

2. Keep `Worker` and `Employer` as separate models
   - Pros: clearer object-oriented design and better alignment with the project theme
   - Cons: some similar contact fields may be repeated

### Decision
We decided to keep `Worker` and `Employer` as separate models. In Assessment 4, both models were extended with optional one-to-one links to Django's `User` model.

### Code reference
- `workforceconnect/workforce/models.py`

### Consequences
The design remains clear because workers and employers are treated as different domain objects. Linking each profile type to a user account also supports authentication without merging unrelated responsibilities into one model.

---

## ADR 5: Use SQLite for the development database

### Status
Accepted - carried forward from Assessment 2

### Context
The team needed a database that was easy to set up for local development and testing. The project is a student group project, so the development environment needed to remain simple for all team members.

### Alternatives considered
1. Use PostgreSQL or MySQL
   - Pros: powerful and suitable for production systems
   - Cons: requires more setup and configuration

2. Use SQLite
   - Pros: built into Django, no separate server required, and easy for local development
   - Cons: not suitable for a large production system

### Decision
We decided to use SQLite for the development environment.

### Code reference
- `workforceconnect/config/settings.py`

### Consequences
SQLite makes the project easier to run locally and reduces setup problems for the team. If the project becomes a production system, the database could be changed to PostgreSQL or MySQL later.

---

## ADR 6: Use Django ORM instead of raw SQL

### Status
Accepted - carried forward from Assessment 2 and extended by ADR 8

### Context
The application needs to query data from the database for workers, employers, jobs, training programs, skills, and applications. The team needed to choose between writing raw SQL queries or using Django's ORM.

### Alternatives considered
1. Use raw SQL
   - Pros: flexible and can be highly optimised
   - Cons: harder to maintain, easier to make mistakes, and more exposed to SQL injection problems if written incorrectly

2. Use Django ORM
   - Pros: readable, integrated with Django models, safer, and easier to maintain
   - Cons: less flexible than raw SQL in some complex cases

### Decision
We decided to use Django ORM for normal application queries.

### Code reference
- `workforceconnect/workforce/models.py`
- `workforceconnect/workforce/views.py`
- `workforceconnect/workforce/services.py`
- `workforceconnect/workforce/api.py`

### Consequences
The code is easier to understand and maintain. The ORM also works well with the service layer introduced in Assessment 4 because the business logic can call model queries in a readable way.

---

## ADR 7: Use Django's built-in authentication system

### Status
Accepted - new for Assessment 4

### Context
Assessment 4 requires authentication and login/logout functionality. The project needs a way to identify users before allowing them to perform actions such as applying for jobs or viewing their own applications.

### Alternatives considered
1. Build a custom authentication system
   - Pros: full control over user fields and login behaviour
   - Cons: high risk, more code, and unnecessary for the project scope

2. Use Django's built-in `User` model and authentication views
   - Pros: secure default behaviour, already integrated with Django, supports login/logout, sessions, permissions, and admin
   - Cons: less customised than a fully custom user model

3. Use a custom user model
   - Pros: more flexible for future production use
   - Cons: more complex and unnecessary for the current assignment stage

### Decision
We decided to use Django's built-in authentication system with Django's `User` model. The `Worker` and `Employer` models use optional one-to-one fields to connect profile records to authenticated users.

### Code reference
- `workforceconnect/config/settings.py`
- `workforceconnect/workforce/models.py`
- `workforceconnect/workforce/urls.py`
- `workforceconnect/workforce/templates/workforce/login.html`
- `workforceconnect/workforce/templates/workforce/base.html`

### Consequences
This allows the project to support login and logout without creating an unsafe custom authentication system. It also makes it possible to connect a logged-in user to a worker or employer profile. The trade-off is that profile creation still needs to be managed through the admin interface at this stage.

---

## ADR 8: Introduce a service layer for the job application workflow

### Status
Accepted - new for Assessment 4

### Context
In Assessment 2, most behaviour could be handled directly through views and models. In Assessment 4, the project requires more mature architecture. The job application workflow now includes several business rules: the user must be logged in, the user must have a worker profile, the job must exist, the job must be open, and duplicate applications must be prevented.

### Alternatives considered
1. Put all application logic inside the view
   - Pros: quick to implement
   - Cons: makes views too large and difficult to test

2. Put all application logic inside the model
   - Pros: keeps logic close to the data
   - Cons: the workflow coordinates multiple models, so placing everything in one model would create unclear responsibility

3. Create a separate service layer
   - Pros: separates business workflow from views, easier to test, and supports clearer object-oriented decomposition
   - Cons: adds an extra file and requires the team to understand a new pattern

### Decision
We decided to create a service layer in `workforce/services.py`. The `apply_for_job()` function coordinates the job application workflow and uses a database transaction.

### Code reference
- `workforceconnect/workforce/services.py`
- `workforceconnect/workforce/views.py`
- `workforceconnect/workforce/tests.py`

### Consequences
The view stays focused on receiving the request and returning a response. The service layer handles business rules and can be tested directly without depending on template rendering. This makes the application easier to maintain and demonstrates a clearer separation of concerns.

---

## ADR 9: Use custom exceptions for application workflow errors

### Status
Accepted - new for Assessment 4

### Context
The application workflow can fail for different reasons. For example, a user may not have a worker profile, the job may be closed, or the user may have already applied. These errors should be clear in both the code and the user interface.

### Alternatives considered
1. Return `None` or `False` from the service
   - Pros: simple
   - Cons: does not explain why the workflow failed

2. Use generic exceptions only
   - Pros: less code
   - Cons: harder to understand and harder for the view to respond with specific messages

3. Use custom exception classes
   - Pros: each failure case has a clear meaning and can be handled separately
   - Cons: requires maintaining extra classes

### Decision
We decided to use custom exceptions for the main business-rule failures in the application workflow.

### Code reference
- `workforceconnect/workforce/exceptions.py`
- `workforceconnect/workforce/services.py`
- `workforceconnect/workforce/views.py`

### Consequences
The code is easier to read because each exception name describes a specific failure. The view can show different user messages for different problems, which improves usability and supports robust error handling.

---

## ADR 10: Use a meaningful test strategy focused on behaviour

### Status
Accepted - new for Assessment 4

### Context
Assessment 4 requires a meaningful test suite. The main risk in the current application is not whether Django can save simple models, but whether the job application workflow correctly enforces business rules and permission boundaries.

### Alternatives considered
1. Write only trivial model tests
   - Pros: easy to write
   - Cons: low value because they only test simple Django behaviour

2. Write tests that mirror implementation details
   - Pros: gives more test files
   - Cons: fragile and does not prove meaningful behaviour

3. Write behaviour-focused tests for important workflows
   - Pros: verifies real rules that matter to the application
   - Cons: requires more planning and test data setup

### Decision
We decided to focus the test suite on meaningful behaviour in the job application workflow. The current tests check successful applications, duplicate applications, closed jobs, and users without worker profiles.

### Code reference
- `workforceconnect/workforce/tests.py`
- `workforceconnect/workforce/services.py`
- `workforceconnect/workforce/exceptions.py`

### Consequences
The tests provide evidence that the service layer protects important business rules. This includes a permission boundary because a normal authenticated user cannot apply unless they have a linked Worker profile. The current test suite does not exhaustively test every template or admin screen because those areas mostly use Django's built-in behaviour. Future improvements could add view tests for redirects, API permission tests, and model relationship tests.

---

## ADR 11: Protect application pages using login requirements

### Status
Accepted - new for Assessment 4

### Context
Some pages should be public, such as the home page and general lists. Other pages should be restricted because they relate to a user's own actions or records, such as applying for a job and viewing applications.

### Alternatives considered
1. Make every page public
   - Pros: easier access for testing
   - Cons: unsafe because any visitor could try to apply for jobs or view application records

2. Require login for the whole site
   - Pros: stricter access control
   - Cons: unnecessary for basic public information such as job and worker lists

3. Use mixed access with `LoginRequiredMixin` on protected views
   - Pros: public information remains visible while user-specific actions are protected
   - Cons: requires careful selection of which views need protection

### Decision
We decided to use `LoginRequiredMixin` for protected views such as applying for a job and viewing applications, while keeping general information pages available.

### Code reference
- `workforceconnect/workforce/views.py`
- `workforceconnect/workforce/urls.py`
- `workforceconnect/config/settings.py`

### Consequences
The application has a clearer permission boundary. Users can browse general workforce information, but they must log in before performing user-specific actions. This improves security while keeping the system easy to use.

---

## ADR 12: Add an authenticated REST API for job opportunities

### Status
Accepted - new for Assessment 4

### Context
The application currently uses HTML templates, but Assessment 4 rewards tangible feature growth. A REST API gives the project another way to expose job opportunity data and shows that the system can support future integrations.

### Alternatives considered
1. Do not include an API
   - Pros: keeps the project simpler
   - Cons: limits future integration and feature growth

2. Build a manual JSON response using Django views
   - Pros: fewer dependencies
   - Cons: more manual work and less structured

3. Use Django REST Framework
   - Pros: standard API structure, serializers, generic API views, and permission classes
   - Cons: adds an extra dependency

### Decision
We decided to use Django REST Framework for an authenticated job opportunities API. The API lists open job opportunities and requires authentication.

### Code reference
- `workforceconnect/config/settings.py`
- `workforceconnect/workforce/api.py`
- `workforceconnect/workforce/urls.py`
- `requirements.txt`

### Consequences
The API demonstrates additional functionality beyond the HTML interface. Requiring authentication protects the endpoint and aligns with the Assessment 4 authentication requirement. The trade-off is that the project must include Django REST Framework in `requirements.txt`.

---

## ADR 13: Keep templates simple and extend a shared base template

### Status
Accepted - new for Assessment 4

### Context
The application needs a consistent user interface for home, workers, employers, jobs, training, applications, and login/logout status. The team needed to avoid repeating layout code across templates.

### Alternatives considered
1. Write each template as a full HTML page
   - Pros: simple for beginners
   - Cons: repeated header, navigation, footer, and message display code

2. Use a shared base template and extend it
   - Pros: reusable layout, consistent navigation, easier maintenance
   - Cons: requires understanding Django template inheritance

### Decision
We decided to use a shared `base.html` template and extend it for individual pages.

### Code reference
- `workforceconnect/workforce/templates/workforce/base.html`
- `workforceconnect/workforce/templates/workforce/*.html`
- `workforceconnect/workforce/static/workforce/style.css`

### Consequences
The interface is more consistent and easier to maintain. Authentication links and system messages only need to be managed in one main template.

---

## ADR 14: Use AI coding tools as support, not as final architectural authority

### Status
Accepted - new for Assessment 4

### Context
The assessment permits and expects the use of AI coding tools. However, the team still needs to understand and justify the architecture. AI-generated code is not enough by itself, especially for authentication, service layers, exception handling, and testing.

### Alternatives considered
1. Avoid AI tools completely
   - Pros: full manual control
   - Cons: slower development and less opportunity to compare design options

2. Accept AI output without review
   - Pros: faster coding
   - Cons: high risk of shallow tests, incorrect architecture, and code that the team cannot explain during the viva

3. Use AI tools for suggestions and then review the design manually
   - Pros: faster support while keeping human responsibility for decisions
   - Cons: still requires careful checking and explanation

### Decision
We decided to use AI tools as development support while documenting and reviewing the final architectural decisions ourselves.

### Code reference
- `ADR.md`
- `README.md`
- `workforceconnect/workforce/services.py`
- `workforceconnect/workforce/tests.py`

### Consequences
This helped the team develop and document the project more efficiently while still maintaining accountability for the design. The ADR records the reasons for important choices instead of only presenting generated code.
