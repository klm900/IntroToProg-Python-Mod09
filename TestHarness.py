# ---------------------------------------------------------- #
# Title: TestHarness
# Description: A main module for testing
# ChangeLog (Who,When,What):
# KLMartinez,12.17.2021,Modified script for Assignment09
# Code from RRoot: Listing08,Listing10,Listing12
# ---------------------------------------------------------- #
if __name__ == "__main__":
    import DataClasses as D  # data classes
    import ProcessingClasses as P  # processing classes
    import IOClasses as IO  # IO classes
else:
    raise Exception("This file was not created to be imported")

# Test data module, Person class
print('Testing Person class from DataClasses module:')
objP1 = D.Person("Jane", "Austen")
objP2 = D.Person("Charlotte", "Bronte")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))
print()  # Extra line

# Test data module, Employee class
print('Testing Employee class from DataClasses module:')
objP1 = D.Employee(1, "George", "Eliot")
objP2 = D.Employee(2, "Willa", "Cather")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))
print()  # Extra line

# Test processing module
print('Testing ProcessingClasses module:')
P.FileProcessor.save_data_to_file("TestEmployeeData.txt", lstTable)  # Save lstTable from Employee class test
print('File saved: see TestEmployeeData.txt')
lstFileData = P.FileProcessor.read_data_from_file("TestEmployeeData.txt")  # Load data back to a list of rows
print('Reading from file:')
for row in lstFileData:
    eObj = D.Employee(row[0], row[1], row[2].strip())  # Create employee object for each row, then print
    print(eObj.to_string().strip(), type(eObj))
print()  # Extra line

# Test IO classes
print('Testing IOClasses module:')
IO.EmployeeIO.print_menu_items()  # Print menu
user_choice = IO.EmployeeIO.input_menu_options()  # User selection from menu
print('You entered: ' + user_choice)  # Print back user choice to confirm
print()  # Extra line
IO.EmployeeIO.print_current_list_items(lstTable)  # Print current table
employee_id, first_name, last_name = IO.EmployeeIO.input_employee_data()  # User entry for new employee
new_eObj = D.Employee(employee_id, first_name, last_name)  # Create employee object from entry
print('New employee object:')
print(new_eObj.to_string().strip(), type(new_eObj))  # Print back user input to confirm
