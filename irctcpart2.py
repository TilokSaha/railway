import mysql.connector
from tkinter import *
class IRCTC:
    def __init__(self):
        self.conn=mysql.connector.connect(host="localhost",user="root",password="",database="hit")
        self.mycursor=self.conn.cursor()
        self.root=Tk()
        self.root.title("Account Registration")
        self.root.minsize(400,600)
        self.root.minsize(400,600)
        self.root.configure(background="#00a65a")

        self.lable1=Label(self.root,text="Account Registration",bg="#DAA520",fg="#000000")
        self.lable1.configure(font=("constantia",22,"bold"))
        self.lable1.pack(pady=(30,10))
        
        self.root.mainloop()
        self.user_menu()

    def user_menu(self):
        user_input=input("""
                hi! how would you like to proceed?
                1. Enter 1 to register
                2. Enter 2 to login
                3. Anything else to exit
                """)
        if user_input=='1':
            self.register()
        elif user_input=='2':
            self.login()
        else:
            print("Bye")

    def register(self):
        name=input("Enter your name : ")
        email=input("Enter your email : ")
        password=input("Enter your Password : ")
        try:
            self.mycursor.execute("INSERT INTO users (user_id,name,email,password) VALUES (NULL,'{}','{}','{}')".format(name,email,password))
            self.conn.commit()
        except Exception as e:
            print(e)
        else:
            print("Reg successful")

    def login(self):
        email=input("Enter the Email")
        password=input("Enter the password")

        self.mycursor.execute("SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'".format(email,password))
        if len(self.mycursor.fetchall()) ==0:
            print("Not Found")
        else:
            print("Welcome!")

obj=IRCTC()
        
