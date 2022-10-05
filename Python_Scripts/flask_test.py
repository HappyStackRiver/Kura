from flask import Flask, render_template, abort, url_for, json, jsonify,redirect
import json
import html

app = Flask(__name__, static_url_path='/static')
@app.route("/")
def index():
    Points = f"Scoring data: <a href={url_for('static', filename='Points.json')}>Scoring Data</a>\n"
    Tasks = f" Tasks Completed: <a href={url_for('static', filename='Tasks.txt')}>Tasks</a>\n"
    ReadMe = f"ReadMe: <a href={url_for('static',filename='Readme.html')}>Readme</a>\n"
    Hints = f"Hints: <a href={url_for('static',filename='Hints.html')}>Hints</a>"
    ret = Tasks+Points+ReadMe+Hints
    return(ret)
app.run(host='localhost', debug=True)