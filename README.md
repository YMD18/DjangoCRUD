🚀 Setup Instructions for Django CRUD with MySQL
📌 Prerequisites
Before setting up the project, ensure you have:

Python 3.10+ installed → Download here
Django (installed via pip)
MySQL Server installed and running
MySQL Client (for connecting Django with MySQL)

🔧 Installation Steps
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/your-repository.git
cd your-repository
Create and activate a virtual environment (recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install required dependencies

bash
Copy
Edit
pip install -r requirements.txt
Configure MySQL Database

Create a MySQL database:
sql
Copy
Edit
CREATE DATABASE mydatabase;
Update settings.py with your MySQL credentials:
python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '',
        'PORT': '3306'
    }
}
}
Run migrations to set up database tables

bash
Copy
Edit
python manage.py migrate
(Optional) Create a superuser for admin access

bash
Copy
Edit
python manage.py createsuperuser
Start the Django development server

bash
Copy
Edit
python manage.py runserver
Access the application

Open: http://127.0.0.1:8000/
