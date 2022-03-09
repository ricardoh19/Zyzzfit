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
                "age":age,
                "Weight":weight, 
                "height": height,
                "Gender": gender,
                "Calorie Goal": calorieGoal,
                "Training days":trainingDays
            }
        







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
    

    