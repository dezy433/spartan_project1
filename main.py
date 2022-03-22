from flask import Flask,request,jsonify
import management
import spartan
import json
flask_object = Flask(__name__)

trainee_db = {}

@flask_object.route("/",methods = ["GET"])#1-  method: GET, route: /
def home_page():
    welcome = "Welcome to the Devops Server\n"
    tutorial = ("\nAPI is an interface that allows your application to interact with an external service using a simple set of commands.\n You do not need to know the internal logic of the service, just send a simple command and the service will return the necessary data.")
    description = (welcome+"\n"+tutorial)

    return description
#http:127.0.0.1:500/employee_record/1 GET on postman, gets the database
#method: POST, route: /spartan/remove?id=sparta_id

@flask_object.route("/echo",methods = ["GET"])
def echo_func():

    name_var = request.args.get("name")
    last_name_var = request.args.get("last_name")
    return f"Reply to the user {name_var}- Positon is {last_name_var}"
"""
@flask_object.route("/spartan/<spartan_id>",methods = ["GET"])
def trainee_getter(spartan_id):
    return f"You're getting info on id{spartan_id}"
"""
@flask_object.route("/spartan_record/<spartan_id>", methods = ["GET"])
def employee_record_getter(spartan_id):
    print("t")

def create_trainee(trainee_id, trainee_first_name, trainee_last_name, trainee_birth_year, trainee_birth_month, trainee_birth_day, trainee_course, trainee_stream):

    trainee = spartan.Spartan(trainee_id, trainee_first_name, trainee_last_name, trainee_birth_year, trainee_birth_month, trainee_birth_day,trainee_course, trainee_stream)
    return trainee

@flask_object.route("/spartan/add",methods =["POST"])
def add_trainee():
    try:
        trainee_data = request.get_json()

        trainee_id = trainee_data["s_id"]
        trainee_first_name = trainee_data["f_name"]
        trainee_last_name = trainee_data["l_name"]
        trainee_birth_year = trainee_data["birth_year"]
        trainee_birth_month = trainee_data["birth_month"]
        trainee_birth_day = trainee_data["birth_day"]
        trainee_course = trainee_data["s_course"]
        trainee_stream = trainee_data["s_stream"]

        trainee_first_name = trainee_first_name.strip()
        trainee_last_name = trainee_last_name.strip()
        trainee_birth_year = trainee_birth_year.strip()
        trainee_birth_month = trainee_birth_month.strip()
        trainee_birth_day = trainee_birth_day.strip()
        trainee_course = trainee_course.strip()
        trainee_stream = trainee_stream.strip()

        if not management.val_trainee_id(trainee_id):
            return "Trainee ID is not valid"
        if not management.val_first_name(trainee_first_name):
            return "Trainee First name is not valid"
        if not management.val_last_name(trainee_last_name):
            return "Trainee Last name is not valid"
        if not management.val_birth_year(trainee_birth_year):
            return " Trainee Birth Year is not valid"
        if not management.val_birth_month(trainee_birth_month):
            return "Trainee Birth month is not valid"
        if not management.val_birth_day(trainee_birth_day):
            return "Trainee Birth day is not valid"
        if not management.val_course(trainee_course):
            return "Trainee Course is not valid"
        if not management.val_stream(trainee_stream):
            return "Trainee Stream is not valid"

        trainee = create_trainee(trainee_id, trainee_first_name, trainee_last_name, trainee_birth_year, trainee_birth_month, trainee_birth_day, trainee_course, trainee_stream)

        trainee_db[trainee.get_sparta_id()] = trainee
        management.save_to_json(trainee_db)
        return f"Added {trainee.sparta_id}, {trainee.first_name} {trainee.last_name} to the database"
    except:
        return "There has been an error"

@flask_object.route("/spartan/<spartan_id>",methods =["GET"])
def get_trainee(spartan_id):
    try:
        trainee = trainee_db[f"{spartan_id}"]
        return f"You have loaded trainee: {trainee}"
    except:
        return "Trainee could not be found"

@flask_object.route("/spartan/", methods=["GET"])
def all_trainee_load():

    with open('data.json',"r") as data_file:
        data = json.load(data_file)
        return data

@flask_object.route( "/spartan/remove/<spartan_id>", methods = ["POST"])
def remove_trainee(spartan_id):
    try:
        trainee = trainee_db[f"{spartan_id}"]
        del trainee_db[f"{spartan_id}"]
        management.save_to_json(trainee_db)
        return f"You have removed trainee: {trainee}"
    except:
        return "There has been an error"

if __name__ == "__main__":
    flask_object.run()


