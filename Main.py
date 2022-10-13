""" TEAM - 3  STUDENT SYSTEM """
""" Vahini """

# main module
# We have created an main function
def main():
    while True:
        print('\n------------------------ < < * STUDENT ENROLMENT SYSTEM * > >------------------------------')
        print("-----------------------------------------------------------------")
        print("|                   1. Do You Want To Register ?                |")
        print("|                                                               |")
        print("|                   2. Do You Want To See The Details ?         |")
        print("|                                                               |")
        print("|                   3. Do You Want to Edit The Student Data ?   |")
        print("-----------------------------------------------------------------")

        chose = input("Please Choose Any One From The Above: ") #choice giving to user, that the user can chose any option in the following
        if chose == '1':     # user can register by chosing '1'
            print("Please Fill The Following Details")
            from Linked_List import Data
            Data()  # calling data function

        elif chose == '2':   # user can see the detials
            from Data_Fetching import Fetching
            Fetching()  # calling fetching function

        elif chose == '3':   # and then user can edit
            from Data_Updation import Update
            Update()  #calling update funtion

        else:
            print("Please Chose From The Above.")

main() # calling main here
