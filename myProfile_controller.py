from tkinter import *
from popup_gui import PopUpGUI
import dashboard_gui
import loginlogout_controller
import myProfile_GUI

class MyProfileController():
    def __init__(self, userObject):
        self.userObject = userObject
        

    def createMyProfileGUI(self):
        root = Tk()
        root.geometry("650x550")
        userInformationGUIObject = myProfile_GUI.MyProfileGUI(root, self.userObject)
        root.mainloop()

    """Updates age of user"""
    def updateAge(self, newAge):
        self.userObject.updateAge(newAge)
        print(self.userObject)
