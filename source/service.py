#create a dummy data base

database = {
    1 : "Alice",
    2 : "Bob",
    3 : "Charlie"
}

def get_user_from_db(user_id):
    return database.geta(user_id)