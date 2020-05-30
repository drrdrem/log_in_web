# project/recipes/views.py

#################
#### imports ####
#################

from flask import render_template, Blueprint, request, redirect, url_for, flash, abort, jsonify
from flask_login import current_user, login_required
from web import db, app
from web.models import User
from random import random
from twilio.rest import TwilioRestClient
from werkzeug.utils import secure_filename
import os
import zipfile

from web.model.predict import *

################
#### config ####
################

model_blueprint = Blueprint('model', __name__)

ALLOWED_EXTENSIONS = set(['zip'])

def is_allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

################
#### routes ####
################

@model_blueprint.route('/upload')
@login_required
# print result from the user inquery
def upload():  
    # f = request.files['file']
    # if is_allowed_file(f):
    #     if request.method == 'POST':
    #         return redirect(url_for('model.result'), f)
    return render_template("uploads.html")  

@model_blueprint.route('/results', methods = ['POST'])  
def result():  
    if request.method == 'POST':  
        f = request.files['file']  
        # if is_allowed_file(f):
        try:
            f.save('test.zip')
            with zipfile.ZipFile('test.zip', 'r') as zipObj:
                # Extract all the contents of zip file in current directory
                zipObj.extractall()
            result = run_predic("./test")
            return render_template("results.html", name = result)
        except:
            flash('Please check your uploaded file format.', 'error')
    return render_template("uploads.html")
        