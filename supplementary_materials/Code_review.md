# Code Review Notes

## Project
WorkforceConnect – Theme 2: Economic Strategy & Workforce

## Team Members
- Cahaya
- Brandon
- Kevin
- Veasna

## Purpose
This document records code review discussions and observations made during the development of the Django application. The purpose of the review process was to check whether the project structure, models, views, templates, and documentation matched the assessment requirements and the project theme.

## Review Areas
The team reviewed the following parts of the project:
- Django project structure
- Model relationships
- URL routing
- Views and templates
- Admin configuration
- Documentation files including ADR and README

## Review Notes

### 1. Model Design Review
The team reviewed the database structure and agreed that the system should include separate models for Worker, Employer, Skill, JobOpportunity, TrainingProgram, and Application. It was also discussed that a direct many-to-many relationship between Worker and Skill was not enough because the project needed to store skill proficiency. Because of this, the WorkerSkill model was used as an intermediate model.

### 2. Relationship Review
The team checked whether the relationships matched the workforce planning theme. It was confirmed that:
- one employer can post many job opportunities
- one worker can apply for many jobs
- one job can require many skills
- one worker can have many skills through WorkerSkill

This helped improve the object-oriented design of the application.

### 3. Views and Template Review
The team reviewed the structure of the pages and agreed to use class-based views for standard list and detail pages. Templates were also reviewed to improve consistency, and a shared base template was introduced so the pages could reuse the same layout and navigation bar.

### 4. Admin Review
The admin panel setup was checked to make sure all main models were registered. This made it easier to enter and test data during development.

### 5. Documentation Review
The team reviewed the README and ADR files to make sure they reflected the actual design decisions in the project. Some wording was adjusted so the documents matched the WorkforceConnect theme and the final Django structure.

## Improvements Made After Review
- Added a separate WorkerSkill model instead of a plain many-to-many field
- Kept Worker and Employer as separate models
- Improved consistency in templates using a shared base template
- Registered all major models in Django admin
- Updated README and ADR content to better match the real project

## Reflection
The code review process helped the team identify design improvements and better justify decisions in both the code and documentation. It also showed that the project was developed with discussion, planning, and review rather than only relying on automatically generated code.