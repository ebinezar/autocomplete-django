
# Autocomplete Engine - Django 3

This project is all about search and list the books, it comes with autocomplete feature, which delivers you the list of books in split of seconds

## Technical Stacks used
* Python version: 3.8.1

* Django: 3.0.7

* Mysql: 5.7

* Docker: 18.09.2

* Docker-Compose: 1.23.2

# Installation Prequesties:

As the application is docker supported, it can be run using the docker compose tool. From here we will be guiding you on installing the application in the Mac OS

## Docker & Docker Compose Installation in OSX

Follow this link for installing docker in the local, Docker compose comes with Docker Desktop by default
https://docs.docker.com/docker-for-mac/install/


## Clone the Application 

Once docker is installed clone the application in your local system by 

`git clone https://github.com/ebinezar/autocomplete-django.git`
`cd autocomplete-django`

## Build the application

`docker build -t autocomplete_app .`

## Run the application
`docker-compose -up -d`

## Sample Data load in the database
`docker exec -it <app name> bash`

`python manage.py makemigrations books`

`python manage.py migrate books`

`python manage.py loaddata --app books books`


Now the application runs in the http://localhost:8080

## curl request for search

`curl -X GET  -H "Content-type: application/json"  -H "Accept: application/json"  "http://localhost:8080/books/search?q=le"`

`[{"title": "Designing Evolvable Web APIs with ASP.NET"}, {"title": "Learning JavaScript Design Patterns"}]`