# General-purpose utility scripts or helper functions.

import pandas as pd
from copy import copy

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
    def __init__(self, dataframe, target, ignore):

        self.target = str(target) # Save the name of the target column
        
        # Splitting dataframe from target and removing columns to ignore
        self.dataframe = dataframe.drop(ignore, axis='columns') # List of columns to ignore
        self.target_df = copy(self.dataframe) # Target column
        
        self.dataframe = self.dataframe.drop(str(target), axis='columns') # Dataframe with the remaining columns

        # Getting columns name
        self.columns = list(self.dataframe.columns)

    def counting_categories(self, column):
        
        # Getting values of the expected column
        values = self.dataframe[str(column)]

        # Counting by each category
        count = values.value_counts()

        return(count)
    
    ### JOHN OF FUTURE: START DEBUGGING HERE
    def sum_by_column(self, column, sum_column = None):

        # Check if the user input a column
        if sum_column is None:
            sum_column = self.target
        
        # Create the dataframe with the desired column and target
        df_target_and_column = self.target_df[[str(column), str(sum_column)]] 
        
        df_target_and_column = df_target_and_column.groupby([str(column)],as_index = False).sum()
        df_target_and_column = df_target_and_column.rename(columns = {str(sum_column):'Events',
                                                                      str(column): 'Category'})

        df_target_and_column['Column'] = column
        df_target_and_column = df_target_and_column.iloc[:, [2,0,1]] #Order the columns

        return df_target_and_column
    ### JOHN OF FUTURE: START DEBUGGING HERE

        
    def exploratory_table(self):
        
        final_table = None #Declaring final table that will contain the resultes of the exploratory analysis

        for i in self.dataframe.columns:
            temp = pd.DataFrame(analysis.counting_categories(i)) #Counting table for each category
            temp['Column'] = i #Create a column with the column name that was counted
            temp['Category'] = temp.index #Create a column with the category name that was counted
            temp = temp.reset_index() 
            temp = temp.drop(columns=i) #Remove the old index (it were the category name)
            temp = temp.iloc[:, [1,2,0]] #Order the columns
            
            if final_table is None:
                final_table = copy(temp)

            if final_table is not None:
                final_table = pd.concat([final_table, temp], axis = 0)

        # for i in self.target.columns:
        #     temp = self.target[]

        return final_table

            





"""Debug generating an generic small dataframe to check if the functions works properly"""
if __name__ == '__main__':
    data = [['tom', 'athletic','f',18, 0]
           ,['erika', 'sedentary','f',22, 0]
           ,['robert', 'sedentary','m',56, 1]]
    
    df = pd.DataFrame(data, columns=['Name', 'Activity', 'Sex', 'Age', 'Diabetes'])
    analysis = ExploratoryAnalysis(dataframe = df, target = 'Diabetes', ignore=['Name'])

    final_table = analysis.exploratory_table()
    print(final_table)

    sum = analysis.sum_by_column('Sex')
    print(sum)


# Table
## Column | Category | Count | Events | Non-events