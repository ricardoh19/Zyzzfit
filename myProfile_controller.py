from tkinter import *
from popup_gui import PopUpGUI
import dashboard_controller
import loginlogout_controller
import myProfile_GUI
from user import User
from exerciseData import ExerciseData
from database_manager import DB


"""This class controls the logic for user changing their personal information"""
class MyProfileController():
    def __init__(self, userObject, exerciseObject):
        self.userObject = userObject
        self.exerciseObject = exerciseObject
        self.databaseManagerObject = DB()

    '''
    Intent: creates My Profile GUI
    * Preconditions: 
    * Tkinter is imported and working
    * My Profile GUI exists
    * Postconditions:
    * Post0. My Profile GUI is created
    '''
    def createMyProfileGUI(self):
        root = Tk()
        root.geometry("710x550")
        userInformationGUIObject = myProfile_GUI.MyProfileGUI(root, self.userObject, self.exerciseObject)
        root.mainloop()


    '''
    Intent: Will return currentUserExerciseData and currentUserJunctionData lists based on the length of list of days. 
    '''
    def insertExercises(self, listOfDays):
        if len(listOfDays) == 2:
            self.currentUserExerciseData,self.currentUserJunctionData = self.insertNewExercisesFor2Days(listOfDays)
        elif len(listOfDays) == 3:
            self.currentUserExerciseData,self.currentUserJunctionData = self.insertNewExercisesFor3Days(listOfDays)
        elif len(listOfDays) == 4:
            self.currentUserExerciseData,self.currentUserJunctionData = self.insertNewExercisesFor4Days(listOfDays)
        elif len(listOfDays) == 5:
            self.currentUserExerciseData,self.currentUserJunctionData = self.insertNewExercisesFor5Days(listOfDays)
        elif len(listOfDays) == 6:
            self.currentUserExerciseData,self.currentUserJunctionData = self.insertNewExercisesFor6Days(listOfDays)
        elif len(listOfDays) == 7:
            self.currentUserExerciseData,self.currentUserJunctionData = self.insertNewExercisesFor7Days(listOfDays)
        return self.currentUserExerciseData,self.currentUserJunctionData


        

    '''
    Intent: Creates Dashboard Controller and calls functions to create user and exercise objects and dashboard GUI.
    * Preconditions: 
    * dashboardController() exists
    * Postconditions:
    * Post0. dashboard controller class is created.
    '''
    def createDashboardController(self, currentUserData, trainingDaysList, exerciseObject, myProfileGUI):
        myProfileGUI.destroy()
        # create new user object
        userObject =  User(currentUserData, trainingDaysList)
        
        # set new exercises in exercise object based on trainingDayList
        self.currentUserExerciseData,self.currentUserJunctionData = self.insertExercises(trainingDaysList)
        exerciseObject = self.createUserExerciseObject(self.currentUserExerciseData, self.currentUserJunctionData)

         # create dashboard controller and dashboard GUI
        dashboardController = dashboard_controller.DashboardController(userObject, exerciseObject)
        dashboardController.createDashboardGUI()

    '''
    Intent: Creates exercise object by passing username parameter. Returns exercise object
    * Preconditions: AllExercises table exists in database.
    * Postconditions:
    * Post0. exercise object created and returned.
    * Post1. exercise object is returned as None.
    '''
    def createUserExerciseObject(self, currentUserExerciseData, currentUserJunctionData):
        allExercises = self.databaseManagerObject.getDatabaseExerciseData()
        self.userExerciseObject =  ExerciseData(currentUserExerciseData, currentUserJunctionData, allExercises)
        return self.userExerciseObject


    '''
    Intent: Returns userExerciseData and userExerciseJunction lists. Workout Data for 2 days is inserted into these lists.
    '''
    def insertNewExercisesFor2Days(self, listOfDays):
        userExerciseData = []
        userExerciseJunction = []
        userExerciseId = 0
        for i in range(1,7):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[0]])
            userExerciseId +=1 

        for i in range(7,11):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[1]])
            userExerciseId +=1 
        return userExerciseData, userExerciseJunction


    '''
    Intent: Returns userExerciseData and userExerciseJunction lists. Workout Data for 3 days is inserted into these lists.
    '''
    def insertNewExercisesFor3Days(self, listOfDays):
        userExerciseData = []
        userExerciseJunction = []
        userExerciseId = 0
        for i in range(12,18):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[0]])
            userExerciseId +=1 

        for i in range(18,23):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[1]])
            userExerciseId +=1 

        for i in range(23, 28):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[2]])
            userExerciseId +=1 
        return userExerciseData, userExerciseJunction


    '''
    Intent: Returns userExerciseData and userExerciseJunction lists. Workout Data for 4 days is inserted into these lists.
    '''
    def insertNewExercisesFor4Days(self, listOfDays):
        userExerciseData = []
        userExerciseJunction = []
        userExerciseId = 0
        for i in range(12,18):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[0]])
            userExerciseId +=1 

        for i in range(18,23):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[1]])
            userExerciseId +=1 

        for i in range(23, 28):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[2]])
            userExerciseId +=1 

        for i in range(28, 34):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[3]])
            userExerciseId +=1 
        return userExerciseData, userExerciseJunction


    '''
    Intent: Returns userExerciseData and userExerciseJunction lists. Workout Data for 5 days is inserted into these lists.
    '''
    def insertNewExercisesFor5Days(self, listOfDays):
        userExerciseData = []
        userExerciseJunction = []
        userExerciseId = 0
        for i in range(12,16):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[0]])
            userExerciseId +=1 

        for i in range(34,37):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[1]])
            userExerciseId +=1 

        for i in range(37,41):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[2]])
            userExerciseId +=1 

        for i in range(23,28):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[3]])
            userExerciseId +=1 

        for i in range(41,44):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[4]])
            userExerciseId +=1 
        return userExerciseData, userExerciseJunction

    '''
    Intent: Returns userExerciseData and userExerciseJunction lists. Workout Data for 6 days is inserted into these lists.
    '''
    def insertNewExercisesFor6Days(self, listOfDays):
        userExerciseData = []
        userExerciseJunction = []
        userExerciseId = 0
        for i in range(12,18):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[0]])
            userExerciseId +=1 

        for i in range(18,23):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[1]])
            userExerciseId +=1 

        for i in range(23,28):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[2]])
            userExerciseId +=1 

        for i in range(12,18):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[3]])
            userExerciseId +=1 

        for i in range(18,23):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[4]])
            userExerciseId +=1 

        for i in range(23,28):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[5]])
            userExerciseId +=1 
        return userExerciseData, userExerciseJunction

    '''
    Intent: Returns userExerciseData and userExerciseJunction lists. Workout Data for 7 days is inserted into these lists.
    '''
    def insertNewExercisesFor7Days(self, listOfDays):
        userExerciseData = []
        userExerciseJunction = []
        userExerciseId = 0
        for i in range(12,18):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[0]])
            userExerciseId +=1 

        for i in range(18,23):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[1]])
            userExerciseId +=1 

        for i in range(23,28):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[2]])
            userExerciseId +=1 

        for i in range(12,18):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[3]])
            userExerciseId +=1 

        for i in range(18,23):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[4]])
            userExerciseId +=1 

        for i in range(23,28):
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[5]])
            userExerciseId +=1 
        
        userExerciseData.append([userExerciseId, self.userObject.getUserId(),0 ,0, 0, 0])
        userExerciseId = userExerciseData[-1][0]
        userExerciseJunction.append([userExerciseId, 44, listOfDays[6]])
        
        return userExerciseData, userExerciseJunction
        

        
