

class ExerciseData():
    def __init__(self, current_user_exerciseData= None, current_user_junctionData=None, allExerciseData=None):
        self.current_user_exerciseData = current_user_exerciseData
        self.current_user_junctionData = current_user_junctionData
        self.exerciseData = allExerciseData
        self.currentExerciseData = {}

        if current_user_exerciseData != None and current_user_exerciseData != [] : # don't try to add stock if there is not any associated with our user
            self.user_exercise_data_to_dict(current_user_exerciseData, current_user_junctionData, allExerciseData)
        else:
            print("Info: No exercise data associated with user.")


    def __str__(self):
        return f"User Exercise Data: {self.current_user_exerciseData} \n {self.currentExerciseData}"


    def user_exercise_data_to_dict(self, current_user_exerciseData, current_user_junctionData, allExerciseData):
        """Take in all users exercises and make them into the format of a dictionary"""
        # make it into list of lists because user will have multiple exercises
        
        for i in range(len(current_user_exerciseData)):
            userExerciseId = current_user_exerciseData[i][0]
            sets = current_user_exerciseData[i][2]
            reps = current_user_exerciseData[i][3]
            maxWeight = current_user_exerciseData[i][4]
            originalWeight = current_user_exerciseData[i][5]
            trainingDay = current_user_junctionData[i][2]

            # iterate through allExerciseData and match the exerciseId with exerciseName and grab that
            for data in allExerciseData:
                if data[0] == current_user_junctionData[i][1]:
                    exerciseName = data[2]
            

            self.currentExerciseData[exerciseName] = \
                {
                    "userexerciseId": userExerciseId, 
                    "training Day": trainingDay,
                    "sets":sets,
                    "reps":reps,
                    "Max Weight": maxWeight,
                    "Original weight": originalWeight
                }

        