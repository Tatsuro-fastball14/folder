from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'welocome to Flask world!'

if __name__=='__main__':
  app.debug = True
  app.run(host='localhost')