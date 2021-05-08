from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

"""
  references :
    https://pymongo.readthedocs.io/en/stable/tutorial.html
    https://www.w3schools.com/python/python_mongodb_query.asp
"""
# connect to the MongoDB.
conn = MongoClient('localhost', 27017)

# Access the testdb database and the emp collection.
db = conn.testdb.emp

# create a dictionary to hold emp details.

# create dictionary.
emp_rec = {}

# set flag variable.
flag = True

my_list = [
  {"name": "Amy", "address": "Apple st 652", "created_at": datetime.now()},
  {"name": "Hannah", "address": "Mountain 21", "created_at": datetime.now()},
  {"name": "Michael", "address": "Valley 345", "created_at": datetime.now()},
  {"name": "Sandy", "address": "Ocean blvd 2", "created_at": datetime.now()},
  {"name": "Betty", "address": "Green Grass 1", "created_at": datetime.now()},
  {"name": "Richard", "address": "Sky st 331", "created_at": datetime.now()},
  {"name": "Susan", "address": "One way 98", "created_at": datetime.now()},
  {"name": "Vicky", "address": "Yellow Garden 2", "created_at": datetime.now()},
  {"name": "Ben", "address": "Park Lane 38", "created_at": datetime.now()},
  {"name": "William", "address": "Central st 954", "created_at": datetime.now()},
  {"name": "Chuck", "address": "Main Road 989", "created_at": datetime.now()},
  {"name": "Viola", "address": "Sideway 1633", "created_at": datetime.now()}
]

#x = db.insert_many(my_list)

# find all documents.
ret = db.find()

print()
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')

# display documents from collection.
for record in ret:
    # print out the document.
    print(str(ObjectId(record.get('_id'))) + ',', record['name'] + ',', record['address']+ ',', record['created_at'])

print()

my_query = {"address": "Central st 954"}
my_doc = db.find(my_query)
for x in my_doc:
    print(x)

# close the conn to MongoDB
conn.close()
