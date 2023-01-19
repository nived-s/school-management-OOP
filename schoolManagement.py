import time
from dataclasses import dataclass

@dataclass
# Parent class containing all details of student
class Student():
    """ def __init__(self , stud_name, stud_age, stud_reg_no):
        self.stud_name = stud_name
        self.stud_age = stud_age
        self.stud_reg_no = stud_reg_no """
    # above init method code can be reduces by using data clasess
    stud_name: str
    stud_age: int
    stud_reg_no: int

    def stud_details(self):
        # checking if stud_list is empty
        if len(list_of_students) == 0:
            print("no data to show")

        else:
            # Looping thro all students list and displaying
            print("{0}\t{1}\t{2}".format('Name', 'Age', 'RegNo'))
            for i in list_of_students:
                print(f"{i[0]}\t{i[1]}\t{i[2]}")

        print("* "*12 ,"\n")
        # Waiting 1 sec before showing main menub
        time.sleep(1)

    def stud_add_new(self):
        # Inputing data
        self.stud_name = input("Enter name:")
        self.stud_age = int(input("Enter age:"))
        self.stud_reg_no = int(input("Enter register number:"))

        # Adding to all student list 
        list_of_students.append([self.stud_name, self.stud_age, self.stud_reg_no])
        print("\nNew student added seccessfully. \n")
        time.sleep(0.5)

    def stud_delete(self, data_count):
        self.data_count = data_count
        del list_of_students[data_count-1]
        print("\nDeletion seccessful.\n")
        time.sleep(0.5)

# Function displays all options user can select from
def user_options():
    print("1) Add\n2) Delete\n3) Display\n4) Exit")

# All students will be added to list in form of individual tuples containg name, age, regno
list_of_students = []
# Blank object for function calling it will be updated in parent class
empty_obj = Student('', 0, 0)

# Main deiver code
# Program starts here >>>
if __name__ == "__main__":

    # main loop for user input and exit program
    while True:
        try:
            # user selects from available options
            user_options()
            usr_choice = int(input("Enter choice: "))
            

        except ValueError:
            # if user inputs non-integer
            print("Enter a integer between 1 to 5: ")
            continue

        #loops though availabe options to call the required function from  main class
        if usr_choice in range(1 , 5):
            print("\n")
            if usr_choice == 1:
                # Insert
                empty_obj.stud_add_new()

            elif usr_choice == 2:
                # delete
                toDelete = int(input("Enter reg no of student to delete:"))
                # Flag to stop looping till the reg no is found, if not found return reg no(student) not found
                found = True

                # data_count contains the index of list that we searching for
                data_count = 0
                # data is list with index as 'data_count' it can to passed to function to directly acces reg no for easy access rather than looping for second time
                for data in list_of_students:
                    data_count += 1
                    while found:
                        if data[2] == toDelete:
                            found = False
                            empty_obj.stud_delete(data_count)

                if found == True:
                    print("Reg No not found.") 
                    continue

            elif usr_choice == 3:
                # display
                empty_obj.stud_details()

            elif usr_choice == 4:
                # exit
                print("closing program")
                exit()
            
            else:
                break
        else:
            print("Value must be between 1 and 5 !\n")
            time.sleep(0.5)