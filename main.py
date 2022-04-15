from tkinter import *
import os
from login_gui import mainLoginGUI


def set_env_variables():
    #export variables to environment
    os.environ["GENIUS_FINC_DB_NAME"]= "ZyzzfitDB"
    os.environ['SQLUser']='root'
    os.environ['SQLPassword']= 'Rhern_19'
    os.environ['SQLHost'] = "localhost"
    os.environ['DB_NAME'] ='ZyzzfitDB'

def main():
    set_env_variables()
    mainLoginGUI()

if __name__ == "__main__":
    main()