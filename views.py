from flask import Blueprint,render_template,Request,redirect,flash

#create blueprint
bp = Blueprint("views", __name__, url_prefix="/views")