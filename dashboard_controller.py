from tkinter import *
from popup_gui import PopUpGUI
import dashboard_gui
import loginlogout_controller
import myProfile_controller
import myworkout_controller
import datetime
import requests


"""This class is the intersection of App traffic after login. """
class DashboardController():
    def __init__(self, userObject, userExerciseObject, allExercises):
        self.loginlogout_controller = loginlogout_controller.LoginLogoutControllers()
        self.userObject = userObject
        self.exerciseObject = userExerciseObject
        self.allExercises = allExercises

        
        

    """This function creates the Dashboard GUI Object"""
    def createDashboardGUI(self):
        root = Tk()
        root.geometry("1400x700")
        dashboardGUIObject = dashboard_gui.DashboardGUI(root, self.userObject, self.exerciseObject, self.allExercises)
        root.mainloop()

    """This function creates the Dashboard GUI Object"""
    def openLoginGUI(self):
        self.loginlogout_controller.createLoginGUI()


    """This function creates the My Workouts Controller"""
    def createMyWorkoutsController(self, dashboardGUI):
        dashboardGUI.destroy() # close the dashboard GUI

        # create my profile controller and GUI
        myWorkoutsControllerObject = myworkout_controller.MyWorkoutsController(self.userObject, self.exerciseObject, self.allExercises)
        myWorkoutsControllerObject.createMyWorkoutsGUI()
    
    """This function creates the My Profile Controller"""
    def createMyProfileController(self, dashboardGUI):
        dashboardGUI.destroy() # close the dashboard GUI

        # create my profile controller and GUI
        windowOpenedFrom = "dashboard"
        myProfileControllerObject = myProfile_controller.MyProfileController(self.userObject, self.exerciseObject, windowOpenedFrom, self.allExercises)
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
        fullresponse = requests.get("https://zenquotes.io/api/quotes/random") # API
        response = fullresponse.json()[0]
        quote = response['q']
        author = response['a']
        return {"q":quote, "a": author} 

    """This function calculates and returns amount of calories user should be intaking in a day to meet their goal
    Based on user's age, height, weight, and gender.
    """
    def calculateCalorieIntake(self):
        # get data from user Object using GET methods
        age = self.userObject.getAge()
        weight = self.userObject.getWeight()
        height = self.userObject.getHeight()
        gender = self.userObject.getGender()
        goal = self.userObject.getCalorieGoal()
        
        # calculate calories to intake
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
    def logOutPushChanges(self, username, finalUserObject, finalExerciseObject):
        self.loginlogout_controller.logout_push_changes_to_database(username, finalUserObject, finalExerciseObject)
