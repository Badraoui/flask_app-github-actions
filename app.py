import os
from flask import Flask




app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "successfully")
    return f"the flask app has been deployed  {name}!"



@app.route("/prod")
def hello_prod():
    name = os.environ.get("NAME", "prod")
    return f"voila le {name}!"

@app.route("/action")
def make_action():
    print('it s working on console')

    return "it s working on browser"




if app == "__main__":

    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8000)))