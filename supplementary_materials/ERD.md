# WorkforceConnect ERD Notes – Assessment 4

## Purpose
This supplementary ERD explains the database structure for the Assessment 4 version of **WorkforceConnect**. The system supports the Economic Strategy and Workforce theme by organising workers, employers, job opportunities, skills, training programs, and job applications in one Django application.

Assessment 4 extends the Assessment 2 data model by adding authentication-related profile links and by showing how application behaviour is protected by login, service-layer rules, and predictable exception handling.

## Main Entities

### Django Auth User
- id (PK)
- username
- email
- password
- is_active

**Notes:**
- This is Django's built-in authentication user table.
- A user account can be connected to a Worker profile or an Employer profile.
- The user table supports login, logout, authentication checks, and permission boundaries.

### Worker
- id (PK)
- user_id (FK to Django Auth User, unique profile link)
- name
- email
- phone
- experience_level
- availability

**Notes:**
- A Worker represents a youth worker or job seeker using the system.
- A logged-in Worker can apply for suitable open job opportunities.
- Worker-specific pages, such as a user's own application list, should require authentication.

### Employer
- id (PK)
- user_id (FK to Django Auth User, unique profile link)
- organisation_name
- industry
- location
- contact_email

**Notes:**
- An Employer represents an organisation connected to workforce planning.
- Employers post job opportunities and use worker information to identify skill gaps.

### Skill
- id (PK)
- name
- category

**Notes:**
- Skills are used to describe worker capabilities.
- Skills are also used by job opportunities and training programs.

### WorkerSkill
- id (PK)
- worker_id (FK to Worker)
- skill_id (FK to Skill)
- proficiency_level

**Notes:**
- WorkerSkill is an intermediate table between Worker and Skill.
- It is used instead of a plain many-to-many relationship because the system needs to store proficiency level.

### JobOpportunity
- id (PK)
- employer_id (FK to Employer)
- title
- description
- salary_range
- status

**Notes:**
- A JobOpportunity belongs to one Employer.
- Job opportunities can be open or closed.
- Only open jobs should be returned through the protected job opportunity API and should allow applications.

### JobOpportunityRequiredSkill
- id (PK)
- job_opportunity_id (FK to JobOpportunity)
- skill_id (FK to Skill)

**Notes:**
- This represents the many-to-many relationship between JobOpportunity and Skill.
- If Django creates this through a `ManyToManyField`, the physical database table may be automatically generated, but it is shown in the ERD to make the relationship clear.

### TrainingProgram
- id (PK)
- title
- provider
- target_skill_id (FK to Skill)
- duration_weeks

**Notes:**
- A TrainingProgram targets one main Skill.
- A Skill can be linked to many training programs.

### Application
- id (PK)
- worker_id (FK to Worker)
- job_opportunity_id (FK to JobOpportunity)
- application_date
- status

**Notes:**
- An Application records a Worker applying for a JobOpportunity.
- The application workflow is handled through the service layer in `workforce/services.py`.
- The service should prevent duplicate applications, closed-job applications, and applications from users without Worker profiles.

## Relationship Summary
- One Django Auth User can be linked to one Worker profile.
- One Django Auth User can be linked to one Employer profile.
- One Employer can post many JobOpportunity records.
- One Worker can submit many Application records.
- One JobOpportunity can receive many Application records.
- One Worker can have many Skill records through WorkerSkill.
- One Skill can belong to many Worker records through WorkerSkill.
- One JobOpportunity can require many Skill records through JobOpportunityRequiredSkill.
- One Skill can be required by many JobOpportunity records through JobOpportunityRequiredSkill.
- One Skill can be targeted by many TrainingProgram records.

## Assessment 4 Architecture Notes
- Authentication separates public browsing from user-specific actions.
- Login-required pages are used for job applications and application-list access.
- Business rules for applying to jobs are moved out of views and into the service layer.
- Custom exceptions make expected application errors clearer and easier to test.
- The protected API endpoint returns open job opportunity data only to authenticated users.
- Tests should focus on meaningful behaviour, including successful applications, duplicate applications, closed jobs, missing worker profiles, and protected access.
