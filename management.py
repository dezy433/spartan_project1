from flask import Flask,request,jsonify
import json
import spartan
import main

def val_trainee_id(trainee_id):

    if trainee_id.isdigit():
        return True
    else:
        return False

def val_first_name(trainee_first_name):

    if len(trainee_first_name) >= 2:
        return True
    else:
        return False


def val_last_name(trainee_last_name):

    if len(trainee_last_name) >= 2:
        return True
    else:
        return False

def val_birth_year(trainee_birth_year):

    if trainee_birth_year.isdigit():
        birth_year = int(trainee_birth_year)
        if (birth_year >= 1900) and (birth_year <= 2004):
            return True
        else:
            return False
    else:
        return False
def val_birth_month(trainee_birth_month):

    if trainee_birth_month.isdigit():
        month = int(trainee_birth_month)
        if (month >= 1) and (month <= 12):
            return True
        else:
            return False
    else:
        return False

def val_birth_day(trainee_birth_day):

    if trainee_birth_day.isdigit():
        day = int(trainee_birth_day)
        if (day >= 1) and (day <= 31):
            return True
        else:
            return False
    else:
        return False

def val_course(trainee_course):

    if len(trainee_course) >= 1:
        return True
    else:
        return False

def val_stream(trainee_stream):

    if len(trainee_stream) >= 1:
        return True
    else:
        return False

def save_to_json(trainee_db):
    dict_of_dict = {}
    for trainee_id in trainee_db:
        trainee_obj = trainee_db[trainee_id]
        trainee_dict = trainee_obj.__dict__# it contains all the attributes which describe the object in question. It can be used to alter or read the attributes
        dict_of_dict[trainee_id] = trainee_dict

    with open("data.json", "w+") as data_file:
        json.dump(dict_of_dict, data_file)


def load_from_json():

    with open('data.json', "r") as dict_of_dict:
        data = json.load(dict_of_dict)
        print(data)
