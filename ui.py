# This function generate outputs like this:
# Main menu:
# (1) Mentors
# (2) Mentor nicknames
# (3) Query by first name
# (4) Query by email domain
# (5) Insert applicant
# (6) Update applicant
# (7) Delete applicant
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")
def print_menu(title, list_options, exit_message):
    print(title)
    for option in enumerate(list_options):
        print("({0}) {1}".format(option[0] + 1, option[1]))
    print("({0}) {1}".format("0", exit_message))
    print("\n")

# This function prints the query results
#
# result_tuples: list of tuples - the query results
def print_query_result(result_tuples):
    for tuples in result_tuples:
        joined = ' '.join(tuples)
        print(joined)
    print("\n")

# This function prints an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    print("Error: {0}".format(message))
    