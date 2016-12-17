# Flask Boilerplate

Starter Flask App, powered by Real Python >> http://www.flaskboilerplate.com

## Welcome

Hello. Want to get started with Flask quickly? Good. You came to the right place. This Flask app framework is pre-configured with a number of extensions and packages. Use this starter boilerplate for all your new Flask projects, to get up and running locally and on Heroku or [PythonAnywhere](https://www.pythonanywhere.com/) quickly. Cheers!

<hr>

![real-python-logo](https://raw.githubusercontent.com/realpython/about/master/rp_small.png)

**Designed for the [Real Python](http://www.realpython.com) course.**

<hr>

Preview the skeleton app here - [http://www.flaskboilerplate.com/](http://www.flaskboilerplate.com/)

**EXAMPLE APP: [http://flasktaskr.herokuapp.com/](http://flasktaskr.herokuapp.com/)**

**What is Flask?** Flask is a microframework for Python based on Werkzeug and Jinja2.

Project Structure
--------

```sh
├── Procfile
├── app
│   ├── __init__.py
│   ├── controllers
│   │   ├── __init__.py
│   │   └── pages.py
│   ├── forms.py
│   ├── static
│   │   ├── css
│   │   │   ├── bootstrap-3.0.0.min.css
│   │   │   ├── bootstrap-theme-3.0.0.css
│   │   │   ├── bootstrap-theme-3.0.0.min.css
│   │   │   ├── font-awesome-4.0.1.min.css
│   │   │   ├── layout.forms.css
│   │   │   ├── layout.main.css
│   │   │   ├── main.css
│   │   │   ├── main.quickfix.css
│   │   │   └── main.responsive.css
│   │   ├── fonts
│   │   │   ├── FontAwesome.otf
│   │   │   ├── fontawesome-webfont.eot
│   │   │   ├── fontawesome-webfont.svg
│   │   │   ├── fontawesome-webfont.ttf
│   │   │   └── fontawesome-webfont.woff
│   │   ├── ico
│   │   │   ├── apple-touch-icon-114-precomposed.png
│   │   │   ├── apple-touch-icon-144-precomposed.png
│   │   │   ├── apple-touch-icon-57-precomposed.png
│   │   │   ├── apple-touch-icon-72-precomposed.png
│   │   │   └── favicon.png
│   │   ├── img
│   │   └── js
│   │       ├── libs
│   │       │   ├── bootstrap-3.0.0.min.js
│   │       │   ├── jquery-1.10.2.min.js
│   │       │   ├── modernizr-2.6.2.min.js
│   │       │   └── respond-1.3.0.min.js
│   │       ├── plugins.js
│   │       └── script.js
│   └── templates
│       ├── errors
│       │   ├── 404.html
│       │   └── 500.html
│       ├── forms
│       │   ├── forgot.html
│       │   ├── login.html
│       │   └── register.html
│       ├── layouts
│       │   ├── form.html
│       │   └── main.html
│       └── pages
│           ├── placeholder.about.html
│           └── placeholder.home.html
├── config
│   ├── __init__.py
│   └── development
│       ├── __init__.py
│       └── requirements.txt
├── fabfile.py
├── run.py
├── shell.py
└── tests
    ├── __init__.py
    ├── helpers.py
    └── test_page.py
```

### Screenshots

![Pages](https://raw.github.com/mjhea0/flask-boilerplate/master/screenshots/pages.png)

![Forms](https://raw.github.com/mjhea0/flask-boilerplate/master/screenshots/forms.png)

## Quick Start

1. Clone the repo

  ```
  $ git clone https://github.com/mjhea0/flask-boilerplate.git
  $ cd flask-boilerplate
  ```

1. Initialize and activate a virtualenv:

  ```
  $ pyenv-3.5 env
  $ source env/bin/activate
  ```

1. Install the dependencies:

  ```
  $ pip install -r config/development/requirements.txt
  ```

1. Run the development server:

  ```
  $ python run.py
  ```

  Navigate to [http://localhost:5000](http://localhost:5000)

1. Test:

  ```
  $ py.test tests/
  ```

## Learn More

1. [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/python)
2. [PythonAnywhere - Help](https://www.pythonanywhere.com/help/)
1. [Flask Documentation](http://flask.pocoo.org/docs/)
2. [Flask Extensions](http://flask.pocoo.org/extensions/)
1. [Real Python](http://www.realpythonfortheweb.com) :)
