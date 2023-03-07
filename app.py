import os
from flask import Flask
import json
from flask_cors import CORS








app = Flask(__name__)
CORS(app)



@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "successfully")
    return f"the flask app has been deployed {name}!"

@app.route("/getTasks")
def getTasks():
 
    x =  ' [{ "id" :1, "text": "Doctors appointments", "day":"1st january 2023", "reminder":true},\
        { "id" :2, "text": "Doctors appointments", "day":"1st january 2023", "reminder":true}, \
    { "id" :3, "text": "Doctors appointments", "day":"1st january 2023", "reminder":true} ]'
    y = json.loads(x)
    return y



@app.route("/prod")
def hello_prod():
    name = os.environ.get("NAME", "prod")
    return f"voila le {name}!"

@app.route("/action")
def make_action():
    print('it s working on console')

    return "it s working on browser"




if __name__ == "__main__":

    app.run(debug=True,host='127.0.0.1',port=int(os.environ.get('PORT', 8080)))