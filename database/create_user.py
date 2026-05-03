from database.get_db_connection import get_db_connection

def create_user(username, email, password):
    with get_db_connection() as connection:
        database_cursor = connection.cursor()
        query = """
        INSERT INTO users (username, email, password)
        VALUES (?, ?, ?);
        """        
        database_cursor.execute(query, (username, email, password))                
    print(f"    Created user: {username}, {email}.")
    connection.close()
    print("    Connection securely closed.")