from flask import Flask, render_template
app = Flask(__name__)
@app.route("/", methods = ['GET'])
def form_view():
    return render_template('index.html')
