from flask import Flask, render_template, request
from utils import *
app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def process_data():
    if request.method == 'POST':
        userid = int(request.form['userid'])
        number_show = int(request.form['number_show'])
        result = list(find_similar_users(userid, number_show))
        return render_template('test.html', number_show = number_show, userid = userid, result = result)
    else:
        return render_template('test.html')

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
