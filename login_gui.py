from tkinter import *
import tkinter as tk
from tkinter import ttk
import loginlogout_controller 



# this class controls the graphical user interface of the Log In window. Its methods include createMainFrame, createUsernamePasswordFrame,
# createLoginSignUpForgetPasswordFrame, handleLoginEvent, createSignUpGUI, closeWindow, and createForgetPassword.
class LoginGUI():
    def __init__(self, master):
        self.loginlogout_ControllerObject = loginlogout_controller.LoginLogoutControllers()
        self.master = master
        self.master.configure(background= "#3E3C3C")
        self.master.title("Log In or Register")
        self.createMainFrame()

    '''
    Intent: creates the main frame for the login GUI
    * Preconditions: master is connected to TKinter. 
    * createUsernamePasswordFrame and createLoginSignUpForgetPasswordFrame have the appropriate GUI code to be called in this method.
    * Postconditions:
    * Post0. main frame for login is created
    '''
    def createMainFrame(self): 
        # logo on top left side
        self.welcomeTitle = Label(self.master, text="Welcome to",font=("Fixedsys", 14),height = 0, width = 40,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=0,column=0, pady=10, padx=0, sticky='w')
        self.title = Label(self.master, text="Zyzzfit",font=("Fixedsys", 40, "bold"),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=1,column=0, pady=0, padx=0)
        self.createUsernamePasswordFrame()
        self.createLoginSignUpForgetPasswordFrame()
        self.exitButton = Button(self.master,text="Exit", command=lambda:self.closeWindow(), borderwidth=0).grid(row = 4,column=0)

    '''
    Intent: creates the username and password frame for the login GUI
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. username and password frame is created.
    '''
    def createUsernamePasswordFrame(self):
            # top credentials frame
        self.credentials = Frame(self.master, width = 350, height = 170,borderwidth=0, background='LightGray').grid(row = 2,column=0, ipadx = 5, ipady = 5)
        self.usernameLabel = Label(self.credentials, text="Username",font='Helvetica 13 bold',borderwidth=0, background='LightGray').grid(row = 2,column=0, padx=100, pady=15, ipadx=5, ipady=5, sticky='nw')
        self.passwordLabel = Label(self.credentials, text="Password",font='Helvetica 13 bold',borderwidth=0, background='LightGray').grid(row=2, column=0, padx=100, pady=15, ipadx=5, ipady=5,sticky="sw")
        
        self.usernameEntry = Entry(self.credentials)
        self.usernameEntry.grid(row = 2,column=0, padx=100, pady=15, ipadx=2, ipady=2, sticky="ne")
        self.passwordEntry = Entry(self.credentials, show="*")
        self.passwordEntry.grid(row = 2,column=0, padx=100, pady=15, ipadx=2, ipady=2, sticky="se")
    
    '''
    Intent: creates the login , signup, and forget password frame with its buttons.
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. login , signup, and forget password frame with the three buttons.
    '''
    def createLoginSignUpForgetPasswordFrame(self):
        # bottom button frame
        self.buttons= Frame(self.master, width = 350, height = 150, borderwidth=0, background='LightGray').grid(row = 3,column=0,pady=5, padx=5, ipadx = 5, ipady = 5)
        self.logInButton = Button(self.buttons, text="Log In", borderwidth=0).grid(row = 3,column=0,padx=100,pady=15,ipadx=2,ipady=2, sticky="nw")
        self.RegisterButton = Button(self.buttons, text="Register", borderwidth=0,command=lambda:self.createSignUpGUI()).grid(row = 3,column=0,padx=100,pady=15,ipadx=2,ipady=2, sticky="ne")
        self.ForgotButton = Button(self.buttons, text="Forgot Password",borderwidth=0, command=lambda:self.createForgetPasswordGUI).grid(row = 3,column=0,padx=30,pady=25,ipadx=2,ipady=2, sticky="s")
    

    '''
    Intent: handles the logic for the user logging in.
    * Preconditions: loginlogout_ControllerObject is an instance of loginlogoutController class
    * Postconditions:
    * Post0. loginlogoutController calls loginUser().
    '''
    def handleLoginEvent(self):
        self.loginlogout_ControllerObject.loginUser(self.usernameEntry.get(),self.passwordEntry.get(),self.master)
        
        
        
    
    '''
    Intent: creates the signup GUI
    * Preconditions:
    * Postconditions:
    * Post0. login window is closed and sign in window is created and displayed.
    '''
    def createSignUpGUI(self):
        self.closeWindow()
        self.loginlogout_ControllerObject.createSignUpGUI()
        
    '''
    Intent: close the login window .
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. closes the login window
    '''
    def closeWindow(self):
        self.master.destroy()

    
    
    '''
    Intent: creates the forget password GUI
    * Preconditions: 
    * Postconditions:
    * Post0. forget password GUI is created and displayed
    '''
    def createForgetPasswordGUI(self):
        self.closeWindow()
        self.loginlogout_ControllerObject.createForgottenPasswordGUI()
    

def main():
    root = Tk()
    root.geometry("550x550")
    loginGUIObject = LoginGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()