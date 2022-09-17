import pymongo as pm

client = pm.MongoClient("mongodb://localhost:27017/")
# creates or connects a new database - testdatabase_sept22
testdatabase_sept22= client["testdatabase_sept22"]
# Create or connect to collection in database
h2k_courses_collection = testdatabase_sept22["h2k_tech_courses"]

# course01 = { "Name" : "H2KInfosys Cloud Course", "Details" : "Introduction to cloud computing",  "Price" : 399.99,}
course_list = [
{ "Name" : "H2KInfosys AWS Course", "Details" : "Introduction to AWS computing",  "Price" : 799.99,},
{ "Name" : "H2KInfosys Azure Course", "Details" : "Introduction to Azure computing",  "Price" : 799.99,},
{ "Name" : "H2KInfosys GCP Course", "Details" : "Introduction to GCP computing",  "Price" : 799.99,}
]
# result = h2k_courses_collection.insert_one(course01)
result = h2k_courses_collection.insert_many(course_list)
print(result.inserted_ids)

client.close()