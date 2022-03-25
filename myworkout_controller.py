from tkinter import *
from popup_gui import PopUpGUI
import myworkout_gui

class MyWorkoutsController():
    def __init__(self, userObject, exerciseObject):
        self.userObject = userObject
        self.exerciseObject = exerciseObject

    def createMyWorkoutsGUI(self):
        root = Tk()
        root.geometry("1200x600")
        myWorkoutsGUIObject = myworkout_gui.MyWorkoutGUI(root, self.userObject, self.exerciseObject)
        root.mainloop()