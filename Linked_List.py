""" Satish """

import re  # imported regular expression
import mysql.connector # imported mysql.connector to enables Python programs to access MySQL databases and to store the data.
mydb = mysql.connector.connect(host="localhost", user="root", passwd="AI@12345", database="data") # connected python with database

mycursor = mydb.cursor()  # used to execute statements to communicate with the MySQL database

# created class node
class Node:
    def __init__(self):  # We have created an node function and initialized the node
        # global info1,info2,info3,info4,info5
        try:
            info1 = input("Enter Student Name:")
            while not info1.replace(" ", "").isalpha():
            # user should fill the information given below
                 info1 = input("Your Name Must Contain Atleast Three Charecters And Name Do Not Contain numbers.\nEntre your name: ")
            info2 = input("Enter Student Roll_no:")
            info3 = input("Enter Student College_name:")
            info4 = input("Enter Student Email_ID:")
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}\b'
            while not re.fullmatch(regex, info4):
                info4 = input("please entre a valid mail id: ")
            info5 = input("Enter Student Course_name:")
            # mycursor.execute used to executes the given database operation (query or command)
            mycursor.execute("Insert into Student_info(Name,Roll_no,College_name,Email_ID,Course_name) values(%s,%s,%s,%s,%s)", (info1, info2, info3, info4, info5))
            # here asking user wheather he/she wants to save the data
            data_saving = input("Do You Want To Save The Data.? Yes/Y or No/N\n--->")
            if data_saving == "y":  # if yes, the data will be saved
                mydb.commit()  # commit() method is used to confirm the changes made by the user to the database.
                print("Your Data Has Been saved")
                data_continue = input("Do you want to continue? please enter yes/Y\nDo you want to quit? please enter quit/Q\n--->")
                if data_continue == "y":
                    print("ok")
                if data_continue == "q":
                    quit()
            if data_saving == "n":  # if no, again it asks wheather user wants to edit the data or quit
                update_request = input("Do You Want To Edit The Student Data.? Please Enter Yes/Y\nDo You Want To Quite.? Please Enter Quit/Q\n--->")
                if update_request == "y":  # if user wants to edit the data, here the data function will be called and user can edit the previous data
                    Data() # calling data function here
                    print("Data Has been Updated")
                if update_request == "q":   # if user wants to quit
                    quit()
            self.ref = None
        except mysql.connector.errors.IntegrityError:  # integrityerror exception is raised when the relational integrity of the data is affected
            print("Please Check Student Roll_no & Email_ID\nThese Two Should Be Unique")

# We have created linkedlist class
class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(self)
                n = n.ref

    def add_end(self):
        new_node = Node()
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

#We have created an data function
def Data():
    LL1 = LinkedList()
    LL1.add_end()



