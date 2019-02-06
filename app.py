#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json

from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
import pandas as pd
from logging import Formatter, FileHandler
from forms import *
import os

import random



#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


class Point:
    def __init__(self, lat, lng, count):
        self.lat = lat
        self.lng = lng
        self.count = count

    def to_dict(self):
        return {
            'lat': self.lat,
            'lng': self.lng,
            'count': self.count
        }

def generateRandomPoints(numPoints):
    pointList = []
    for x in range(0, numPoints):
        pointObj = Point(random.randint(-100, 100), random.randint(-100, 100), random.randint(0, 50))
        pointList.append(pointObj)
    return pointList


@app.route('/')
def home():
    df = pd.read_csv('data.csv').drop('Open', axis=1)
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)


    point_data = generateRandomPoints(5000)
    df2 = pd.DataFrame.from_records([ point.to_dict() for point in point_data])
    point_data = df2.to_dict(orient="records")
    point_data = json.dumps(point_data, indent=2)
    
    data = {'chart_data': chart_data, 'point_data': point_data}

    print(data)

    return render_template('pages/placeholder.home.html', data=data)


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/login')
def login():
    form = LoginForm(request.form)
    return render_template('forms/login.html', form=form)


@app.route('/register')
def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)

# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
