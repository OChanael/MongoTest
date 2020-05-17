import pymongo

# connect to mongo
myclient = pymongo.MongoClient(
    "mongodb+srv://Ori:OriPass1@cluster0-lkeyg.mongodb.net/test?retryWrites=true&ssl_cert_reqs=CERT_NONE")

print(myclient.list_database_names())

db_list = myclient.list_database_names()
curr_db = myclient['examples']
cluster = curr_db.inventory

# populate database
cluster.insert_many([
   { 'item': "journal", 'qyt': 25, 'status': "A", 'size': { 'h': 14, 'w': 21, 'uom': "cm" }, 'tags': [ "blank", "red" ] },
   { 'item': "notebook", 'qyt': 50, 'status': "A", 'size': { 'h': 8.5, 'w': 11, 'uom': "in" }, 'tags': [ "red", "blank" ] },
   { 'item': "paper", 'qyt': 10, 'status': "D", 'size': { 'h': 8.5, 'w': 11, 'uom': "in" }, 'tags': [ "red", "blank", "plain" ] },
   { 'item': "planner", 'qyt': 0, 'status': "D", 'size': { 'h': 22.85, 'w': 30, 'uom': "cm" }, 'tags': [ "blank", "red" ] },
   { 'item': "postcard", 'qyt': 45, 'status': "A", 'size': { 'h': 10, 'w': 15.25, 'uom': "cm" }, 'tags': [ "blue" ] }
]);

# MongoDB adds an _id field with an ObjectId value if the field is not present in the document

# print everything
for i in cluster.find():
    print(i)

print('\n')

# print item field (names)
for i in cluster.find():
    print(i['item'])

print('\n')

# print status
for i in cluster.find():
    print(i['status'])

print('\n')

# find item with name equal to 'journal'
for i in cluster.find({'item': {'$eq': 'journal'}}):
    print(i)

print('\n')

# insert new item: crackers
cluster.insert_one({'item': 'crackers', 'qyt' : 10, 'status' : 'A', 'size': { 'h': 2, 'w': 2, 'uom': "cm" }, 'tags' : ['white']})

# print everything again
for i in cluster.find():
    print(i)