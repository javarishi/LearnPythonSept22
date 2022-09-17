class Actor:

    def __init__(self, actor_id, first_name, last_name):
        self.actorId = actor_id
        self.firstName = first_name
        self.lastName = last_name
        print("Actor is created ", self.actorId, self.firstName, self.lastName)