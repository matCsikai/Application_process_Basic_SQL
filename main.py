import ui  # User Interface
import psycopg2
import sys


def choose_query():
    option = input("Please enter a number: ")
    try:
        # setup connection string8
        connect_str = "dbname='csikai' user='csikai' host='localhost' password='csikai'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # set autocommit option, to do every query when we call it
        conn.autocommit = True
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        # run a SELECT statement
        if option == "1":
            cursor.execute("""SELECT first_name, last_name FROM  public.mentors;""")
        elif option == "2":
            cursor.execute("""SELECT nick_name FROM public.mentors WHERE city = 'Miskolc';""")
        elif option == "3":
            cursor.execute("""SELECT first_name || ' ' || last_name AS full_name, phone_number FROM applicants
            WHERE first_name = 'Carol';""")
        elif option == "4":
            cursor.execute("""SELECT first_name || ' ' || last_name AS full_name, phone_number FROM applicants
            WHERE email LIKE '%@adipiscingenimmi.edu';""")
        elif option == "5":
            cursor.execute("""INSERT INTO applicants
            VALUES (11, 'Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823);""")
            cursor.execute("""SELECT * FROM applicants WHERE last_name = 'Schaffarzyk';""")
        elif option == "6":
            cursor.execute("""UPDATE applicants SET phone_number = '003670/223-7459'
            WHERE first_name='Jemima' AND last_name='Foreman';""")
            cursor.execute("""SELECT phone_number FROM applicants WHERE first_name='Jemima' AND last_name='Foreman';""")
        elif option == "7":
            cursor.execute("""DELETE FROM applicants WHERE email LIKE '%@mauriseu.net';""")
        elif option == "0":
            sys.exit(0)
        else:
            raise KeyError("There is no such option.")
        # Fetch and print the result of the last execution
        rows = cursor.fetchall()
        ui.print_query_result(rows)
    except Exception as e:
        print("The following error occured:")
        print(e)
        print("\n")


def handle_menu():
    options = ["Mentors",
               "Mentor nicknames",
               "Query by first name",
               "Query by email domain",
               "Insert applicant",
               "Update applicant",
               "Delete applicant"]

    ui.print_menu("Main menu", options, "Exit program")


def main():
    while True:
        handle_menu()
        try:
            choose_query()
        except KeyError as err:
            ui.print_error_message(err)


if __name__ == '__main__':
    main()