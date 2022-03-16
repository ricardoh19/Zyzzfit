from collections import UserDict
import logging 
import database_manager


"""User class holds login details of user """
class User():
    def __init__(self, current_user_data= None, current_user_training_days=None):
        self.current_user_data = current_user_data
        self.current_user_training_days = current_user_training_days
        
        if current_user_data != None and current_user_data != []: 
            self.user_data_to_dict(current_user_data, current_user_training_days)
            
        else:
            print("Info: No data associated with user.")


    def __str__(self):
        return f"User Data: {self.current_user_data} \n"
    
    def user_data_to_dict(self, current_user_data, current_user_training_days):
        userId = current_user_data[0]
        username = current_user_data[1]
        password = current_user_data[2]
        age = current_user_data[4]
        weight = current_user_data[5]
        height = current_user_data[6]
        gender = current_user_data[7]
        calorieGoal = current_user_data[8]
        trainingDays = [i[1] for i in current_user_training_days]
        
        self.current_user_data = \
            {
                "userId": userId, 
                "username": username,
                "password":password,
                "age": age,
                "Weight":weight, 
                "height": height,
                "gender": gender,
                "Calorie Goal": calorieGoal,
                "Training days":trainingDays
            }
        
    def updateAge(self, newAge):
        """Updates age of user"""
        try:
            self.current_user_data["age"] = newAge
        except KeyError:
            print(f"Unable to change age")
            return False
        return True

    def updateWeight(self, newWeight):
        """Updates weight of user"""
        try:
            self.current_user_data["weight"] = newWeight
        except KeyError:
            print(f"Unable to change weight")
            return False
        return True

    def updateHeight(self, newHeight):
        """Updates height of user"""
        try:
            self.current_user_data["height"] = newHeight
        except KeyError:
            print(f"Unable to change height")
            return False
        return True

    def updateGender(self, newGender):
        """Updates gender of user"""
        try:
            self.current_user_data["gender"] = newGender
        except KeyError:
            print(f"Unable to change gender")
            return False
        return True

    def updateGoal(self, newGoal):
        """Updates calorie goal of user"""
        try:
            self.current_user_data["Calorie Goal"] = newGoal
        except KeyError:
            print(f"Unable to change calorie goal")
            return False
        return True


    



    