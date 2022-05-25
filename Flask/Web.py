

from flask import Flask, render_template
from flask import request 
import string,random

app = Flask(__name__)

@app.route("/")
def index():
    return  render_template('index.html')

@app.route("/", methods=['POST'])
def gen_password():
    length = int(request.form.get('password'))
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    characters = lower + upper + num + symbols
    temp = random.sample(characters,length)
    password = "".join(temp)
    return password
if __name__:
    app.run()