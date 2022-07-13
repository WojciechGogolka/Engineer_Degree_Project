from mysql import connector

db_config = {
    'user' : 'root',
    'password' : "adminadmin",
    'host' : 'localhost',
    'database' : 'urlops_database_main'
}

def db_connect():
    connection = None
    try:
        connection = connector.connect(**db_config)
    except connector.Error as err:
        print(f"Connection error: {err.msg}")
        return False
    return connection
