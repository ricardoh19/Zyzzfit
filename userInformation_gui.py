from tkinter import *
import tkinter as tk
from tkinter import ttk
import loginlogout_controller 



# this class controls the graphical user interface of the userInformation window. Its methods include createMainFrame, createDaysFrame,
# handleSaveInformationEvent, and closeWindow
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
    Intent: creates the main frame for the userInformation GUI
    * Preconditions: master is connected to TKinter. 
    * Postconditions:
    * Post0. main frame for userInformation is created
    '''
    def createMainFrame(self): 
        title = Label(self.master, text="User Information",font=("Fixedsys", 40, "bold"),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=1,column=0, columnspan=2, pady=0, padx=0)
        
        age = Label(self.master, text="Age",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=2,column=0, sticky='w')
        self.ageEntry = Entry(self.master)
        self.ageEntry.grid(row = 2,column=1)
        weight = Label(self.master, text="Weight (Lbs.)",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=3,column=0, sticky='w')
        self.weightEntry = Entry(self.master)
        self.weightEntry.grid(row = 3,column=1)
        height = Label(self.master, text="Height (Inches)",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=4,column=0, sticky='w')
        self.heightEntry = Entry(self.master)
        self.heightEntry.grid(row = 4,column=1)
        
        gender = Label(self.master, text="Gender",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=5,column=0, sticky='w')
        self.clickedGender = StringVar()
        self.clickedGender.set("?")
        self.chooseGender = OptionMenu(self.master, self.clickedGender, "Man", "Woman", "Other")
        self.chooseGender.grid(row=5,column=1)

        goal = Label(self.master, text="What is your goal?",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=6,column=0, sticky='w')
        self.clickedGoal = StringVar()
        self.clickedGoal.set("Maintain")
        self.chooseGoal = OptionMenu(self.master, self.clickedGoal, "Lose", "Maintain", "Gain")
        self.chooseGoal.grid(row=6,column=1)

        self.createDaysFrame()

        saveButton = Button(self.master,text="Finish Set Up", borderwidth=0, command=lambda:self.handleSaveInformationEvent(),  highlightthickness=0).grid(row = 14,column=1, pady=1, sticky="e")

    
    '''
    Intent: creates the frame with days checkboxes for the userInformation GUI
    * Preconditions: master is connected to TKinter. 
    * Postconditions:
    * Post0. day frame for userInformationGUI is created
    '''
    def createDaysFrame(self):
        days = Label(self.master, text="How many days are you\n exercising?",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=7,column=0, sticky='w', ipadx=10)
        
        self.varMonday = StringVar()
        monday= Checkbutton(self.master, text = "Monday", background='#3E3C3C', foreground='white', variable=self.varMonday, onvalue="Monday", offvalue="0")
        monday.grid(row=7,column=1, sticky='w')
        monday.deselect()

        self.varTuesday = StringVar()
        tuesday = Checkbutton(self.master, text = "Tuesday", background='#3E3C3C', foreground='white', variable=self.varTuesday, onvalue="Tuesday", offvalue="0")
        tuesday.grid(row=8,column=1,sticky='w')
        tuesday.deselect()

        self.varWednesday = StringVar()
        wednesday = Checkbutton(self.master, text = "Wednesday", background='#3E3C3C', foreground='white', variable=self.varWednesday, onvalue="Wednesday", offvalue="0")
        wednesday.grid(row=9,column=1,sticky='w')
        wednesday.deselect()

        self.varThursday = StringVar()
        thursday = Checkbutton(self.master, text = "Thursday", background='#3E3C3C', foreground='white', variable=self.varThursday, onvalue="Thursday", offvalue="0")
        thursday.grid(row=10,column=1,sticky='w')
        thursday.deselect()

        self.varFriday = StringVar()
        friday= Checkbutton(self.master, text = "Friday", background='#3E3C3C', foreground='white', variable=self.varFriday, onvalue="Friday", offvalue="0")
        friday.grid(row=11,column=1,sticky='w')
        friday.deselect()

        self.varSaturday = StringVar()
        saturday= Checkbutton(self.master, text = "Saturday", background='#3E3C3C', foreground='white', variable=self.varSaturday, onvalue="Saturday", offvalue="0")
        saturday.grid(row=12,column=1,sticky='w')
        saturday.deselect()

        self.varSunday = StringVar()
        sunday= Checkbutton(self.master, text = "Sunday", background='#3E3C3C', foreground='white', variable=self.varSunday, onvalue="Sunday", offvalue="0")
        sunday.grid(row=13,column=1,sticky='w')
        sunday.deselect()

    '''
    Intent: Calls method in loginlogoutController to save information inputted by user.
    * Preconditions: loginlogout_ControllerObject is an instance of loginlogoutController class
    * Postconditions:
    * Post0. loginlogoutController calls userInformationProcessing().
    '''
    def handleSaveInformationEvent(self):
        self.listOfDays = []
        
        if self.varMonday.get() != '0':
            self.listOfDays.append('Monday')
        if self.varTuesday.get() != '0':
            self.listOfDays.append('Tuesday')
        if self.varWednesday.get() != '0':
            self.listOfDays.append('Wednesday')
        if self.varThursday.get() != '0':
            self.listOfDays.append('Thursday')
        if self.varFriday.get() != '0':
            self.listOfDays.append('Friday')
        if self.varSaturday.get() != '0':
            self.listOfDays.append('Saturday')
        if self.varSunday.get() != '0':
            self.listOfDays.append('Sunday')
        
        
        userInformationDict = {"username":self.username, "password":self.password, "security question":self.securityQuestion, "age":self.ageEntry.get(), "weight":self.weightEntry.get(), "height":self.heightEntry.get(), "gender":self.clickedGender.get(), "calorie goal":self.clickedGoal.get()}
        self.loginlogout_ControllerObject.userInformationProcessing(userInformationDict, self.listOfDays, self.master)
        
        

  
    '''
    Intent: close the userInformation window .
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. closes the userInformation window
    '''
    def closeWindow(self):
        self.master.destroy()

