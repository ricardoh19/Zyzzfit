from tkinter import *
from popup_gui import PopUpGUI
import myworkout_gui
import dashboard_controller
import editExercise_controller
import myProfile_controller
import addExerciseController

class MyWorkoutsController():
    def __init__(self, userObject, exerciseObject):
        self.userObject = userObject
        self.exerciseObject = exerciseObject

    """This function creates the My Workouts GUI Object"""
    def createMyWorkoutsGUI(self):
        root = Tk()
        root.geometry("1200x650")
        myWorkoutsGUIObject = myworkout_gui.MyWorkoutGUI(root, self.userObject, self.exerciseObject)
        root.mainloop()

    """This function creates the My Profile Controller"""
    def createMyProfileController(self, myWorkoutsGUI):
        myWorkoutsGUI.destroy() # close the My workouts GUI

        # create my profile controller and my profile GUI
        windowOpenedFrom = "myWorkouts"
        myProfileControllerObject = myProfile_controller.MyProfileController(self.userObject, self.exerciseObject, windowOpenedFrom)
        myProfileControllerObject.createMyProfileGUI()


    '''
    Intent: Creates Dashboard Controller and calls functions to create user and exercise objects and dashboard GUI.
    '''
    def createDashboardController(self, myWorkoutsGUI):
        myWorkoutsGUI.destroy() # close myWorkouts GUI window

        # create dashboard controller and dashboard GUI
        dashboardController = dashboard_controller.DashboardController(self.userObject, self.exerciseObject)
        dashboardController.createDashboardGUI()


    def createSuggestion(self):
        return "Try to keep compound movements in the beginning of a workout.\nSome examples of compound Movements are Bench Press, Deadlift, Squat, and PullUps."
        

    '''
    Intent: Creates edit exercise Controller and calls functions to create user and exercise objects and edit exercise GUI.
    '''
    def createEditExerciseController(self, exerciseName, myWorkoutGUI):
        myWorkoutGUI.destroy() # close myWorkouts GUI window

        # create edit exercise controller and display edit Exercise GUI
        editExercise_controllerObject = editExercise_controller.EditExerciseController(self.userObject, self.exerciseObject)
        editExercise_controllerObject.createEditExerciseGUI(exerciseName)

    '''
    Intent: Creates add exercise Controller and calls functions to create user and exercise objects and add exercise GUI.
    '''
    def createAddExerciseController(self, myWorkoutGUI):
        myWorkoutGUI.destroy() # close myWorkouts GUI window
        addExerciseControllerObject = addExerciseController.AddExerciseController(self.userObject, self.exerciseObject)
        addExerciseControllerObject.createAddExerciseGUI()
   
    '''
    Intent: Removes exercise from exerciseObject. 
    '''
    def removeExercise(self, exerciseName):
        self.exerciseObject.removeExercise(exerciseName)
        


    def handleLogoutEvent(self):
        pass