from flask import Blueprint
from flask import request, redirect
from flask import render_template, jsonify, send_from_directory

import os

# template_dir = os.path.abspath('../../templates')
proj_root_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
static_dir = os.path.join(proj_root_dir, 'static')
template_dir = os.path.join(proj_root_dir, 'templates')

api = Blueprint('api', __name__, template_folder=template_dir)

@api.route('/')
def base():
    return render_template('index.html')

@api.route('/info')
def infoz():
    return static_dir

@api.route('/healthz')
def healthcheck():
    return jsonify(status="ok")

# @api.route('/static/<path:filename>')
# def send_static(filename):
#     return send_from_directory(static_dir, filename)

@api.route('/tweet_process')
def process_tweet():
    param_string = ""
    param_dict = {}
    param_dict["otn"] = request.args.get("otn")
    param_dict["oth"] = request.args.get("oth")
    param_dict["otc"] = request.args.get("otc")
    param_dict["itn"] = request.args.get("itn")
    param_dict["ith"] = request.args.get("ith")
    param_dict["itc"] = request.args.get("itc")
    for key in param_dict:
        if param_dict[key] != "":
            param_string += " -" + key + " " + '"' + param_dict[key] + '"'
    os.system("../../tweet_process.py " + param_string + " -s True")
    return render_template("cropped_tweet_temp.html")
