

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
        for junct in current_user_junctionData:
            for exerciseInfo in current_user_exerciseData:
                userExerciseId = exerciseInfo[0]
                sets = exerciseInfo[2]
                reps = exerciseInfo[3]
                maxWeight = exerciseInfo[4]
                originalWeight = exerciseInfo[5]


                trainingDayId = junct[2]
                #exerciseId = current_user_junctionData[1]

                # iterate through allExerciseData and match the exerciseId with exerciseName and grab that
                for data in allExerciseData:
                    if data[0] == junct[1]:
                        exerciseName = data[2]


                self.currentExerciseData[exerciseName] = \
                    {
                        "userexerciseId": userExerciseId, 
                        "trainingDayId": trainingDayId,
                        "sets":sets,
                        "reps":reps,
                        "Max Weight": maxWeight,
                        "Original weight": originalWeight
                    }
    