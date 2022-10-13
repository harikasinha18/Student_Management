"""Vahini and Harika Sinha"""

# We have created an update function
def Update():  # it is used to edit the information
    import mysql.connector  # imported mysql.connector
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="ChinnI@25_", database="data")  # to connect database using python

    mycursor = mydb.cursor()   # used to execute statements to communicate with the MySQL database
    ask = input("Please Enter The Roll_no Of The Student\n--->")

    info1 = input("Enter Student Name:")
    info2 = input("Enter Student Roll_no:")
    info3 = input("Enter Student College_name:")
    info4 = input("Enter Student Email_ID:")
    info5 = input("Enter Student Course_name:")
    sql = "update Student_info set Name='"+info1+"',Roll_no='" + info2 + "',College_name = '" + info3 + "',Email_ID = '" + info4 + "',Course_name = '" + info5 + "' where Roll_no =" + ask
    mycursor.execute(sql)

    mydb.commit()   # commit() method is used to confirm the changes made by the user to the database.

    con = input("Do you want to continue y/n")
    from Main import main  # importing main
    if con == 'n':
        quit()
    if con == 'y':
        main()

