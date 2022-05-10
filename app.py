#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import *
from models import *
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
import logging
from logging import Formatter, FileHandler
from forms import *
import os

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

#----------------------------------------------------------------------------#
# Blueprints.
#----------------------------------------------------------------------------#

# from __ import __
# app.register_blueprint(__)

#----------------------------------------------------------------------------#
# Flask_Admin.
#----------------------------------------------------------------------------#

panel = Admin(
    app,
    name='Admin Control Panel',
    template_mode='bootstrap3',
)
panel.add_link(MenuLink(name='Logout', category='', url='/logout'))
panel.add_view(DefaultModelView(User, db.session, column_searchable_list=['username', 'email']))

#----------------------------------------------------------------------------#
# Login.
#----------------------------------------------------------------------------#

login_manager = LoginManager()
login_manager.init_app(app)

class LoginUser(UserMixin):
    @property
    def is_admin(self):
        return self.is_authenticated and self.id == 'admin' 
        # TODO: YOU NEED TO IMPLEMENT THIS!! A SUGGESTION IS ADDING A "ROLE" COLUMN TO THE USER DATABSE


@login_manager.user_loader
def user_loader(username):
    if User.query.filter_by(username=username).first() is None:
        return
    user = LoginUser()
    user.id = username
    return user

#----------------------------------------------------------------------------#
# Controllers.
#    I suggest you create Blueprints for your routes to keep them tidy (up there),
#    but I won't to that here.
#----------------------------------------------------------------------------#

@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')

@app.route('/profile')
@login_required
def profile():
    if current_user.is_admin:
        return """
            Hello, {}
            <br>
            <a href="/admin/">Admin Panel?</a>
            <a href="/logout">Logout</a>
        """.format(current_user.id)
    return """
        Hello, {}
        <br>
        <a href="/logout">Logout</a>
    """.format(current_user.id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.checkPassword(form.password.data):
            luser = LoginUser()
            luser.id = user.username
            if login_user(luser, remember=True):
                return redirect(url_for('profile'))
            else: return "bad"
        else:
            flash('Invalid username or password.')
    return render_template('forms/login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        try:
            db.session.commit()
        except:
            flash('Error: User already exists.')
            return redirect(url_for('register'))
        flash('You are now registered and can log in!', 'success')
        return redirect(url_for('login'))
    return render_template('forms/register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've successfully logged out.", 'success')
    return redirect(url_for('home'))

# Error handlers ------------------------------------------------------------#

@app.errorhandler(500)
def internal_error(error):
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
