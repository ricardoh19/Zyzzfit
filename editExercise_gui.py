from tkinter import *
import tkinter as tk
from tkinter import ttk
import loginlogout_controller 



# this class controls the graphical user interface of the userInformation window. Its methods include createMainFrame, createDaysFrame,
# handleSaveInformationEvent, and closeWindow
class EditExerciseGUI():
    def __init__(self, master):
        self.loginlogout_ControllerObject = loginlogout_controller.LoginLogoutControllers()
        self.master = master
        self.master.configure(background= "#3E3C3C")
        self.master.title("Edit Workout")
        

        self.createMainFrame()

    '''
    Intent: creates the main frame for the userInformation GUI
    * Preconditions: master is connected to TKinter. 
    * Postconditions:
    * Post0. main frame for userInformation is created
    '''
    def createMainFrame(self): 
        self.title = Label(self.master, text="Edit Exercise",font=("Fixedsys", 40, "bold"),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=1,column=0, columnspan=2 )
        
        self.exerciseName = Label(self.master, text="Exercise name",font=("Fixedsys", 20, "bold"),height = 2, width = 35,borderwidth=1, background='lightgray', foreground='black').grid(row=2,column=0, columnspan=2) 

        self.sets = Label(self.master, text="Sets",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=3,column=0, sticky='w', pady=5)
        self.setsEntry = Entry(self.master)
        self.setsEntry.grid(row = 3,column=1,pady=5)
        self.reps = Label(self.master, text="Reps",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=4,column=0, sticky='w',pady=5)
        self.repsEntry = Entry(self.master)
        self.repsEntry.grid(row =4,column=1,pady=5)
        self.maxWeight = Label(self.master, text="Max Weight",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=5,column=0, sticky='w',pady=5)
        self.maxWeightEntry = Entry(self.master)
        self.maxWeightEntry.grid(row = 5,column=1,pady=5)
        
        self.originalWeight = Label(self.master, text="Original Weight",font=("Fixedsys", 15),height = 2, width = 20,borderwidth=0, background='#3E3C3C', foreground='white').grid(row=6,column=0, sticky='w',pady=5)
        self.originalWeightEntry = Entry(self.master)
        self.originalWeightEntry.grid(row = 6,column=1,pady=5)



        self.saveButton = Button(self.master,text="Save", borderwidth=0, command=lambda:self.handleSaveInformationEvent(),  highlightthickness=0).grid(row = 7,column=1, pady=5,padx=5,)
        self.cancelButton = Button(self.master,text="Cancel", borderwidth=0,  highlightthickness=0, command=lambda:self.closeWindow()).grid(row = 7,column=1, pady=5, padx=5,sticky="e")

    
    

    '''
    Intent: Calls method in loginlogoutController to save information inputted by user.
    * Preconditions: loginlogout_ControllerObject is an instance of loginlogoutController class
    * Postconditions:
    * Post0. loginlogoutController calls userInformationProcessing().
    '''
    def handleSaveInformationEvent(self):
        self.loginlogout_ControllerObject.userInformationProcessing(self.username, self.password, self.securityQuestion, self.ageEntry.get(), self.weightEntry.get(), self.heightEntry.get(), self.clickedGender.get(), self.clickedGoal.get(), self.listOfDays, self.master)
        
        

  
    '''
    Intent: close the userInformation window .
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. closes the userInformation window
    '''
    def closeWindow(self):
        self.master.destroy()



def main():
    root = Tk()
    root.geometry("650x550")
    userInformationGUIObject = EditExerciseGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()