# Import flask dependencies
from flask import Blueprint, request, render_template, jsonify

# Import module forms
from application.mod_default.forms import SMAForm

# Import functions and utils modules
from application.common import functions
from application.common import utils

# Define the blueprint: 'default', set its url prefix: app.url/
mod_default = Blueprint('auth', __name__)


# Set the route and accepted methods
@mod_default.route('/', methods=['GET', 'POST'])
def home_default():
    smaform = SMAForm()

    return render_template("default/index.html", sma_form=smaform)


@mod_default.route('/default/calculatesma', methods=['GET', 'POST'])
def default_sma():

    if request.method == 'POST':
        jsondata = request.get_json()
        base_sma = int(jsondata['base'])
        periods_sma = jsondata['periods']
        demands_sma = jsondata['demands']

        dataarray = utils.createarraywithtuplespm(periods_sma, demands_sma)
        answer = functions.mms(dataarray, base_sma)

        usermsg = {'status': True, 'msg': "Calculado com sucesso", 'data': answer}

        return jsonify(usermsg)


