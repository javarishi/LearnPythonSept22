import pymongo as pm

client = pm.MongoClient("mongodb://localhost:27017/")
# creates or connects a new database - testdatabase_sept22
testdatabase_sept22= client["testdatabase_sept22"]
# Create or connect to collection in database
h2k_courses_collection = testdatabase_sept22["h2k_tech_courses"]
'''
result = h2k_courses_collection.find_one()
print(result)
'''
myquery = { 'Price': { "$gt": 499.00 } }
for each_records in h2k_courses_collection.find(myquery, {'_id': 0, 'Name': 1, 'Price': 1}):
    print(each_records)

client.close()