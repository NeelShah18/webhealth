from pymongo import MongoClient
import json
import avgCal

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['webhealth']
collection = db['userdata']

def money(email):
    #temp_result = collection.find_one({"Email" : str(email)})
    #return temp_result["Saving"]
    return 0

def get_name(email):
    print(email)
    temp_result = db.login.find_one({"Email" : str(email)})
    print(temp_result)
    username = str(temp_result["First_Name"])+" "+str(temp_result["Last_Name"])
    return str(username)
    #return "test"

def line_value(email):
    return json.dumps(avgCal.valEar)

def get_value(email):
    return 0
