import json
import spartan



def read_trainee_id():
    while True:
        id_str = input("Please enter the Trainee ID:")
        id_str = id_str.strip()

        if id_str.isdigit():
            id = int(id_str)
            if id > 0:
                return id
            else:
                print("Error, The Trainee ID should be positive number")
        else:
            print("Error, The Trainee ID should be a number")



def read_first_name():
    while True:
        first_name = input("Please enter the trainee first name")
        first_name = (first_name.strip())
        if len(first_name) >= 2:
            return first_name
        else:
            print("Error, Trainee name has to be at least 2 characters")

def read_last_name():
    while True:
        last_name = input("Please enter the Trainee last name")
        last_name = last_name.strip()
        if len(last_name) >= 2:
            return last_name
        else:
            print("Error,Trainee last name has to be at least 2 characters")

def read_year():
    while True:
        year_str = input("Please enter the Trainee Birth Year:")
        year_str = year_str.strip()

        if year_str.isdigit():
            year = int(year_str)
            if (year >= 1900) and (year <= 2004):
                return year
            else:
                print("Error, The Trainee Birth Year should be between 1900 and 2004")



def read_month():
    while True:
        month_str = input("Please Enter the Trainee Birth Month:")
        month_str = month_str.strip()

        if month_str.isdigit():
            month = int(month_str)
            if (month >= 1) and (month <= 12):
                return month
            else:
                print("Error, The Trainee Birth Month should be between 1 and 12")
        else:
            print("Error, The Trainee Birth Month should be a number")


def read_day():
    while True:
        day_str = input("Please Enter the Trainee Birth Day:")
        day_str = day_str.strip()

        if day_str.isdigit():
            day = int(day_str)
            if (day >= 1) and (day <= 31):
                return day
            else:
                print("Error, The Trainee Birth Day should be between 1 and 31")
        else:
            print("Error, The Trainee Birth Day should be a number")

def read_course():
    while True:
        course = input("Please Enter The Trainee Course:")
        course = course.strip()

        if len(course) >= 1:
            return course
        else:
            print("Error, The Trainee Course should be at least 1 Characters")

def read_stream():
    while True:
        stream = input("Please Enter The Trainee Stream:")
        stream = stream.strip()

        if len(stream) >= 1:
            return stream
        else:
            print("Error, The Trainee stream should be at least 1 Characters")

def create_trainee():
    trainee_id = read_trainee_id()
    trainee_first_name = read_first_name()
    trainee_last_name = read_last_name()
    trainee_birth_year = read_year()
    trainee_birth_month = read_month()
    trainee_birth_day = read_day()
    trainee_course = read_course()
    trainee_stream = read_stream()

    trainee = spartan.Spartan(trainee_id,trainee_first_name, trainee_last_name, trainee_birth_year, trainee_birth_month, trainee_birth_day,trainee_course, trainee_stream, )
    return trainee

def add_trainee():

    trainee = create_trainee()

    trainee_db[trainee.get_sparta_id()] = trainee
    print("The trainee was added to the list")
    save_to_json()

def print_trainee_db():
    global trainee_db
    for entry in trainee_db:
        print(trainee_db[entry])

def print_all_trainee_data():
    for trainee_id_key in all_trainee_dict:
        print(f"The data of the Trainers with Trainee_ID = {trainee_id_key}")
        print(all_trainee_dict[trainee_id_key])

def save_to_json():
    global trainee_id
    temp_dict_of_dict = {}
    for trainee_id in all_trainee_dict:
        trainee_obj = all_trainee_dict[trainee_id]
        trainee_dict = trainee_obj.__dict__
        temp_dict_of_dict[trainee_id] = trainee_dict

    with open("data.json", "w+") as data_file:
        json.dump(temp_dict_of_dict, data_file)


def load_from_json():

    with open('data.json', "r") as temp_dict_of_dict:
        data = json.load(temp_dict_of_dict)
        print(data)
"""      
        for spartan in spartans:
            spartanDict = json.loads(spartan)
            #spartanList.append(spartanDict)
            print(spartanDict)
"""
def read_options():
    while True:
        options = input("Options: \nadd) Add an Trainee \nremove) Remove an Trainee\nlist) List of Trainees \nupdate) Update Trainee Data \nsave) Save \nload)Load\nexit) Exit\n")
        options = options.strip()
        if options in ["add", "remove", "update", "list", "save","load","exit"]:
            return options
        else:
            print("Error, You should select one of the options in the list")

if __name__ == "__main__":
    all_trainee_dict = {}

    while True:
        option = read_options()

        if option == "add":
            print("The user wants to add an Trainee")
            trainee_object = create_trainee()

            trainee_id = trainee_object.get_sparta_id()
            all_trainee_dict[trainee_id] = trainee_object
            print(all_trainee_dict.get(trainee_id))


            save_to_json()

        elif option == "remove":
            print("The user wants to remove an trainee")
            trainee_id = read_trainee_id()
            del all_trainee_dict[trainee_id]


        elif option == "list":
            print("The user wants a list of the trainee")
            print_all_trainee_data()
            load_from_json()

        elif option == "save":
            save_to_json()

        elif option == "load":

            load_from_json()

        elif option == "exit":
            print("You have exited")
            break
        else:
            print("Unknown option")