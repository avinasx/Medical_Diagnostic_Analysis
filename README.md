# Medical_Diagnostic_Analysis
A Django application deployed with docker which works on a pseudo-data of typical medical prescription to extract desired result. The project is in ALPHA PHASE

How to use:
1. Install Python, django
2. Install MySql and uplaod the dump "juxt.sql" to your mysql server
4. Run migrations.
2. Go(CD) to "Project" folder of this repo
3. Run "python manage.py runserver" 
4. In your browser Go to {root utl} or http://127.0.0.1:8000 to start using


You won't have to install mysql or django(python) when using docker file(comming soon)


****************************
file details:

juxt.sql: sql dump of the databse;

database.txt: database query and aother details.;

git_error_solution.log: not relavent to project(just some git related bugs and fixes);

A docker file for the project is on the way:)