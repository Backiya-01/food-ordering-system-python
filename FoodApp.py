# food ordering system 

from User import User
from UserManager import UserManager
from mainmenu import MainMenu


class LoginSystem:

    def Login(self):
        mailid=input("Email Id : ")
        password = input("Password:")

        user=UserManager.FindUser(mailid=mailid,pwd=password)
        if user is not None:
            print("Login Successfull")
            menu=MainMenu()
            menu.Start()
        else:
            print("Invalid MailId/Password....please Retry")


    def Register(self):

    # Name validation
        while True:
            name = input("Name : ")
            if name.isalpha() and len(name) >= 3:
                break
            else:
                print("Invalid name! Use only letters (min 3 characters)")

    # Mobile number validation
        while True:
            mobile = input("Mobile No : ")
            if mobile.isdigit() and len(mobile) == 10:
                mobile = int(mobile)
                break
            else:
                print("Invalid mobile number! Enter 10 digits")

    # Email validation
        while True:
            mailid = input("Email Id : ")
            if "@" in mailid and ".com" in mailid:
                break
            else:
                print("Invalid email format!")

    # Password validation
        while True:
            password = input("Password : ")
            if len(password) >= 6:
                break
            else:
                print("Password must be at least 6 characters")

        print("\nRegistration Successful!")

        user=User( name= name, phn= mobile, mail= mailid, pwd= password)
        UserManager.AddUser(user)


    def GuestLogin(self):
        pass

    def Exit(self):
        print("Thank You For Using")
        exit()
        
    def validateoption(self,option):
            getattr(self,option)()
            


class FoodApp:

    LoginOptions ={1:"Login",2:"Register",3:"Guest",4:"Exit"}

    @staticmethod
    def Welcome(): #Initial Method
        print("<< Welcome to Online food Ordering >>")

        loginsystem=LoginSystem()


        while True:
            for option in FoodApp.LoginOptions:
                print(f"{option}.{FoodApp.LoginOptions[option]}",end="  ")
            print()
            try:
                choice=int(input("Please Enter Your Choice : "))
                loginsystem.validateoption(FoodApp.LoginOptions[choice])
            except (ValueError,KeyError):
                print("Invalid input..Please Enter the Valid Choice")