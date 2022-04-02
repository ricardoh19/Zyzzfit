from cgitb import text
from tkinter import *
import tkinter as tk
from tkinter import ttk
from popup_gui import PopUpGUI
import loginlogout_controller 
import myProfile_controller



# this class controls the graphical user interface of the My Profile window. Its methods include createMainFrame, createDaysFrame,
# handleSaveInformationEvent, and closeWindow
class MyProfileGUI():
    def __init__(self, master, userObject, exerciseObject):
        self.loginlogout_ControllerObject = loginlogout_controller.LoginLogoutControllers()
        self.master = master
        self.master.configure(background= "#3E3C3C")
        self.master.title("My Profile Information")
        self.myProfileController = myProfile_controller.MyProfileController(userObject ,exerciseObject)
        self.userObject = userObject
        self.exerciseObject = exerciseObject
        self.listOfDays = self.userObject.getTrainingDays()
        self.originalUserObject = {"age":self.userObject.getAge(), "Weight":self.userObject.getWeight(), "height": self.userObject.getHeight(),"gender": self.userObject.getGender(), "Calorie Goal": self.userObject.getCalorieGoal(), "Training days":self.userObject.getTrainingDays()}

        self.currentUserData = [self.userObject.getUserId(), self.userObject.getUsername(), self.userObject.getPassword(), "DummyData", self.userObject.getAge(), self.userObject.getWeight(),  self.userObject.getHeight(),self.userObject.getGender(), self.userObject.getCalorieGoal()]
        self.createMainFrame()

    '''
    Intent: creates the main frame for the My profile GUI
    * Preconditions: master is connected to TKinter. 
    * Postconditions:
    * Post0. main frame for userInformation is created
    '''
    def createMainFrame(self): 
        self.title = Label(self.master, text="My Profile",font=("Fixedsys", 40, "bold"),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=1,column=0, columnspan=2, pady=0, padx=0)
        
        
        self.age = Label(self.master, text="Age",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=2,column=0, sticky='w')
        self.ageEntry = Entry(self.master)
        self.ageEntry.insert(0, self.userObject.getAge())

        self.ageEntry.grid(row = 2,column=1)
        self.weight = Label(self.master, text="Weight (Lbs.)",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=3,column=0, sticky='w')
        self.weightEntry = Entry(self.master)
        self.weightEntry.grid(row = 3,column=1)
        self.weightEntry.insert(0, self.userObject.getWeight())

        self.height = Label(self.master, text="Height (Inches)",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=4,column=0, sticky='w')
        self.heightEntry = Entry(self.master)
        self.heightEntry.grid(row = 4,column=1)
        self.heightEntry.insert(0, self.userObject.getHeight())
        
        self.gender = Label(self.master, text="Gender",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=5,column=0, sticky='w')
        self.clickedGender = StringVar()
        self.clickedGender.set(str(self.userObject.getGender()))
        self.chooseGender = OptionMenu(self.master, self.clickedGender, "Man", "Woman", "Other")
        self.chooseGender.grid(row=5,column=1)

        self.goal = Label(self.master, text="What is your goal?",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=6,column=0, sticky='w')
        self.clickedGoal = StringVar()
        self.clickedGoal.set(str(self.userObject.getCalorieGoal()))
        self.chooseGoal = OptionMenu(self.master, self.clickedGoal, "Lose", "Maintain", "Gain")
        self.chooseGoal.grid(row=6,column=1)

        self.createDaysFrame()
        self.selectDays()

        self.saveButton = Button(self.master,text="Save", borderwidth=0, command=lambda:self.handleSaveInformationEvent(),  highlightthickness=0).grid(row = 14,column=1, pady=1, sticky="e")
        self.cancelButton = Button(self.master,text="Cancel", borderwidth=0,  highlightthickness=0, command=lambda:self.closeWindow()).grid(row = 14,column=2, pady=1, sticky="e")

    
    '''
    Intent: creates the frame with days checkboxes for the My profile GUI
    * Preconditions: master is connected to TKinter. 
    * Postconditions:
    * Post0. day frame for My Profile GUI is created
    '''
    def createDaysFrame(self):
        self.days = Label(self.master, text="How many days are you\n exercising?",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=7,column=0, sticky='w', ipadx=10)
    

        self.varMonday = StringVar()
        self.monday= Checkbutton(self.master, text = "Monday", background='#3E3C3C', foreground='white', variable=self.varMonday, onvalue="Monday", offvalue="0")
        self.monday.grid(row=7,column=1, sticky='w')
        self.monday.deselect()

        self.varTuesday = StringVar()
        self.tuesday = Checkbutton(self.master, text = "Tuesday", background='#3E3C3C', foreground='white', variable=self.varTuesday, onvalue="Tuesday", offvalue="0")
        self.tuesday.grid(row=8,column=1,sticky='w')
        self.tuesday.deselect()

        self.varWednesday = StringVar()
        self.wednesday = Checkbutton(self.master, text = "Wednesday", background='#3E3C3C', foreground='white', variable=self.varWednesday, onvalue="Wednesday", offvalue="0")
        self.wednesday.grid(row=9,column=1,sticky='w')
        self.wednesday.deselect()

        self.varThursday = StringVar()
        self.thursday = Checkbutton(self.master, text = "Thursday", background='#3E3C3C', foreground='white', variable=self.varThursday, onvalue="Thursday", offvalue="0")
        self.thursday.grid(row=10,column=1,sticky='w')
        self.thursday.deselect()

        self.varFriday = StringVar()
        self.friday= Checkbutton(self.master, text = "Friday", background='#3E3C3C', foreground='white', variable=self.varFriday, onvalue="Friday", offvalue="0")
        self.friday.grid(row=11,column=1,sticky='w')
        self.friday.deselect()

        self.varSaturday = StringVar()
        self.saturday= Checkbutton(self.master, text = "Saturday", background='#3E3C3C', foreground='white', variable=self.varSaturday, onvalue="Saturday", offvalue="0")
        self.saturday.grid(row=12,column=1,sticky='w')
        self.saturday.deselect()

        self.varSunday = StringVar()
        self.sunday= Checkbutton(self.master, text = "Sunday", background='#3E3C3C', foreground='white', variable=self.varSunday, onvalue="Sunday", offvalue="0")
        self.sunday.grid(row=13,column=1,sticky='w')
        self.sunday.deselect()

    '''
    Intent: selects theuser's training days for My profile GUI to let the user know which days they are already working out.
    '''
    def selectDays(self):
        for day in self.listOfDays:
            if day == "Monday":
                self.monday.select()
            if day == "Tuesday":
                self.tuesday.select()
            if day == "Wednesday":
                self.wednesday.select()
            if day == "Thursday":
                self.thursday.select()
            if day == "Friday":
                self.friday.select()
            if day == "Saturday":
                self.saturday.select()
            if day == "Sunday":
                self.sunday.select()
            

    '''
    Intent: handles the save button. Saves information by calling function in My Profile controller.
    * Preconditions: loginlogout_ControllerObject is an instance of loginlogoutController class
    * Postconditions:
    * Post0. create dashboard Controller is callled in My Profile controller.
    * Post1. appropriate rrror message is displayed if information is not entered correctly. 
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
        

        elif len(self.listOfDays) == 1:
            popupGUI = PopUpGUI("Please choose atleast two days to exercise.")
            popupGUI.createPopUp()
            return False

        try: 
            age = int(self.ageEntry.get())
            weight = int(self.weightEntry.get())
            height = int(self.heightEntry.get())
            self.newCurrentUserData = [self.userObject.getUserId(), self.userObject.getUsername(), self.userObject.getPassword(), "DummyData", age, weight, height, self.clickedGender.get(), self.clickedGoal.get()]
            #return userObject and pass it into dashboard controller
            self.myProfileController.createDashboardController(self.newCurrentUserData, self.listOfDays, self.exerciseObject, self.master)
        except ValueError:
            popupGUI = PopUpGUI("Please provide an appropriate age, weight, or height.")
            popupGUI.createPopUp()
            


        

  
    '''
    Intent: close the My Profile window .
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. closes the MyProfile window
    '''
    def closeWindow(self):
        self.myProfileController.createDashboardController(self.currentUserData, self.listOfDays, self.exerciseObject, self.master)
