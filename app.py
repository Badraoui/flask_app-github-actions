import os
from flask import Flask




app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"



@app.route("/prod")
def hello_prod():
    name = os.environ.get("NAME", "prod")
    return f"voila le {name}!"

@app.route("/action")
def make_action():
    print('it s working on console')

    return "it s working on browser"




if __name__ == "__main__":
    app.run()