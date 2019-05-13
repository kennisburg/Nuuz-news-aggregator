from flask import Flask, render_template
from main import newssite, getapn, getreut, getcnbc, getnpr, getbbc



app = Flask(__name__)

@app.route("/")
def index():
  stories = {}
  stories['ap'] = getapn()
  stories['reut'] = getreut()
  stories['cnbc'] = getcnbc()
  stories['npr'] = getnpr()
  stories['bbc'] = getbbc() 
  sites = newssite()
  
  return render_template("index.html", stories=stories, sites=sites)