
def get_xls_file_path():
    try:
        input_file_path = input("File path? ")
        f = open(input_file_path)
        f.close()
        return input_file_path
    except FileNotFoundError:
        print("File Path not correct")
        get_xls_file_path()


def get_number_of_resources():
    try:
        return int(input("Number Of resources? "))
    except ValueError:
        print("the inserted Value should be integer")
        get_number_of_resources()


def get_daily_working_hours():
    try:
        return float(input("Working Hrs? "))
    except ValueError:
        print("the inserted Value should be integer or decimal")
        get_daily_working_hours()
