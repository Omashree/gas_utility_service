# Gas Utility Service Django Application

# Overview
  The Gas Utility Service Django application is designed to provide an online platform for gas utility customers to submit service requests, track the status of their requests, and view their account information. Additionally, customer support representatives can manage service requests and provide support to customers.  
  
# Features
  **- Customer Service Request Submission**: Customers can submit service requests online, including selecting the type of service, providing details, and attaching files.  
  **- Request Tracking**: Customers can track the status of their service requests, view submission dates, and resolution dates.  
  **- Account Information**: Customers can view and update their account information, including address and phone number.  
  **- Customer Support Management**: Support representatives can manage and resolve service requests.  

# Prerequisites
  Python 3.12 or higher  
  Django 5.0.7  
  A virtual environment for Python dependencies  

# Installation
**1. Clone the Repository**
      - git clone https://github.com/yourusername/gas_utility_service.git  
      - cd gas_utility_service  
**2. Set Up a Virtual Environment**  
      - Create and activate a virtual environment:  
      - python -m venv myenv  
      - source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`  
**3. Install Dependencies**  
      - Install the required Python packages:  
      - pip install -r requirements.txt  
**4. Set Up the Database**  
      - Apply the database migrations:  
      - python manage.py makemigrations  
      - python manage.py migrate  
**5. Create a Superuser**  
      - Create a superuser account for accessing the Django admin interface:  
      - python manage.py createsuperuser  
      - Follow the prompts to set up the superuser account.  
**6. Run the Development Server**  
      - Start the Django development server:  
      - python manage.py runserver  
      - Visit http://127.0.0.1:8000/ in your web browser to view the application.  

# Usage Accessing the Application
**Customer Features:**  
  - Submit Request: Navigate to /customer_service/submit_request/ to submit a new service request.  
  - Track Requests: Navigate to /customer_service/track_requests/ to view the status of your service requests.  
  - Account Information: Navigate to /customer_service/account_info/ to view and update your account information.  

**Admin Features:**  
  - Admin Interface: Access the Django admin interface at /admin to manage users, service requests, and other administrative tasks.  

# User Roles
  **- Customer**: Can submit and track service requests, and manage their account information.  
  **- Support Representative**: Can manage and resolve service requests through the Django admin interface.  

# Configuration Settings
  **- Database**: By default, the application uses SQLite. Modify settings.py to configure a different database if needed.  
  **- Static Files**: Static files are served from the static/ directory. Ensure the STATIC_URL and STATIC_ROOT settings are configured correctly.  

# Contributing
  - Fork the repository.  
  - Create a new branch (git checkout -b feature-branch).  
  - Make your changes and commit them (git commit -am 'Add new feature').  
  - Push to the branch (git push origin feature-branch).  
  - Create a pull request.  
