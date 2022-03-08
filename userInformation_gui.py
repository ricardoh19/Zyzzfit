from tkinter import *
import tkinter as tk
from tkinter import ttk
import loginlogout_controller 



# this class controls the graphical user interface of the Log In window. Its methods include createMainFrame, createUsernamePasswordFrame,
# createLoginSignUpForgetPasswordFrame, handleLoginEvent, createSignUpGUI, closeWindow, and createForgetPassword.
class UserInformationGUI():
    def __init__(self, master, username, password,securityQuestion):
        self.loginlogout_ControllerObject = loginlogout_controller.LoginLogoutControllers()
        self.master = master
        self.master.configure(background= "#3E3C3C")
        self.master.title("User Information")
        self.username = username
        self.password = password
        self.securityQuestion = securityQuestion


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
        self.title = Label(self.master, text="User Information",font=("Fixedsys", 40, "bold"),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=1,column=0, columnspan=2, pady=0, padx=0)
        
        self.age = Label(self.master, text="Age",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=2,column=0, sticky='w')
        self.ageEntry = Entry(self.master)
        self.ageEntry.grid(row = 2,column=1)
        self.weight = Label(self.master, text="Weight (Lbs.)",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=3,column=0, sticky='w')
        self.weightEntry = Entry(self.master)
        self.weightEntry.grid(row = 3,column=1)
        self.height = Label(self.master, text="Height (Inches)",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=4,column=0, sticky='w')
        self.heightEntry = Entry(self.master)
        self.heightEntry.grid(row = 4,column=1)
        
        self.gender = Label(self.master, text="Gender",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=5,column=0, sticky='w')
        self.clickedGender = StringVar()
        self.clickedGender.set("Whatever you want I guess")
        self.chooseGender = OptionMenu(self.master, self.clickedGender, "Man", "Woman", "Other")
        self.chooseGender.grid(row=5,column=1)

        self.goal = Label(self.master, text="What is your goal?",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=6,column=0, sticky='w')
        self.clickedGoal = StringVar()
        self.clickedGoal.set("Maintain")
        self.chooseGoal = OptionMenu(self.master, self.clickedGoal, "Lose", "Maintain", "Gain")
        self.chooseGoal.grid(row=6,column=1)

        self.createDaysFrame()

        
        self.saveButton = Button(self.master,text="Save", borderwidth=0, command=lambda:self.handleSaveInformationEvent(),  highlightthickness=0).grid(row = 14,column=1, pady=1, sticky="w")
        self.exitButton = Button(self.master,text="Cancel", command=lambda:self.closeWindow(), borderwidth=0,  highlightthickness=0).grid(row = 14,column=1, pady=10)

    
    def createDaysFrame(self):
        self.days = Label(self.master, text="How many days are you\n exercising?",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=7,column=0, sticky='w')
        self.monday= Checkbutton(self.master, text = "Monday", background='#3E3C3C', foreground='white').grid(row=7,column=1, sticky='w')
        self.tuesday= Checkbutton(self.master, text = "Tuesday", background='#3E3C3C', foreground='white').grid(row=8,column=1,sticky='w')
        self.wednesday= Checkbutton(self.master, text = "Wednesday", background='#3E3C3C', foreground='white').grid(row=9,column=1,sticky='w')
        self.thursday= Checkbutton(self.master, text = "Thursday", background='#3E3C3C', foreground='white').grid(row=10,column=1,sticky='w')
        self.friday= Checkbutton(self.master, text = "Friday", background='#3E3C3C', foreground='white').grid(row=11,column=1,sticky='w')
        self.saturday= Checkbutton(self.master, text = "Saturday", background='#3E3C3C', foreground='white').grid(row=12,column=1,sticky='w')
        self.sunday= Checkbutton(self.master, text = "Sunday", background='#3E3C3C', foreground='white').grid(row=13,column=1,sticky='w')


    '''
    Intent: 
    * Preconditions: loginlogout_ControllerObject is an instance of loginlogoutController class
    * Postconditions:
    * Post0. loginlogoutController calls userInformationProcessing().
    '''
    def handleSaveInformationEvent(self):
        self.loginlogout_ControllerObject.userInformationProcessing(self.username, self.password, self.securityQuestion, self.ageEntry.get(), self.weightEntry.get(), self.heightEntry.get(), self.clickedGender.get(), self.clickedGoal.get(), self.master)
        
        
    
  
    '''
    Intent: close the login window .
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. closes the login window
    '''
    def closeWindow(self):
        self.master.destroy()



def main():
    root = Tk()
    root.geometry("550x550")
    
    userInformationGUIObject = UserInformationGUI(root, "ricardo", "password", "pizza")
    root.mainloop()
if __name__ == "__main__":
    main()