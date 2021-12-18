# ------------------------------------------------------------------------ #
# Title: Main
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# # KLMartinez,12.17.2021,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
if __name__ == '__main__':
    import DataClasses as D  # data classes
    import ProcessingClasses as P  # processing classes
    import IOClasses as IO  # IO classes
else:
    raise Exception('This file was not created to be imported')

# Main Body of Script  ---------------------------------------------------- #

IO.GeneralIO.output_welcome()  # Display program description
lstTable = []  # Initialize list of objects

# Load data from text file and create list of objects
# Error handling for FileNotFoundError and general exception built in to P.FileProcessor method
lstFileData = P.FileProcessor.read_data_from_file('EmployeeData.txt')  # Load data from file into a list of rows
for row in lstFileData: # Create list of employee objects using the list of rows
    eObj = D.Employee(row[0], row[1], row[2].strip())  # Create employee object, strip newline
    lstTable.append(eObj)  # Append to list of employee objects

while (True):
    IO.EmployeeIO.print_menu_items()  # Show user a menu of options
    user_choice = IO.EmployeeIO.input_menu_options()  # Get user's menu option choice
    try:  # Try/Except block to catch cases where the user enters a off-menu text
        if user_choice.strip() not in ['1','2','3','4']:
            raise IO.CustomException_UserChoice()  # Custom exception to remind the user to use 1-4, but not quit
    except Exception as e:  # To handle other unexpected error cases, then continue
        print(e)

    if user_choice == '1':  # User choice 1: Show current employee data
        IO.EmployeeIO.print_current_list_items(lstTable)

    elif user_choice == '2':  # User choice 2: Add new employee data
        try:
            employee_id, first_name, last_name = IO.EmployeeIO.input_employee_data()  # Get user entries
            new_eObj = D.Employee(employee_id, first_name, last_name)  # New employee data object
            lstTable.append(new_eObj)  # Append new employee object to the list of data objects
        except Exception as e:
            print()  # Extra line
            print(e)  # Will print the first exception encountered, if there are multiple

    elif user_choice == '3':  # User choice 3: Save employee data to file
        P.FileProcessor.save_data_to_file('EmployeeData.txt', lstTable)
        IO.GeneralIO.output_save_confirmation()

    elif user_choice == '4':  # User choice 4: Exit
        IO.GeneralIO.output_exit_confirmation()
        break

# Main Body of Script  ---------------------------------------------------- #
