from popup_gui import PopUpGUI
from tkinter import *
import tkinter as tk
import dashboard_controller 
from database_manager import DB
from user import User
from exerciseData import ExerciseData
import login_gui
import sign_up_GUI
import forgotPassword_GUI
import userInformation_gui



# this class controls the logic of loginGUI, signUpGUI, userInformationGUI, and forgetPassword. 
# It is the coordinator between these classes the its GUI classes. The methods in this class are createLoginGUI, 
# getSnapshotOfDatabase, setCurrentUserData
class LoginLogoutControllers():
    def __init__(self):
        #initializes and pulls data from DB
        self.databaseManagerObject = DB()
        

        # get this data from DB Manager
        self.databaseUserData = None # list: #list: id:int, username:str, password:str, securityquestionanswer:str
        self.databaseUserTrainingDays = None
        self.databaseUserExerciseData = None
        self.databaseUserJunctionData = None

        self.currentUserData = None 
        self.currentUserTrainingDays = []
        self.currentUserExerciseData = None
        self.currentUserJunctionData = None


        self.userObject = None
        self.sign_up_gui_object = None
        self.loginGUIObject = None

        #Load data from db
        self.getSnapshotOfDatabase()
        
        # insert all exercises into system
        self.databaseManagerObject.insertAllExercisesIntoDatabase()


        
       

    '''
    Intent: creates the GUI frame to log-in user.
    * Preconditions: LogIn GUI class exists.
    * Postconditions:
    * Post0. LogIn GUI class is created and called.
    '''
    def createLoginGUI(self):
        root = Tk()
        root.geometry("650x550")
        self.loginGUIObject = login_gui.LoginGUI(root)
        root.mainloop()
        
    

    '''
    Intent: Pulls all data from database and stores it in each specific list. Returns the lists.
    * Preconditions: self.databaseManagerObject is created and initializeded to class DB.
    * self.databaseUserData is created.
    * self.databaseUserTrainingDays is created.
    * self.databaseUserExerciseData is created.
    * self.databaseUserJunctionData is created.
    * Postconditions:
    * Post0. data is inserted into appropriate lists.
    * Post1. No data is pulled from database if connection to database fails.
    '''
    def getSnapshotOfDatabase(self):
        userData = self.databaseManagerObject.getDatabaseUserData()
        trainingDay = self.databaseManagerObject.getTrainingDays()
        userExerciseData = self.databaseManagerObject.getDatabaseUserExerciseData()
        userExerciseJunctionData = self.databaseManagerObject.getDatabaseUserExerciseJunctionData()

        self.databaseUserData = userData
        self.databaseUserTrainingDays = trainingDay
        self.databaseUserExerciseData = userExerciseData
        self.databaseUserJunctionData = userExerciseJunctionData
        return self.databaseUserData, self.databaseUserTrainingDays, self.databaseUserExerciseData, self.databaseUserJunctionData


    '''
    Intent: Compares username to all usernames in the database. Returns a list of the corresponding user data.
    * Returns an object of user data corresponding to the specific username. Returns None if nothing is found for username.
    * Preconditions: 
    * username is unique to the database.
    * self.databaseUserData is created.
    * If self.databaseUserData is None, return None.
    * Postconditions:
    * Post0. An object of the User data pertaining to specific user with username is set.
    '''
    def setCurrentUserData(self,username):
        if self.databaseUserData == None:
            return self.currentUserData

        for data in self.databaseUserData:
            if data[1] == username:
                self.currentUserData = data
                
        if self.currentUserData == None:
            self.currentUserData = (-1, '', '', '')
        return self.currentUserData


    '''
    Intent: Compares username to all usernames in the database. Returns a list of the corresponding user training day data.
    * Returns an object of user training day data corresponding to the specific username. Returns None if nothing is found for username.
    * Preconditions: 
    * username is unique to the database.
    * self.databaseUserData is created.
    * If self.databaseUserData is None, return None.
    * Postconditions:
    * Post0. An object of the User training day data pertaining to specific user with username is set.
    '''
    def setCurrentTrainingDays(self,username):
        if self.databaseUserTrainingDays == None:
            return self.currentUserTrainingDays

        userData = self.setCurrentUserData(username)
        userId = userData[0]

        for data in self.databaseUserTrainingDays:
            if data[2] == userId:
                self.currentUserTrainingDays.append(data)
        
        return self.currentUserTrainingDays
        


    '''
    Intent: compares userId to all userId's in the database to get exercise data. Returns a list of the corresponding exercise data.
    * Returns None if nothing is found for specific userId.
    * Preconditions: 
    * setCurrentUserData() has returned a user object. 
    * userId is taken from setCurrentUserData().
    * Postconditions:
    * Post0. An object of the exerrcise data pertaining to specific user with userId is set.
    '''
    def setCurrentUserExerciseData(self,username):
        if self.setCurrentUserData(username) == None:
            return self.currentUserExerciseData

        userData = self.setCurrentUserData(username)
        userId = userData[0]
        
        self.currentUserExerciseData = []
        for data in self.databaseUserExerciseData:
            if data[1] == userId:
                self.currentUserExerciseData.append(data)
        return self.currentUserExerciseData
        

  

    '''
    Inserts exercise data and junction data into the tables if user is new.
    Will insert exercises based on how many days user is training.
    For example, if user is training twice per week, it will enter userId, exerciseId, day, sets, and reps 5 times for 
    one day and 5 times for the other.
    
    '''
    def insertExercisesIfNewUser(self, listOfDays, username ,userId):
        if len(listOfDays) == 2:
            # have to insert exercise data and junction data
            for i in range(1,7):
                self.databaseManagerObject.insertDatabaseUserExerciseData(userId, 3, 10, 0, 0)
                self.getSnapshotOfDatabase()
                self.setCurrentUserExerciseData(username)

                userExerciseId = self.currentUserExerciseData[-1][0]
                self.databaseManagerObject.insertDatabaseUserExerciseJunction(userExerciseId, i, listOfDays[0])
                self.getSnapshotOfDatabase()
           
           


    '''
    Intent: compares userExerciseId in current user exercise data and junction data to build a list for current user. Returns a list of the corresponding exercise junction data.
    * Preconditions: 
    * setCurrentUserData() has returned a user object. 
    * Postconditions:
    * Post0. An object of the junction data pertaining to current user  is set.
    '''
    def setCurrentUserJunctionData(self):
        # iterate through User Exercise Data 
        # iterate through junction data and if userExerciseId match, append to self.currentJunctionData
        self.currentUserJunctionData = []
        for data in self.currentUserExerciseData:
            for junctData in self.databaseUserJunctionData:
                if data[0] == junctData[0]:
                    self.currentUserJunctionData.append(junctData)
        return self.currentUserJunctionData
        
            
          

    '''
    Intent: logic for signing user up. Displays appropriate message to user.
    * Preconditions: 
    * PopUpGUI exists
    * Postconditions:
    * Post0. shows user appropriate message based on sign-up status
    '''
    def signUpUserProcessing(self, username, password, secondPassword,securityQuestion, signUpGUI):
        if len(securityQuestion) == 0:
            popupGUI = PopUpGUI("Please answer security question.")
            popupGUI.createPopUp()

        elif self.checkUsernameTaken(username):
            popupGUI = PopUpGUI("Username is taken.")
            popupGUI.createPopUp()

        elif password != secondPassword:
            popupGUI = PopUpGUI("Passwords do not match.")
            popupGUI.createPopUp()

        elif self.validateUsernamePassword(username,password):
            signUpGUI.destroy()

            # collect user information and add it to database
            # then add user information to database
            self.createUserInformationGUI(username, password,securityQuestion)

        else:
            popupGUI = PopUpGUI("Username or password is incorrect")
            popupGUI.createPopUp()

    

    '''
    Intent: logic for processing user information.
    * Preconditions: 
    * userInformationGUI and databaseManager exists
    * Postconditions:
    * Post0. user is signed in and information is saved. userInformationGUI is closed and dashboard controller is created
    '''
    def userInformationProcessing(self, username, password, securityQuestion, age, weight, height, gender, calorieGoal, listOfDays, userInformationGUI):
        if len(listOfDays) < 2:
            popupGUI = PopUpGUI("Please choose atleast two days to exercise.")
            popupGUI.createPopUp()
            return False
        if gender == "?":
            popupGUI = PopUpGUI("Please provide a gender.")
            popupGUI.createPopUp()
            return False
        try: 
            age = int(age)
            weight = int(weight)
            height = int(height)
        except ValueError:
            popupGUI = PopUpGUI("Please provide an appropriate age, weight, or height.")
            popupGUI.createPopUp()
            return False

        self.databaseManagerObject.insertDatabaseUserData(username, password, securityQuestion, age, weight, height, gender, calorieGoal)
        self.getSnapshotOfDatabase()

        self.currentUserData = self.setCurrentUserData(username)
        userId = self.currentUserData[0]
        for day in listOfDays:
            self.databaseManagerObject.insertTrainingDays(day, userId)

        self.insertExercisesIfNewUser(listOfDays, username, userId)  # insert all of users exercises here
        self.getSnapshotOfDatabase()
        userInformationGUI.destroy()
        self.createDashboardController(username)

    
    


    '''
    Intent: creates and call the userInformatioGUI.
    * Preconditions: 
    * userInformationGUI exists
    * Postconditions:
    * Post0. userInformationGUI is created and displayed to the user.
    '''
    def createUserInformationGUI(self,username, password,securityQuestion):
        """This function creates the Dashboard GUI Object"""
        root = Tk()
        root.geometry("650x550")
        userInformationGUIObject = userInformation_gui.UserInformationGUI(root, username, password,securityQuestion)
        root.mainloop()


    '''
    Intent: Logs the User in by creating user object then creating dashboard controller. 
    * Preconditions: 
    * self.validateUsernamePassword(username,password) validates the username and password of user.
    * self.createPopupGui creates the popup GUI with text when called.
    * self.createDashboardController() creates the dashboard when called.
    * Postconditions:
    * Post0. creates user object if username and password validated by the method validateUsernamePassword(username,password)
    * Post1. does not create the user object. Shows popup GUI with error message.
    '''
    def loginUser(self, username, password, loginGUI):
        if not self.checkUsernameTaken(username):
            popupGUI = PopUpGUI("Username not found")
            popupGUI.createPopUp()
            
        elif self.validateUsernamePassword(username,password) and self.checkPasswordCorrect(username, password):
            loginGUI.destroy()
            
            self.createDashboardController(username)
        else:
            popupGUI = PopUpGUI("Username or password is incorrect")
            popupGUI.createPopUp()
            
           


    '''
    Intent: Creates Dashboard Controller and calls functions to create user and exercise objects and dashboard GUI.
    * Preconditions: 
    * dashboardController() exists
    * Postconditions:
    * Post0. dashboard controller class is created.
    '''
    def createDashboardController(self,username):
        self.userObject = self.createUserObject(username)
        self.exerciseUserObject = self.createUserExerciseObject(username)
        dashboardController = dashboard_controller.DashboardController(self.userObject, self.exerciseUserObject)
        dashboardController.createDashboardGUI()
    
    
    '''
    Intent: Creates User object by passing username parameter. Returns user object
    * Preconditions: 
    * Postconditions:
    * Post0. User object created and returned.
    * Post1. User object is returned as None.
    '''
    def createUserObject(self, username):
        self.currentUserData = self.setCurrentUserData(username)
        self.currentUserTrainingDays = self.setCurrentTrainingDays(username)
        self.userObject =  User(self.currentUserData, self.currentUserTrainingDays)
        print(self.userObject)
        return self.userObject


    '''
    Intent: Creates exercise object by passing username parameter. Returns exercise object
    * Preconditions: 
    * Postconditions:
    * Post0. exercise object created and returned.
    * Post1. exercise object is returned as None.
    '''
    def createUserExerciseObject(self, username):
        self.currentUserExerciseData = self.setCurrentUserExerciseData(username)
        self.currentUserJunctionData = self.setCurrentUserJunctionData()

        allExercises = self.databaseManagerObject.getDatabaseExerciseData()
        self.userExerciseObject =  ExerciseData(self.currentUserExerciseData, self.currentUserJunctionData, allExercises)
        print(self.userExerciseObject)
        return self.userExerciseObject







   
    '''
    Intent: Compares securityQuestionAnswer to data in the database pertaining to specific username. 
    * Returns True if securityQuestionAnswer matches with username's securityQuestionAnswer. Returns False otherwise.
    * Preconditions: if self.setCurrentUserData() == None, return True
    * This method would only be called when User forgets password.
    * Postconditions: 
    * Post0. securityQuestionAnswer is validated.
    * Post1. securityQuestionAnswer is not validated if self.setCurrentUserData(username) equal to None. 
    '''
    def verifySecurityQuestionAnswerUsername(self, securityQuestionAnswer, username):
        if self.setCurrentUserData(username) == None:
            return True 
        userData = self.setCurrentUserData(username)
        if userData[3] == securityQuestionAnswer:
            return True
        return False
        
   
   
    '''
    Intent: Checks if username if unique and password is validated. Returns True if both validated. Return False otherwise.
    * Preconditions: 
    * self.checkUsernameTaken(username) returns a boolean.
    * If username or passwordEntered equal None, return False.
    * Postconditions:
    * Post0. Username and password are both validated.
    * Post1. username or password are not validated if equal None.
    '''
    def validateUsernamePassword(self, username, passwordEntered):
        if username == None or passwordEntered == None:
            return False

        if len(passwordEntered) < 5:
            return False
        
        # check for special characters
        specialChars = "!#$^*"
        charCount = 0
        for char in specialChars:
            if char in passwordEntered:
                charCount+=1
        if charCount < 1:
            return False
        
        # check for uppercase letters
        if passwordEntered.islower():
            return False
        return True
       
      
    '''
    Intent: Checks if username already in database if new user. Returns True if username exists, False otherwise.
    * Preconditions: 
    * self.databaseUserData is created.
    * username entered != None
    * Postconditions:
    * Post0. username is compared to all other usernames in database.
    * Post1. username is not compared if equal to None.
    '''
    def checkUsernameTaken(self, username):
        for data in self.databaseUserData:
            if data[1] == username:
                    return True
        return False

    '''
    Intent: Checks if password entered matches with the password connected to the specific username 
    * Preconditions: 
    * self.databaseUserData is created.
    * password entered != None
    * Postconditions:
    * Post0. password is compared to password of username entered in database.
    * Post1. password is not compared if equal to None.
    '''
    def checkPasswordCorrect(self, username, password):
        if password == None:
            return False
        for data in self.databaseUserData:
            if data[1] == username:
                if data[2] == password:
                    return True
        return False
        

    
    
    '''
    Intent: creates a pop-up GUI with given error message."
    * Preconditions: 
    * popupGuiObject is an instance of PopUpGUI class.
    * message is a string
    * Postconditions:
    * Post0. pop up message is created
    '''
    def createPopupGUI(self, message):
        popUpGUIObj = PopUpGUI(message)
        popUpGUIObj.createPopUp()
        

   
    '''
    Intent: creates sign-up GUI
    * Preconditions: 
    * Tkinter is imported and working
    * signUpGUI exists
    * Postconditions:
    * Post0. signUpGUI is created
    '''
    def createSignUpGUI(self):
        root = Tk()
        root.geometry("650x600")
        self.sign_up_gui_object = sign_up_GUI.SignUpGUI(root)
        root.mainloop()
       
    
    
            


    '''
    Intent: verifies user information when using forgot Password feature.
    * Preconditions: 
    * PopUpGUI exists
    * Postconditions:
    * Post0. user's password is changed successfully.
    * Post1. user's password is not changed. Shows popup GUI with error message.
    '''
    def forgetPasswordProcessing(self, username, newPassword, newPassword2, security_question_answer, forgetPasswordGUI):
        """Call VerifySecurityQuestionAnswerUsername if its correct reset password for user in DB.
        then creates login gui.
        Else error message pop up GUI."""
        if not self.checkUsernameTaken(username):
            popupGUI = PopUpGUI("Username not found")
            popupGUI.createPopUp()
        elif newPassword != newPassword2:
            popupGUI = PopUpGUI("New passwords do not match.")
            popupGUI.createPopUp()

        # check security question answer
        elif not self.verifySecurityQuestionAnswerUsername(security_question_answer, username):
            popupGUI = PopUpGUI("Security Question is wrong")
            popupGUI.createPopUp()

        elif self.validateUsernamePassword(username,newPassword):
            forgetPasswordGUI.destroy()
            # update user information in database
            self.databaseManagerObject.updateDatabaseUserData(username, "password", newPassword)
            self.createLoginGUI()
        else:
            popupGUI = PopUpGUI("information entered is incorrect")
            popupGUI.createPopUp()

    
    '''
    Intent: creates forgot password GUI
    * Preconditions: 
    * Tkinter is imported and working
    * signUpGUI exists
    * Postconditions:
    * Post0. forgot password GUI is created
    '''
    def createForgottenPasswordGUI(self):
        root = Tk()
        root.geometry("650x600")
        forgotPasswordObject = forgotPassword_GUI.ForgotPasswordGUI(root)
        root.mainloop()





    '''
    Intent: 
    * Preconditions: 
    * username and finalUserObject exists
    * self.createUserObejct creates the initial user object
    * Postconditions:
    * Post0. 
    '''
    def logout_push_changes_to_database(self,username, finalUserObject):
        """Check what has to be changed in objects. """
        pass
