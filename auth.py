from flask import Blueprint,render_template,Request,redirect,flash

#create blueprint
auth = Blueprint("auth", __name__, url_prefix="/auth")