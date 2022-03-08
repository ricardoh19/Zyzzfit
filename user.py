from collections import UserDict
import logging 
import database_manager
from utils import convert_to_type

"""User class holds login details of user """
class User():

    def __init__(self, current_user_data= None,):
        #self.databaseManager = database_manager.DB()
        self.current_user_data = current_user_data
        

        #self.check_current_user_data() #checks current user data input is correct type
        #list: id:int, username:str, password:str, securityquestionanswer:str
        
        
        if current_user_data != None and current_user_data != [] : # don't try to add stock if there is not any associated with our user
            self.user_data_to_dict(current_user_data)
            
        
        else:
            print("Info: No data associated with user.")


    def __str__(self):
        return f"User Data: {self.current_user_data} \n"
    
    def user_data_to_dict(self, current_user_data):
        userId = current_user_data[0]
        username = current_user_data[1]
        password = current_user_data[2]
        age = current_user_data[3]
        weight = current_user_data[4]
        height = current_user_data[5]
        maxWeight = current_user_data[6]
        originalWeight = current_user_data[7]
        
        self.current_user_data = \
            {
                "userId": userId, 
                "username": username,
                "password":password,
                "age":age,
                "Weight":weight, 
                "height": height,
                "Max Weight": maxWeight,
                "Original weight": originalWeight
            }
        


    '''
    def check_current_user_data(self):
        id = self.current_user_data[0]
        username = self.current_user_data[1]
        password = self.current_user_data[2]
        age = self.current_user_data[3]
        weight = self.current_user_data[4]
        height = self.current_user_data[5]
        gender = self.current_user_data[6]
        calorieGoal = self.current_user_data[7]
        # Function in utils.py
        # Checks if the variable is of the wanted type if not tries to convert it. 
        #Throws error message if it can't convert it
        convert_to_type(variable_name= "User id", variable_type= int, variable_value = id)
        convert_to_type(variable_name= "Username", variable_type= str, variable_value = username)
        convert_to_type(variable_name= "password", variable_type= str, variable_value = password)
        convert_to_type(variable_name= "age", variable_type= int, variable_value = age)
        convert_to_type(variable_name= "weight", variable_type= int, variable_value = weight)
        convert_to_type(variable_name= "height", variable_type= int, variable_value = height)
        convert_to_type(variable_name= "gender", variable_type= str, variable_value = gender)
        convert_to_type(variable_name= "calorieGoal", variable_type= str, variable_value = calorieGoal)
    '''

    def user_exercise_to_dict(self, current_user_exerciseData):
        """Take in all users exercises and make them into the format of a dictionary"""
        for exerciseInfo in current_user_exerciseData:
            if exerciseInfo[1] == self.current_user_data[0]:
                sets = exerciseInfo[2]
                reps = exerciseInfo[3]
                maxWeight = exerciseInfo[4]
                originalWeight = exerciseInfo[5]

            self.current_user_exerciseData = \
                {
                    "userexerciseId": exerciseInfo[0], 
                    "userId": exerciseInfo[1],
                    "sets":sets,
                    "reps":reps,
                    "Max Weight": maxWeight,
                    "Original weight": originalWeight
                }
            

    def user_trainingDay_to_dict(self, current_user_trainingDays):
        """Take in all users exercises and make them into the format of a dictionary"""
        if current_user_trainingDays[2] == self.current_user_data[0]:
                day = current_user_trainingDays[1]
                userId = current_user_trainingDays[2]
                
        self.current_user_trainingDays = \
            {
                "training day Id": current_user_trainingDays[0], 
                "day": day,
                "userId":userId
            }


    def user_junction_to_dict(self, current_user_junctionData):
        if current_user_junctionData[2] == self.current_user_data[0]:
            userexerciseId = current_user_junctionData[0]
            exerciseId = current_user_junctionData[1]
            trainingdayId = current_user_junctionData[2]
        
        self.current_user_junctionData = \
            {
                "user exercise Id": userexerciseId, 
                "exercise Id": exerciseId,
                "trainingday Id":trainingdayId
            }
        print(self.current_user_junctionData)


    

       








    def delete_stock(self, stockname):
        """Function deletes specified stockname from current user stoccks"""
        try:
            del self.current_user_stocks[stockname]
        except KeyError:
            print(f"Unable to remove {stockname} from User because it does not exist as a key in the dictionary.")
            return False
        return True

    def append_stock(self, stocksymbol, userId, stockid = -1, stockOwnedDef = 0):
        """Appends a stock to the users collection of stocks. If not specified the stockid is -1
        to be changed when pushed to DB. Default stock owned is 0. """
        stock = {"stockid": stockid, "stockowned": stockOwnedDef}
        self.current_user_stocks[stocksymbol]= stock

        #stockOwned = stockOwnedDef
        #self.databaseManager.insertDatabaseStockData(stocksymbol,userId,stockOwned)

    def update_stock_owned(self, stocksymbol, stockowned = 0):
        """Changes the amount of a certain stock that the user owns."""
        try:
            # self.current_user_stocks[stocksymbol]
            self.current_user_stocks[stocksymbol]["stockowned"] = stockowned
        except KeyError:
            print(f"Unable to remove {stocksymbol} from User because it does not exist as a key in the dictionary.")
            return False
        return True


    def return_users_stock_symbols(self):
        """Returns a list of all user stocksymbols."""
        return self.current_user_stocks.keys()
    

    