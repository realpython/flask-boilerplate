work in progess ... should be complete by Sunday night ..

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

Only four steps!

1. Install [Python](http://install.python-guide.org/), [virtualenv](http://install.python-guide.org/), and [pip](http://install.python-guide.org/) - if you don't already have them, of course
1. Clone this repo: 

            $ git clone git://github.com/mjhea0/flask-boilerplate.git
            $ cd flask-boilerplate

1. Create and activate a virtualenv:
    
- Unix:

            $ virtualenv venv --no-site-packages
            $ source venv/bin/activate

- Windws:  

            $ virtualenv venv --no-site-packages
            $ venv\scripts\activate
        
1. Install requirements:
        
            $ pip install -r requirements.txt

Test Locally
-----------

Only one step! :)

1. Download the gem and then run locally:

            $ gem install foreman heroku
            $ foreman start -f Procfile.dev

Look good? Press CTRL-C to exit.

Deploy to Heroku
----------------

Only 4 steps!!

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

1. Deploy:

            $ heroku create
            $ git push heroku master
            $ heroku ps:scale web=1

1. Test to make sure it's up and running:

            $ heroku ps
            $ heroku open
            
What's next?
---------

1. Deactivate virtualenv: `deactivate`
1. Reactivate virtualenv:

- Unix: `source venv/bin/activate`
- Windows: `venv\scripts\activate`

1. If you need to look at Heroku error logs - `heroku logs`
1. Add your Google Analytics ID to the *template.html* file
1. 


        
