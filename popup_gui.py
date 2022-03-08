from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox


# this class controls the graphical user interface of the Pop up window and what it displays.
#  The attibute message is what will be displayed. Its methods are createPopUp()
class PopUpGUI():
    def __init__(self,message):
        self.message = message


    '''
    Intent: creates the message box that will be displayde with the message.
    * Preconditions: TKinter is imported.
    * Postconditions:
    * Post0. message is displayed through tkinter.messagebox.showinfo method
    '''
    def createPopUp(self):
        tkinter.messagebox.showinfo("message", self.message)
        



