from tkinter import *
from popup_gui import PopUpGUI
import dashboard_gui
import loginlogout_controller
import myProfile_controller
import myworkout_controller
import requests
import datetime


"""This class is the intersection of App traffic after login. """
class DashboardController():
    def __init__(self, userObject, userExerciseObject):
        self.loginlogout_controller = loginlogout_controller.LoginLogoutControllers()
        self.dashboardGUIObject = None
        self.userObject = userObject
        self.exerciseObject = userExerciseObject
        self.popup_GUI_object = None
        
        

    """This function creates the Dashboard GUI Object"""
    def createDashboardGUI(self):
        root = Tk()
        root.geometry("1400x700")
        self.dashboardGUIObject = dashboard_gui.DashboardGUI(root, self.userObject, self.exerciseObject)
        root.mainloop()

    """This function creates the Dashboard GUI Object"""
    def openLoginGUI(self):
        self.loginlogout_controller.createLoginGUI()


    """This function creates the My Workouts Controller"""
    def createMyWorkoutsController(self, dashboardGUI):
        myWorkoutsControllerObject = myworkout_controller.MyWorkoutsController(self.userObject, self.exerciseObject)
        dashboardGUI.destroy()
        myWorkoutsControllerObject.createMyWorkoutsGUI()
    
    """This function creates the My Profile Controller"""
    def createMyProfileController(self, dashboardGUI):
        myProfileControllerObject = myProfile_controller.MyProfileController(self.userObject, self.exerciseObject)
        dashboardGUI.destroy()
        myProfileControllerObject.createMyProfileGUI()


    """This function returns the full date using Python's Date Module"""
    def getFullDate(self):
        x = datetime.datetime.now()
        dayWeek = x.strftime("%A")
        month = x.strftime("%B")
        day = x.day
        date = "{}, {} {}".format(dayWeek ,month, day)
        return date

    """This function returns the day of the week using Python's Date Module"""
    def getDay(self):
        x = datetime.datetime.now()
        dayWeek = x.strftime("%A")
        return dayWeek

    """This function returns dictionary with quote and author fetched from zenquotes API"""
    def getQuote(self):
        fullresponse = requests.get("https://zenquotes.io/api/quotes/random")
        response = fullresponse.json()[0]
        quote = response['q']
        author = response['a']
        return {"q":quote, "a": author} 

    """This function calculates and returns amount of calories user should be intaking in a day to meet their goal."""
    def calculateCalorieIntake(self):
        age = self.userObject.getAge()
        weight = self.userObject.getWeight()
        height = self.userObject.getHeight()
        gender = self.userObject.getGender()
        goal = self.userObject.getCalorieGoal()
        

        if gender == "Man":
            caloriesResult = 66.47 + (6.24 * float(weight)) + (12.7 * float(height)) - (6.755 * float(age))
        else:
            caloriesResult = 655.1 + (4.35 * float(weight)) + (4.7 * float(height)) - (4.7 * float(age))
            
        if goal =="Maintain":
                caloriesResult *= 1.5
        if goal == "Lose":
            caloriesResult *= 1.15
        if goal == "Gain":
            caloriesResult *= 1.65
        return int(caloriesResult)

    
    """In Dashboard GUI logout button is pressed.
    The controller passes the control back to login/logout controller.
    Login logout controller function is called which pushes the changes to the database"""
    def logOutPushChanges(self, username, finalUserObject):
        self.loginlogout_controller.logout_push_changes_to_database(username,finalUserObject)
