from flask import Flask
from datetime import datetime
from flask import render_template
from flask import request



app = Flask(__name__)

test_id = "Python"
test_pw = "Blockchain"

@app.route("/")

def index():
    return 'Flask 웹사이트다!'


@app.route("/html_sample")
def html_sample():
    return render_template("sample.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method=="POST":
        print("login 버튼을 누름")
        input_value = request.form.to_dict(flat=False)
        print(input_value)
        if (input_value['wallet_id'][0] == test_id) & (input_value['password'][0] == test_pw):
            print("로그인 성공")
            return "로그인 성공!!!!!"
        else:
             return render_template("login.html")
    return render_template("login.html")


app.run()