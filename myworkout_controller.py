from tkinter import *
from popup_gui import PopUpGUI
import myworkout_gui

class MyWorkoutsController():
    def __init__(self, userObject):
        self.userObject = userObject

    def createMyWorkoutsGUI(self):
        root = Tk()
        root.geometry("1200x600")
        myWorkoutsGUIObject = myworkout_gui.MyWorkoutGUI(root)
        root.mainloop()