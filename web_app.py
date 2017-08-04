from flask import Flask
from wbapp import search4letters
app = Flask(__name__)
@app.route('/')
def hello() -> str:
@app.route('/search4')
def do_search()->str:
  return str(search4letters('life,the universe, and everything', ;eiru')
