# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

# Import module forms
from application.mod_default.forms import SMAForm

# Define the blueprint: 'default', set its url prefix: app.url/
mod_default = Blueprint('auth', __name__)


# Set the route and accepted methods
@mod_default.route('/', methods=['GET', 'POST'])
def home_default():
    smaform = SMAForm(request.form)

    return render_template("default/index.html", sma_form=smaform)

