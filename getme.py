from pymongo import MongoClient

client = MongoClient()
client = MongoClient('mongodb://neel:shah@ds247078.mlab.com:47078/webhealth')
db = client['webhealth']
collection = db['userdata']

def money(email):
    temp_result = collection.find_one({"Email" : str(email)})
    return temp_result["Saving"]

def get_name(email):
    temp_result = db.login.find_one({"Email" : str(email)})
    username = str(temp_result["First_Name"])+" "+str(temp_result["Last_Name"])
    return str(username)
