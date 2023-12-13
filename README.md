# A Book Store Backend

This is a Book Store backend application implementing RESTful API and CRUD operations using Django Rest Framework, Python and SQLite3 as the database.

***
***
## Prerequisites

- Python=>3.10

***
***
## Getting started

First you will need to clone down the project onto your local machine

1) Create a new directory on your local machine. 

  

2) Navigate into the newly created directory and open a terminal here.

  

3) You can now clone the repository using several ways;

```

#option 1 - HTTPS

git clone https://github.com/Asif-GD/a-django-book-store.git



#option 2 - Download.zip

you will have the option to down the entire repository as an archived folder on github.com

```



4) Navigate into the project directory; a-django-book-store-master. I will refer this as root directory

```
cd a-django-book-store-master
```



5) Inside the root directory, let's setup the virtual environment for the project.

```
python -m venv venv
```



6) Now, activate this virtual environment.

```

# windows machine

venv\Scripts\Activate

  

#mac/linux

source venv/bin/activate

```

You will know your virtual environment is active when your terminal displays the following:

```

(venv) path\to\project\drf_course>

```



7) Packages and requirements - This project will rely on a lot of 3rd party packages (requirements) to function. I have created a requirements.txt file. Check out /a-django-book-store-master/requirements.txt. Install them all using the command as below

```
pip install -r requirements.txt
```

This should successfully setup the project on your local machine and ready for use.



8) Start the server. The command below is used to start our Django server on our local machine with default values of local host and port.

```
python manage.py runserver
```

You should now have a server running on http://127.0.0.1:8000/

***
***