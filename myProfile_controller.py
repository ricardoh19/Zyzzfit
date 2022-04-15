from tkinter import *
from popup_gui import PopUpGUI
import dashboard_controller
import myworkout_controller
import myProfile_GUI
from user import User
from exerciseData import ExerciseData
import loginlogout_controller


"""This class controls the logic for user changing their personal information or training days."""
class MyProfileController():
    def __init__(self, userObject, exerciseObject, windowOpenedFrom, allExercises):
        self.userObject = userObject
        self.exerciseObject = exerciseObject
        self.windowOpenedFrom = windowOpenedFrom
        self.allExercises = allExercises
        self.loginLogoutControllerObject = loginlogout_controller.LoginLogoutControllers()

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
        userInformationGUIObject = myProfile_GUI.MyProfileGUI(root, self.userObject, self.exerciseObject, self.windowOpenedFrom, self.allExercises)
        root.mainloop()


    '''
    Intent: Will return currentUserExerciseData and currentUserJunctionData lists based on the length of list of days. 
    '''
    def insertExercises(self, listOfDays):
        if len(listOfDays) == 2:
            currentUserExerciseData, currentUserJunctionData = self.insertNewExercisesFor2Days(listOfDays)
        elif len(listOfDays) == 3:
            currentUserExerciseData, currentUserJunctionData = self.insertNewExercisesFor3Days(listOfDays)
        elif len(listOfDays) == 4:
            currentUserExerciseData,currentUserJunctionData = self.insertNewExercisesFor4Days(listOfDays)
        elif len(listOfDays) == 5:
            currentUserExerciseData,currentUserJunctionData = self.insertNewExercisesFor5Days(listOfDays)
        elif len(listOfDays) == 6:
            currentUserExerciseData,currentUserJunctionData = self.insertNewExercisesFor6Days(listOfDays)
        elif len(listOfDays) == 7:
            currentUserExerciseData,currentUserJunctionData = self.insertNewExercisesFor7Days(listOfDays)
        return currentUserExerciseData,currentUserJunctionData


        

    '''
    Intent: Creates Dashboard Controller and calls functions to create user and exercise objects and dashboard GUI.
    * Preconditions: 
    * dashboardController() exists
    * Postconditions:
    * Post0. dashboard controller class is created.
    '''
    def createController(self, currentUserData, trainingDaysList, exerciseObject, windowOpenedFrom, myProfileGUI):
        myProfileGUI.destroy() # close the MyProfile GUI

        if len(trainingDaysList) != 0:  # set new exercises in exercise object based on trainingDayList if new days added
            userObject =  User(currentUserData, trainingDaysList)  # create new user object
            currentUserExerciseData,currentUserJunctionData = self.insertExercises(trainingDaysList)
            exerciseObject = self.createUserExerciseObject(currentUserExerciseData, currentUserJunctionData)


        else: # keep old exercises if no new days added
            trainingDays = self.userObject.getTrainingDays()
            userObject = User(currentUserData, trainingDays)
            exerciseObject = self.exerciseObject

        # create dashboard controller or myWorkouts controller
        if windowOpenedFrom == "dashboard":
            dashboardController = dashboard_controller.DashboardController(userObject, exerciseObject, self.allExercises)
            dashboardController.createDashboardGUI()
        else:
            myWorkoutsController = myworkout_controller.MyWorkoutsController(userObject, exerciseObject, self.allExercises)
            myWorkoutsController.createMyWorkoutsGUI()


    

    '''
    Intent: Creates exercise object by passing username parameter. Returns exercise object
    * Preconditions: AllExercises table exists in database.
    * Postconditions:
    * Post0. exercise object created and returned.
    * Post1. exercise object is returned as None.
    '''
    def createUserExerciseObject(self, currentUserExerciseData, currentUserJunctionData):
        allExercises = self.loginLogoutControllerObject.returnAllExercises() # gets all exercises from database
        self.userExerciseObject =  ExerciseData(currentUserExerciseData, currentUserJunctionData, allExercises) # create exercise object
        return self.userExerciseObject


    '''
    Intent: Returns userExerciseData and userExerciseJunction lists. Workout Data for 2 days is inserted into these lists.
    '''
    def insertNewExercisesFor2Days(self, listOfDays):
        userExerciseData = []
        userExerciseJunction = []
        userExerciseId = 0
        for i in range(1,7): # will insert full body exercises for first day
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[0]])
            userExerciseId +=1 

        for i in range(7,12): # will insert full body exercises for second day 
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
        for i in range(12,18): # will insert chest, triceps, and shoulders exercises for first day 
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[0]])
            userExerciseId +=1 

        for i in range(18,23): # will insert back and biceps exercises for second day 
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[1]])
            userExerciseId +=1 

        for i in range(23, 27): # will insert legs exercises for third day 
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
        for i in range(27,31): # will insert chest and triceps exercises for first day 
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[0]])
            userExerciseId +=1 

        for i in range(18,23): # will insert back and biceps exercises for second day 
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[1]])
            userExerciseId +=1 

        for i in range(23, 27): # will insert legs exercises for third day 
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[2]])
            userExerciseId +=1 

        for i in range(31, 37): # will insert shoulders/Arms exercises for fourth day 
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
        for i in range(12,16): # will insert chest exercises for first day 
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[0]])
            userExerciseId +=1 

        for i in range(37,40): # will insert back exercises for second day 
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[1]])
            userExerciseId +=1 

        for i in range(40,44): # will insert biceps and triceps exercises for third day 
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[2]])
            userExerciseId +=1 

        for i in range(23,27): # will insert legs exercises for fourth day 
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[3]])
            userExerciseId +=1 

        for i in range(44,47): # will insert shoulders exercises for fifth day 
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
        for i in range(12,18): # will insert Chest, Shoulders, Triceps exercises for first day 
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[0]])
            userExerciseId +=1 

        for i in range(18,23): # will insert back and biceps exercises for second day 
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[1]])
            userExerciseId +=1 

        for i in range(23,27): # will insert legs exercises for third day 
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[2]])
            userExerciseId +=1 

        for i in range(48,53): # will insert Chest, Shoulders, Triceps exercises for fourth day 
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[3]])
            userExerciseId +=1 

        for i in range(53,58): # will insert back and biceps exercises for fifth day 
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[4]])
            userExerciseId +=1 

        for i in range(58,63): # will insert legs exercises for sixth day 
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
        for i in range(12,18): # will insert Chest, Shoulders, Triceps exercises for first day 
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[0]])
            userExerciseId +=1 

        for i in range(18,23): # will insert back and biceps exercises for second day 
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[1]])
            userExerciseId +=1 

        for i in range(23,27): # will insert legs exercises for third day 
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[2]])
            userExerciseId +=1 

        for i in range(48,53): # will insert Chest, Shoulders, Triceps exercises for fourth day 
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[3]])
            userExerciseId +=1 

        for i in range(53,58): # will insert back and biceps exercises for fifth day 
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[4]])
            userExerciseId +=1 

        for i in range(58,63): # will insert legs exercises for sixth day 
            userExerciseData.append([userExerciseId, self.userObject.getUserId(), 3, 10, 0, 0])
            userExerciseId = userExerciseData[-1][0]
            userExerciseJunction.append([userExerciseId, i, listOfDays[5]])
            userExerciseId +=1 
        
        # will insert cardio exercises for seventh day 
        userExerciseData.append([userExerciseId, self.userObject.getUserId(),0 ,0, 0, 0])
        userExerciseId = userExerciseData[-1][0]
        userExerciseJunction.append([userExerciseId, 47, listOfDays[6]])
        return userExerciseData, userExerciseJunction
        

        
