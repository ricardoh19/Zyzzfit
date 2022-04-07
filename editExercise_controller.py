import editExercise_gui
from tkinter import *
import myworkout_controller




"""This class controls the logic for user changing information about a specific exercise."""
class EditExerciseController():
    def __init__(self, userObject, exerciseObject):
        self.exerciseObject = exerciseObject
        self.userObject = userObject
       

    '''
    Intent: creates edit exercise GUI
    * Preconditions: 
    * Tkinter is imported
    * editExercise_gui exists
    * Postconditions:
    * Post0. edit exercise GUI is created
    '''
    def createEditExerciseGUI(self, exerciseName):
        root = Tk()
        root.geometry("600x450")
        editExerciseGUIObject = editExercise_gui.EditExerciseGUI(root, self.userObject, self.exerciseObject, exerciseName)
        root.mainloop()


    '''
    Intent: This class compares the original exercise object with exercise object created in GUI. Information will be replaced if there
    are any changes. editExerciseGUI is also closed and myWorkouts controller is created and displayed.
    '''
    def compareExerciseObjects(self, exerciseName, newExerciseObject, editExerciseGUI):
        if self.exerciseObject.getSets(exerciseName) != newExerciseObject["sets"]:
            self.exerciseObject.updateSets(exerciseName, newExerciseObject["sets"])
        if self.exerciseObject.getReps(exerciseName) != newExerciseObject["reps"]:
            self.exerciseObject.updateReps(exerciseName, newExerciseObject["reps"])
        if self.exerciseObject.getMaxWeight(exerciseName) != newExerciseObject["Max Weight"]:
            self.exerciseObject.updateMaxWeight(exerciseName, newExerciseObject["Max Weight"])
        if self.exerciseObject.getOriginalWeight(exerciseName) != newExerciseObject["Original weight"]:
            self.exerciseObject.updateOriginalWeight(exerciseName, newExerciseObject["Original weight"])

        editExerciseGUI.destroy() # close dit exercise GUI

        # create MYWorkout controller and display GUI
        myWorkoutController = myworkout_controller.MyWorkoutsController(self.userObject, self.exerciseObject)
        myWorkoutController.createMyWorkoutsGUI()



    
        

