from flask import render_template, Blueprint


blueprint = Blueprint('pages', __name__)


@blueprint.route('/')
def index():
    return render_template("pages/index.html")
