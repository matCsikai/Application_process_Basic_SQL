
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
    