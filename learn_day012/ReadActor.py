from learn_day012.ConnectionTest import get_connection, close_connection
from learn_day012.ActorFile import Actor

read_statement = " SELECT * FROM actor WHERE actor_id > %s "

def get_actor(actorId):
    connection = get_connection()
    cursor = connection.cursor()
    value = (actorId,)
    cursor.execute(read_statement, value)
    # result = cursor.fetchone() # result is single tuple
    result = cursor.fetchall()
    list_actors = []
    for eachRow in result:
        actor = Actor(eachRow[0], eachRow[1], eachRow[2])
        list_actors.append(actor)
    print(list_actors)
    close_connection(connection)
    return list_actors
# executeMany for multiple value --> pass list of tuple


list_of_actors = get_actor(279)