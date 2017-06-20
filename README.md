
# "Data Deposit portal Development"

Below are the steps to successfully run the django project djtest (Data Deposit Portal)

## Clone the Repository

git clone git@git.zib.de:rdm-deposit/djtest.git

## Creating and Activating Virtual Environment

1. pip install virtualenv (If you already have virtualenv installed, skip this step)

2. cd djtest

3. virtualenv venv

    virtualenv venv will create a folder (venv) in the current directory which will contain all the Python executable files,
    and a copy of the pip library which you can use to install other packages.

4. virtualenv -p /usr/bin/python3.4 venv

    Select Python3.4 as your interpreter (Note : This project will work only for Python 3.0 and above)

5. source venv/bin/activate  (activating virtual environment)

## Install requirements

6. pip install -r requirements.txt

## Running the Django Project

7. python manage.py runserver

    This will start the Django development server on the internal IP at port 8000(default)
    Click on the link  http://127.0.0.1:8000/ to see the development server running and quit the server with Ctrl + C

8. python manage.py makemigrations 

    This will create all necessary models and you need to run this command every-time you make a change to the the model
 
9. python manage.py migrate

    This will create the database(final_database_db) tables for all the models which are stored in migrations.

## Creating the Portal(web) admin

10. python manage.py createsuperuser

    This will create the superuser(admin to the portal) and follow the instructions on the terminal (self-explanatory)
    you can access the admin site using http://127.0.0.1:8000/admin enter the admin credentials for login

## Create roles (groups)

11. In the web Admin page, Under Authentication and Authorization section, Click on Groups to create new roles (groups) such as 
    'Project Admin', 'Transfer Curator' etc and assign the corresponding permissions.

## Create Users

12. In the web Admin page, Under Authentication and Authorization section, Click on Users to create new users and assign them roles.
   
## Add Mandatory metadata Attributes

13. In the web Admin page, Under Metadata Section, Click on MetaDataAttributes and add Project metadata fields. 
   (This has to done only for the first time, for subsequent projects the (project)metadata fields will be automatically added)
   
## Create a New Project 

14. In the web Admin page, Under Projects Section, Click on Project and create a new project and assign a project admin for the newly created project.
    Note. Don't create a project before all the Project metadata attributes for the project has been defined. 

## Deactivating Virtual Environment

15. deactivate

    Once you have finished working on the project, commit the changes to git with a commit message. Then you can deactivate the virtual environment


