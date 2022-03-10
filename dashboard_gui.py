from tkinter import *
import tkinter as tk
from tkinter import ttk
import datetime
import dashboard_controller



# this class controls the graphical user interface of the dashboard window. Its methods include 

class DashboardGUI():
    def __init__(self, master, userObject, exerciseObject):
        self.master = master
        self.master.configure(background= "#3E3C3C")
        self.master.title("Dashboard")
        self.createMainFrame()
        
        self.userObject = userObject
        self.exerciseObject = exerciseObject
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

        self.profile = Button(self.master, text="My Profile",font='Fixedsys 12',  height=3, width = 15, borderwidth=3, relief="solid", background='white').grid(row=0,column=4, pady=4, sticky='e')
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


    def createWorkoutFrame(self):
        self.tree = ttk.Treeview(self.master, column=("Exercise", "Sets","Reps"), show='headings', height=19)
        self.tree.grid(row=2,column=1, padx=5, columnspan=2, rowspan=2)

        self.tree.heading('Exercise', text='Exercise')
        self.tree.column("Exercise", stretch=NO, width=400)

        self.tree.heading('Sets', text='Sets')
        self.tree.column("Sets", stretch=NO, width=75)

        self.tree.heading('Reps', text='Reps')
        self.tree.column("Reps", stretch=NO, width=75)

        
        
        
        #self.workouts = Label(self.master, text="workouts",font='fixedsys 12',  width = 55, height=25, borderwidth=0, background='white').grid(row=2,column=1, padx=5, columnspan=2, rowspan=2)

    def createQuoteFrame(self):
        userObject = None
        exerciseObject = None
        self.dashboardControllerObject = dashboard_controller.DashboardController(userObject,exerciseObject)
        quote = self.dashboardControllerObject.getQuote()
        print(quote)
        self.quote = Label(self.master, text="{}\n{}\n-{}".format(quote['q'][:100], quote['q'][100:], quote['a']),font='fixedsys 10', height=4, width = 78, borderwidth=0, background='white').grid(row=1,column=1, columnspan=2)

    def createDateFrame(self):
        x = datetime.datetime.now()
        dayWeek = x.strftime("%A")
        month = x.strftime("%B")
        day = x.day
        date = "{}, {} {}".format(dayWeek ,month, day)

        self.date = Label(self.master, text=date,font='fixedsys 17 bold', height=2, width = 29, background='lightGray', foreground="black").grid(row=1,column=3, columnspan=2)

    def createDaysFrame(self):
        self.dayNumber = Label(self.master, text="3 day split",font='fixedsys 12', height=12, width = 41, borderwidth=0, background='white').grid(row=2,column=3,columnspan=2)

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
    root.geometry("1200x600")
    userObject = None
    exerciseObject = None
    dashboardGUIObject = DashboardGUI(root, userObject, exerciseObject)
    root.mainloop()

if __name__ == "__main__":
    main()