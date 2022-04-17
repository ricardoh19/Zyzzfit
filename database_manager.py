from __future__ import print_function
import sys
import mysql.connector
from mysql.connector import errorcode
import os


# This class creates and maintains the Zyzzfit database.
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
        * Post0. Database ZyzzfitDB is created successfully if no exception is thrown.
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
            "  `trainingday` varchar(15) NOT NULL,"
            "  FOREIGN KEY (`userexerciseId`) REFERENCES `UserExerciseInfo` (`userexerciseId`), FOREIGN KEY (`exerciseId`) REFERENCES `Exercises` (`exerciseId`)"
            ") ENGINE=InnoDB")
            
        

            
        #connect to mysql server as root user
        cursor, cnx = self.connect_to_db()
       

        #check if database name already exists otherwise create it 
        try:
            cursor.execute(f"USE {self.DB_NAME}")
            
        except mysql.connector.Error as err:
            
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database(cursor)
                
                cnx.database =  self.DB_NAME
                
            else:
                print(err)
                sys.exit(1)

        #specify table description for the table 
        
        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
               
                cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    
                    table_exists = True
                else:
                    print(err.msg)
           

        
        cursor.close()
        cnx.close()



   # GET Methods

    '''
    Intent: Query User data from database. Return a list of all User data from database
    * Preconditions: 
    * cursor is connected to correct database (ZyzzfitDB)
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
    Intent: Query all exercise data from database,return a list of all exercise data from database. 
    * Preconditions: 
    * cursor is connected to correct database (ZyzzfitDB)
    * Exercises table already exists.
    * Postconditions:
    * Post0. Selects all data from the Exercises table if connection to database if successful.
    * Post1. Displays None if connection to database is not successful.
    '''
    def getDatabaseExerciseData(self):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = ("SELECT * FROM Exercises")
        cursor.execute(query)
        result = [list(i) for i in cursor]
        return result

    

    '''
    Intent: Query all user exercise data from database,return a list of all exercise data from database. 
    * Preconditions: 
    * cursor is connected to correct database (ZyzzfitDB)
    * UserExerciseInfo table already exists.
    * Postconditions:
    * Post0. Selects all user exercise data from the Exercises table if connection to database if successful.
    * Post1. Displays None if connection to database is not successful.
    '''
    def getDatabaseUserExerciseData(self):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = ("SELECT * FROM UserExerciseInfo")
        cursor.execute(query)
        result = [list(i) for i in cursor]
        return result

    '''
    Intent: Query all user exercise junction data from database,return a list of all user exercise junction data from database. 
    * Preconditions: 
    * cursor is connected to correct database (ZyzzfitDB)
    * UserExerciseJunctionData table already exists.
    * Postconditions:
    * Post0. Selects all user exercise junction data from the Exercises table if connection to database if successful.
    * Post1. Displays None if connection to database is not successful.
    '''
    def getDatabaseUserExerciseJunctionData(self):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = ("SELECT * FROM UserExerciseJunction")
        cursor.execute(query)
        result = [list(i) for i in cursor]
        return result

   
    '''
    Intent: Query all training day data from database,return a list of all training day data from database. 
    * Preconditions: 
    * cursor is connected to correct database (ZyzzfitDB)
    * TrainingDay table already exists.
    * Postconditions:
    * Post0. Selects all training day data from the Exercises table if connection to database if successful.
    * Post1. Displays None if connection to database is not successful.
    '''
    def getTrainingDays(self):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = ("SELECT * FROM TrainingDay")
        cursor.execute(query)
        result = [list(i) for i in cursor]
        return result






    # INSERTION METHODS


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

    '''
    Intent: Inserts training day data into TrainingDay table
    * Preconditions: 
    * cursor is connected to correct database
    * TrainingDay table already exists.
    * Postconditions:
    * PostO. trainingDay and userId is inserted into the database if connection to database is successful.
    * Post1. Data is not inserted into the database if connection to database fails.
    * Post2. Data is not inserted into the database if a parameter or all parameters are equal to None.
    '''
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
    * DB_Name is equal to 'ZyzzfitDB'.
    * Table that is being inserted to is "Exercises" and already exists.
    * cursor is connected to correct database (ZyzzfitDB)
    * Postconditions:
    * PostO. exerciseName, and bodyPart is inserted into the database if connection to database is successful.
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

    '''
    Intent: Inserts all exercise data from exercise text file.
    * Preconditions: 
    * DB_Name is equal to 'ZyzzfitDB'.
    * Table that is being inserted to is "Exercises" and already exists.
    * cursor is connected to correct database (ZyzzfitDB)
    * exercise.txt exists and is in current directory. 
    * Postconditions:
    * PostO. exerciseName, and bodyPart is inserted into the database if connection to database is successful.
    * Post1. Data is not inserted into the database if connection to database fails.
    * Post2. Data is not inserted into the database if a parameter or all parameters are equal to None.
    * Post3. Data is not inserted if text file does not contain data.
    '''
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
            
    '''
    Intent: Inserts data into userExerciseTable
    * Preconditions: 
    * DB_Name is equal to 'ZyzzfitDB'.
    * Table that is being inserted to is "UserExerciseInfo" and already exists.
    * cursor is connected to correct database (ZyzzfitDB)
    * Postconditions:
    * PostO. userId, sets, repetitions, maxWeight, originalWeight is inserted into the database if connection to database is successful.
    * Post1. Data is not inserted into the database if connection to database fails.
    * Post2. Data is not inserted into the database if a parameter or all parameters are equal to None.
    '''
    def insertDatabaseUserExerciseData(self, userId, sets, repetitions, maxWeight, originalWeight):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"INSERT INTO UserExerciseInfo"
                    "(userId, sets, repetitions, maxWeight, originalWeight) "
                    "VALUES (%s, %s, %s, %s, %s)")
        data = (userId, sets, repetitions, maxWeight, originalWeight)
        cursor.execute(query,data)
        cnx.commit()

    '''
    Intent: Inserts data into UserExerciseJunction
    * Preconditions: 
    * DB_Name is equal to 'ZyzzfitDB'.
    * Table that is being inserted to is "UserExerciseJunction" and already exists.
    * cursor is connected to correct database (ZyzzfitDB)
    * Postconditions:
    * PostO. userexerciseId, exerciseId, trainingday is inserted into the database if connection to database is successful.
    * Post1. Data is not inserted into the database if connection to database fails.
    * Post2. Data is not inserted into the database if a parameter or all parameters are equal to None.
    '''
    def insertDatabaseUserExerciseJunction(self, userexerciseId, exerciseId, trainingday):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"INSERT INTO UserExerciseJunction"
                    "(userexerciseId, exerciseId, trainingday) "
                    "VALUES (%s, %s, %s)")
        data = (userexerciseId, exerciseId, trainingday)
        cursor.execute(query,data)
        cnx.commit()




    #UPDATE Methods

    '''
    Intent: Updates data into User table
    * Preconditions: 
    * userId matches with userID that is currently logged in.
    * DB_Name is equal to 'ZyzzfitDB'.
    * Table that is being updated to is "User" and already exists.
    * cursor is connected to correct database (ZyzzfitDB)
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
    Intent: Updates user age in User table.
    * Preconditions: 
    * DB_Name is equal to 'ZyzzfitDB'.
    * Table that is being updated to is "User" and already exists.
    * cursor is connected to correct database (ZyzzfitDB)
    * Postconditions:
    * PostO. age is updated in the database if connection to database is successful.
    * Post1. age is not updated into the database if connection to database fails.
    * Post2. age is not updated into the database if a parameter or all parameters are equal to None.
    '''
    def updateUserAge(self, username, newAge):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"UPDATE User SET age = '{newAge}' WHERE username = '{username}'")
        cursor.execute(query)
        cnx.commit()

    '''
    Intent: Updates user weight in User table.
    * Preconditions: 
    * DB_Name is equal to 'ZyzzfitDB'.
    * Table that is being updated to is "User" and already exists.
    * cursor is connected to correct database (ZyzzfitDB)
    * Postconditions:
    * PostO. weight is updated in the database if connection to database is successful.
    * Post1. weight is not updated into the database if connection to database fails.
    * Post2. weight is not updated into the database if a parameter or all parameters are equal to None.
    '''
    def updateUserWeight(self, username, newWeight):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"UPDATE User SET weight = '{newWeight}' WHERE username = '{username}'")
        cursor.execute(query)
        cnx.commit()

    '''
    Intent: Updates user height in User table.
    * Preconditions: 
    * DB_Name is equal to 'ZyzzfitDB'.
    * Table that is being updated to is "User" and already exists.
    * cursor is connected to correct database (ZyzzfitDB)
    * Postconditions:
    * PostO. height is updated in the database if connection to database is successful.
    * Post1. height is not updated into the database if connection to database fails.
    * Post2. height is not updated into the database if a parameter or all parameters are equal to None.
    '''
    def updateUserHeight(self, username, newHeight):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"UPDATE User SET height = '{newHeight}' WHERE username = '{username}'")
        cursor.execute(query)
        cnx.commit()

    '''
    Intent: Updates user gender in User table.
    * Preconditions: 
    * DB_Name is equal to 'ZyzzfitDB'.
    * Table that is being updated to is "User" and already exists.
    * cursor is connected to correct database (ZyzzfitDB)
    * Postconditions:
    * PostO. gender is updated in the database if connection to database is successful.
    * Post1. gender is not updated into the database if connection to database fails.
    * Post2. gender is not updated into the database if a parameter or all parameters are equal to None.
    '''
    def updateUserGender(self, username, newGender):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"UPDATE User SET gender = '{newGender}' WHERE username = '{username}'")
        cursor.execute(query)
        cnx.commit()

    '''
    Intent: Updates user calorie goal in User table.
    * Preconditions: 
    * DB_Name is equal to 'ZyzzfitDB'.
    * Table that is being updated to is "User" and already exists.
    * cursor is connected to correct database (ZyzzfitDB)
    * Postconditions:
    * PostO. calorie goal is updated in the database if connection to database is successful.
    * Post1. calorie goal is not updated into the database if connection to database fails.
    * Post2. calorie goal is not updated into the database if a parameter or all parameters are equal to None.
    '''
    def updateUserCalorieGoal(self, username, newCalorieGoal):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"UPDATE User SET calorieGoal = '{newCalorieGoal}' WHERE username = '{username}'")
        cursor.execute(query)
        cnx.commit()

    
        
    '''
    Intent: Update sets of specific exercise in the UserExerciseInfo table.
    * Preconditions: 
    * DB_Name is equal to 'ZyzzfitDB'.
    * Table that is being updated to is "UserExerciseInfo" and already exists.
    * cursor is connected to correct database (ZyzzfitDB)
    * Postconditions:
    * PostO. sets is updated in the database if connection to database is successful.
    * Post1. sets is not updated into the database if connection to database fails.
    * Post2. sets is not updated into the database if a parameter or all parameters are equal to None.
    '''
    def updateUserExerciseSets(self, newSets, userExerciseId):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"UPDATE UserExerciseInfo SET sets = '{newSets}' WHERE userexerciseId = '{userExerciseId}'")
        cursor.execute(query)
        cnx.commit()

    '''
    Intent: Update repetitions of specific exercise in the UserExerciseInfo table.
    * Preconditions: 
    * DB_Name is equal to 'ZyzzfitDB'.
    * Table that is being updated to is "UserExerciseInfo" and already exists.
    * cursor is connected to correct database (ZyzzfitDB)
    * Postconditions:
    * PostO. repetitions is updated in the database if connection to database is successful.
    * Post1. repetitions is not updated into the database if connection to database fails.
    * Post2. repetitions is not updated into the database if a parameter or all parameters are equal to None.
    '''
    def updateUserExerciseReps(self, newReps, userExerciseId):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"UPDATE UserExerciseInfo SET repetitions = '{newReps}' WHERE userexerciseId = '{userExerciseId}'")
        cursor.execute(query)
        cnx.commit()

    '''
    Intent: Update maxweight of specific exercise in the UserExerciseInfo table.
    * Preconditions: 
    * DB_Name is equal to 'ZyzzfitDB'.
    * Table that is being updated to is "UserExerciseInfo" and already exists.
    * cursor is connected to correct database (ZyzzfitDB)
    * Postconditions:
    * PostO. maxweight is updated in the database if connection to database is successful.
    * Post1. maxweight is not updated into the database if connection to database fails.
    * Post2. maxweight is not updated into the database if a parameter or all parameters are equal to None.
    '''
    def updateUserExerciseMaxWeight(self, newMaxWeight, userExerciseId):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"UPDATE UserExerciseInfo SET maxweight = '{newMaxWeight}' WHERE userexerciseId = '{userExerciseId}'")
        cursor.execute(query)
        cnx.commit()

    '''
    Intent: Update originalweight of specific exercise in the UserExerciseInfo table.
    * Preconditions: 
    * DB_Name is equal to 'ZyzzfitDB'.
    * Table that is being updated to is "UserExerciseInfo" and already exists.
    * cursor is connected to correct database (ZyzzfitDB)
    * Postconditions:
    * PostO. originalweight is updated in the database if connection to database is successful.
    * Post1. originalweight is not updated into the database if connection to database fails.
    * Post2. originalweight is not updated into the database if a parameter or all parameters are equal to None.
    '''
    def updateUserExerciseOriginalWeight(self, newOriginalWeight, userExerciseId):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"UPDATE UserExerciseInfo SET originalweight = '{newOriginalWeight}' WHERE userexerciseId = '{userExerciseId}'")
        cursor.execute(query)
        cnx.commit()



    # delete methods

    '''
    Intent: Delete user exercise info from UserExerciseInfo table
    * Preconditions: 
    * DB_Name is equal to 'ZyzzfitDB'.
    * Table that is being updated to is "UserExerciseInfo" and already exists.
    * cursor is connected to correct database (ZyzzfitDB)
    * Postconditions:
    * PostO. user exercise info is deleted in the database if connection to database is successful.
    * Post1. user exercise info is not deleted into the database if connection to database fails.
    * Post2. user exercise info is not deleted into the database if a parameter or all parameters are equal to None.
    '''
    def deleteDatabaseExerciseData(self, userExerciseId):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"SET FOREIGN_KEY_CHECKS={0};")
        cursor.execute(query)
        query = (f"DELETE FROM UserExerciseInfo WHERE userexerciseId = '{userExerciseId}'")
        cursor.execute(query)
        cnx.commit()
    

    '''
    Intent: deletes a row from UserExerciseInfo table depending on the userId parameter
    * Preconditions: 
    * DB_Name is equal to 'ZyzzfitDB'.
    * Table that is being deleted from to is "UserExerciseInfo" and already exists.
    * cursor is connected to correct database (ZyzzfitDB)
    * Postconditions:
    * PostO. row from UserExerciseInfo is deleted in the database if connection to database is successful.
    * Post1. row from UserExerciseInfo is not deleted into the database if connection to database fails.
    * Post2. row from UserExerciseInfo is not deleted into the database if a parameter or all parameters are equal to None.
    '''
    def deleteUserIdDatabaseExerciseData(self, userId):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"SET FOREIGN_KEY_CHECKS={0};")
        cursor.execute(query)
        query = (f"DELETE FROM UserExerciseInfo WHERE userId = '{userId}'")
        cursor.execute(query)
        cnx.commit()

    '''
    Intent: deletes a row from UserExerciseJunction table depending on the userexerciseId parameter
    * Preconditions: 
    * DB_Name is equal to 'ZyzzfitDB'.
    * Table that is being deleted from to is "UserExerciseJunction" and already exists.
    * cursor is connected to correct database (ZyzzfitDB)
    * Postconditions:
    * PostO. row from UserExerciseJunction is deleted in the database if connection to database is successful.
    * Post1. row from UserExerciseJunction is not deleted into the database if connection to database fails.
    * Post2. row from UserExerciseJunction is not deleted into the database if a parameter or all parameters are equal to None.
    '''
    def deleteUserExerciseJunction(self, userExerciseId):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"SET FOREIGN_KEY_CHECKS={0};")
        cursor.execute(query)
        query = (f"DELETE FROM UserExerciseJunction WHERE userexerciseId = '{userExerciseId}'")
        cursor.execute(query)
        cnx.commit()

    '''
    Intent: gets data from UserExerciseJunction table. Returns a list of the result
    * Preconditions: 
    * DB_Name is equal to 'ZyzzfitDB'.
    * Table that is being deleted from to is "UserExerciseJunction" and already exists.
    * cursor is connected to correct database (ZyzzfitDB)
    * Postconditions:
    * PostO. data from UserExerciseJunction table is returned if connection to database is successful.
    * Post1. data from UserExerciseJunction table is not returned if connection to database fails.
    * Post2. data from UserExerciseJunction table is not returned if a parameter or all parameters are equal to None.
    '''
    def getUserExerciseJunctionInfo(self):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"SELECT * FROM UserExerciseJunction")
        cursor.execute(query)
        result = [list(i) for i in cursor]
        return result



    '''
    Intent: deletes user training days if they are changed
    * Preconditions: 
    * DB_Name is equal to 'ZyzzfitDB'.
    * Table that is being deleted from to is "TrainingDay" and already exists.
    * cursor is connected to correct database (ZyzzfitDB)
    * Postconditions:
    * PostO. user training days are deleted in the database if connection to database is successful.
    * Post1. user training days are not deleted into the database if connection to database fails.
    * Post2. user training days are not deleted into the database if a parameter or all parameters are equal to None.
    '''
    def deleteUserTrainingDays(self, userId):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"SET FOREIGN_KEY_CHECKS={0};")
        cursor.execute(query)
        query = (f"DELETE FROM TrainingDay WHERE userId = '{userId}'")
        cursor.execute(query)
        cnx.commit()