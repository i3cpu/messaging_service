# messaging_service

## About

The project involves the development of a messaging service for
sending messages to clients. Users can create, manage, and schedule
message broadcasts with specified rules. The service automatically
sends messages to clients based on defined filters and scheduled times.
Comprehensive statistics are collected for each sent message to
generate reports. Error handling is implemented to ensure that issues
with external services do not affect the stability of message broadcasts.
The API allows users to manage clients, broadcasts, and obtain
statistics.

## User Guide for the System for Sending Newsletters to Clients
1. Make sure you have Python and pip (Python package installer) installed.
2. Activate or create a virtual environment (venv) to isolate the project.
  Install the required dependencies listed in the requirements.txt file using the command:
      pip3 install -r requirements.txt
3.  Perform Django database migrations. Migrations are needed to create database tables related to your project's models. Execute the following commands:
      python3 manage.py makemigrations
      python3 manage.py migrate
5.  Run the Django development server:
      python3 manage.py runserver
6. Activate Celery Worker:
      celery -A messaging_service worker -l INFO
7. Activate Celery Beat:
      celery -A messaging_service beat -l INFO


## Using API Endpoints:

  ### 1) Routes for Clients (clients):
  
    1. Get the List of Clients and Create a New Client::
        ◦ URL: /clients/
        ◦ HTTP Methods: GET, POST

        Example of a Successful Response:
        
  ![image](https://github.com/i3cpu/messaging_service/assets/106595656/a52cf054-db73-44bd-863d-2fa30a3ce36e)


    2. Get, Update, and Delete Client Information by ID:
        • URL: /clients/<int:pk>/
        • HTTP Methods: GET, PUT, DELETE

        Example of a Successful Response:
        
  ![image](https://github.com/i3cpu/messaging_service/assets/106595656/7ef79711-dd6a-49b5-94fd-99fb243d0985)

  ### 2) Routes for Campaigns (сampaigns):

    1. Get the List of Campaigns and Create a New Campaign:
        ◦ URL: /campaigns/
        ◦ HTTP Methods: GET, POST

        Example of a Successful Response:

![image](https://github.com/i3cpu/messaging_service/assets/106595656/5f363ed9-dd81-49fc-ad58-231d7855625a)

  
    2. Get, Update, and Delete Campaign Information by ID:
        ◦ URL: /campaigns/<int:pk>/
        ◦ HTTP Methods: GET, PUT, DELETE 


![image](https://github.com/i3cpu/messaging_service/assets/106595656/35d73dff-85ef-4c19-8d6b-0416f25a4af3)


 ### 3) Routes for Messages(messages):
    1. Get the List of Messages and Create a New Message:
        ◦ URL: /messages/
        ◦ HTTP Methods: GET, POST
       
       Example of a Successful Response:

![image](https://github.com/i3cpu/messaging_service/assets/106595656/4234d3a3-69cb-4e8d-b461-a3d56a444584)

       

    3. Get, Update, and Delete Message Information by ID:
        ◦ URL: /messages/<int:pk>/
        ◦ HTTP Methods: GET, PUT, DELETE

       Example of a Successful Response:

![image](https://github.com/i3cpu/messaging_service/assets/106595656/9fefbe0d-d099-4c0b-bbe1-11087eb1f603)










        




