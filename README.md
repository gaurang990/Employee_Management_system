# Employee_Management_system
# 👨‍💼 Employee Record System (Django)

A web-based **Employee Record System** developed using **Django** that helps organizations manage employee information efficiently. The system allows users to store, view, update, and delete employee records through a simple and user-friendly interface.

## 🚀 Features

* 🔐 User authentication (Login/Logout)
* ➕ Add new employee records
* 📋 View employee details
* ✏️ Update employee information
* 🗑️ Delete employee records
* 🔎 Search and filter employees
* 🏢 Manage department details
* 🗄️ Database management using Django ORM
* 📱 Responsive user interface

## 🛠️ Technologies Used

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, Bootstrap, JavaScript
* **Database:** SQLite
* **Version Control:** Git & GitHub

## 📂 Project Structure

```text
employee-record-system/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── employee_management/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── employees/
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── urls.py
    └── templates/
```

## ⚙️ Installation & Setup

### Clone the repository

```bash
git clone https://github.com/your-username/employee-record-system.git
```

### Navigate to the project directory

```bash
cd employee-record-system
```

### Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Apply database migrations

```bash
python manage.py migrate
```

### Create admin user

```bash
python manage.py createsuperuser
```

### Run the development server

```bash
python manage.py runserver
```

Open the application:

```text
http://127.0.0.1:8000/
```

## 🗃️ Employee Information Managed

The system stores employee details such as:

* Employee ID
* Full Name
* Email Address
* Phone Number
* Date of Birth
* Gender
* Address
* Department
* Job Position
* Joining Date
* Salary Details

## 📝 Usage

1. Login to the system.
2. Add employee information.
3. View employee records.
4. Edit or delete employee details.
5. Manage employee data from the dashboard.

## 🔮 Future Enhancements

* Attendance management
* Payroll management
* Leave management system
* Employee performance tracking
* Export reports to PDF/Excel
* REST API integration
* Role-based access permissions

## 👨‍💻 Author

**Your Name**

GitHub: https://github.com/gaurang990

## 📄 License

This project is created for educational and development purposes.
