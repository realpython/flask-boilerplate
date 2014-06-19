## Welcome

Hello. Want to get started with Flask quickly? Good. You came to the right place. This Flask application framework is pre-configured with **Flask-SQLAlchemy**, **Flask-WTF**, **Fabric**, **Coverage**, and the **Bootstrap** frontend (among others). This will get your Flask app up and running on Heroku or PythonAnywhere quickly. Use this starter, boilerplate for all you new Flask projects. Cheers!

<hr>

![real-python-logo](https://raw.githubusercontent.com/realpython/about/master/rp_small.png)

Designed for the [Real Python](http://www.realpython.com) course.

<hr>

Preview the skeleton app here - [http://www.flaskboilerplate.com/](http://www.flaskboilerplate.com/)

**EXAMPLE APP: [http://flasktaskr.herokuapp.com/](http://flasktaskr.herokuapp.com/)**

**What is Flask?** Flask is a microframework for Python based on Werkzeug and Jinja2.

Project Structure
--------

  ```sh
  ├── Procfile
  ├── Procfile.dev
  ├── README.md
  ├── app.py
  ├── config.py
  ├── error.log
  ├── forms.py
  ├── models.py
  ├── requirements.txt
  ├── static
  │   ├── css
  │   │   ├── bootstrap-3.0.0.min.css
  │   │   ├── bootstrap-theme-3.0.0.css
  │   │   ├── bootstrap-theme-3.0.0.min.css
  │   │   ├── font-awesome-3.2.1.min.css
  │   │   ├── layout.forms.css
  │   │   ├── layout.main.css
  │   │   ├── main.css
  │   │   ├── main.quickfix.css
  │   │   └── main.responsive.css
  │   ├── font
  │   │   ├── FontAwesome.otf
  │   │   ├── fontawesome-webfont.eot
  │   │   ├── fontawesome-webfont.svg
  │   │   ├── fontawesome-webfont.ttf
  │   │   └── fontawesome-webfont.woff
  │   ├── ico
  │   │   ├── apple-touch-icon-114-precomposed.png
  │   │   ├── apple-touch-icon-144-precomposed.png
  │   │   ├── apple-touch-icon-57-precomposed.png
  │   │   ├── apple-touch-icon-72-precomposed.png
  │   │   └── favicon.png
  │   ├── img
  │   └── js
  │       ├── libs
  │       │   ├── bootstrap-3.0.0.min.js
  │       │   ├── jquery-1.10.2.min.js
  │       │   ├── modernizr-2.6.2.min.js
  │       │   └── respond-1.3.0.min.js
  │       ├── plugins.js
  │       └── script.js
  └── templates
      ├── errors
      │   ├── 404.html
      │   └── 500.html
      ├── forms
      │   ├── forgot.html
      │   ├── login.html
      │   └── register.html
      ├── layouts
      │   ├── form.html
      │   └── main.html
      └── pages
          ├── placeholder.about.html
          └── placeholder.home.html
  ```

### Screenshots

![Pages](https://raw.github.com/mjhea0/flask-boilerplate/master/screenshots/pages.png)

![Forms](https://raw.github.com/mjhea0/flask-boilerplate/master/screenshots/forms.png)


### Quick Start

1. Clone the repo
  ```
  $ git clone https://github.com/mjhea0/flask-boilerplate.git
  $ cd flask-boilerplate
  ```

2. Initialize and activate a virtualenv:
  ```
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

3. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

5. Run the development server:
  ```
  $ python app.py
  ```

6. Navigate to [http://localhost:5000](http://localhost:5000)


Deploying to Heroku
------

1. Signup for [Heroku](https://api.heroku.com/signup)
2. Login to Heroku and download the [Heroku Toolbelt](https://toolbelt.heroku.com/)
3. Once installed, open your command-line and run the following command - `heroku login`. Then follow the prompts:

  ```
  Enter your Heroku credentials.
  Email: michael@mherman.org
  Password (typing will be hidden):
  Could not find an existing public key.
  Would you like to generate one? [Yn]
  Generating new SSH public key.
  Uploading ssh public key /Users/michaelherman/.ssh/id_rsa.pub
  ```

4. Activate your virtualenv
5. Heroku recognizes the dependencies needed through a *requirements.txt* file. Create one using the following command: `pip freeze > requirements.txt`. Now, this will only create the dependencies from the libraries you installed using pip. If you used easy_install, you will need to add them directly to the file.
6. Create a Procfile. Open up a text editor and save the following text in it:

  ```
  web: python run.py
  ```

   Then save the file in your applications root or main directory as *Procfile* (no extension). The word "web" indicates to Heroku that the application will be attached to the HTTP routing stack once deployed.

7. Create a local Git repository (if necessary):

  ```
  $ git init
  $ git add .
  $ git commit -m "initial files"
  ```

8. Create your app on Heroku:

  ```
  $ heroku create <name_it_if_you_want>
  ```

9. Deploy your code to Heroku:

  ```
  $ git push heroku master
  ```

10. View the app in your browser:

  ```
  $ heroku open
  ```

11. You app should look similar to this - [http://www.flaskboilerplate.com/](http://www.flaskboilerplate.com/)

12. Having problems? Look at the Heroku error log:

  ```
  $ heroku logs
  ```

### Deploying to PythonAnywhere

1. Install [Git](http://git-scm.com/downloads) and [Python](http://install.python-guide.org/) - if you don't already have them, of course.

  > If you plan on working exclusively within PythonAnywhere, which you can, because it provides a cloud solution for hosting and developing your application, you can skip step one entirely. :)

2. Sign up for [PythonAnywhere](https://www.pythonanywhere.com/pricing/), if you haven't already
3. Once logged in, you should be on the Consoles tab.
4. Clone this repo:
  ```
  $ git clone git://github.com/mjhea0/flask-boilerplate.git
  $ cd flask-boilerplate
  ```

5. Create and activate a virtualenv:
  ```
  $ virtualenv venv --no-site-packages
  $ source venv/bin/activate
  ```

6. Install requirements:
  ```
  $ pip install -r requirements.txt
  ```

7. Next, back on PythonAnywhere, click Web tab.
8. Click the "Add a new web app" link on the left; by default this will create an app at your-username.pythonanywhere.com, though if you've signed up for a paid "Web Developer" account you can also specify your own domain name here. Once you've decided on the location of the app, click the "Next" button.
9. On the next page, click the "Flask" option, and on the next page just keep the default settings and click "Next" again.
Once the web app has been created (it'll take 20 seconds or so), you'll see a link near the top of the page, under the "Reload web app" button, saying "It is configured via a WSGI file stored at..." and a filename.  Click this, and you get to a page with a text editor.
10. Put the following lines of code at the start of the WSGI file (changing "your-username" appropriately)

  ```
  activate_this = '/home/your-username/flask-boilerplate/venv/bin/activate_this.py'
  execfile(activate_this, dict(__file__=activate_this))
  ```

11. Then update the following lines of code:

  from

  ```
  project_home = u'/home/your-username/mysite'
  ```

  to

  ```
  project_home = u'/home/your-username/flask-boilerplate'
  ```

  from

  ```
  from flask_app import app as application
  ```

  to

  ```
  from app import app as application
  ```

12. Save the file.
13. Go to the website http://your-username.pythonanywhere.com/ (or your own domain if you specified a different one earlier), and you should see something like this - [http://www.flaskboilerplate.com/](http://www.flaskboilerplate.com/).

*Now you're ready to start developing!*

***Need to PUSH your PythonAnywhere repo to Github?***

1. Start a bash console
2. Run:

  ```
  $ ssh-keygen -t rsa
  ```

3. Just accept the defaults, then show the public key:

  ```
  $ cat ~/.ssh/id_rsa.pub
  ```

4. Log in to GitHub.
5. Go to the "Account settings" option at the top right (currently a wrench and a screwdriver crossed)
6. Select "SSH Keys" from the list at the left.
7. Click the "Add SSH key" button at top right.
8. Enter a title (I suggest something like "From PythonAnywhere" and then paste the output of the previous "cat" command into the Key box.
9. Click the green "Add key" button.  You'll be prompted to enter your password.

PUSH and PULL away!

### What's next?

1. Using Heroku? Make sure you deactivate your virtualenv once you're done deploying: `deactivate`
2. Need to reactivate? (1) Unix - `source venv/bin/activate` (2) Windows - `venv\scripts\activate`
4. Add your Google Analytics ID to the *main.html* file
5. Add a domain name to [Heroku](https://devcenter.heroku.com/articles/custom-domains) or PythonAnywhere via a [CNAME](http://en.wikipedia.org/wiki/CNAME_record) record
5. DEVELOP YOUR APP - need [help](http://realpython.com)?

### Learn More

1. [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/python)
2. [PythonAnywhere - Help](https://www.pythonanywhere.com/help/)
1. [Flask Documentation](http://flask.pocoo.org/docs/)
2. [Flask Extensions](http://flask.pocoo.org/extensions/)
1. [Real Python](http://www.realpythonfortheweb.com) :)

