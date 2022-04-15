from database_manager import DB
import os


def set_env_variables():
    #export variables to environment
    os.environ["GENIUS_FINC_DB_NAME"]= "ZyzzfitDB"
    os.environ['SQLUser']='root'
    os.environ['SQLPassword']= 'Rhern_19'
    os.environ['SQLHost'] = "localhost"
    os.environ['DB_NAME'] ='ZyzzfitDB'

def test_database_manager():
    set_env_variables()
    databaseTest = DB()
    # get all user data
    #print(databaseTest.getDatabaseUserData())

    # get all exercises
    #print(databaseTest.getDatabaseExerciseData())

    # get user exercise info 
    #print(databaseTest.getDatabaseUserExerciseData())




    # insert user data
    #databaseTest.insertDatabaseUserData("ricardoh","passwrd","pizza", 21,170, 70, "male", "lose")
    #print(databaseTest.getDatabaseUserData())

    # insert training days for specific user
    #databaseTest.insertTrainingDays("Tuesday", 3)
    #print(databaseTest.getTrainingDays())

    # insert exercise data
    #print(databaseTest.insertAllExercisesIntoDatabase())
    #print(databaseTest.getDatabaseExerciseData())
    

    # insert user exercise info data into tables
    #databaseTest.insertDatabaseUserExerciseData(3, 3, 10, 0, 0) # (userId, sets, repetitions, maxWeight, originalWeight)
    #print(databaseTest.insertDatabaseUserExerciseJunction(3, 1, 1)) # (userId, exerciseId, trainingdayid)

    # get UserExercise data 
    #print(databaseTest.getDatabaseUserExerciseData()) # (userexerciseid, userId, sets, repetitions, maxWeight, originalWeight)
    

    # insert UserExerciseJunction with day and exercise
    #print(databaseTest.insertDatabaseUserExerciseJunction(1,1,1)) # (userId, exerciseId, trainingdayid)

    # get UserExerciseJunction with day and exercise
    #print(databaseTest.getDatabaseUserExerciseJucntionData()) # (userId, exerciseId, trainingdayid)

    databaseTest.deleteDatabase()



    

    
if __name__ == "__main__":
    test_database_manager()
    