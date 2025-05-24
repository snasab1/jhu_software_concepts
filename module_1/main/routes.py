from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/projects/')
def projects():
    return render_template('projects.html')

@main.route('/contact/')
def contact():
    return render_template('contact.html')