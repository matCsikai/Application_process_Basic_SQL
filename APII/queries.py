import psycopg2
import ui


def connect(query):
    try:
        # setup connection string8
        connect_str = "dbname='csikai' user='csikai' host='localhost' password='csikai'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
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


def mentors_schools_query():
    # a query that returns the name of the mentors plus the name and country of
    # the school (joining with the schools table) ordered by the mentors id column (columns: mentors.first_name,
    # mentors.last_name, schools.name, schools.country).
    result = connect("""SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                        FROM mentors 
                        INNER JOIN schools
                        ON mentors.city = schools.city
                        ORDER BY mentors.id ASC;""")
    return result
    