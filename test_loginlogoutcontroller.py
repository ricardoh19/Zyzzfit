from loginlogout_controller import LoginLogoutControllers
from test_user import test_user_object

def test_getSnapshotOfDatabase():
    loginlogoutController = LoginLogoutControllers()
    result = loginlogoutController.getSnapshotOfDatabase()
    print(result)

def test_setCurrentUserData():
    loginlogoutController = LoginLogoutControllers()
    loginlogoutController.getSnapshotOfDatabase()
    result = loginlogoutController.setCurrentUserData("ricardoh")
    print(result)

def test_setCurrentUserExerciseData():
    loginlogoutController = LoginLogoutControllers()
    loginlogoutController.getSnapshotOfDatabase()
    result = loginlogoutController.setCurrentUserExerciseData("ricardoh")
    print(result)


def test_setCurrentUserTrainingDays():
    loginlogoutController = LoginLogoutControllers()
    loginlogoutController.getSnapshotOfDatabase()
    result = loginlogoutController.setCurrentTrainingDays("ricardoh81")
    print(result)

def test_setCurrentUserUserExerciseJunctionData():
    loginlogoutController = LoginLogoutControllers()
    loginlogoutController.getSnapshotOfDatabase()
    result = loginlogoutController.setCurrentUserExerciseJunctionData("ricardoh")
    print(result)

def test_createUserObject():
    loginlogoutController = LoginLogoutControllers()
    loginlogoutController.getSnapshotOfDatabase()
    result = loginlogoutController.createUserObject("ricardoh")
    print(result)

def test_createUserExerciseObject():
    loginlogoutController = LoginLogoutControllers()
    loginlogoutController.getSnapshotOfDatabase()
    result = loginlogoutController.createUserExerciseObject("ricardoh")
    print(result)



def test_verifySecurityQuestionAnswerUsername():
    loginlogoutController = LoginLogoutControllers()
    result = loginlogoutController.verifySecurityQuestionAnswerUsername("sosa", "john")
    print(result)


def test_validateUsernamePassword():
    loginlogoutController = LoginLogoutControllers()
    # unique username and validated password
    result = loginlogoutController.validateUsernamePassword("johnO", "Passwrd1233#")
    print(result)

def test_checkUsernameTaken():
    loginlogoutController = LoginLogoutControllers()
    # unique username and validated password
    result = loginlogoutController.checkUsernameTaken("john")
    print(result)

def test_checkPasswordCorrect():
    loginlogoutController = LoginLogoutControllers()
    # unique username and validated password
    result = loginlogoutController.checkPasswordCorrect("ricardo", "Password1234!")
    print(result)

def test_loginUser():
    loginlogoutController = LoginLogoutControllers()
    # unique username and validated password
    LoginGUI = None
    loginlogoutController.getSnapshotOfDatabase()
    result = loginlogoutController.loginUser("ricardoh19", "Pass1!", LoginGUI)
    print(result)



if __name__ == "__main__":
    test_getSnapshotOfDatabase()
    #test_setCurrentUserData()
    #test_setCurrentUserExerciseData()
    #test_setCurrentUserTrainingDays()
    #test_setCurrentUserUserExerciseJunctionData()
    #test_createUserObject()


    #test_verifySecurityQuestionAnswerUsername()
    #test_validateUsernamePassword()
    #test_checkUsernameTaken()
    #test_loginUser()
    #test_checkPasswordCorrect()
    