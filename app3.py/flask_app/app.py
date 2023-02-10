from flask  import  Flask, render_template

app =Flask(__name__)

@app.route('/')
def test_jinja():
    return  render_template('test_jinja2.html',name="taro")




@app.route('/test_ifa')
def if_testa(name=None):
    name='jiro'
    return render_template('test_if.html',name=name)

@app.route('/test_ifb')
def if_testb(name=None):
    name='sumijiro'
    return  render_template('test_if.html',name=name)

@app.route('/test_for')
def test_for():
    brothers=["太郎","次郎","三郎"]
    return render_template('test_for.html',users=brothers)




app.run(debug=True)