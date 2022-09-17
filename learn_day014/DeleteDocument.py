import pymongo as pm

client = pm.MongoClient("mongodb://localhost:27017/")
# creates or connects a new database - testdatabase_sept22
testdatabase_sept22= client["testdatabase_sept22"]
# Create or connect to collection in database
h2k_courses_collection = testdatabase_sept22["h2k_tech_courses"]
myquery = { 'Price': 399.99 }

# run the example for delete many

result = h2k_courses_collection.delete_one(myquery)
print(result.deleted_count, " documents deleted.")
client.close()