from flask import Flask#, render_template, request, redirect
# import os
app = Flask(__name__)

@app.route('/')
def main():
    return "Test"
#     return render_template('index.html')

# @app.route('/tweet_process')
# def process_tweet():
#     param_string = ""
#     param_dict = {}
#     param_dict["otn"] = request.args.get("otn")
#     param_dict["oth"] = request.args.get("oth")
#     param_dict["otc"] = request.args.get("otc")
#     param_dict["itn"] = request.args.get("itn")
#     param_dict["ith"] = request.args.get("ith")
#     param_dict["itc"] = request.args.get("itc")
#     for key in param_dict:
#         if param_dict[key] != "":
#             param_string += " -" + key + " " + '"' + param_dict[key] + '"'
#     os.system("tweet_process.py " + param_string + " -s True")
#     return render_template("cropped_tweet_temp.html")