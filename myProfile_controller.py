from tkinter import *
from popup_gui import PopUpGUI
import dashboard_controller
import loginlogout_controller
import myProfile_GUI
from user import User

class MyProfileController():
    def __init__(self, userObject, exerciseObject):
        self.userObject = userObject
        self.exerciseObject = exerciseObject
        
    '''
    Intent: creates My Profile GUI
    * Preconditions: 
    * Tkinter is imported and working
    * My Profile GUI exists
    * Postconditions:
    * Post0. My Profile GUI is created
    '''
    def createMyProfileGUI(self):
        root = Tk()
        root.geometry("710x550")
        userInformationGUIObject = myProfile_GUI.MyProfileGUI(root, self.userObject, self.exerciseObject)
        root.mainloop()

    '''
    Intent: Creates Dashboard Controller and calls functions to create user and exercise objects and dashboard GUI.
    * Preconditions: 
    * dashboardController() exists
    * Postconditions:
    * Post0. dashboard controller class is created.
    '''
    def createDashboardController(self, userObject, exericiseObject):
        userObject =  User(self.currentUserData, self.currentUserTrainingDays)
        dashboardController = dashboard_controller.DashboardController(userObject, exericiseObject)
        dashboardController.createDashboardGUI()

    def compareObjects(self, userObjectToCompare, newUserObject, myProfileGUI):

        # traverse and compare both userObjects and save if there are any changes
        for key,value in userObjectToCompare.items():
            if userObjectToCompare[key] != newUserObject[key]:
                if key == 'age':
                    self.userObject.updateAge(newUserObject[key])
                #userObjectToCompare[key] = newUserObject[key]
        
        myProfileGUI.destroy()
        return self.userObject

        
