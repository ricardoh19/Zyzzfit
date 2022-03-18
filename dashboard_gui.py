from tkinter import *
import tkinter as tk
from tkinter import ttk
import datetime

import dashboard_controller
from PIL import ImageTk,Image 



# this class controls the graphical user interface of the dashboard window. Its methods include 

class DashboardGUI():
    def __init__(self, master, userObject, exerciseObject):
        self.master = master
        self.master.configure(background= "#3E3C3C")
        self.master.title("Dashboard")
        self.userObject = userObject
       
        self.exerciseObject = exerciseObject
        self.createMainFrame()
        self.dashboardControllerObject = dashboard_controller.DashboardController(userObject, exerciseObject)

    '''
    Intent: creates the main frame for the dashboard GUI
    * Preconditions: master is connected to TKinter. 
    * createWatchlistPortfolioFrame and createSearchbarFrame have the appropriate GUI code to be called in this method.
    * Postconditions:
    * Post0. main frame for dashboard is created
    '''
    def createMainFrame(self):
        self.createMenuFrame()
        self.title = Label(self.master, text="Dashboard",font='fixedsys 20 bold', height=5, width = 20, borderwidth=0, background='#3E3C3C', foreground="white").grid(row=0,column=1, pady=5, padx=5, columnspan=2, sticky='w')

        self.profile = Button(self.master, text="My Profile",font='Fixedsys 12', command=lambda:self.openMyWorkoutsGUI(), height=3, width = 15, borderwidth=3, relief="solid", background='white').grid(row=0,column=4, pady=4, sticky='e')
        self.createQuoteFrame()
        self.createDateFrame()
        self.createWorkoutFrame()
        self.createDaysFrame()
        self.createCaloriesFrame()

        self.exitButton = Button(self.master,text="Log Out", command=lambda:self.handleLogoutEvent(), borderwidth=0).grid(row = 3,column=0, sticky='s')


    def createMenuFrame(self):
        self.menuFrame = Frame(self.master, height=555, width = 150, relief="solid", background='white').grid(row=0,column=0, pady=5, padx=15, rowspan=4)
        self.menu = Label(self.menuFrame, text="Zyzzfit",font='fixedsys 25 bold', background='white').grid(row=0,column=0)
        self.dashboardButton = Button(self.menuFrame, text="Dashboard",font='fixedsys 10 bold', borderwidth=0).grid(row=1,column=0, sticky='ne', padx=20) 
        self.myWorkoutsButton = Button(self.menuFrame, text="My Workouts",font='fixedsys 10 bold', borderwidth=0).grid(row=1,column=0, sticky='se', padx=20) 
        image = Image.open("assets/dashboard.png")
        resize_image = image.resize((15,15))
        img = ImageTk.PhotoImage(resize_image)
        panel = Label(self.master, image = img, width=15, height=15)
        panel.image = img
        panel.grid(row=1,column=0, sticky='nw', padx=20)

        image = Image.open("assets/workout.png")
        resize_image = image.resize((15,15))
        img = ImageTk.PhotoImage(resize_image)
        panel = Label(self.master, image = img, width=15, height=15)
        panel.image = img
        panel.grid(row=1,column=0, sticky='sw', padx=20)

    def createDateFrame(self):
        self.date = self.dashboardControllerObject.getFullDate()
        self.date = Label(self.master, text=self.date,font='fixedsys 17 bold', height=2, width = 29, background='lightGray', foreground="black").grid(row=1,column=3, columnspan=2)

    def createWorkoutFrame(self):
        self.title = Label(self.master, text="Today's Workout",font='fixedsys 10 bold', height=1, width = 20, borderwidth=0, background='#3E3C3C', foreground="white").grid(row=2,column=1, sticky='w')

        self.tree = ttk.Treeview(self.master, column=("Exercise", "Sets","Reps"), show='headings', height=12)
        self.tree.grid(row=2,column=1, pady=5, padx=3, rowspan=2, columnspan=2, sticky='s')
        
        self.tree.heading('Exercise', text='Exercise')
        self.tree.column("Exercise", stretch=NO, width=400)

        self.tree.heading('Sets', text='Sets')
        self.tree.column("Sets", stretch=NO, width=75)

        self.tree.heading('Reps', text='Reps')
        self.tree.column("Reps", stretch=NO, width=75)

        self.day = self.dashboardControllerObject.getDay()

        DayCount = 0
        if self.exerciseObject != None:
            for i in self.exerciseObject:
                if self.exerciseObject[i]["training Day"] == self.day:
                    DayCount +=1 
                    try:
                        self.sets = self.exerciseObject[i]["sets"]
                        self.reps = self.exerciseObject[i]["reps"]
                        self.tree.insert('', 'end', text=i, values=(i, self.sets, self.reps))
                    except KeyError:
                        self.tree.insert('', 'end', text=i, values=(i, "N/A", "N/A"))
                
        if DayCount == 0:
            self.tree.insert('', 'end', text=i, values=("No Exercises Today", "N/A", "N/A"))
        
        
    
    def openMyWorkoutsGUI(self):
        self.dashboardControllerObject.createMyProfileController()

        
    def createQuoteFrame(self):
        userObject = None
        exerciseObject = None
        self.dashboardControllerObject = dashboard_controller.DashboardController(userObject,exerciseObject)
        quote = self.dashboardControllerObject.getQuote()
        print(quote)
        self.quote = Label(self.master, text="{}\n{}\n-{}".format(quote['q'][:100], quote['q'][100:], quote['a']),font='fixedsys 10 bold', height=4, width = 78, borderwidth=0, background='white').grid(row=1,column=1, columnspan=2)

    

    def createDaysFrame(self):
        if self.userObject != None:
            daySplit = len(self.userObject["Training days"])
            self.dayNumber = Label(self.master, text="{} Day Split".format(daySplit),font='fixedsys 12', height=12, width = 41, borderwidth=0, background='white').grid(row=2,column=3,columnspan=2)


    def createCaloriesFrame(self):
        self.calories = Label(self.master, text="Calories",font='fixedsys 12', height=12, width = 41,borderwidth=0, background='white').grid(row=3,column=3, columnspan=2)



    '''
    Intent: handles the logic for the user clicking logout button.
    * Preconditions: 
    * Postconditions: 
    * Post0. changes are pushed to database, dashboard window is closed and login window is opened.
    * Post1. Changes are not pushed to database beacause connection to database could not be estbalished.
    
    '''
    def handleLogoutEvent(self):
        #username = self.userObject.current_user_data[1]
        #self.dashboardControllerObject.logOutPushChanges(username, self.userObject)

        self.closeWindow()
        self.dashboardControllerObject.openLoginGUI()
        
    

    '''
    Intent: close the dashboard window .
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. closes the dashboard window
    '''
    def closeWindow(self):
        self.master.destroy()



def main():
    root = Tk()
    root.geometry("1400x700")
    userObject = None
    exerciseObject = None
    dashboardGUIObject = DashboardGUI(root, userObject, exerciseObject)
    root.mainloop()

if __name__ == "__main__":
    main()