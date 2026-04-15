# Architectural Decision Records

## ADR 1: Use a separate WorkerSkill model for Worker–Skill relationships

### Status
Accepted

### Context
This is a system we created to collect data on the information and skills of workers. In reality, a worker can encompass multiple skills, and a single skill can belong to multiple workers. This is a many-to-many relationship.
Furthermore, the system also stores information on each employee's skills, so designing it to filter data helps provide a more objective view of each employee.

### Alternatives considered
1. Use a direct ManyToManyField between Worker and Skill  
   - Pros: simple and fast to implement  
   - Cons: cannot store extra information such as proficiency level  

2. Store skills as text inside the Worker model  
   - Pros: very easy to set up  
   - Cons: poor database design, difficult to query, and not scalable  

3. Use a separate WorkerSkill model  
   - Pros: supports extra fields, more flexible, and better for future expansion  
   - Cons: requires more code and slightly more complex queries  

### Decision
We decided to use a separate `WorkerSkill` model with ForeignKey links to `Worker` and `Skill`.

### Code reference
- `workforce/models.py`

### Consequences
This decision makes the system more flexible and better organised. It also allows the project to store proficiency levels for each worker’s skill, which is important for workforce planning and job matching.

---

## ADR 2: Use Django admin for initial data management

### Status
Accepted

### Context
During development, the project needed a quick and reliable way to add, edit, and test data for workers, employers, jobs, training programs, and applications.

### Alternatives considered
1. Build custom HTML forms from the beginning  
   - Pros: more suitable for end users  
   - Cons: slower to develop in the early stage  

2. Use Django admin first  
   - Pros: fast, built-in, and useful for testing  
   - Cons: less customised than a normal front-end page  

### Decision
We decided to use Django admin first to manage data during development.

### Code reference
- `workforce/admin.py`

### Consequences
This decision helped speed up development and made it easier to test the database structure and model relationships before building more advanced front-end features.

---

## ADR 3: Use class-based views for standard pages

### Status
Accepted

### Context
The project requires several common pages, such as worker lists, worker details, employer lists, and job lists. The team needed to decide whether these pages should be built with function-based views or class-based views.

### Alternatives considered
1. Use function-based views  
   - Pros: simple and clear for beginners  
   - Cons: repetitive for common list and detail pages  

2. Use class-based views  
   - Pros: reusable, cleaner for standard pages, and follows Django conventions  
   - Cons: can be harder to understand at first  

### Decision
We decided to use class-based views for standard list and detail pages.

### Code reference
- `workforce/views.py`
- `workforce/urls.py`

### Consequences
This reduced repeated code and made the views more organised. It also helped demonstrate a better understanding of Django’s built-in generic views.

---

## ADR 4: Keep Employer and Worker as separate models

### Status
Accepted

### Context
The system includes both workers and employers, but they represent different types of entities. Workers are people looking for opportunities, while employers are organisations offering jobs.

### Alternatives considered
1. Use one combined model for both  
   - Pros: fewer models  
   - Cons: unclear design, mixed responsibilities, and harder to maintain  

2. Keep Worker and Employer as separate models  
   - Pros: clearer object-oriented design, easier to understand, and better matches the project theme  
   - Cons: some similar fields may be repeated  

### Decision
We decided to keep `Worker` and `Employer` as separate models.

### Code reference

- `workforce/models.py`

### Consequences
This made the project structure clearer and easier to explain. It also better reflects the real-world roles in a workforce system.

---

## ADR 5:Using SQLite for Development Environments

### Status

Accepted

### Context

A basic database management and information gathering system is essential for rapid development in a local environment. Filtering information is detailed, accurate, neat, and immediate.

### Options Considered
1. PostgreSQL / MySQL
   - Pros: Powerful, suitable for production environments
   - Cons: Complex configuration

2. SQLite
   - Pros: No server installation required
                 Built-in in Django
                 Easy to use
   - Cons: Not suitable for large systems

### Decision

Use SQLite for development.

### Code reference

- `settings.py`

### Consequences

Helps to accelerate development and simplify the environment. Can be switched to PostgreSQL at deployment.

## ADR 6: Using Django ORM instead of raw SQL

### Status

Accepted

### Context

The team needs to query data from a database. Raw SQL or ORM can be used.

### Options Considered
1. Raw SQL
   - Pros: Optimized, flexible
   - Cons: Difficult to maintain, prone to errors

2. Django ORM
   - Pros: Easy to read
                 Secure (avoids SQL injection)
                 Integrated with Django
   - Cons: Less flexible than pure SQL

### Decision

Use Django ORM for all queries.

### Code Reference

- `models.py/views.py`

### Consequence

The code is easy to understand, easy to maintain, suitable for learning projects and medium-sized projects.
