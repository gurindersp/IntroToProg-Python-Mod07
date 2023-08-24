#-----------------------------------------#
# Title: Assignment07.py
# Desc: This script takes in inputs by user and converts it
#       into binary data and then saves and reads it.
# Change Log: (Who, When, What)
# GPabla, 2023-08-23, Created File
#-----------------------------------------#

import pickle                # This imports code from another file

# Data ---------------------------------------------------------------------- #
file = 'ToDoList.dat'
lst_Work = []
lst_print = []


# Processing  --------------------------------------------------------------- #
def save_data(file_name, lst_data):
    obj_file = open(file_name, "ab")
    pickle.dump(lst_data, obj_file)
    obj_file.close()

def read_data(file_name, rows_you_want):
    counter = 0
    obj_file = open(file_name, "rb")
    while counter < rows_you_want:
        lst_data = pickle.load(obj_file)
        lst_print.append(lst_data)
        counter += 1
    return lst_print


# Presentation (Input/Output)  -------------------------------------------- #
try:
    strTask = input("Please enter in a task: ")
    strPriority = input("Please enter the corresponding priority: ")
    if not strPriority.isnumeric():
        raise Exception("Please only use numbers for the 'Priority' description.")
    else:
        rows = int(input("Please enter how many tasks you would like to see from list: "))

        lstWork = [strTask, strPriority]

        save_data(file, lstWork)                     # This saves list object into binary file
        print(read_data(file, rows))                 # This prints out the list object in binary file


except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')









