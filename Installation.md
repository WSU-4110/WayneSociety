# This ReadMe is for our Development Team
## Setting up Flask locally
Flask Website link: https://flask.palletsprojects.com/en/2.0.x/installation/#install-flask


## Installations
Open up an IDE or Code Editor
Preffered: VSCode, Bracket, Pycharm etc...


## Create an Environment
## macOS/Linux
```
$ mkdir Project-Name
$ cd  Project-Name
$ python3 -m venv venv
```

## Activate the Environment
```
$ . venv/bin/activate
```

## Install Flask
```
$ pip3 install Flask
$ pip3 install flask-bcrypt
$ pip3 install Flask-SQLAlchemy
$ pip3 install Flask-Login
$ pip3 install pysqlite3 
```

## Windows
```
> mkdir Project-Name
> cd  Project-Name
> py -3 -m venv venv
```

## Activate the Environment
```
> venv\Scripts\activate
```

## Install Flask
```
> pip3 install Flask
> pip3 install flask-bcrypt
> pip3 install Flask-SQLAlchemy
> pip3 install Flask-Login
> pip3 install pysqlite3 
```



## Running Flask Application Locally
```
$ flask run
```

## Running WayneSociety using Flask
```
$ git clone git@github.com:WSU-4110/WayneSociety.git
$ cd WayneSociety
$ export FLASK_APP=WayneSociety_Project
$ export FLASK_DEBUG=1
$ flask run
On Browser, Open http://localhost:5000/ to view website
```
## Debugging when developing
```
FLASK_DEBUG=1 flask run
This is to keep flask updated every each time a code is changed, instead of having to refresh the browser everytime
```
