from tkinter import *
import tkinter as tk
from tkinter import ttk
import datetime
import dashboard_controller 
from PIL import ImageTk,Image 

# this class controls the graphical user interface of the My workouts window. 
class MyWorkoutGUI():
    def __init__(self, master, userObject, exerciseObject):
        self.master = master
        self.master.configure(background= "#3E3C3C")
        self.master.title("My Workouts")
        self.userObject = userObject
        self.exerciseObject = exerciseObject
        self.dashboardControllerObject = dashboard_controller.DashboardController(userObject, exerciseObject)
        userObject = None
        exerciseObject = None
        self.createMainFrame()

    '''
    Intent: creates the main frame for the My Workouts GUI
    * Preconditions: master is connected to TKinter. 
    * createWatchlistPortfolioFrame and createSearchbarFrame have the appropriate GUI code to be called in this method.
    * Postconditions:
    * Post0. main frame for dashboard is created
    '''
    def createMainFrame(self):
        self.createMenuFrame()
        self.title = Label(self.master, text="My Workouts",font='Ubuntu 20 bold', height=5, width = 20, borderwidth=0, background='#3E3C3C', foreground="white").grid(row=0,column=1, pady=5, padx=5, columnspan=2, sticky='w')
    
        self.createProfileButton()
        self.createSuggestionFrame()
        self.createWorkoutFrame()
        self.createDaysFrame()
        
        self.exitButton = Button(self.master,text="Log Out", command=lambda:self.handleLogoutEvent(), highlightthickness=0, borderwidth=0).grid(row = 6,column=0, sticky='s')


    def createMenuFrame(self):
        self.menuFrame = Frame(self.master, height=555, width = 150, relief="solid", background='white').grid(row=0,column=0, pady=5, padx=15, rowspan=7)
        self.menu = Label(self.menuFrame, text="Zyzzfit",font='Ubuntu 25 bold', background='white').grid(row=0,column=0)
        self.dashboardButton = Button(self.menuFrame, text="Dashboard",font='Ubuntu 10 bold', highlightthickness=0,borderwidth=0).grid(row=1,column=0, sticky='ne', padx=20) 
        self.myWorkoutsButton = Button(self.menuFrame, text="My Workouts",font='Ubuntu 10 bold', highlightthickness=0,borderwidth=0).grid(row=1,column=0, sticky='se', padx=20)
        image = Image.open("assets/dashboard.png")
        resize_image = image.resize((15,15))
        img = ImageTk.PhotoImage(resize_image)
        panel = Label(self.master, image = img, width=15, height=15)
        panel.image = img
        panel.grid(row=1,column=0, sticky='nw', padx=20)
        
        image = Image.open("assets/workout.png")
        resize_image = image.resize((15,15))
        img = ImageTk.PhotoImage(resize_image)
        panel = Label(self.master, image = img, width=15, height=15)
        panel.image = img
        panel.grid(row=1,column=0, sticky='sw', padx=20)

    def createProfileButton(self):
        self.profile = Button(self.master, text="My Profile",font='fixedsys 12',  height=3, width = 10, borderwidth=3, relief="solid", background='white').grid(row=0,column=4, sticky='e')


    def createSuggestionFrame(self):
        self.quote = Label(self.master, text="Suggestion", height=4, width = 87, borderwidth=0, background='white').grid(row=1,column=1, columnspan=3)


    def createWorkoutFrame(self):
        self.tree = ttk.Treeview(self.master, column=("Exercise", "Sets","Reps", "Max_Weight", "Original_Weight"), show='headings', height=17)
        self.tree.grid(row=2,column=1, columnspan=3, rowspan=5, padx=5)

        self.tree.heading('Exercise', text='Exercise')
        self.tree.column("Exercise", stretch=NO, width=400)

        self.tree.heading('Sets', text='Sets')
        self.tree.column("Sets", stretch=NO, width=75)

        self.tree.heading('Reps', text='Reps')
        self.tree.column("Reps", stretch=NO, width=75)

        self.tree.heading('Max_Weight', text='Max Weight(Lbs.)')
        self.tree.column("Max_Weight", stretch=NO, width=120)

        self.tree.heading('Original_Weight', text='Original Weight(Lbs.)')
        self.tree.column("Original_Weight", stretch=NO, width=120)

        self.day = self.dashboardControllerObject.getDay()

        DayCount = 0
        if self.exerciseObject != None:
            for i in self.exerciseObject:
                if self.exerciseObject[i]["training Day"] == self.day:
                    DayCount +=1 
                    try:
                        self.sets = self.exerciseObject[i]["sets"]
                        self.reps = self.exerciseObject[i]["reps"]
                        self.tree.insert('', 'end', text=i, values=(i, self.sets, self.reps))
                    except KeyError:
                        self.tree.insert('', 'end', text=i, values=(i, "N/A", "N/A"))
                
        if DayCount == 0:
            self.tree.insert('', 'end', text='', values=("No Exercises Today", "N/A", "N/A"))
    

    def createDaysFrame(self):
        button_dict = {}
        for i in range(len(self.userObject["Training days"])):
            button_dict[i] = Button(self.master, text="Workout" + str(i+1),font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(i), height=1, width =10, highlightthickness=0, borderwidth=0, background='white').grid(row=i+1,column=4)
        print(button_dict)

    
    def changeWorkoutDisplayed(self, day):
        print(day)

    '''
    Intent: handles the logic for the user clicking logout button.
    * Preconditions: dashboard controller object exists
    * Postconditions: 
    * Post0. changes are pushed to database, dashboard window is closed and login window is opened.
    * Post1. Changes are not pushed to database beacause connection to database could not be estbalished.
    '''
    def handleLogoutEvent(self):
        #username = self.userObject.current_user_data[1]
        #self.dashboardControllerObject.logOutPushChanges(username, self.userObject)
        self.closeWindow()
        self.dashboardControllerObject.openLoginGUI()
        
    

    '''
    Intent: close the dashboard window .
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. closes the dashboard window
    '''
    def closeWindow(self):
        self.master.destroy()
