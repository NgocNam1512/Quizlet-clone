# Quizlet-clone

## Get the code
```bash
$ git clone https://github.com/NgocNam1512/Quizlet-clone.git
$ cd Quizlet-clone
```
## Virtualenv modules installation (Unix based systems)
```bash
$ python3 -m venv env
$ source env/bin/activate
```
## Virtualenv modules installation (Windows based systems)
```bash
$ virtualenv env
$ .\env\Scripts\activate
```
## Install modules - SQLite Storage
```bash
$ pip3 install -r requirements.txt
```
## Create tables
```bash
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
## Start the application (development mode)
```bash
$ python3 manage.py runserver # default port 8000
```
