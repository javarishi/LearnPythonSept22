import learn_day012.ConnectionTest as ct
insert_query = "INSERT INTO actor (first_name, last_name, last_update) VALUES ( %s, %s, CURRENT_TIMESTAMP)"

connection = ct.get_connection()
cursor = connection.cursor()
# value = ('ARUN', 'KUMAR')
# cursor.execute(insert_query, value)
values = [
    ('KRISHNA', 'YADAV'),
    ('BALRAM', 'YADAV'),
]
cursor.executemany(insert_query, values)
connection.commit()
print("Number of rows inserted " , cursor.rowcount)
ct.close_connection(connection)