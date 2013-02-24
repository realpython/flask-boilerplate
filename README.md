#------------------------------------------------------------------------------#
Flask-Boilerplate
=================
#------------------------------------------------------------------------------#

Welcome
-------
Hello. Want to get started with Flask quickly? Good. You are at the right place. This Flask application framework is pre-configured with Flask-SQLAlchemy, Flask-WTF, and the Twiiter Bootstrap frontend. This will get your Flask app up and running on Heroku quickly. Use this starter, boilerplate for all you new Flask projects. Cheers!

Project Structure
--------

    flask-boilerplate/
        static/
            css/
                boostrap-responsive.css
                bootstrap.css
            img/
                glyphicons-halflings-white.png
                glyphicons-halflings.png
            js/
                libs/
                    boostrap.min.js
                    jquery.min.js
                    modernizr-2.0.6.min.js
                plugins.js
                script.js
            favicon.ico
        templates/
            404.html
            500.html
            index.html
            login.html
            register.html
            template.html           
        app.py
        error.log
        forms.py
        models.py

Install
------

Follow these 10 easy steps ...

1. Install [Python](http://install.python-guide.org/), [virtualenv](http://install.python-guide.org/), and [pip](http://install.python-guide.org/) - if you don't already have them, of course
1. Clone this repo: 

            $ git clone git://github.com/mjhea0/flask-boilerplate.git
            $ cd flask-boilerplate

1. Create and activate a virtualenv:
        
            $ virtualenv venv --distribute --no-site-packages
            $ source venv/bin/activate
        
1. Install requirements:
        
            $ pip install -r requirements.txt
