from tkinter import *
import tkinter as tk
from tkinter import ttk
import dashboard_controller
from PIL import ImageTk,Image 



# this class controls the graphical user interface of the dashboard window. Its methods include createMainframe, createMenuFrame, createDateFrame, createWorkoutFrame, openMyWorkoutGUI, 
# createQuoteFrame, createDaysFrame, createCaloriesFrame, handleLogoutEvent, and closeWindow. 
class DashboardGUI():
    def __init__(self, master, userObject, exerciseObject, allExercises):
        self.master = master
        self.master.configure(background= "#3E3C3C")
        self.master.title("Dashboard")
        self.userObject = userObject
        self.exerciseObject = exerciseObject
        self.dashboardControllerObject = dashboard_controller.DashboardController(userObject, exerciseObject, allExercises)
        self.createMainFrame()
        

    '''
    Intent: creates the main frame for the dashboard GUI
    * Preconditions: master is connected to TKinter. 
    * Postconditions:
    * Post0. main frame for dashboard is created
    '''
    def createMainFrame(self):
        self.createMenuFrame()
        title = Label(self.master, text="Dashboard",font='fixedsys 20 bold', height=5, width = 20, borderwidth=0, background='#3E3C3C', foreground="white").grid(row=0,column=1, pady=5, padx=5, columnspan=2, sticky='w')

        profile = Button(self.master, text="My Profile",font='Fixedsys 12', command=lambda:self.openMyProfileGUI(), height=3, width = 10, borderwidth=3, relief="solid", background='white').grid(row=0,column=4, pady=4, sticky='e')
        self.createQuoteFrame()
        self.createDateFrame()
        self.createWorkoutFrame()
        self.createDaysFrame()
        self.createCaloriesFrame()

        exitButton = Button(self.master,text="Log Out", command=lambda:self.handleLogoutEvent(), borderwidth=0).grid(row = 3,column=0, sticky='s')

    '''
    Intent: creates the menu frame for GUI
    * Preconditions: master is connected to TKinter. 
    * Postconditions:
    * Post0. frame with dashboard, My Workouts buttons, and logout buttons are created for dashboard GUI
    '''
    def createMenuFrame(self):
        menuFrame = Frame(self.master, height=555, width = 150, relief="solid", background='white').grid(row=0,column=0, pady=5, padx=15, rowspan=4)
        menu = Label(menuFrame, text="Zyzzfit",font='fixedsys 23 bold', background='white').grid(row=0,column=0)
        dashboardButton = Button(menuFrame, text="Dashboard",font='fixedsys 10 bold', borderwidth=0).grid(row=1,column=0, sticky='ne', padx=20) 
        myWorkoutsButton = Button(menuFrame, text="My Workouts",font='fixedsys 10 bold', borderwidth=0, command=lambda:self.openMyWorkoutsGUI()).grid(row=1,column=0, sticky='se', padx=20) 
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

    '''
    Intent: creates the date frame for GUI
    * Preconditions: master is connected to TKinter. 
    * dashboard controller object exists
    * Postconditions:
    * Post0. date frame for dashboard GUI is created
    '''
    def createDateFrame(self):
        date = self.dashboardControllerObject.getFullDate()
        date = Label(self.master, text=date,font='fixedsys 15 bold', height=2, width = 30, background='lightGray', foreground="black").grid(row=1,column=3, columnspan=2)

    '''
    Intent: creates the workout frame for GUI
    * Preconditions: master is connected to TKinter. 
    * Postconditions:
    * Post0. workout frame for dashboard is created
    '''
    def createWorkoutFrame(self):
        title = Label(self.master, text="Today's Workout",font='fixedsys 10 bold', height=1, width = 20, borderwidth=0, background='#3E3C3C', foreground="white").grid(row=2,column=1, sticky='w')

        tree = ttk.Treeview(self.master, column=("Exercise", "Sets","Reps"), show='headings', height=12)
        tree.grid(row=2,column=1, pady=5, padx=3, rowspan=2, columnspan=2, sticky='s')
        
        tree.heading('Exercise', text='Exercise')
        tree.column("Exercise", stretch=NO, width=400)

        tree.heading('Sets', text='Sets')
        tree.column("Sets", stretch=NO, width=75)

        tree.heading('Reps', text='Reps')
        tree.column("Reps", stretch=NO, width=75)

        day = self.dashboardControllerObject.getDay()
        
        DayCount = 0
        if self.exerciseObject != None:
            for exerciseName in self.exerciseObject.keys():
                if self.exerciseObject.getTrainingDay(exerciseName) == day:
                    DayCount +=1 
                    try:
                        sets = self.exerciseObject.getSets(exerciseName)
                        reps = self.exerciseObject.getReps(exerciseName)
                        tree.insert('', 'end', text=exerciseName, values=(exerciseName, sets, reps))
                    except KeyError:
                        tree.insert('', 'end', text=exerciseName, values=(exerciseName, "N/A", "N/A"))
                
        if DayCount == 0:
            tree.insert('', 'end', text='', values=("No Exercises Today", "N/A", "N/A"))
        
        
    '''
    Intent: creates the My Workouts controller
    * Preconditions: master is connected to TKinter. 
    * dashboard controller object exists
    * Postconditions:
    * Post0. creates My Workouts Controller
    '''
    def openMyWorkoutsGUI(self):
        self.dashboardControllerObject.createMyWorkoutsController(self.master)

    '''
    Intent: creates the My Profile controller
    * Preconditions: master is connected to TKinter. 
    * dashboard controller object exists
    * Postconditions:
    * Post0. creates My Profile Controller
    '''
    def openMyProfileGUI(self):
        self.dashboardControllerObject.createMyProfileController(self.master)
        
    '''
    Intent: creates the quotes frame
    * Preconditions: 
    * master is connected to TKinter. 
    * dashboard controller object exists
    * Postconditions:
    * Post0. creates frame with quote and author
    '''
    def createQuoteFrame(self):
        quoteAPI = self.dashboardControllerObject.getQuote()
        quote = Label(self.master, text="{}\n{}\n-{}".format(quoteAPI['q'][:80], quoteAPI['q'][80:], quoteAPI['a']),font='fixedsys 9 bold', height=4, width = 78, borderwidth=0, background='white').grid(row=1,column=1, ipadx=15,columnspan=2)

    
    '''
    Intent: creates the quotes frame
    * Preconditions: 
    * master is connected to TKinter. 
    * dashboard controller object exists
    * Postconditions:
    * Post0. creates frame with quote and author
    '''
    def createDaysFrame(self):
        if self.userObject != None:
            trainingDays = self.userObject.getTrainingDays()
            daySplit = len(trainingDays)
            dayNumber = Label(self.master, text="{} Day Split".format(daySplit),font='fixedsys 21 bold', height=7, width = 24, borderwidth=0, background='white').grid(row=2,column=3,columnspan=2)

    '''
    Intent: creates the calories frame
    * Preconditions: 
    * master is connected to TKinter. 
    * dashboard controller object exists
    * Postconditions:
    * Post0. creates frame with calories number 
    '''
    def createCaloriesFrame(self):
        caloriesResult = self.dashboardControllerObject.calculateCalorieIntake()
        calories = Label(self.master, text="Eat {} Calories \n a day to \n{} weight".format(caloriesResult, self.userObject.getCalorieGoal()), font="fixedsys 21 bold", height=7, width = 24,borderwidth=0, background='red').grid(row=3,column=3, columnspan=2)



    '''
    Intent: handles the logic for the user clicking logout button.
    * Preconditions: 
    * Postconditions: 
    * Post0. changes are pushed to database, dashboard window is closed and login window is opened.
    * Post1. Changes are not pushed to database beacause connection to database could not be estbalished.
    '''
    def handleLogoutEvent(self):
        username = self.userObject.getUsername()
        self.dashboardControllerObject.logOutPushChanges(username, self.userObject, self.exerciseObject)
       

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


