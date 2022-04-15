from shutil import ExecError
import addExercise_gui
from tkinter import *
import myworkout_controller


"""This class controls the logic for user changing information about a specific exercise."""
class AddExerciseController():
    def __init__(self, userObject, exerciseObject, allExercises):
        self.exerciseObject = exerciseObject
        self.userObject = userObject
        self.allExercises = allExercises

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
        userInformationGUIObject = addExercise_gui.AddExerciseGUI(root, self.userObject, self.exerciseObject, self.allExercises)
        root.mainloop()

    '''
    Intent: All exercises obtained frmo database will be gotten and search for bodyPart parameter. 
    Exercise pertianing to that body part will be returned in a list.
    '''
    def searchBodyPart(self, bodyPart):
        
        allExercisesList = []
        for exercise in self.allExercises:
            if exercise[1] == bodyPart and exercise[2] not in allExercisesList:
                allExercisesList.append(exercise[2])
        return allExercisesList

    '''
    Intent: Exercise will be added to exercise object with the last userExerciseId obtained. AddWorkoutsGUI will be closed and 
    MyWorkouts GUI will be displayed.
    '''
    def addExercise(self, exerciseName, day, addExerciseGUI):
        # get last userExerciseId
        largestExerciseId = self.exerciseObject.getUserExerciseId(list(self.exerciseObject.keys())[0])
        for data in self.exerciseObject.keys():
            if self.exerciseObject.getUserExerciseId(data) > largestExerciseId:
                largestExerciseId = self.exerciseObject.getUserExerciseId(data)
        

        # add whole exercise to exerciseObject
        self.exerciseObject.insertExercise(exerciseName, largestExerciseId, day)

        addExerciseGUI.destroy() # close add exercise GUI

        # create my workout controller and displays my workouts GUI
        myWorkoutController = myworkout_controller.MyWorkoutsController(self.userObject, self.exerciseObject, self.allExercises)
        myWorkoutController.createMyWorkoutsGUI()