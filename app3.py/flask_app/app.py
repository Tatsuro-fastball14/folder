# -- coding: utf-8 --
from  flask import  Flask,  render_template
from  flask import  Flask,  render_template,  url_for
from  flask import  Flask,  render_template,  request


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html' , 
    title="Index  with  Jinja", 
    message="これはJinjaテンプレートの利用例です。!")
@app.route('/<id>/<password>')
def index2(id,  password):
  msg = f'id:{id}, pass:{password}'
  return  render_template('index.html',title="Index with Jinja", message=msg)

@app.route('/', methods=['GET'])
def index():
    return  render_template('index.html',title="Form  sample",  message="お名前は？" )

@app.route('/', methods=['post'])
def form():
    Field = request.form['field']
    return  render_template('index.html', title="Form sample",  message="こんにちは、%さん!" % field)



if __name__=='__main__':
  app.debug = True
  app.run(host='localhost')



