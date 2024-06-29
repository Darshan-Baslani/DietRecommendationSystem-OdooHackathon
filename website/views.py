from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
def home():
    print(url_for('static', filename='css/common.css'))
    return render_template('index.html',user=current_user)


@views.route('/index.html')
def home2():
    return render_template('index.html', user=current_user)
