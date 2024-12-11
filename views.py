from flask import Blueprint,render_template,Request,redirect,flash

#create blueprint
views = Blueprint("views", __name__, url_prefix="/")

@views.route('/')
def home():
    return "Hello from views!"