from flask import Flask, request
import json
from getAttractionsFromName import getAttractions

app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
  return "Hello this is cool"

@app.route('/attractions', method=['GET'])
def attactions():

  return getAttractions(request.args.get('city'))

