
"""Exercise class holds exercise details of user """
class ExerciseData():
    def __init__(self, current_user_exerciseData= None, current_user_junctionData=None, allExerciseData=None):
        self.current_user_exerciseData = current_user_exerciseData
        self.current_user_junctionData = current_user_junctionData
        self.exerciseData = allExerciseData
        self.currentExerciseData = {}

        if current_user_exerciseData != None and current_user_exerciseData != []: # does not add exercise data if there is not any associated with user
            self.user_exercise_data_to_dict(current_user_exerciseData, current_user_junctionData, allExerciseData)
        else:
            print("Info: No exercise data associated with user.")

    def __iter__(self):
        return iter(self.currentExerciseData)

    def keys(self):
        return self.currentExerciseData.keys()

   
        
    def __str__(self):
        return f"User Exercise Data: {self.current_user_exerciseData} \n {self.currentExerciseData}"


    """
    Intent: Takes in user exercise data: current_user_exerciseData, current_user_junctionData, and allExercises originating 
    from text file. and converts into a dictionary.
    Preconditions: 
    1. current_user_ExerciseData != None
    PostConditions:
    1. currentExerciseData (dict) is created.
    """
    def user_exercise_data_to_dict(self, current_user_exerciseData, current_user_junctionData, allExerciseData):
        # grab information from current_user_exerciseData list
        for i in range(len(current_user_exerciseData)):
            userExerciseId = current_user_exerciseData[i][0]
            sets = current_user_exerciseData[i][2]
            reps = current_user_exerciseData[i][3]
            maxWeight = current_user_exerciseData[i][4]
            originalWeight = current_user_exerciseData[i][5]
            trainingDay = current_user_junctionData[i][2]

            # iterate through allExerciseData and match the exerciseId with exerciseName
            for data in allExerciseData:
                if data[0] == current_user_junctionData[i][1]:
                    exerciseName = data[2]
            
            # create dictionary
            self.currentExerciseData[exerciseName] = \
                {
                    "userexerciseId": userExerciseId, 
                    "training Day": trainingDay,
                    "sets":sets,
                    "reps":reps,
                    "Max Weight": maxWeight,
                    "Original weight": originalWeight
                }


    # GET methods
    "returns userexerciseID based on exerciseName"
    def getUserExerciseId(self, exerciseName):
        return self.currentExerciseData[exerciseName]["userexerciseId"]
    
    "returns sets based on exerciseName"
    def getSets(self, exerciseName):
        return self.currentExerciseData[exerciseName]["sets"]

    "returns reps based on exerciseName"
    def getReps(self, exerciseName):
        return self.currentExerciseData[exerciseName]["reps"]
    
    "returns max weight based on exerciseName"
    def getMaxWeight(self, exerciseName):
        return self.currentExerciseData[exerciseName]["Max Weight"]

    "returns original weight based on exerciseName"
    def getOriginalWeight(self, exerciseName):
        return self.currentExerciseData[exerciseName]["Original weight"]
     
    "returns training day based on exerciseName"
    def getTrainingDay(self, exerciseName):
        return self.currentExerciseData[exerciseName]["training Day"]


    # SET methods

    """Updates sets of exercise data"""
    def updateSets(self, newSets):
        self.currentExerciseData["sets"] = newSets

    """Updates reps of exercise data"""
    def updateReps(self, newReps):
        self.currentExerciseData["reps"] = newReps
    
    """Updates original weight of exercise data"""
    def updateOriginalWeight(self, newOriginalWeight):
        self.currentExerciseData["Original weight"] = newOriginalWeight
    
    """Updates max weight of exercise data"""
    def updateMaxWeight(self, newMaxWeight):
        self.currentExerciseData["Max Weight"] = newMaxWeight


    
        