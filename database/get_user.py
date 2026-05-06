from database.get_db_connection import get_db_connection
from handlers.handle_exception import handle_error

def get_user(username, email, password):
    connection = get_db_connection()
    try:        
        database_cursor = connection.cursor()
        query = """
        SELECT 
              id
            , role 
        FROM 
            users
        WHERE
            username = ?
        AND
            email = ?
        AND
            password = ?
        ;
        """
        database_cursor.execute(query, (username, email, password))        
        user_data = database_cursor.fetchone()        
        if user_data:
            return {"id": user_data[0], "role": user_data[1]}
        else:
            print("    User not found")
            return None
    except Exception as e:
        return handle_error(e, username=username, failed_action="get_user")        
    finally:
        connection.close()
        print("    Connection securely closed.")