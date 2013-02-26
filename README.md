[![Flask-Boilerplate](http://www.backwardsteps.com/4bJIj81361722486.png)](#readme)
------------------------------------------------------------------------------

Currently in beta ...

Welcome
-------
Hello. Want to get started with Flask quickly? Good. You are at the right place. This Flask application framework is pre-configured with Flask-SQLAlchemy, Flask-WTF, and the Twiiter Bootstrap frontend. This will get your Flask app up and running on Heroku or PythonAnywhere quickly. Use this starter, boilerplate for all you new Flask projects. Cheers!

Preview the skeleton app here - [http://www.flaskboilerplate.com/](http://www.flaskboilerplate.com/)

**What is Flask?** Flask is a microframework for Python based on Werkzeug and Jinja2. It's intended for getting started very quickly and was developed with best intentions in mind. :)

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

Deploying to Heroku
------

1. Install [Git](http://git-scm.com/downloads), [Python](http://install.python-guide.org/), [virtualenv](http://install.python-guide.org/), and [pip](http://install.python-guide.org/) - if you don't already have them, of course
1. Sign up for [Heroku](https://api.heroku.com/signup), if you haven't already, and install the [Heroku Toolbelt](https://toolbelt.heroku.com/), if you haven't already.
1. Generate SSH key (use the same email and password used to sign up for Heroku):

            $ heroku login
              Enter your Heroku credentials.
              Email: michael@mherman.org
              Password (typing will be hidden): 
              Could not find an existing public key.
              Would you like to generate one? [Yn]
              Generating new SSH public key.
              Uploading ssh public key /Users/michaelherman/.ssh/id_rsa.pub

3. Clone this repo: 

            $ git clone git://github.com/mjhea0/flask-boilerplate.git
            $ cd flask-boilerplate

3. Create and activate a virtualenv:
    
    Unix:

            $ virtualenv venv --no-site-packages
            $ source venv/bin/activate

    Windows:  

            $ virtualenv venv --no-site-packages
            $ venv\scripts\activate
        
4. Install requirements:
        
            $ pip install -r requirements.txt

1. Create a local repo:
    
            $ git init
            $ git add .
            $ git commit -m "init"

1. Deploy:

            $ heroku create
            $ git push heroku master
            $ heroku ps:scale web=1

1. Test to make sure it's up and running:

            $ heroku ps
            $ heroku open
            
1. You app should look similar to this - [http://www.flaskboilerplate.com/](http://www.flaskboilerplate.com/)
            
1. Having problems? Look at the Heroku error log:

            $ heroku logs

Deploying to PythonAnywhere
------

1. Install [Git](http://git-scm.com/downloads) and [Python](http://install.python-guide.org/) - if you don't already have them, of course
1. Sign up for [PythonAnywhere](https://www.pythonanywhere.com/pricing/), if you haven't already
2. Once logged in, you should be on the Consoles tab. Under the header "Start a new console:" click the link for Bash, which will open a new terminal. 
3. Clone this repo: 

            $ git clone git://github.com/mjhea0/flask-boilerplate.git
            $ cd flask-boilerplate
            
3. Create and activate a virtualenv:

            $ virtualenv venv --no-site-packages
            $ source venv/bin/activate

4. Install requirements:
        
            $ pip install -r requirements.txt

5. Click the link for Dashboard, then the link for Web.
6. Now you need to edit the WSGI file. Update the following line of code:

            project_home = u'/home/realpython/mysite'
to:

            project_home = u'/home/realpython/flask-boilerplate'

7. Save the file, then click the back button. Click the Reload web app. You're now good to go.
8. Click the link to view the live app. You should see something similar to this - [http://www.flaskboilerplate.com/](http://www.flaskboilerplate.com/).

What's next?
---------

1. Using Heroku? Make sure you deactivate your virtualenv once your done deploying: `deactivate`
2. Need to reactivate? (1) Unix - `source venv/bin/activate` (2) Windows - `venv\scripts\activate`
4. Add your Google Analytics ID to the *template.html* file
5. Add a domain name to [Heroku](https://devcenter.heroku.com/articles/custom-domains) or PythonAnywhere via a [CNAME](http://en.wikipedia.org/wiki/CNAME_record) record
5. DEVELOP YOUR APP - need [help](http://www.youtube.com/playlist?list=PLLjmbh6XPGK5pM1QJ8I1ccdGiCTHa1IC8)?
7. Sign up for Github, create a new repo, push your app.

Learn More
---------

1. [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/python)
2. [PythonAnywhere - Help](https://www.pythonanywhere.com/help/)
1. [Flask Documentation](http://flask.pocoo.org/docs/)
2. [Flask Extensions](http://flask.pocoo.org/extensions/)
1. [Real Python for the Web](http://www.realpythonfortheweb.com) :)
        
