import logging
from main import set_env_variables
from user import User


    
def create_valid_user_object():
    """Returns user object that can be used when testing other objects or user oject"""
    #Correct User Object:
    user_id, username, password, sec, age, weight, height, gender, calorieGoal = 1, "ricardoh", "pw", "pizza", 21, 180, 70, "male", "lose"
    trainingDays = [[1, "Monday",1]]
    current_user_data = [user_id, username, password, sec, age, weight, height, gender, calorieGoal]
    

    myuser = User(current_user_data, trainingDays)
    print(myuser)
    return myuser

def changeAge():
    user_id, username, password, sec, age, weight, height, gender, calorieGoal = 1, "ricardoh", "pw", "pizza", 21, 180, 70, "male", "lose"
    trainingDays = [[1, "Monday",1]]
    current_user_data = [user_id, username, password, sec, age, weight, height, gender, calorieGoal]
    myuser = User(current_user_data, trainingDays)
    myuser.updateAge(30)
    print(myuser)
    return myuser




if __name__ == "__main__":
    # test_input()
    create_valid_user_object()
    #changeAge()