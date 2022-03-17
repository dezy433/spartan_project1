from flask import Flask,request,jsonify
import management
flask_object = Flask(__name__)

@flask_object.route("/",methods = ["GET"])#1-  method: GET, route: /
def home_page():
    welcome = "Welcome to the Devops Server\n"
    tutorial = ("\nAPI is an interface that allows your application to interact with an external service using a simple set of commands.\n You do not need to know the internal logic of the service, just send a simple command and the service will return the necessary data.")
    description = (welcome+"\n"+tutorial + management.app())
    return description
#method: POST, route: /spartan/remove?id=sparta_id
@flask_object.route("/spartan/add",methods = ["POST"])
def echo_func():
    name_var = request.args("name")
    position
if __name__ == "__main__":
    flask_object.run()


