from learn_day012.ConnectionTest import get_connection, close_connection

delete_statement = " DELETE FROM actor WHERE actor_id = %s "

connection = get_connection()
cursor = connection.cursor()
values = ('285',)
cursor.execute(delete_statement, values)
# executeMany for multiple value --> pass list of tuple
connection.commit()
print("Number of rows deleted " , cursor.rowcount)
close_connection(connection)