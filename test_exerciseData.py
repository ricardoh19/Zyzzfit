from exerciseData import ExerciseData



def create_valid_user_exercise_object():
    """Returns user exercise object that can be used when testing other objects or user oject"""
    #do tests on methods 

    current_user_trainingDays = [1, "Monday", 1]
    current_user_junctionData = [1, 1, 1]
    #note: user id of exercise must be the same as user_id in user data otherwise it wont be added.
    
    row1 = [1, 1, 3, 10, 0, 0] # userexerciseid, userId, sets, repetitions, maxWeight, originalWeight
    current_user_exerciseData = [row1]

    myuser = ExerciseData(current_user_exerciseData, current_user_junctionData)
    print(myuser)
    return myuser 


if __name__ == "__main__":
    create_valid_user_exercise_object()