from learn_day012.ConnectionTest import get_connection, close_connection

update_statement = " UPDATE actor SET first_name = %s, last_name = %s, last_update = CURRENT_TIMESTAMP WHERE actor_id = %s "

connection = get_connection()
cursor = connection.cursor()
values = ('KRISHNA', 'CHANDRAWANSHI', '286')
cursor.execute(update_statement, values)
# executeMany for multiple value --> pass list of tuple
connection.commit()
print("Number of rows affected " , cursor.rowcount)
close_connection(connection)