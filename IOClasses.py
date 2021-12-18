# ---------------------------------------------------------- #
# Title: IOClasses
# Description: A module of IO classes
# ChangeLog (Who,When,What):
# KLMartinez,12.17.2021,Modified script for Assignment09
# Code from RRoot: Listing11
# ---------------------------------------------------------- #
if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')
# Removed Import DataClasses module to keep error handling and object creation in the main script

class EmployeeIO:
    """  A class for performing Employee Input and Output

    methods:
        print_menu_items():

        input_menu_options(): --> (string)

        print_current_list_items(list_of_rows):

        input_employee_data(): --> (employee data object)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class:
    """
    @staticmethod
    def print_menu_items():
        """ Print a menu of choices to the user  """
        print('''
        Menu of Options
        1) Show current employee data
        2) Add new employee data
        3) Save employee data to file
        4) Exit program
        ''')

    @staticmethod
    def input_menu_options():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input('Which option would you like to perform? [1 to 4] - ')).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_list_items(list_of_rows: list):
        """ Print the current items in the list of Employee rows

        :param list_of_rows: (list) of rows you want to display
        """
        print('******* The current employees are: *******')
        for row in list_of_rows:
            print(str(row.employee_id) + ', '
                  + row.first_name + ' ' + row.last_name)
        print('*******************************************')

    @staticmethod
    def input_employee_data():
        """ Gets data to be used as inputs for an employee object

        :return: (3 variables) with input data
        """
        employee_id = (input('What is the employee ID? - ').strip())
        first_name = str(input('What is the employee first name? - ').strip())
        last_name = str(input('What is the employee last name? - ').strip())
        return employee_id, first_name, last_name

class GeneralIO:
    """  A class for performing general Input and Output in the main body of the script

    methods:
        output_welcome():

        output_save_confirmation():

        output_exit_confirmation():

    changelog: (When,Who,What)
        KLMartinez,12.17.2021,Created Class:
    """

    @staticmethod
    def output_welcome():
        """  Display the description of the program to the user

        :return: nothing
        """
        print('\nWelcome to the Employee Data program! \n'
              'This program lets you view, add to, and save a list of employee names and IDs.')

    @staticmethod
    def output_save_confirmation():
        """ Shows the user that the list was saved.

        :return: nothing
        """
        print('Employee list saved.')
        print()  # Extra line

    @staticmethod
    def output_exit_confirmation():
        """ Shows the user that the list was saved.

        :return: nothing
        """
        print('Goodbye!')
        print()  # Extra line

class CustomException_UserChoice(Exception):
    """ Custom error message to raise if the user choice is not 1-4

    :return: nothing
    """
    def __str__(self):
        return 'Oops! Please enter either 1, 2, or 3.'