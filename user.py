
"""User class holds login details of user """
class User():
    def __init__(self, current_user_data, current_user_training_days=None):
        self.current_user_data = current_user_data
        self.current_user_training_days = current_user_training_days
        self.user_data = {}
        
        if current_user_data != None and current_user_data != []: 
            self.user_data_to_dict(current_user_data, current_user_training_days)
            
        else:
            print("Info: No data associated with user.")


    def __str__(self):
        return f"User data: {self.user_data}"

  
    
    """Takes in user information such as userId, username, password, age, weight, height, gender, calorieGoal, and trainingDays. Turns it into the format of a dictionary"""
    def user_data_to_dict(self, current_user_data, current_user_training_days):
        userId = current_user_data[0]
        username = current_user_data[1]
        password = current_user_data[2]
        age = current_user_data[4]
        weight = current_user_data[5]
        height = current_user_data[6]
        gender = current_user_data[7]
        calorieGoal = current_user_data[8]
        trainingDays = current_user_training_days
        
        # create dictionary containning user data obtained from above.
        self.user_data = \
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

    # GET methods
    """return userId """
    def getUserId(self):
        return self.user_data["userId"]

    """return username"""
    def getUsername(self):
        return self.user_data["username"]

    """return password"""
    def getPassword(self):
        return self.user_data["password"]   
        

    """return age """
    def getAge(self):
        return self.user_data["age"]

    """return weight """
    def getWeight(self):
        return self.user_data["Weight"]

    """return height """
    def getHeight(self):
        return self.user_data["height"]

    """return gender """
    def getGender(self):
        return self.user_data["gender"]

    """return calorie goal """
    def getCalorieGoal(self):
        return self.user_data["Calorie Goal"]

    """return training days"""
    def getTrainingDays(self):
        return self.user_data["Training days"]


    # SET methods
    
    """Updates age of user"""
    def updateAge(self, newAge):
        try:
            self.user_data["age"] = newAge
        except KeyError:
            print(f"Unable to change age")
            return False
        return True

    """Updates weight of user"""
    def updateWeight(self, newWeight):
        try:
            self.user_data["weight"] = newWeight
        except KeyError:
            print(f"Unable to change weight")
            return False
        return True

    """Updates height of user"""
    def updateHeight(self, newHeight):
        try:
            self.user_data["height"] = newHeight
        except KeyError:
            print(f"Unable to change height")
            return False
        return True

    """Updates gender of user"""
    def updateGender(self, newGender):
        try:
            self.user_data["gender"] = newGender
        except KeyError:
            print(f"Unable to change gender")
            return False
        return True

    """Updates calorie goal of user"""
    def updateGoal(self, newGoal):
        try:
            self.user_data["Calorie Goal"] = newGoal
        except KeyError:
            print(f"Unable to change calorie goal")
            return False
        return True

    """Updates the days the user is exercising"""
    def updateDaysExercising(self, newDaysList):
        try:
            self.user_data["Training days"] = newDaysList
        except KeyError:
            print(f"Unable to change training days")
            return False
        return True

    



    