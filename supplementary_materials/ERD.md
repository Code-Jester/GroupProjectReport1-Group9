Worker
- id (PK)
- name
- email
- phone
- experience_level
- availability

Skill
- id (PK)
- name
- category

WorkerSkill
- id (PK)
- worker_id (FK)
- skill_id (FK)
- proficiency_level

Employer
- id (PK)
- organisation_name
- industry
- location
- contact_email

JobOpportunity
- id (PK)
- employer_id (FK)
- title
- description
- salary_range
- status

TrainingProgram
- id (PK)
- title
- provider
- target_skill_id (FK)
- duration_weeks

Application
- id (PK)
- worker_id (FK)
- job_opportunity_id (FK)
- application_date
- status

## ERD Notes
- One employer can post many job opportunities.
- One worker can have many skills through the WorkerSkill model.
- One skill can belong to many workers through the WorkerSkill model.
- One worker can submit many applications.
- One job opportunity can receive many applications.
- One skill can be linked to many training programs.
- A job opportunity can require multiple skills.