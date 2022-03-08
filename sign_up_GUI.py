from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import login_gui
import loginlogout_controller 


# this class controls the graphical user interface of the Sign Up window. Its methods include createMainFrame, 
# createSignUpUsernamePasswordFrame, createSecurityQuestionFrame, handleSignUpEvent, 
# handleCloseEvent.
class SignUpGUI():
    def __init__(self, master):
        # will update new methods and attribute in class diagram
        self.master = master
        
        self.master.configure(background= "#3E3C3C")
        self.loginlogoutControllerObject = loginlogout_controller.LoginLogoutControllers()
        self.master.title("Sign Up")
        self.createMainFrame()

    '''
    Intent: creates the main frame for the Sign Up GUI
    * Preconditions: master is connected to TKinter. createSignUpUsernamePasswordFrame and createSecurityQuestionFrame
    * have the appropriate GUI codeto be called in this method.
    * Postconditions:
    * Post0. main frame for sign up is created
    '''
    def createMainFrame(self): 
        # logo on top left side
        self.welcomeTitle = Label(self.master, text="Welcome to",font=("Fixedsys", 14),height = 0, width = 40,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=0,column=0, pady=10, padx=0, sticky='w')
        self.title = Label(self.master, text="Zyzzfit",font=("Fixedsys", 40, "bold"),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=1,column=0, pady=0, padx=0)        
        self.createSignUpUsernamePasswordFrame()
        self.createSecurityQuestionFrame()

        self.exitButton = Button(self.master,text="Close",command=lambda: self.handleCloseEvent(), background="red").grid(row = 5,column=0,sticky="se")
        self.SignUpButton = Button(self.master,text="Sign Up",command=lambda: self.handleSignUpEvent(), background="lightgreen").grid(row = 5,column=0)

    '''
    Intent: creates frame with SignUp, Username, and Password entries for the sign up GUI
    * Preconditions: master is connected to TKinter. 
    * Postconditions:
    * Post0. frame with SignUp, Username, and Password entries is implemented for sign up 
    '''
    def createSignUpUsernamePasswordFrame(self):
        # top credentials frame
        self.signUpcredentials = Frame(self.master, width = 450, height = 180,borderwidth=0, background="LightGray").grid(row = 3,column=0,padx=20)
        self.usernameLabel = Label( self.signUpcredentials, text="Enter a Username",font='Fixedsys 13 bold',borderwidth=0, background="LightGray").grid(row = 3,column=0,padx=30,pady=25,ipadx=5,ipady=5, sticky="nw")
        self.passwordLabel = Label( self.signUpcredentials, text="Enter a Password",font='Fixedsys 13 bold',borderwidth=0, background="LightGray").grid(row=3, column=0,padx=30,pady=25, ipadx=5,ipady=5,sticky="w")
        self.reenterPasswordLabel = Label( self.signUpcredentials, text="Reenter the Password",font='Fixedsys 13 bold',borderwidth=0, background="LightGray").grid(row=3, column=0,padx=25,pady=25, ipadx=3,ipady=5,sticky="sw")
        self.usernameEntry = Entry(self.signUpcredentials)
        self.usernameEntry.grid(row = 3,column=0,padx=55,pady=15,ipadx=2,ipady=2, sticky="ne")
        self.passwordEntry = Entry(self.signUpcredentials,show="*")
        self.passwordEntry.grid(row = 3,column=0,padx=55,pady=15,ipadx=2,ipady=2, sticky="e")
        self.reenterPasswordEntry = Entry(self.signUpcredentials,show="*")
        self.reenterPasswordEntry.grid(row = 3,column=0,padx=55,pady=15,ipadx=2,ipady=2, sticky="se")
        self.requirements = Label(self.master, text="Password should be atleast 10 characters, \n have one uppercase letter, and one special symbol(!, #, $, ^, *)", font='Fixedsys 9', background= "Gray").grid(row = 3,column=0,sticky="s",padx=40)
        #self.requirement2 = Label(self.master, text="have one uppercase letter, and one special symbol(!, #, $, ^, *)", font='Fixedsys 9', background= "Gray").grid(row = 3,column=0,sticky='s')
        
    '''
    Intent: creates the frame with the security question for the sign up GUI
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. frame with the security question for sign up is created
    '''
    def createSecurityQuestionFrame(self):
        # security question frame
        self.buttons= Frame(self.master, width = 450, height = 150, borderwidth=0, background="LightGray").grid(row = 4,column=0,padx=20, pady=5)
        self.securityQuestionLabel = Label( self.signUpcredentials, text="Security Question: What is your  favorite food?",font='Fixedsys 13 bold',borderwidth=0, background="white").grid(row=4, column=0,padx=15,pady=15, ipadx=1,ipady=1,stick="n")
        self.securityQuestionEntry = Entry(self.signUpcredentials)
        self.securityQuestionEntry.grid(row = 4,column=0,padx=8,pady=15,ipadx=2,ipady=2)
        
        
    '''
    Intent: handles the close event for sign up GUI. When closed, sign up GUI is closed and login GUI is created and displayed.
    * Preconditions: master is connected to TKinter.
    * loginlogoutController is an instance of the class. 
    * createLoginGUI() is ready to be called from loginlogoutController
    * Postconditions:
    * Post0. sign up GUI is closed and login GUI is created and displayed
    '''
    def handleCloseEvent(self):
        self.master.destroy()
        self.loginlogoutControllerObject.createLoginGUI()


    '''
    Intent: handles the sign up event for sign up GUI
    * Preconditions:    
    * loginlogoutController is an instance of the class. 
    * Postconditions:
    * Post0. signUpUserProcessing() is called by loginlogoutController
    '''
    def handleSignUpEvent(self):
        self.loginlogoutControllerObject.signUpUserProcessing(self.usernameEntry.get(),self.passwordEntry.get(),self.reenterPasswordEntry.get(),self.securityQuestionEntry.get(), self.signUpMaster)
        
            
       
        
            

def main():
    root = Tk()
    root.geometry("550x600")
    signupGUIObject = SignUpGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()

