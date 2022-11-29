#DJANGO CHEATSHEET

""" Django is a Python framework used for web development, it's known
for its easy and fast deployment of web apps. It builds around a MVT
(Model-View-Template) design and it configures the patterns to use
automatically, so you can focus only on building the app. """

#Setting up a virtual environment
1. py -m venv {venv_name} #for windows
2. python -m venv {venv_name} #for linux/macOS

#Activate your virtual environment
1. {venv_name}\Scripts\activate.bat #for windows
2. source {venv_name}/bin/activate #for linux/macOS

#Create a project
django-admin startproject {project_name}

#Create an app
django-admin startapp {app_name}

#Make migrations
python manage.py migrate #go inside your project directory to migrate

#Run server
python manage.py runserver #it runs the server on your localhost http://127.0.0.1:8000/

#URLs
urlpatters = [
  path('{template}/', views.{template}, name='template'),
  path('{template}/', views.{template}, name='template'),
  path('{template}/', views.{template}, name='template')
]

#Views
def {template}(request):
  return render(request, '{template}.html', {})
        ###and/or###
def {template}(request):
  action = ###
  context = {
    'action':action
  }
  return render(request, '{template}.html', context)

#Create a superuser
django-admin createsuperuser {superuser}

#Display the usage information
django-admin help

#List of available commands
django-admin help {command}
