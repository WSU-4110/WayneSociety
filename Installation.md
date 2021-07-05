# This ReadMe is for our Development Team


## Install Flask
```
$ pip3 install Flask
$ pip3 install flask-bcrypt
$ pip3 install Flask-SQLAlchemy
$ pip3 install Flask-Login
$ pip3 install pysqlite3 
```



## Running WayneSociety using Flask (Mac Os)
```
$ git clone git@github.com:WSU-4110/WayneSociety.git
$ cd WayneSociety
$ python3 -m venv venv
$ . venv/bin/activate
$ export FLASK_APP=WayneSociety_Project
$ export FLASK_DEBUG=1
$ flask run
On Browser, Open http://localhost:5000/ to view website
```

## Running WayneSociety using Flask (Windows)
```
Advice: Use CMD instead of PowerShell
> git clone git@github.com:WSU-4110/WayneSociety.git
> cd WayneSociety
> py -3 -m venv venv
> venv\Scripts\activate
> set FLASK_APP=WayneSociety_Project
> setFLASK_DEBUG=1
> flask run
On Browser, Open http://localhost:5000/ to view website
```
## Debugging when developing
```
FLASK_DEBUG=1 flask run
This is to keep flask updated every each time a code is changed, instead of having to refresh the browser everytime
```
