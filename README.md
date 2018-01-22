# Simple Python Web App for Heroku

[This App on Heroku](https://flaskapp01.herokuapp.com)
[Python on Heroku](https://devcenter.heroku.com/categories/python-support)

#### Install

    sudo pip install heroku gunicorn flask

**Setup Git**

    git init
    git add app.py Procfile requirements.txt 
    heroku git:remote -a flaskapp01
    git commit -am "init"
    git push heroku master
    
**Run App Locally:**

    export FLASK_APP=app.py
    flask run --host=0.0.0.0 --port=8080

**Ref:**

* [Flask Example](http://flask.pocoo.org)
* [Bash in Python](http://blog.nuventure.in/2014/09/04/executing-bash-commands-via-python)