import pymongo as pm

client = pm.MongoClient("mongodb://localhost:27017/")
# creates or connects a new database - testdatabase_sept22
testdatabase_sept22= client["testdatabase_sept22"]
# List all the databased
list_of_databases = client.list_database_names()
for each_database_name in list_of_databases:
    print(each_database_name)
print("******* TEST_FEB22 **************** ")
TEST_FEB22 = client["TEST_FEB22"]
collection_names = TEST_FEB22.list_collection_names()
for each_collection in collection_names:
    print(each_collection)

# Create or connect to collection in database
h2k_courses_collection = testdatabase_sept22["h2k_tech_courses"]

client.close()