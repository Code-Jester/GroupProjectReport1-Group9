# Architectural Decision Records

## ADR 1: Use a separate Participation model for Youth–Program relationships

### Status
Accepted

### Context
The system needs to record which youth participates in which program. A simple direct many-to-many relationship could connect Youth and Program, but the project may need extra details such as participation start date and status.

### Alternatives considered
1. Use a direct ManyToManyField between Youth and Program  
   - Pros: simpler to write  
   - Cons: hard to store additional participation details

2. Use a separate Participation model  
   - Pros: supports extra fields like start_date and status, more flexible for future extension  
   - Cons: requires more code and an extra model

### Decision
We chose a separate Participation model with ForeignKey links to Youth and Program.

### Code reference
- `core/models.py`

### Consequences
This design is more scalable and better represents real-world participation records. It also supports future features such as attendance, notes, or completion status.

---

## ADR 2: Use Django admin for initial data management

### Status
Accepted

### Context
The project needs a quick and reliable way to create, edit, and test Youth, Program, and Participation data during development.

### Alternatives considered
1. Build custom HTML forms immediately  
   - Pros: more user-friendly for final users  
   - Cons: slower to implement early in development

2. Use Django admin first  
   - Pros: fast setup, built-in CRUD, useful for testing  
   - Cons: not a polished public-facing interface

### Decision
We chose to use Django admin first for rapid development and testing.

### Code reference
- `core/admin.py`

### Consequences
This speeds up development and helps verify the database structure before building more advanced front-end features.

---

## ADR 3: Use function-based views for the first version

### Status
Accepted

### Context
The first version of the project needs simple pages to display youth, programs, and participations.

### Alternatives considered
1. Use class-based views  
   - Pros: reusable and powerful  
   - Cons: harder for beginners to understand at the start

2. Use function-based views  
   - Pros: simple, clear, easy to debug  
   - Cons: may become repetitive in larger systems

### Decision
We chose function-based views for the initial implementation.

### Code reference
- `core/views.py`
- `core/urls.py`

### Consequences
This makes the first version easier to understand and explain. The system can later be refactored to class-based views if needed.