# Import dependencies
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Import controllers
from application.mod_default.controllers import mod_default as default_module

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Register blueprint(s)
app.register_blueprint(default_module)

