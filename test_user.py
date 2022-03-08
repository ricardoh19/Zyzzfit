import logging
from main import set_env_variables
from user import User

def test_input():
    user_ids = [1, "1", "wrong type"]
    passwords =  ["password", 1, "1", ]
    security_question_answers = ["something", 1, "1", ]
    #stockids = [1, "1", "wrong type"]
    #stocksymbols = ["APPL", 1, "1", ] 
    #stockowned_all = [1, "1", "wrong type"]
    

    #test all possible combinations of input types
    for user_id in user_ids:
        for password in passwords:
            for security_question_answer in security_question_answers:
                for stockid in stockids:
                    for stocksymbol in stocksymbols:
                        for stockowned in stockowned_all:
                            current_user_data  = [user_id, password, security_question_answer]#current_user_data : userid, password, security question answer
                            current_user_stocks = [[stockid, stocksymbol,  user_id, stockowned]]#current_user_stocks : `stockId`, `stockName`  `userId``StockOwnedAmount` 
                            print(current_user_data)
                            print(current_user_stocks)
                            myuser = User(current_user_data, current_user_stocks)
                            # myuser = User(current_user_data, [])
                            print(myuser)
                            
def test_user_object(): 
    def test_delete_stock(myuser, stocksymbol):
        print(f"Test remove {stocksymbol}:")
        myuser.delete_stock(stocksymbol)
        print(myuser) 

    myuser = create_valid_user_object()
    print(myuser)
    #test delete stock:
    test_delete_stock(myuser, "APPL")
    test_delete_stock(myuser, "AAAA")

    #test add stock:
    print("Test: Add GOOG stock:")
    myuser.append_stock("GOOG", stockowned=100)
    print(myuser)

    #Test update stock owned:
    print("Test: Update GOOG stock:")
    myuser.update_stock_owned("GOOG", 222)
    print(myuser)

    print("Test: Update AAAA stock:")
    myuser.update_stock_owned("AAAA", 222)
    print(myuser)

    #get user stock symbols:
    print("Test: return all stock symbols")
    print(myuser.return_users_stock_symbols())

    #get amount of stock owned:
    print("Test: return Stock owned of GOOG")
    print(myuser.get_stockowned("GOOG"))
    print("Test: return Stock owned of AAAA")
    print(myuser.get_stockowned("AAAA"))

    
def create_valid_user_object():
    """Returns user object that can be used when testing other objects or user oject"""
    #do tests on methods 
    #Correct User Object:
    user_id, username, password, age, weight, height, gender, calorieGoal = 1, "ricardoh", "pw", 21, 180, 70, "male", "lose"
    current_user_data = [user_id, username, password, age, weight, height, gender, calorieGoal]
    current_user_trainingDays = [1, "Monday", 1]
    current_user_junctionData = [1, 1, 1]
    #note: user id of exercise must be the same as user_id in user data otherwise it wont be added.
    
    row1 = [1, 1, 3, 10, 0, 0] # userexerciseid, userId, sets, repetitions, maxWeight, originalWeight
    current_user_exerciseData = [row1]

    myuser = User(current_user_data)
    print(myuser)
    return myuser 


if __name__ == "__main__":
    # test_input()
    #test_user_object()
    create_valid_user_object()