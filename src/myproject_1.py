from flask import Flask, render_template, request
from utils import *
app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def process_data():
    result = ""
    if request.method == 'POST':
        userid = request.form['userid']
        number_show = request.form['number_show']
        result = find_similar_users(userid, number_show)
    return render_template('test.html', result = result)

@app.route("/handle_data", methods=['POST'])
def handle_data():
    userid = request.form['userid']
    return userid+"Success"
 
@app.route("/hello")
def hello():
    return "Hello World!"
 
@app.route("/members")
def members():
    return "Members"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
