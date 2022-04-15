from hashlib import new
from tkinter import *
import tkinter as tk
from tkinter import ttk
import addExerciseController
import myworkout_controller
from popup_gui import PopUpGUI



# this class controls the graphical user interface of the add exercise window.
class AddExerciseGUI():
    def __init__(self, master, userObject, exerciseObject, allExercises):
        self.master = master
        self.master.configure(background= "#3E3C3C")
        self.master.title("Add Exercise")
        self.exerciseObject = exerciseObject
        self.userObject = userObject
        self.allExercises = allExercises
        self.addExerciseControllerObject = addExerciseController.AddExerciseController(self.userObject,self.exerciseObject, allExercises)
        self.varExercise = None
        self.varBodyPart = None
        self.createMainFrame()

    '''
    Intent: creates the main frame for the Add Exercise GUI
    * Preconditions: master is connected to TKinter. 
    * Postconditions:
    * Post0. main frame for Add Exercise is created
    '''
    def createMainFrame(self): 
        title = Label(self.master, text="Add Exercise",font=("Fixedsys", 40, "bold"),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=0,column=0, columnspan=2 )
        

        bodyPart = Label(self.master, text="Body Part",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=1,column=0, sticky='w', pady=5)
        
        self.varBodyPart = StringVar()
        self.varBodyPart.set("None")
        bodyPartEntry = OptionMenu(self.master, self.varBodyPart, "Chest", "Back", "Shoulders", "Biceps", "Triceps", "Legs", "Cardio")
        bodyPartEntry.grid(row = 1,column=1,pady=5, sticky="w")       
        

        enterButton = Button(self.master,text="Enter Body Part", borderwidth=0, command=lambda:self.getExercisesBasedOnBodyPart(self.varBodyPart.get()),  highlightthickness=0).grid(row = 1,column=1, pady=5,padx=5,sticky="e")

        exercise = Label(self.master, text="Exercise",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=3,column=0, sticky='w', pady=5)
        self.varExercise = StringVar()
        self.varExercise.set("None")
        exerciseEntry = OptionMenu(self.master, self.varExercise, "None")
        exerciseEntry.grid(row = 3,column=1,pady=5)       
        
        trainingDay = Label(self.master, text="Training Day",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=4,column=0, sticky='w', pady=5)
        self.varTrainingDay = StringVar()
        listOfDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        trainingDayEntry = OptionMenu(self.master, self.varTrainingDay, *listOfDays)
        trainingDayEntry.grid(row = 4,column=1,pady=5)       

        saveButton = Button(self.master,text="Save", borderwidth=0, command=lambda:self.handleSaveInformationEvent(),  highlightthickness=0).grid(row = 5,column=1, pady=50,padx=5,sticky="w")
        cancelButton = Button(self.master,text="Cancel", borderwidth=0,  highlightthickness=0, command=lambda:self.closeWindow()).grid(row = 5,column=1, pady=50, padx=5)

    
    '''
    Intent: searches through  all aexercises to match body part parameter. Calls function in addExerciseController.
    Inputs list of returned exercises into exercise optionMenu.
    '''
    def getExercisesBasedOnBodyPart(self, bodyPart):
        listOfExercises = self.addExerciseControllerObject.searchBodyPart(bodyPart.lower())
        
        exerciseEntry = OptionMenu(self.master, self.varExercise, *listOfExercises)
        exerciseEntry.grid(row = 3,column=1,pady=5) 


    '''
    Intent: handles the save information button for add exercise GUI. Adds exercise 
    user successfully inputs information about the exercise. 
    '''
    def handleSaveInformationEvent(self):
        exerciseName = self.varExercise.get()
        day = self.varTrainingDay.get()

        if exerciseName == "None":
            popupGUI = PopUpGUI("Please choose an exercise.")
            popupGUI.createPopUp()
            return False
        elif day == "":
            popupGUI = PopUpGUI("Please choose an training day.")
            popupGUI.createPopUp()
            return False

        # if day is not in userObject, display error message
        elif day not in self.userObject.getTrainingDays():
            popupGUI = PopUpGUI("Please choose one of your training days.")
            popupGUI.createPopUp()
            return False

        self.addExerciseControllerObject.addExercise(exerciseName, day, self.master)
        
        

  
    '''
    Intent: close the add exercise window and create and display my workouts GUI.
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. closes the add exercise window
    '''
    def closeWindow(self):
        self.master.destroy()
        myWorkoutController = myworkout_controller.MyWorkoutsController(self.userObject, self.exerciseObject, self.allExercises)
        myWorkoutController.createMyWorkoutsGUI()
