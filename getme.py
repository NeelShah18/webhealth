from pymongo import MongoClient
import json
import avgCal

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['webhealth']
collection = db['userdata']

def get_name(email):
    #print(email)
    temp_result = db.login.find_one({"Email" : str(email)})
    #print(temp_result)
    username = str(temp_result["First_Name"])+" "+str(temp_result["Last_Name"])
    return str(username)
    #return "test"

def line_value(email):
    return str(avgCal.valEar)

def get_per(email):
    temp_result = db.login.find_one({"Email" : str(email)})
    per = str(temp_result['per'])
    return str(per)

def get_money(email):
    temp_result = db.login.find_one({"Email" : str(email)})
    money = str(temp_result['money'])
    return str(money)
