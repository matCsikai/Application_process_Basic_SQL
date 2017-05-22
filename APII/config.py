import personal_config
import psycopg2


def connect(query):
    try:
        connect_str = personal_config.my_connection()
        # use our connection values to establish a connection
        conn = psycopg2.connect(host=connect_str["host"],
                                user=connect_str["user"],
                                password=connect_str["passwd"],
                                dbname=connect_str["dbname"])
        # set autocommit option, to do every query when we call it
        conn.autocommit = True
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        cursor.execute(query)
        if "SELECT" in query:
            rows = cursor.fetchall()
            return rows
    except Exception as e:
        print("The following error occured:")
        print(e)
        print("\n")