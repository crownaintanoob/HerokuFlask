# Simple Python Web App for Heroku

* [This App on Heroku](https://flaskapp01.herokuapp.com)  
* [Python Docs on Heroku](https://devcenter.heroku.com/categories/python-support)  
* [Inception on Heroku](https://github.com/EN10/InceptionHeroku)

#### Install

    sudo pip install heroku gunicorn flask

**Setup Git**

    git init
    git add requirements.txt Procfile app.py  
    git commit -am "init"  
    
**Setup Heroku**

    heroku login
    heroku git:remote -a flaskapp01

**Push to Heroku**

    git push heroku master
    
**Run App Locally:**

    export FLASK_APP=app.py
    flask run --host=0.0.0.0 --port=8080

**Ref:**

* [Flask Example](http://flask.pocoo.org)