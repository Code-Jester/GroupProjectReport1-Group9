# WorkforceConnect - Group9
Project theme: Economic Strategy and Workforce

Team Members: Brandon - S389937 Cahaya - S387346 Chanveasna - S377961 Kevin - S385480
## Overview
WorkforceConnect is a Django web application developed for Theme 2: Economic Strategy & Workforce. The purpose of this project is to create a simple system that can manage workers, employers, job opportunities, training programs, and applications in one place. The project focuses on workforce planning and supports the idea of connecting people, skills, and employment opportunities through a structured web application.

## Features
- View and manage worker records
- View and manage employer records
- View and manage job opportunities
- View and manage training programs
- Track worker applications for jobs
- Use Django admin to add, edit, and delete data
- View workforce information through a web interface

## Technologies Used
- Python
- Django
- HTML
- CSS

## Project Structure
- `config` – main Django project settings and URL configuration
- `workforce` – main application containing models, views, admin, urls, and templates
- `manage.py` – Django management file
- `static` – CSS files for styling
- `templates` – HTML templates for the user interface

## Requirements
To run this project, you need:
- Python 3.14 or compatible Python 3 version
- Django 6.0.4
- Other required packages listed in `requirements.txt`

Install the required packages by running:
1. ```bash
   pip install -r requirements.txt

## How to Run the Project
1. Open the project folder in VS Code
2. Open the terminal
3. Activate the virtual environment
4. Make Sure Directory in Terminal is :
   ```bash
   \GroupProjectReport1-Group9\workforceconnect
7. Run the server with:
   ```bash
   python manage.py runserver
8. Open Browser and open this url : http://127.0.0.1:8000/
