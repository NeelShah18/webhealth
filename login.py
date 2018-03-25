from pymongo import MongoClient
import hashlib
import random
import cal as cp

sav = ['1000', '1500', '200', '-1200', '3000', '-100']

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['webhealth']
collection = db['login']

def crete_hash(st):
    pass_text = str(st)
    hash_obj = hashlib.sha256(pass_text.encode())
    hash_dig = hash_obj.hexdigest()
    return hash_dig

def isExists(check):
    return bool(db.login.find_one({'Email': str(check)}))

def isVerify(email_txt, password_txt):
    temp = db.login.find_one({'Email': str(email_txt)})
    if temp['Hash_Value'] == crete_hash(password_txt):
        return True
    else:
        return False

def login(email_txt, password_txt):
    flag = False
    result_json = {}
    try:
        if (isVerify(email_txt, password_txt)==True):
            result_json = {
                "flag" : True,
                "Note" : "Welcome!"
            }
        else:
            result_json = {
                "flag" : False,
                "Note" : "Username or Password is wrong"
            }
    except:
        result_json = {
            "falg" : False,
            "Note" : "Server error!"
        }
    return result_json

def update(email_txt, password_txt):
    flag = False
    result_json = {}
    try:
        if(isExists(str(email_txt))==True):
            collection.update({"Email" : str(email_txt)},{ '$set': {"Hash_Value": crete_hash(password_txt)}})
            return_json = {
                "flag" : True,
                "Note" : "Succesfull!"
            }
        else:
            result_json = {
                "flag" : False,
                "Note" : "Username is not exits! Try different Email."
            }
    except:
        return_json = {
            "flag" : False,
            "Note" : "Not succesfull, Sorry!"
        }
    return return_json

def singup(firstname, lastname, username, password, email, food, exer):
    flag = False
    temp_cal = cp.Count_cal(text_food=str(food), text_exe=str(exer))
    userdata_json = {
    "Email" : str(email),
    "Saving" : str(random.choice(sav))
    }
    result_json = {
        "User_Name" : str(username),
        "Hash_Value" : crete_hash(password),
        "Email" : str(email),
        "First_Name" : str(firstname),
        "Last_Name" : str(lastname),
        "Food" : str(food),
        "Exer" : str(exer),
        "cal" : temp_cal,
        "per" : str(cp.Count_per(temp_cal[2])),
        "money" : str(cp.Count_money(cp.Count_per(temp_cal[2])))
    }
    return_json = {}
    try:
        if(isExists(str(email))==False):
            db.userdata.insert_one(userdata_json)
            collection.insert_one(result_json)
            return_json = {
                "flag" : True,
                "Note" : "Succesfull!"
            }
        else:
            result_json = {
                "flag" : False,
                "Note" : "Username is already exits! Try different Email."
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
