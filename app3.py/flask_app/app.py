# -- coding: utf-8 --
from  flask import  Flask,  render_template
from  flask import  Flask,  render_template,  url_for
from  flask import  Flask,  render_template,  request




app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    data =['one','Two','Three']
    person = {'name':'Taro','mail':'taro@yamada'}
    return render_template('layout.html',title='Template sample',message='これは、サンプルのページです.',data=data,person= person)
    

@app.route('/', methods=['post'])
def form():
    ck  =   request.form.get('check')
    rd  =   request.form.get('radio')
    sel =   request.form.getlist('sel')
    return  render_template('layout.html',   title="Form sample",    message=[ck,rd,sel])





    field = request.form['field']
    return  render_template('index.html', title="Form sample",  message="こんにちは、%s さん!" % field)


if __name__=='__main__':
  app.debug = True
  app.run(host='localhost')



