from tkinter import *
import tkinter as tk
from tkinter import ttk
import datetime
import dashboard_controller 
import editExercise_controller
import myworkout_controller
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
        self.myWorkoutControllerObject = myworkout_controller.MyWorkoutsController(userObject, exerciseObject)
        self.tree = None
        userObject = None
        exerciseObject = None
        self.createMainFrame()

    '''
    Intent: creates the main frame for the My Workouts GUI
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. main frame for my workouts is created
    '''
    def createMainFrame(self):
        self.createMenuFrame()
        title = Label(self.master, text="My Workouts",font='Ubuntu 20 bold', height=5, width = 20, borderwidth=0, background='#3E3C3C', foreground="white").grid(row=0,column=1, pady=5, padx=5, columnspan=2, sticky='w')
        self.createProfileButton()
        self.createSuggestionFrame()
        self.createWorkoutFrame()
        self.createDaysFrame()
        exitButton = Button(self.master,text="Log Out", command=lambda:self.handleLogoutEvent(), highlightthickness=0, borderwidth=0).grid(row = 6,column=0, sticky='s')

    '''
    Intent: creates the menu frame for the My Workouts GUI
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. menu frame for my workouts is created
    '''
    def createMenuFrame(self):
        menuFrame = Frame(self.master, height=555, width = 150, relief="solid", background='white').grid(row=0,column=0, pady=5, padx=15, rowspan=7)
        menu = Label(menuFrame, text="Zyzzfit",font='Ubuntu 25 bold', background='white').grid(row=0,column=0)
        self.dashboardButton = Button(menuFrame, text="Dashboard",font='Ubuntu 10 bold', highlightthickness=0,borderwidth=0, command=lambda:self.displayDashboard()).grid(row=1,column=0, sticky='ne', padx=20) 
        self.myWorkoutsButton = Button(menuFrame, text="My Workouts",font='Ubuntu 10 bold', highlightthickness=0,borderwidth=0).grid(row=1,column=0, sticky='se', padx=20)
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
    Intent: creates the my profile button for this GUI.
    '''
    def createProfileButton(self):
        profile = Button(self.master, text="My Profile",font='fixedsys 12',  height=3, width = 10, borderwidth=3, relief="solid", background='white', command=lambda:self.createMyProfileController()).grid(row=0,column=4, sticky='e')

    '''
    Intent: Calls function in myWorkouts controller to create the myProfile controller.
    '''
    def createMyProfileController(self):
        self.myWorkoutControllerObject.createMyProfileController(self.master)

    '''
    Intent: creates the suggestion frame for My workouts GUI. Calls function in myWorkouts controller to get suggestion.
    '''
    def createSuggestionFrame(self):
        suggestion = self.myWorkoutControllerObject.createSuggestion()
        quote = Label(self.master, text=suggestion, height=4, width = 87, borderwidth=0, background='white').grid(row=1,column=1, columnspan=3)

    '''
    Intent: creates the workout frame for the My Workouts GUI
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. workout frame for my workouts is created
    '''
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

        self.changeWorkoutDisplayed(0)
                
        self.addExerciseButton = Button(self.master, text="Add Exercise",font='fixedsys 12',  height=1, width = 10, borderwidth=0, highlightthickness=0,background='white', command=lambda:self.displayAddExerciseGUI()).grid(row=7,column=2,sticky='w', padx=5, pady=5)
        self.tree.bind('<ButtonRelease-1>', self.selectItem)
        
        
    '''
    Intent: creates exercise and remove button. Focus on one exercise to edit or remove it. 
    '''
    def selectItem(self,a):
        curItem = self.tree.focus()
        exerciseText = self.tree.item(curItem)['text']

        editExerciseButton = Button(self.master, text="Edit Exercise",font='fixedsys 12',  height=1, width = 10, borderwidth=0, highlightthickness=0,background='white', command=lambda:self.displayEditExerciseGUI(str(exerciseText))).grid(row=7,column=1, sticky='w', padx=5, pady=5)
        removeExerciseButton = Button(self.master, text="Remove Exercise",font='fixedsys 12',  height=1, width = 10, borderwidth=0, highlightthickness=0,background='white', command=lambda:self.removeExercise(exerciseText)).grid(row=7,column=3,sticky='w', padx=5, pady=5)

    '''
    Intent: calls my workout controller to create edit exercise controller
    '''
    def displayEditExerciseGUI(self, exerciseName):
        self.myWorkoutControllerObject.createEditExerciseController(exerciseName ,self.master)

    '''
    Intent: calls my workout controller to create add exercise controller
    '''
    def displayAddExerciseGUI(self):
        self.myWorkoutControllerObject.createAddExerciseController(self.master)

    '''
    Intent: calls my workout controller to remove exercise. Also upates the workout displayed.
    '''
    def removeExercise(self, exerciseName):
        self.myWorkoutControllerObject.removeExercise(exerciseName)
        self.changeWorkoutDisplayed(0)

    '''
    Intent: calls my workout controller to create dashboard controller
    '''
    def displayDashboard(self):
        self.myWorkoutControllerObject.createDashboardController(self.master)

    '''
    Intent: creates the day frame for the My Workouts GUI
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. day frame for my workouts is created
    '''
    def createDaysFrame(self):
        length = len(self.userObject.getTrainingDays())
        if length == 2:
            self.button1 = Button(self.master, text=f"{self.userObject.getTrainingDays()[0]}'s Workout" , font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(0), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button1.grid(row=1,column=4)
            
            self.button2 = Button(self.master, text=f"{self.userObject.getTrainingDays()[1]}'s Workout" , font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(1), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button2.grid(row=2,column=4)


        elif length ==3:
            self.button1 = Button(self.master, text=f"{self.userObject.getTrainingDays()[0]}'s Workout" , font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(0), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button1.grid(row=1,column=4)
            self.button2 = Button(self.master, text=f"{self.userObject.getTrainingDays()[1]}'s Workout" ,font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(1), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button2.grid(row=2,column=4)
            self.button3 = Button(self.master, text=f"{self.userObject.getTrainingDays()[2]}'s Workout" ,font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(2), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button3.grid(row=3,column=4)
        
        elif length ==4:
            self.button1 = Button(self.master, text=f"{self.userObject.getTrainingDays()[0]}'s Workout" ,font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(0), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button1.grid(row=1,column=4)
            self.button2 = Button(self.master, text=f"{self.userObject.getTrainingDays()[1]}'s Workout" ,font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(1), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button2.grid(row=2,column=4)
            self.button3 = Button(self.master, text=f"{self.userObject.getTrainingDays()[2]}'s Workout" ,font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(2), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button3.grid(row=3,column=4)
            self.button4 = Button(self.master, text=f"{self.userObject.getTrainingDays()[3]}'s Workout",font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(3), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button4.grid(row=4,column=4)

        elif length ==5:
            self.button1 = Button(self.master, text="Workout 1" ,font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(0), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button1.grid(row=1,column=4)
            self.button2 = Button(self.master, text="Workout 2" ,font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(1), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button2.grid(row=2,column=4)
            self.button3 = Button(self.master, text="Workout 3" ,font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(2), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button3.grid(row=3,column=4)
            self.button4 = Button(self.master, text="Workout 4",font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(3), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button4.grid(row=4,column=4)
            self.button5 = Button(self.master, text="Workout 5" ,font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(4), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button5.grid(row=5,column=4)

        elif length ==6:
            self.button1 = Button(self.master, text="Workout 1" ,font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(0), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button1.grid(row=1,column=4)
            self.button2 = Button(self.master, text="Workout 2" ,font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(1), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button2.grid(row=2,column=4)
            self.button3 = Button(self.master, text="Workout 3" ,font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(2), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button3.grid(row=3,column=4)
            self.button4 = Button(self.master, text="Workout 4",font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(3), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button4.grid(row=4,column=4)
            self.button5 = Button(self.master, text="Workout 5" ,font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(4), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button5.grid(row=5,column=4)
            self.button6 = Button(self.master, text="Workout 6" ,font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(5), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button6.grid(row=6,column=4)

        elif length ==7:
            self.button1 = Button(self.master, text="Workout 1" ,font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(0), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button1.grid(row=1,column=4)
            self.button2 = Button(self.master, text="Workout 2" ,font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(1), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button2.grid(row=2,column=4)
            self.button3 = Button(self.master, text="Workout 3" ,font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(2), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button3.grid(row=3,column=4)
            self.button4 = Button(self.master, text="Workout 4",font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(3), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button4.grid(row=4,column=4)
            self.button5 = Button(self.master, text="Workout 5" ,font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(4), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button5.grid(row=5,column=4)
            self.button6 = Button(self.master, text="Workout 6" ,font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(5), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button6.grid(row=6,column=4)
            self.button7 = Button(self.master, text="Workout 7" ,font='fixedsys 12', command=lambda:self.changeWorkoutDisplayed(6), height=1, width =13, highlightthickness=0, borderwidth=0, background='white')
            self.button7.grid(row=7,column=4)

    '''
    Intent: self.tree is cleared. self. tree displays all workout information for a specific day.
    '''
    def clear_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
       
    
    '''
    Intent: Calls function clear tree and changes the workout displayed through the tree.
    '''
    def changeWorkoutDisplayed(self, day):
        self.clear_tree()
        
        trainingDay = self.userObject.getTrainingDays()
        for exerciseName in self.exerciseObject.keys():
            if self.exerciseObject.getTrainingDay(exerciseName) == trainingDay[day]:
                try:
                    self.sets = self.exerciseObject.getSets(exerciseName)
                    self.reps = self.exerciseObject.getReps(exerciseName)
                    self.originalWeight = self.exerciseObject.getOriginalWeight(exerciseName)
                    self.maxWeight = self.exerciseObject.getMaxWeight(exerciseName)
                    self.tree.insert('', 'end', text=exerciseName, values=(exerciseName, self.sets, self.reps, self.maxWeight, self.originalWeight))
                except KeyError:
                    self.tree.insert('', 'end', text=exerciseName, values=(exerciseName, "N/A", "N/A","N/A","N/A" ))

        
   
   
    '''
    Intent: handles the logic for the user clicking logout button.
    * Preconditions: dashboard controller object exists
    * Postconditions: 
    * Post0. changes are pushed to database, 
    * Post1. Changes are not pushed to database beacause connection to database could not be established.
    '''
    def handleLogoutEvent(self):
        #username = self.userObject.current_user_data[1]
        #self.dashboardControllerObject.logOutPushChanges(username, self.userObject)
        self.closeWindow()
        self.dashboardControllerObject.openLoginGUI()
        
    

    '''
    Intent: close the My Workout window .
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. closes the My Workout window
    '''
    def closeWindow(self):
        self.master.destroy()

