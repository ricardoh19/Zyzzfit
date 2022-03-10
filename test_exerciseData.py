from exerciseData import ExerciseData
from database_manager import DB
import os


def set_env_variables():
    #export variables to environment
    os.environ["GENIUS_FINC_DB_NAME"]= "ZyzzfitDB"
    os.environ['SQLUser']='root'
    os.environ['SQLPassword']= 'Rhern_19'
    os.environ['SQLHost'] = "localhost"
    os.environ['DB_NAME'] ='ZyzzfitDB'




def create_valid_user_exercise_object():
    """Returns user exercise object that can be used when testing other objects or user oject"""
    #do tests on methods 
    set_env_variables()
    databaseTest = DB()

    current_user_trainingDays = [1, "Monday", 1]
    current_user_junctionData = [[1, 1, "Monday"], [2, 2, "Monday"]] # userExerciseId, exerciseId, trainingDayId

    allExercises = databaseTest.getDatabaseExerciseData()
    #note: user id of exercise must be the same as user_id in user data otherwise it wont be added.
    
    row1 = [1, 1, 3, 10, 0, 0] # userexerciseid, userId, sets, repetitions, maxWeight, originalWeight
    row2 = [2, 1, 3, 10, 0, 0]
    current_user_exerciseData = [row1, row2]

    myuser = ExerciseData(current_user_exerciseData, current_user_junctionData, allExercises)
    print(myuser)
    return myuser 




if __name__ == "__main__":
    create_valid_user_exercise_object()