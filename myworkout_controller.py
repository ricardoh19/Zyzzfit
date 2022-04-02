from tkinter import *
from popup_gui import PopUpGUI
import myworkout_gui
import dashboard_controller

class MyWorkoutsController():
    def __init__(self, userObject, exerciseObject):
        self.userObject = userObject
        self.exerciseObject = exerciseObject

    def createMyWorkoutsGUI(self):
        root = Tk()
        root.geometry("1200x650")
        myWorkoutsGUIObject = myworkout_gui.MyWorkoutGUI(root, self.userObject, self.exerciseObject)
        root.mainloop()

    def createMyProfileController(self):
        pass

    '''
    Intent: Creates Dashboard Controller and calls functions to create user and exercise objects and dashboard GUI.
    * Preconditions: 
    * dashboardController() exists
    * Postconditions:
    * Post0. dashboard controller class is created.
    '''
    def createDashboardController(self, gui):
        gui.destroy()
        
         # create dashboard controller and dashboard GUI
        dashboardController = dashboard_controller.DashboardController(self.userObject, self.exerciseObject)
        dashboardController.createDashboardGUI()


    def createSuggestion(self):
        pass

    def createEditExerciseController(self):
        pass
        
    def createAddExerciseController(self):
        pass

    def createEditWorkoutController(self):
        pass

    def removeExercise(self):
        pass


    def handleLogoutEvent(self):
        pass