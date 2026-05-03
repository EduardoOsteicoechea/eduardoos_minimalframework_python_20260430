from database.get_db_connection import get_db_connection

def create_users_table():
    with get_db_connection() as connection:
        database_cursor = connection.cursor()        
        create_users_table_query = """
        CREATE TABLE IF NOT EXISTS users (
              id        INTEGER PRIMARY KEY AUTOINCREMENT
            , username  TEXT NOT NULL
            , email     TEXT UNIQUE NOT NULL
            , password  TEXT NOT NULL
        );
        """
        database_cursor.execute(create_users_table_query)
        print(" -> [✓] Users table is ready.")    
    print("Closing connection")    
    connection.close()
        