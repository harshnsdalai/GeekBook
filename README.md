## Project Title
Geek Book
## Getting Started
You can clone code from my github repository.
## Prerequisites
To follow this tutorial, you should have all of the Common Prerequisites for Python installed, including the following packages:
•	Python 3.6
•	pip
•	virtualenv
•	awsebcli

## Installing Locally
1.Create a virtual environment
On Windows Command Prompt, enter the following command at any directory you like(here used C directory):	
C:\> virtualenv env-name
2.Activate virtual env.
	C:\>.\eb-env\Scripts\activate
(eb-env) C:\>	
3. Installing required packages
After cloning app from github to specified directory, open cmd at that directory.Then run following commands(to go to directory where app resides)
	(eb-env) C:\> cd geekbook
	(eb-env) C:\geekbook> 

Then install required packages from requirements.text in app folder using following commands
	(eb-env) C:\geekbook>pip install -r requirements.txt
(eb-env) C:\geekbook>cd hack	
4. Creating database and running locally.
(eb-env) C:\geekbook\hack>python manage.py migrate
(eb-env) C:\geekbook\hack>python manage.py createsuperuser
(eb-env) C:\geekbook\hack>python manage.py runserver
5. Go to your browser and type your local URL on port 8000.This url should be
	http://127.0.0.1:8000/
and you can see the website running.

## Deployment on AWS Elastic Beanstalk

With the AWS Elastic Beanstalk CLI working, the first thing we want to do is create a Beanstalk environment to host the application on. Run this from the project directory (“geekbook”):
$ eb init

This will prompt you with a number of questions to help you configure your environment.
Default region
Choosing the region closest to your end users will generally provide the best performance
Credentials
Next, it’s going to ask for your AWS credentials.
Application name
This will default to the directory name. Just go with that.
Python version
Next, the CLI should automagically detect that you are using Python and just ask for confirmation
Select Python 3.6
SSH
Say yes to setting up SSH for your instances. Then add key value pair for your instances (e.g.aws-bc)
Once eb init is finished, you will see a new hidden folder called .elasticbeanstalk in your project directory.
Configure EB – Create an Environment
1.	Coming back to the terminal, in your project directory(‘geekbook’) type:
$ eb create django-env

The .ebextension is already set up so no need to worry. This directory is used by AWS to locate your wsgi.py and environment variables in your web app.    (For more information on .ebextension and its configuration go to https://realpython.com/deploying-a-django-app-and-postgresql-to-aws-elastic-beanstalk/#customizing-the-deployment-process.)

You should see a bunch of information about the environment being set up displayed to your screen, as well as information about eb trying to deploy. 
     2. When the environment update process completes, open your web site with eb open:
$ eb open

## Built With

* [Bootstrap 4] (https://getbootstrap.com/- The CSS framework used
* [Django v2] (https://docs.djangoproject.com/en/2.2/)
– The web framework used
* [PostgreSQL]( https://www.postgresql.org/) – Database

## Authors

***Harsh Dalai*** - (https://github.com/harshnsdalai)


