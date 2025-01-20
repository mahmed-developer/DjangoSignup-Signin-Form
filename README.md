# DjangoSignup-Signin-Form
First Download Django using pip install django
then=> create a django proj using:
DjangoProj> python -m django startproject registration_system
PS E:......\DjangoProj> cd registration_system

create app  (Actually we have Different apps in Django for Different purposes)
PS E:\.....\DjangoProj\registration_system> python manage.py startapp app1

Go to setting.py in registration_system and add 'app1' name in "installed apps"

then we have our template folder which will have all our Template

and then add it to settings.py in the registration_system.


then add home.html, signup.html , login.html in template


then go to app1 in views.py and Create Views for Each


then for view of Signup go to registration_system => Urls.py and set urls 

then in def ftn SignUp render signup.html

run server using python manage.py runserver


we Also need to make super uuser by running >>python manage.py makemigrations & >>python manage.py migrate
=> and then python mange.py createsuperuser


this way we can go to admin panel 
