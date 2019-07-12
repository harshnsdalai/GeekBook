# Project Title
Tech Takshila
# Getting Started
 Clone the code from bitbucket repository.
# Prerequisites
To follow this tutorial, you should have all of the Common Prerequisites for Python installed, including the following packages:
•	Python 3.6
•	pip
•	virtualenv
•	awsebcli

# Installing Locally
1.Create a virtual environment

On Windows Command Prompt, enter the following command at any directory you like(here used C directory) to create a virtual environment(here named 'eb-env'):	

	C:\> virtualenv eb-env

2.Activate virtual env.
	
	C:\>.\eb-env\Scripts\activate
	
	(eb-env) C:\>	

3. Installing required packages

After cloning app(techtakshila) from github to specified directory in where virtual environment reside(here C directory), ""open cmd at that directory(root directory)"".Then run following commands(to go to directory where app resides)
	
	(eb-env) C:\> cd techtakshila
	
	(eb-env) C:\techtakshila> 

Then install required packages from requirements.text in techtakshila folder using following commands
	
	(eb-env) C:\techtakshila>pip install -r requirements.txt
	
	(eb-env) C:\techtakshila>cd app	

4. Running locally.
	
		(eb-env) C:\techtakshila\app>python manage.py runserver

5. Go to your browser and type your local URL on port 8000.This url should be
	http://127.0.0.1:8000/
			and you can see the website running.

# Deployment on AWS Elastic Beanstalk

With the AWS Elastic Beanstalk CLI working, the first thing we want to do is create a Beanstalk environment to host the
application on. Run this from the project directory (“geekbook”):
	
	$ eb init

This will prompt you with a number of questions to help you configure your environment.

## Default region

Choosing the region closest to your end users will generally provide the best performance
## Credentials

Next, it’s going to ask for your AWS credentials.
## Application name

This will default to the directory name. Just go with that.
## Python version

Next, the CLI should automagically detect that you are using Python and just ask for confirmation
Select Python 3.6

## SSH
Say yes to setting up SSH for your instances. Then add key value pair for your instances (e.g.aws-bc)
Once eb init is finished, you will see a new hidden folder called .elasticbeanstalk in your project directory.

## Transfering static files to S3.
1.Go to the directory where manage.py is located. In this case(C:\techtakshila\app).Then run the following command to upload the static files in S3.
	
	(eb-env) C:\techtakshila\app>python manage.py collectstatic
Note:  If this throws error like aws credentials not defined then, go to settings.py(C:\techtakshila\app\app\settings.py) and then remove the commented tags from the last credentials section that is commented out for running locally and fetching contents locally.Then again run the command above.

## Configure EB 
1.Initiate a git at techtakshila directory and commit all changes(aws uses git for deploy)

2. Go to settings.py(C:\techtakshila\app\app\settings.py) and change deployurl value form
	
		deploy_url = ""#app/"   
	to
	
		deploy_url="app/"
2. Go to views_setup.py in (tectakshila\app\course\views) and do the same changes as mentioned above.
3.Commit new changes to git
4.Coming back to the terminal, in your project directory(‘techtakshila’) where requirements.txt reside type:
	
	$ eb create django-env

The .ebextension is already set up so no need to worry. This directory is used by AWS to locate your wsgi.py and environment variables in your web app.    (For more information on .ebextension and its configuration go to https://realpython.com/deploying-a-django-app-and-postgresql-to-aws-elastic-beanstalk/#customizing-the-deployment-process.)

You should see a bunch of information about the environment being set up displayed to your screen, as well as information about eb trying to deploy. 

5. When the environment update process completes, open your web site with eb open:
	
		$ eb open
6.Browser will pop up and a site will be displayed ,copy url of that site and go to settings.py and in the ALLOWED_HOST = []
paste the url under apostrophe.
	
	ALLOWED_HOST=['example.com']
Set the Debug = False

7. Again commit the changes in git and then run  the deploy command in root("techtakshila")

		$ eb deploy
8. Again run 
	
		$ eb open
Voila you will see the site running in EB

# Built With

* [Materialize CSS] (https://materializecss.com/ The CSS framework used
* [Django v2] (https://docs.djangoproject.com/en/2.2/)
– The web framework used

# Authors

***Harsh Dalai*** - (https://github.com/harshnsdalai)


