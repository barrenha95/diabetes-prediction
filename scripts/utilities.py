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
        count = pd.DataFrame(values.value_counts())

        count['Column'] = str(column) #Create a column with the column name that was counted
        count['Category'] = count.index #Create a column with the category name that was counted
        count = count.reset_index() 
        count = count.drop(columns=column) #Remove the old index (it were the category name)
        count = count.iloc[:, [1,2,0]] #Order the columns

        count = count.rename(columns = {'count':'Count'})

        return(count)
    
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

        
    def exploratory_table(self):
        
        final_table = None #Declaring final table that will contain the results of the exploratory analysis

        for i in self.dataframe.columns:
            temp_count = analysis.counting_categories(i) #Counting table for each category
            temp_sum = analysis.sum_by_column(i) #Sum the target column for each category

            temp_table = pd.merge(temp_count, temp_sum, how = 'inner', on=["Column","Category"])
            
            # Logict to bind the result of each column
            if final_table is None:
                final_table = copy(temp_table)

            if final_table is not None:
                final_table = pd.concat([final_table, temp_table], axis = 0)

        final_table['NonEvents'] = final_table.apply(lambda row: row.Count - row.Events, axis = 1) #Counting non events
    

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