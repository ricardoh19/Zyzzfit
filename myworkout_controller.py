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
        self.dashboardControllerObject = dashboard_controller.DashboardController(self.userObject, self.exerciseObject)

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

    '''
    Intent: Creates the suggestion based on the length of user's training days. Returns suggestion
    '''
    def createSuggestion(self, dayLength):
        suggestion = ''
        if dayLength == 2:
            suggestion = "Suggested structure of workout for 2 days: DAY 1: Full Body 1, DAY 2: Full Body 2"
        if dayLength == 3:
            suggestion = "Suggested structure of workout for 3 days: DAY 1: Chest, Shoulders, Triceps DAY 2: Back, Biceps DAY 3: Legs"
        if dayLength == 4:
            suggestion = "Suggested structure of workout for 4 days: DAY 1: Chest, Triceps DAY 2: Back, Biceps DAY 3: Legs\nDAY 4: Shoulders"
        if dayLength == 5:
            suggestion = "Suggested structure of workout for 5 days: DAY 1: Chest DAY 2: Biceps, Triceps DAY 3: Legs \nDAY 4: Legs DAY 5: Shoulders"
        if dayLength == 6:
            suggestion = "Suggested structure of workout for 6 days: DAY 1: Chest, Shoulders, Triceps DAY 2: Back, Biceps DAY 3: Legs \nDAY 4: Chest, Shoulders, Triceps DAY 5: Back, Biceps DAY 6: Legs"
        if dayLength == 7:
            suggestion = "Suggested structure of workout for 6 days: DAY 1: Chest, Shoulders, Triceps DAY 2: Back, Biceps DAY 3: Legs \nDAY 4: Chest, Shoulders, Triceps DAY 5: Back, Biceps DAY 6: Legs DAY 7: Cardio"
        return "Try to keep compound movements in the beginning of a workout.\n \
        Some examples of compound Movements are Bench Press, Deadlift, Squat, and PullUps.\n\n" + suggestion

        

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
        

    """In My Workouts GUI logout button is pressed.
    The controller passes the control back to login/logout controller.
    Login logout controller function is called which pushes the changes to the database"""
    def handleLogoutEvent(self):
        username = self.userObject.getUsername()
        self.dashboardControllerObject.logOutPushChanges(username, self.userObject, self.exerciseObject)