from shutil import ExecError
import addExercise_gui
from database_manager import DB
from tkinter import *
import myworkout_controller

"""This class controls the logic for user changing information about a specific exercise."""
class AddExerciseController():
    def __init__(self, userObject, exerciseObject):
        self.exerciseObject = exerciseObject
        self.userObject = userObject
        self.databaseManagerObject = DB()

    '''
    Intent: creates add exercise GUI
    * Preconditions: 
    * Tkinter is imported
    * Postconditions:
    * Post0. add exercise GUI is created
    '''
    def createAddExerciseGUI(self):
        root = Tk()
        root.geometry("600x450")
        userInformationGUIObject = addExercise_gui.AddExerciseGUI(root, self.userObject, self.exerciseObject)
        root.mainloop()

    def searchBodyPart(self, bodyPart):
        allExercises = self.databaseManagerObject.getDatabaseExerciseData()
        allExercisesList = []
        for exercise in allExercises:
            if exercise[1] == bodyPart and exercise[2] not in allExercisesList:
                allExercisesList.append(exercise[2])
        return allExercisesList

    
    def addExercise(self, exerciseName, day, addExerciseGUI):
        # get last userExerciseId
        largestExerciseId = self.exerciseObject.getUserExerciseId("Bench Press")
        for data in self.exerciseObject.keys():
            if self.exerciseObject.getUserExerciseId(data) > largestExerciseId:
                largestExerciseId = self.exerciseObject.getUserExerciseId(data)
        

        # add whole exercise to exerciseObject
        self.exerciseObject.insertExercise(exerciseName, largestExerciseId, day)

        addExerciseGUI.destroy() # close add exercise GUI

        myWorkoutController = myworkout_controller.MyWorkoutsController(self.userObject, self.exerciseObject)
        myWorkoutController.createMyWorkoutsGUI()