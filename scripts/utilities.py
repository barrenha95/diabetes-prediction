# General-purpose utility scripts or helper functions.

import pandas as pd

class ExploratoryAnalysis:
    """
    This class was created to turn exploratory analysis easier
    
    Operations:
    - Count by category
    - Events by category (Positive answer in target column)
    - Non-events by category (Positive answer in target column)
    - Exposure (events/total)
    - Exposure ratio (category expose / dataframe exposure)
    - Category WOE (Weight of Evidence)
    - Category IV (Information Value)
    - Total IV (Information Value)
    - The percentage rep those operations

    """

    # Getting input from user
    def __init__(self, dataframe, target):

        # Splitting dataframe from target
        self.dataframe = dataframe.drop(str(target), axis='columns')
        self.target = dataframe[str(target)]


"""Debug generating an generic small dataframe to check if the functions works properly"""
if __name__ == '__main__':
    data = [['tom', 'athletic','f',18, 0],['erika', 'sedentary','f',22, 0],['robert', 'sedentary','m',56, 1]]
    df = pd.DataFrame(data, columns=['Name', 'Activity', 'Sex', 'Age', 'Diabetes'])
    analysis = ExploratoryAnalysis(dataframe = df, target = 'Diabetes')
    print(analysis.dataframe)
    print(analysis.target)



# Table
## Column | Category | Count | Events | Non-events

# Pipeline
## Create a list with the name of the columns
## Catch one column name
## Create a list of each category
## Make operations in each category
## Turn into table
## Bind to the output table