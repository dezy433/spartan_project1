from flask import Flask,request,jsonify
import management
import spartan
flask_object = Flask(__name__)

@flask_object.route("/",methods = ["GET"])#1-  method: GET, route: /
def home_page():
    welcome = "Welcome to the Devops Server\n"
    tutorial = ("\nAPI is an interface that allows your application to interact with an external service using a simple set of commands.\n You do not need to know the internal logic of the service, just send a simple command and the service will return the necessary data.")
    description = (welcome+"\n"+tutorial)

    return description
#http:127.0.0.1:500/employee_record/1 GET on postman, gets the database
#method: POST, route: /spartan/remove?id=sparta_id
@flask_object.route("/spartan/add", methods = ["POST"])
def trainee_add(spartan_id):#query string
    data = jsonify()
    return data
@flask_object.route("/spartan/<spartan_id>", methods = ["GET"])
def trainee_getter(spartan_id):#query string


    return f"Informaiton about ID: {spartan_id}"

#  f"Welcome back : {first_name_var}\n Here are you details:\nID: {id_var}\nFirst name: {first_name_var}\n Last name: {last_name_var}\n Birth Year:{birth_year_var}, Birth month:{birth_month_var}\nBirth day: {birth_day_var}\nCourse: {s_course_var}\nStream: {s_stream_var}  "

#@flask_object.route()#this API should return the spartan list as one JSON object.


if __name__ == "__main__":
    flask_object.run()


