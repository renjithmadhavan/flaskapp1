from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('test.html')
 
@app.route("/hello")
def hello():
    return "Hello World!"
 
@app.route("/members")
def members():
    return "Members"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
