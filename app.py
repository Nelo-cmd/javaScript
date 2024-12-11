from flask import Flask
from flask_session import Session
from datetime import timedelta
from flask_wtf.csrf import CSRFProtect
import os 

from flask import Flask, session, redirect, url_for, request, render_template_string

app = Flask(__name__)

# Set the secret key to use for sessions
app.secret_key = os.getenv('FLASK_SECRET_KEY')
app.config["SESSION_PERMANENT"] = False
app.config['SESSION_COOKIE_SECURE'] = True
app.config['WTF_CSRF_SSL_STRICT'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
app.config["SESSION_TYPE"] = "filesystem"
csrf = CSRFProtect(app)

from views import views
app.register_blueprint(views)

from auth import auth
app.register_blueprint(auth)


if __name__ == '__main__':
    app.run(debug=True)
