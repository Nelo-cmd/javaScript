from flask import Flask

from flask import Flask, session, redirect, url_for, request, render_template_string

app = Flask(__name__)

# Set the secret key to use for sessions
app.secret_key = 'your_secret_key_here'  # Replace with a more secure secret key in production!

app.register_blueprint("views", url_prefix = "/views")
app.register_blueprint("auth", url_prefix = "/auth")


if __name__ == '__main__':
    app.run(debug=True)
