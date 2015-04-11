from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.bread
collection = db.customers


def adduser(newuser):
    collection.insert(newuser)


def verifylogin(email,password):
    user = collection.find_one({"email":email})
 
    try: 
        return user['password'] == password
    except:
        return False

def verifyemail(email): 
    count = collection.find({"email":email}).count()
    return count == 0 

  
