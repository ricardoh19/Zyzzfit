from tkinter import *
from popup_gui import PopUpGUI
import dashboard_gui
import loginlogout_controller
import myProfile_controller
import requests
import datetime


"""This class is the intersection of App traffic after login. """
class DashboardController():
    def __init__(self,userObject, userExerciseObject):
        self.loginlogout_controller = loginlogout_controller.LoginLogoutControllers()
        self.dashboardGUIObject = None
        self.userObject = userObject
        self.exerciseObject = userExerciseObject
        self.popup_GUI_object = None
        
    
    def logOutPushChanges(self, username, finalUserObject):
        """In Dashboard GUI logout button is pressed.
        The controller passes the control back to login/logout controller.
        Login logout controller function is called which pushes the changes to the database"""
        self.loginlogout_controller.logout_push_changes_to_database(username,finalUserObject)
        

    def createDashboardGUI(self):
        """This function creates the Dashboard GUI Object"""
        root = Tk()
        root.geometry("1400x700")
        self.dashboardGUIObject = dashboard_gui.DashboardGUI(root, self.userObject, self.exerciseObject)
        root.mainloop()

    def openLoginGUI(self):
        """This function creates the Dashboard GUI Object"""
        self.loginlogout_controller.createLoginGUI()


    '''
    Intent: Creates My Workouts Controller and calls functions to create My Workouts GUI.
    * Preconditions: 
    * MyWorkoutsController() exists
    * Postconditions:
    * Post0. My Workouts controller class is created and My Workouts GUI is created and displayed.
    '''
    def createMyWorkoutsController(self):
        pass
    
    def createMyProfileController(self):
        myWorkoutsControllerObject = myProfile_controller.MyProfileController(self.userObject)
        myWorkoutsControllerObject.createMyProfileGUI()



    def getFullDate(self):
        x = datetime.datetime.now()
        dayWeek = x.strftime("%A")
        month = x.strftime("%B")
        day = x.day
        date = "{}, {} {}".format(dayWeek ,month, day)
        return date

    def getDay(self):
        x = datetime.datetime.now()
        dayWeek = x.strftime("%A")
        return dayWeek


    def getQuote(self):
        fullresponse = requests.get("https://zenquotes.io/api/quotes/random")
        response = fullresponse.json()[0]
        quote = response['q']
        author = response['a']
        return {"q":quote, "a": author} 

    def calculateCalorieIntake(self):
        pass

    
    def getUsername(self):
        pass
    


if __name__ == "__main__":
    userObject = None
    dashboardController = DashboardController(userObject)
    dashboardController.getQuote()