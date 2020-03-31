# Import dependencies
import os
from os import environ

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = os.urandom(24)

# Set the session cookie to be secure
SESSION_COOKIE_SECURE = True

# Set the secret key to a sufficiently random value
SECRET_KEY = os.urandom(24)

# Static Assets
STATIC_FOLDER = environ.get('STATIC_FOLDER')
TEMPLATES_FOLDER = environ.get('TEMPLATES_FOLDER')

