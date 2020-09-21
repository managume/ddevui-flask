from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from dotenv import load_dotenv
import os
import yaml
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@main.route('/projects')
@login_required
def projects():
    import subprocess
    cmd = "ddev list -j"
    output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output_json = json.loads(output.communicate()[0])
    return jsonify(output_json["raw"])