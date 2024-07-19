# Scripts for data cleaning, transformation, and feature engineering.
## What we must implement:

### df['Diabetes_012'] = np.where(df['Diabetes_012'] == 2, 1, df['Diabetes_012'])

# df['BMI'] = pd.cut(x=df['BMI'], bins=[0, 18.4
#                                        , 24.9
#                                        , 29.9
#                                        , 34.9
#                                        , 39.9,100], 
#                    labels=['Underweight'
#                           , 'Normal'
#                           , 'Overweight'
#                           , 'Obesity1'
#                           , 'Obesity2'
#                           , 'Obesity3']) 

## Transform into WOE

# Create class
# Create the preprocessing steps
# Create the pickle serializing the steps
# Test it




## Reference of pickle: https://www.youtube.com/watch?v=HR1mDc-SF9c

class PreprocessingData:
    def __init__(self, dataframe, target, ignore = None)
        
        self.target = str(target) # Save the name of the target column

        try:
            dataframe[str(target)].astype(int)
        except:
            raise Exception("Target must contain only numbers")

        if len(dataframe[dataframe[str(target)]> 1])!= 0:
            raise Exception("Target must be between 0 and 1")
        
        if len(dataframe[dataframe[str(target)]< 0])!= 0:
            raise Exception("Target must be between 0 and 1")
        

        # Removing columns to ignore
        if ignore:
            self.ignore = list(ignore)
            self.dataframe = dataframe.drop(self.ignore, axis='columns') # List of columns to ignore
        else:
            self.ignore = list()
            self.dataframe = dataframe.drop(self.ignore, axis='columns') # List of columns to ignore

        # Splitting dataframe from target            
        self.target_df = copy(pd.DataFrame(self.dataframe)) # Target column
        
        self.dataframe = self.dataframe.drop(str(target), axis='columns') # Dataframe with the remaining columns

        # Getting columns name
        self.columns = list(self.dataframe.columns)

        self.total_observations = int(len(self.dataframe)) #count the number of lines in the dataframe
        self.total_event = dataframe[str(target)].sum()
        self.total_nonevent = self.total_observations - self.total_event 
