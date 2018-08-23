from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1><center>OpenShift (Denis - 23/08) Deploy Python - Flash!</center></h1>"

if __name__ == "__main__":
    application.run()
