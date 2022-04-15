
"""User class holds login details of user """
class User():
    def __init__(self, current_user_data, current_user_training_days=None):
        self.current_user_data = current_user_data
        self.current_user_training_days = current_user_training_days
        self.user_data = {}
        
        if current_user_data != None and current_user_data != []: 
            self.user_data_to_dict(current_user_data, current_user_training_days)
        


    def __str__(self):
        return f"User data: {self.user_data}"

  
    
    """
    Intent: Takes in user information: userId, username, password, age, weight, 
    height, gender, calorieGoal, and trainingDays and converts into a dictionary.
    Preconditions: 
    1. current_user_data != None
    PostConditions:
    1. userData (dict) is created.
    """
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
        self.user_data["age"] = newAge
        
       

    """Updates weight of user"""
    def updateWeight(self, newWeight):
        self.user_data["weight"] = newWeight
       

    """Updates height of user"""
    def updateHeight(self, newHeight):
        self.user_data["height"] = newHeight
        

    """Updates gender of user"""
    def updateGender(self, newGender):
        self.user_data["gender"] = newGender
       

    """Updates calorie goal of user"""
    def updateGoal(self, newGoal):
         self.user_data["Calorie Goal"] = newGoal
       

    """Updates the days the user is exercising"""
    def updateDaysExercising(self, newDaysList):
        self.user_data["Training days"] = newDaysList
        

    



    