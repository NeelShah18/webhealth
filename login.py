from pymongo import MongoClient
import hashlib

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['webhealth']
collection = db['loginDetails']

def crete_hash(st):
    pass_text = str(st)
    hash_obj = hashlib.sha256(pass_text.encode())
    hash_dig = hash_obj.hexdigest()
    return hash_dig

def singup(username, password):
    flag = False
    result_json = {
        "User_Name" : str(username),
        "Hash_Value" : crete_hash(password)
    }
    return_json = {}
    try:
        collection.insert_one(result_json)
        return_json = {
            "flag" : True,
            "Note" : "Succesfull!"
        }
    except:
        return_json = {
            "flag" : False,
            "Note" : "Not succesfull, Sorry!"
        }
    return return_json

def signin():
    flag = False
    return flag
