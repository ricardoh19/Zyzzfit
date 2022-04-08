from hashlib import new
from tkinter import *
import tkinter as tk
from tkinter import ttk
import editExercise_controller
import myworkout_controller
from popup_gui import PopUpGUI



# this class controls the graphical user interface of the edit exercise window.
class EditExerciseGUI():
    def __init__(self, master, userObject, exerciseObject, exerciseName):
        self.master = master
        self.master.configure(background= "#3E3C3C")
        self.master.title("Edit Exercise")
        self.exerciseObject = exerciseObject
        self.userObject = userObject
        self.exerciseNameString = exerciseName
        self.editExercise_controllerObject = editExercise_controller.EditExerciseController(self.userObject, self.exerciseObject)
        self.createMainFrame()

    '''
    Intent: creates the main frame for the editExercise GUI
    * Preconditions: master is connected to TKinter. 
    * Postconditions:
    * Post0. main frame for edit exercise is created
    '''
    def createMainFrame(self): 
        self.title = Label(self.master, text="Edit Exercise",font=("Fixedsys", 40, "bold"),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=1,column=0, columnspan=2 )
        
        self.exerciseName = Label(self.master, text=self.exerciseNameString, font=("Fixedsys", 20, "bold"),height = 2, width = 35,borderwidth=1, background='lightgray', foreground='black').grid(row=2,column=0, columnspan=2) 

        self.sets = Label(self.master, text="Sets",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=3,column=0, sticky='w', pady=5)
        self.setsEntry = Entry(self.master)
        self.setsEntry.grid(row = 3,column=1,pady=5)
        
        self.setsEntry.insert(0, self.exerciseObject.getSets(self.exerciseNameString))
        self.reps = Label(self.master, text="Reps",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=4,column=0, sticky='w',pady=5)
        self.repsEntry = Entry(self.master)
        self.repsEntry.grid(row =4,column=1,pady=5)
        self.repsEntry.insert(0, self.exerciseObject.getReps(self.exerciseNameString))
        self.maxWeight = Label(self.master, text="Max Weight",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=5,column=0, sticky='w',pady=5)
        self.maxWeightEntry = Entry(self.master)
        self.maxWeightEntry.grid(row = 5,column=1,pady=5)
        self.maxWeightEntry.insert(0, self.exerciseObject.getMaxWeight(self.exerciseNameString))
        
        self.originalWeight = Label(self.master, text="Original Weight",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=6,column=0, sticky='w',pady=5)
        self.originalWeightEntry = Entry(self.master)
        self.originalWeightEntry.grid(row = 6,column=1,pady=5)
        self.originalWeightEntry.insert(0, self.exerciseObject.getOriginalWeight(self.exerciseNameString))


        self.saveButton = Button(self.master,text="Save", borderwidth=0, command=lambda: self.handleSaveInformationEvent(),  highlightthickness=0).grid(row = 7,column=1, pady=5,padx=5,)
        self.cancelButton = Button(self.master,text="Cancel", borderwidth=0,  highlightthickness=0, command=lambda: self.closeWindow()).grid(row = 7,column=1, pady=5, padx=5,sticky="e")

    
    

    '''
    Intent: sets, reps, max and orginal weight is gotten and and exercise object is created. This exercise object will be used to 
    compare with the original exercise object. 
    '''
    def handleSaveInformationEvent(self):
        sets = self.setsEntry.get()
        reps = self.repsEntry.get()
        maxWeight = self.maxWeightEntry.get()
        originalWeight = self.originalWeightEntry.get()
        
        try: 
            sets = int(sets)
            reps = int(reps)
            maxWeight = int(maxWeight)
            originalWeight = int(originalWeight)
        except ValueError:
            popupGUI = PopUpGUI("Field left blank.")
            popupGUI.createPopUp()
            return False

        newExerciseObject = {'sets': sets, 'reps': reps, 'Max Weight': maxWeight, 'Original weight': originalWeight}
        
        self.editExercise_controllerObject.compareExerciseObjects(self.exerciseNameString, newExerciseObject, self.master)
        
        

  
    '''
    Intent: close the edit exercise window .
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. closes the edit exercise window
    '''
    def closeWindow(self):
        self.master.destroy()
        myWorkoutController = myworkout_controller.MyWorkoutsController(self.userObject, self.exerciseObject)
        myWorkoutController.createMyWorkoutsGUI()


