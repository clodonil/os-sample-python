from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1><center>OpenShift (OKD 3.10) Deploy Python - Flash!</center></h1>"

if __name__ == "__main__":
    application.run()
