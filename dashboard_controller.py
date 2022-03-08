from tkinter import *
from popup_gui import PopUpGUI
import dashboard_gui
import loginlogout_controller
import requests


"""This class is the intersection of App traffic after login. """
class DashboardController():
    def __init__(self,userObject):
        self.loginlogout_controller = loginlogout_controller.LoginLogoutControllers()
        self.dashboardGUIObject = None
        self.userObject = userObject
        self.popup_GUI_object = None
        
    
    def logOutPushChanges(self, username, finalUserObject):
        """In Dashboard GUI logout button is pressed.
        The controller passes the control back to login/logout controller.
        Login logout controller function is called which pushes the changes to the database"""
        self.loginlogout_controller.logout_push_changes_to_database(username,finalUserObject)
        

    def createDashboardGUI(self):
        """This function creates the Dashboard GUI Object"""
        root = Tk()
        root.geometry("900x600")
        self.dashboardGUIObject = dashboard_gui.DashboardGUI(root, self.userObject)
        root.mainloop()

    def openLoginGUI(self):
        """This function creates the Dashboard GUI Object"""
        self.loginlogout_controller.createLoginGUI()


    def createMyWorkoutsController(self):
        pass
    
    def createMyProfileController(self):
        pass

    def getUserWorkoutsForDay(self):
        pass


    def getFullDate(self):
        pass

    def getDay(self):
        pass


    def getQuote(self):
        fullresponse = requests.get("https://zenquotes.io/api/quotes/random")
        response = fullresponse.json()[0]
        quote = response['q']
        author = response['a']
        return {"q":quote, "a": author} 

    def calculateCalorieIntake(self):
        pass

    def getDaysAmountExercise(self):
        pass

    def getUsername(self):
        pass
    


if __name__ == "__main__":
    userObject = None
    dashboardController = DashboardController(userObject)
    dashboardController.getQuote()