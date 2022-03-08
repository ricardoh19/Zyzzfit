from __future__ import print_function
import sys
import mysql.connector
from mysql.connector import errorcode

import os

#export variables to environment
os.environ["GENIUS_FINC_DB_NAME"]= "ZyzzfitDB"
os.environ['SQLUser']='root'
os.environ['SQLPassword']= 'Rhern_19'
os.environ['SQLHost'] = "localhost"
os.environ['DB_NAME'] ='ZyzzfitDB'



# This class creates and maintains the Genius Finance database with methods: 
# connect_to_db, createDatabaseManager,create_database, getDatabaseUserData, 
# getDatabaseStockData, insertDatabaseUserData, insertDatabaseStockData.
class DB():
    def __init__(self):
        #creates db if necessary
        #get db name from environment 
        try:
            self.DB_NAME = str(os.getenv('DB_NAME'))
        except Exception as e:
            print("Check that MySQL database name is provided in main.py .")
            print("Oops!", sys.exc_info()[0], "occurred.")
            print("Exception: ", e)
            sys.exit(1)
        
        self.createDatabaseManager() 
        

    '''
    Intent: Connects to SQL database, returns cursor and cnx (connection) to database.
    * Cursor interacts with the MySQL server and executes operations on the database.  
    * Preconditions: myuser, mypassword, myhost (and db if given) variables to have valid values for the root 
    * user of a given MySQL server or a given database.
    * Postconditions:
    * Post0. The connection to a database db is established (if db is not None) 
    * Post1. The connection to a MySQL server is established (if db is None)
    '''
    def connect_to_db(self, db = None):
        try:
            myuser = str(os.getenv('SQLUser'))
            mypassword = str(os.getenv('SQLPassword')) 
            myhost = str(os.getenv('SQLHost'))
        except Exception as e:
            print("Check that MySQL database user, password and host are provided in main.py .")
            print("Oops!", sys.exc_info()[0], "occurred.")
            print("Exception: ", e)
        if db:
            cnx = mysql.connector.connect(
            user=myuser, 
            password=mypassword,
            host=myhost,
            database=db)
            self.cursor = cnx.cursor()
            return self.cursor, cnx            
        else:
            cnx = mysql.connector.connect(
            user=myuser, 
            password=mypassword,
            host=myhost)
            self.cursor = cnx.cursor()
            return self.cursor, cnx
        
    '''
    Intent: Creates database and tables in that database.
    * Preconditions: 
    * Connection to database is established.
    * Tables User and Stock are already formatted and ready to be created.
    * Postconditions:
    * Post0. Database is created successfully if database does not exist already.
    * Post1. Tables are created successfully if tables do not exist already.
    * Post2. Failed creating database and error is thrown if database can not be created.
    * Post3. Failed creating tables and error is thrown if tables can not be created.
    '''
    def createDatabaseManager(self):
        '''
        Intent: Creates the database 
        * Preconditions: 
        * DB_name variable is created and set to correct database name.
        * Postconditions:
        * Post0. Database GeniusFinanceDB is created successfully if no exception is thrown.
        * post1. if exception (mysql.connector.Error) is thrown, database can not created
        '''
        def create_database(cursor):
            
            try:
                cursor.execute(f"CREATE DATABASE {self.DB_NAME} DEFAULT CHARACTER SET 'utf8'")
            except mysql.connector.Error as err:
                print(f"Failed creating database: {err}")
                sys.exit(1)


        TABLES = {}

        TABLES['User'] = (
            "CREATE TABLE `User` ("
            "  `userId` int(11) NOT NULL AUTO_INCREMENT,"
            "  `username` varchar(40)  NOT NULL,"
            "  `password` varchar(15) NOT NULL,"
            "  `securityQuestionAnswer` varchar(15) NOT NULL,"
            "  `age` int(11) NOT NULL,"
            "  `weight` int(11) NOT NULL,"
            "  `height` int(11) NOT NULL,"
            "  `gender` varchar(15) NOT NULL,"
            "  `calorieGoal` varchar(15) NOT NULL,"
            "  PRIMARY KEY (`userId`)"
            ") ENGINE=InnoDB")

        TABLES['TrainingDay'] = (
            "CREATE TABLE `TrainingDay` ("
            "  `trainingdayId` int(11) NOT NULL AUTO_INCREMENT,"
            "  `trainingday` varchar(11) NOT NULL,"
            "  `userId` int(11) NOT NULL,"
            "  PRIMARY KEY (`trainingdayId`), FOREIGN KEY (`userId`) REFERENCES `User` (`userId`) "
            ") ENGINE=InnoDB")

        TABLES['Exercises'] = (
            "CREATE TABLE `Exercises` ("
            "  `exerciseId` int(11) NOT NULL AUTO_INCREMENT,"
            "  `bodypart` varchar(15) NOT NULL,"
            "  `exercisename` varchar(30) NOT NULL," 
            "  PRIMARY KEY (`exerciseId`) "
            ") ENGINE=InnoDB")
            
        TABLES['UserExerciseInfo'] = (
            "CREATE TABLE `UserExerciseInfo` ("
            "  `userexerciseId` int(11) NOT NULL AUTO_INCREMENT,"
            "  `userId` int(11) NOT NULL,"
            "  `sets` int(11) NOT NULL,"
            "  `repetitions` int(11) NOT NULL,"
            "  `maxweight` int(11) NOT NULL,"
            "  `originalweight` int(11) NOT NULL,"
            "  PRIMARY KEY (`userexerciseId`), FOREIGN KEY (`userId`) REFERENCES `User` (`userId`)"
            ") ENGINE=InnoDB")


        TABLES['UserExerciseJunction'] = (
            "CREATE TABLE `UserExerciseJunction` ("
            "  `userexerciseId` int(11) NOT NULL,"
            "  `exerciseId` int(11) NOT NULL,"
            "  `trainingdayId` int(11) NOT NULL,"
            "  FOREIGN KEY (`userexerciseId`) REFERENCES `UserExerciseInfo` (`userexerciseId`), FOREIGN KEY (`exerciseId`) REFERENCES `Exercises` (`exerciseId`), FOREIGN KEY (`trainingdayId`) REFERENCES `TrainingDay` (`trainingdayId`)"
            ") ENGINE=InnoDB")
            
        

            
        #connect to mysql server as root user
        cursor, cnx = self.connect_to_db()
       

        #check if database name already exists otherwise create it 
        try:
            cursor.execute(f"USE {self.DB_NAME}")
            
        except mysql.connector.Error as err:
            print(f"Database { self.DB_NAME} does not exists.")
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database(cursor)
                print(f"Database { self.DB_NAME} created successfully.")
                cnx.database =  self.DB_NAME
                
            else:
                print(err)
                sys.exit(1)

        #specify table description for the table 
        
        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                
                else:
                    print(err.msg)
            else:
                print("OK")

        
        cursor.close()
        cnx.close()



   # Get data

    '''
    Intent: Query User data from database. Return a list of all User data from database
    * Preconditions: 
    * cursor is connected to correct database (GeniusFinanceDB)
    * User table already exists.
    * Postconditions:
     * Post0. Selects all data from the User table if connection to database if successful.
    * Post1. Displays None if connection to database is not successful.
    '''
    def getDatabaseUserData(self):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = ("SELECT * FROM User")
        cursor.execute(query)
        result = [list(i) for i in cursor]
        return result
        

    '''
    Intent: Query all Stock data from database,return a list of all Stock data from database. 
    * Preconditions: 
    * cursor is connected to correct database (GeniusFinanceDB)
    * Stock table already exists.
    * Postconditions:
    * Post0. Selects all data from the Stock table if connection to database if successful.
    * Post1. Displays None if connection to database is not successful.
    '''
    def getDatabaseExerciseData(self):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = ("SELECT * FROM Exercises")
        cursor.execute(query)
        result = [list(i) for i in cursor]
        return result

    '''
    Intent:
    * Preconditions: 
    * cursor is connected to correct database (GeniusFinanceDB)
    * Stock table already exists.
    * Postconditions:
    * Post0. Selects all data from the Stock table if connection to database if successful.
    * Post1. Displays None if connection to database is not successful.
    '''
    def getExerciseBasedOnBodyPart(self, bodyPart):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = ("SELECT * FROM Exercises")
        cursor.execute(query)
        result = [list(i) for i in cursor]
        return result


    def getDatabaseUserExerciseData(self):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = ("SELECT * FROM UserExerciseInfo")
        cursor.execute(query)
        result = [list(i) for i in cursor]
        return result

    def getDatabaseUserExerciseJunctionData(self):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = ("SELECT * FROM UserExerciseJunction")
        cursor.execute(query)
        result = [list(i) for i in cursor]
        return result

   

    def getTrainingDays(self):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = ("SELECT * FROM TrainingDay")
        cursor.execute(query)
        result = [list(i) for i in cursor]
        return result









    # insertion


    '''
    Intent: Inserts data into User table
    * Preconditions: 
    * cursor is connected to correct database
    * User table already exists.
    * username, password, and securityQuestionAnswer are validated.
    * username, password, and securityQuestionAnswer are strings.
    * Postconditions:
    * PostO. username, password, securityQuestionAnswer is inserted into the database if connection to database is successful.
    * Post1. Data is not inserted into the database if connection to database fails.
    * Post2. Data is not inserted into the database if a parameter or all parameters are equal to None.
    '''
    def insertDatabaseUserData(self, username, password, securityQuestionAnswer, age, weight, height, gender, calorieGoal):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = ("INSERT INTO User "
                    "(username,password,securityQuestionAnswer,age,weight,height,gender,calorieGoal) "
                    "VALUES (%s, %s, %s,%s,%s,%s,%s,%s)")
        data = (username, password,securityQuestionAnswer,age, weight, height, gender, calorieGoal)
        cursor.execute(query, data)
        cnx.commit()

    def insertTrainingDays(self, trainingDay, userId):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"INSERT INTO TrainingDay"
                    "(trainingday, userId) "
                    "VALUES (%s, %s)")
        data = (trainingDay, userId)
        cursor.execute(query,data)
        cnx.commit()

    '''
    Intent: Inserts data into Exercise table
    * Preconditions: 
    * userId matches with userID that is currently logged in.
    * DB_Name is equal to 'ZyzzfitDB'.
    * Table that is being inserted to is "Stock" and already exists.
    * cursor is connected to correct database (GeniusFinanceDB)
    * Postconditions:
    * PostO. stockName and stockOwnedAmount is inserted into the database if connection to database is successful.
    * Post1. Data is not inserted into the database if connection to database fails.
    * Post2. Data is not inserted into the database if a parameter or all parameters are equal to None.
    '''
    def insertDatabaseExerciseData(self, exerciseName, bodyPart):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"INSERT INTO Exercises"
                    "(exercisename, bodypart) "
                    "VALUES (%s, %s)")
        data = (exerciseName, bodyPart)
        cursor.execute(query,data)
        cnx.commit()


    def insertAllExercisesIntoDatabase(self):
        with open('exercises.txt') as f:
            lines = f.readlines()
            for line in lines:
                new_list = line.split(",")

                cursor, cnx = self.connect_to_db(db=self.DB_NAME)
                query = (f"INSERT INTO Exercises"
                            "(bodypart,exercisename) "
                            "VALUES (%s, %s)")
                data = (new_list[0], new_list[1].replace("\n", ""))
                cursor.execute(query,data)
                cnx.commit()
            

    def insertDatabaseUserExerciseData(self, userId, sets, repetitions, maxWeight, originalWeight):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"INSERT INTO UserExerciseInfo"
                    "(userId, sets, repetitions, maxWeight, originalWeight) "
                    "VALUES (%s, %s, %s, %s, %s)")
        data = (userId, sets, repetitions, maxWeight, originalWeight)
        cursor.execute(query,data)
        cnx.commit()

    
    def insertDatabaseUserExerciseJunction(self, userexerciseId, exerciseId, trainingdayId):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"INSERT INTO UserExerciseJunction"
                    "(userexerciseId, exerciseId, trainingdayId) "
                    "VALUES (%s, %s, %s)")
        data = (userexerciseId, exerciseId, trainingdayId)
        cursor.execute(query,data)
        cnx.commit()






    def deleteDatabase(self):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"DROP DATABASE {self.DB_NAME}")
        cursor.execute(query)
        cnx.commit()






















    '''
    Intent: Deletes data from Exercise table
    * Preconditions: 
    * DB_Name is equal to 'GeniusFinanceDB'.
    * Table that is being deleted from is "Stock" and already exists.
    * cursor is connected to correct database (GeniusFinanceDB)
    * Postconditions:
    * PostO. stockName and stockOwnedAmount is inserted into the database if connection to database is successful.
    * Post1. Data is not deleted from the database if connection to database fails.
    * Post2. Data is not deleted from the database if a parameter or all parameters are equal to None.
    '''
    def deleteDatabaseStockData(self, stockName):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"DELETE FROM Stock WHERE stockName = '{stockName}'")
        cursor.execute(query)
        cnx.commit()




    '''
    Intent: Updates data into User table
    * Preconditions: 
    * userId matches with userID that is currently logged in.
    * DB_Name is equal to 'GeniusFinanceDB'.
    * Table that is being updated to is "User" and already exists.
    * cursor is connected to correct database (GeniusFinanceDB)
    * usernameOrPassword is a string that is either equal to "username" or "password"
    * newValue is a validated username or password
    * username or password are the only valued from User table that can be changed.

    * Postconditions:
    * PostO. username is updated in the database if connection to database is successful.
    * Post1. password is updated in the database if connection to database is successful.
    * Post2. Data is not updated in the database if connection to database fails.
    * Post3. Data is not updated in the database if username or password input type is not a string
    * Post4. Data is not updated in the database if username or password is equal to None.
    '''
    def updateDatabaseUserData(self, username, usernameOrPassword, newValue):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        if usernameOrPassword == "username":
            query = (f"UPDATE User SET username = '{newValue}' WHERE username = '{username}'")
        elif usernameOrPassword == "password":
            query = (f"UPDATE User SET password = '{newValue}' WHERE username = '{username}'")
        cursor.execute(query)
        cnx.commit()

    '''
    can update sets, reps, max weight, original weight
    '''
    def updateUserExerciseData(self):
        pass

    '''
    Can update exerciseId if user hcanges the exercise
    '''
    def updateUserJunctionData(self):
        pass
    
    '''
    Intent: Updates data into Stock table
    * Preconditions: 
    * userId matches with userID that is currently logged in.
    * DB_Name is equal to 'GeniusFinanceDB'.
    * Table that is being updated to is "Stock" and already exists.
    * cursor is connected to correct database (GeniusFinanceDB)
    * stockOwnedAmount is an integer and the only value from Stock table that can being changed.
    * Postconditions:
    * PostO. stockOwnedAmount is updated in the database if connection to database is successful.
    * Post1. Data is not updated in the database if connection to database fails.
    * post2. Data is not updated in the database if stockOwnedAmount input type is not an integer
    '''
    def updateDatabaseStockData(self, username,stockOwnedAmount):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"UPDATE Stock SET stockOwnedAmount = {stockOwnedAmount} WHERE username = '{username}'")
        cursor.execute(query)
        cnx.commit()
        
    