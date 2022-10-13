""" Harika Sinha """

# created funtion fetching
def Fetching():
    import mysql.connector # imported mysql.connector
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="ChinnI@25_", database="data") # to connect database using python
    mycursor = mydb.cursor()  # used to execute statements to communicate with the MySQL database
# if user wants to see the detials here we have enter rollno, then the data will be displayed
    ask = input(f"Enter the Roll_no of the student:")
    mycursor.execute(f"select * from Student_info where Roll_no = {ask}")

    myresult = mycursor.fetchall()
# here the detials will be displayed
    for row in myresult:
        print("Name : ", row[0])
        print('Roll no : ', row[1])
        print("College name  : ", row[2])
        print("email_id  :", row[3])
        print("course :", row[4])
        mydb.close()

    con = input("Do you want to continue y/n")
    from Main import main  # importing main
    if con == 'n':
        quit()
    if con == 'y':
        main()


