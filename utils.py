from datetime import datetime
import sys
def time_stamp_to_time(timestamp = 1545730073):
    dt_obj = datetime.fromtimestamp(timestamp) 
    print("date_time:",dt_obj)
    print("type of dt:",type(dt_obj))
    return time_stamp_to_time

def convert_to_type(variable_name= "variable", variable_type= int, variable_value = "i", crash = True):
    """Checks if the variable is of the wanted type if not tries to convert it. 
    Throws error message if it can't convert it. Crash if you want it to crash"""
    if type(variable_value) != variable_type:
        try:
            variable_value = variable_type(variable_value)
        except:
            print(f"Error: {variable_name} is not an integer: {variable_value}") 
            if crash:
                sys.exit(1) #input is wrong crash
        #print(type(variable_value))


