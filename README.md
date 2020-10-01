## A Python Flask Backend application 
### Keywords: Python | Flask | SQLAlchemy | Backend
### Short description:
#### A backend application that accepts valid German
#### license plates, stores them in a database and provides an endpoint to retrieve all stored plates.

### Requirements
#### We first need to install python flask:
```bash
pip install Flask
```
#### Then we install SQLAlchemy
```bash
sudo pip install flask-sqlalchemy
```
#### Before running the server, we need to create the Database 
```bash
python db_creation.py
```
#### In order to run the Flask server, we need to type the follow command:
```bash
export FLASK_APP=LP_server.py
```
#### We are ready to start the server
```bash
flask run
```
#### For dropping the Database
```bash
python drop_db.py
```