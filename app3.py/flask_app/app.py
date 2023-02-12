from flask import Flask, render_template
from flask import request

app = Flask(__name__)

# トップ画面
@app.route('/')
def index():
    return render_template('index.html')

# get処理の入力フォームを表示
@app.route("/request_get")
def get():
    return render_template('send_get.html')

# getでの入力情報処理
@app.route("/receive_get", methods=["GET"])
def receive_get():
    name = request.args["my_name"]
    if len(name) == 0:
        return "名前が未入力です"
    else:
         return 'あなたが入力した名前は' + str(name) + "です"

@app.route('/')
def test_jinja():
    return  render_template('test_jinja2.html',name="taro")








app.run(debug=True)