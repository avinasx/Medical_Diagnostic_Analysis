# Medical_Diagnostic_Analysis
A Django application deployed with docker which works on a pseudo-data of typical medical prescription to extract desired result. The project is in ALPHA PHASE

Steps to deploy using Docker

1. Install Docker from https://hub.docker.com/ and make sure that it is running.(Virtualization should be enabled in BIOS, Docker should have permissions to your local disk and network)

2. Clone/download this github repo

3. Go to/CD to root of this repo

4. RUN "docker run ."   It will install all dependencies

5. RUN "docker-compose up" It will install mysql server and configure it.
   if it throws error like "cannot connect to MySQL server", then Do NOT cancel the process, wait till the process exits and then re-run the same command. Reason being, mysql server requires a little bit time to get onboard after installation.

6. At this point of time, Application is up and you can visit http://localhost:8000/ to use application. BUT Wait!!!!
   ********Database is still not imported, you will get an error, "table not found". We need to import it first.

7. Cancel the running process using "CTRL+C" or "Command+C"(mac).

8. Run app in background mode using "docker-compose up -d"

9. Now to import database, RUN "cat juxt.sql | docker exec -i db /usr/bin/mysql -u root --password=root juxt" in the root directory.

10.Thats it, Now you can visit:  http://localhost:8000/ 

11. Whenever done, stop and remove all containers using "docker-compose -down"



Other way round:

1. Install Python, django
2. Install MySql and uplaod the dump "juxt.sql" to your mysql server
3. Install mysqlclient and connector for python  https://pypi.org/project/mysqlclient/ and https://pypi.org/project/mysql-connector-python/
4. Import database
5. Run migrations.
6. Go(CD) to "Project" folder of this repo
7. Run "python manage.py runserver" 
8. In your browser Go to {root utl} or http://127.0.0.1:8000 to start using


****************************
file details:

juxt.sql: sql dump of the databse;

database.txt: database query and aother details.;

git_error_solution.log: not relavent to project(just some git related bugs and fixes);

A docker file for the project is on the way:)