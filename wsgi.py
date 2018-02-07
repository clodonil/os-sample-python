from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1><center>OpenShift Deploy Python - Flash!</center></h1>"

if __name__ == "__main__":
    application.run()
