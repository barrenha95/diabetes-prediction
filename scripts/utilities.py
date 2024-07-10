# General-purpose utility scripts or helper functions.

import numpy as np
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

    Parameters:
    dataframe (pd.dataframe): The dataframe you want to do the exploratory analysis.
    target (str): The name of the target column.
    ignore (list of str): The list of name of columns that you want to drop from the analysis.

    """

    # Getting input from user
    def __init__(self, dataframe, target, ignore = None):

        self.target = str(target) # Save the name of the target column
        
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
        df_target_and_column = df_target_and_column.rename(columns = {str(sum_column):'Event',
                                                                      str(column): 'Category'})

        df_target_and_column['Column'] = column
        df_target_and_column = df_target_and_column.iloc[:, [2,0,1]] #Order the columns

        return df_target_and_column

        
    def exploratory_table(self, total_column = 'Count', good_column = 'Event'):
        
        final_table = None #Declaring final table that will contain the results of the exploratory analysis

        for i in self.dataframe.columns:
            temp_count = analysis.counting_categories(i) #Counting table for each category
            temp_sum = analysis.sum_by_column(i) #Sum the target column for each category

            temp_table = pd.merge(temp_count, temp_sum, how = 'inner', on=["Column","Category"])

            # Calculating good and bad ratio
            temp_table['GoodRatio'] = temp_table.apply(lambda row: row[good_column] / row[total_column], axis = 1)
            temp_table['BadRatio']  = temp_table.apply(lambda row: (row[total_column] - row[good_column]) / row[total_column], axis = 1)
            
            # Replacing 0 to not have error when the ratios are 0
            temp_table.loc[temp_table["GoodRatio"] == 0, "GoodRatio"] = 0.001
            temp_table.loc[temp_table["BadRatio"] == 0, "BadRatio"] = 0.001
            
            temp_table['Woe'] = temp_table.apply(lambda row: np.log(row['GoodRatio']/row['BadRatio']), axis = 1)
            temp_table['Iv'] = temp_table.apply(lambda row: (row['GoodRatio']-row['BadRatio'])*row['Woe'], axis = 1)

            temp_table['ColumnIv'] = temp_table['Iv'].sum() # Total IV of the column

            # Logict to bind the result of each column
            if final_table is None:
                final_table = copy(temp_table)

            if final_table is not None:
                final_table = pd.concat([final_table, temp_table], axis = 0)

        final_table['NonEvent'] = final_table.apply(lambda row: row.Count - row.Event, axis = 1) #Counting non events
        final_table['Exposure'] = final_table.apply(lambda row: row.Event / row.Count, axis = 1)  #Exposure = Events / Total

        total_observations = final_table['Count'].sum()
        total_event = final_table['Event'].sum()
        
        final_table['DfExposure'] = total_event/total_observations  #Exposure of the dataframe = events / observations
        final_table['ExposureRatio'] = final_table.apply(lambda row: row.Exposure / row.DfExposure, axis = 1)  #ExposureRatio = Exposure / DfExposure

        final_table = final_table.iloc[:, [0,1,2,3,9,10,11,12,4,5,6,7,8]] #Order the columns
    
        return final_table

            

"""Debug generating an generic small dataframe to check if the functions works properly"""
if __name__ == '__main__':
    data = [['tom', 'athletic','f',18, 0]
           ,['erika', 'sedentary','f',22, 0]
           ,['robert', 'sedentary','m',56, 1]]
    
    df = pd.DataFrame(data, columns=['Name', 'Activity', 'Sex', 'Age', 'Diabetes'])

    # Testing basic combination of the function
    analysis = ExploratoryAnalysis(dataframe = df, target = 'Diabetes', ignore=['Name'])
    final_table = analysis.exploratory_table()
    print("Basic combination: \n")
    print(final_table)

    # Ignoring two columns
    analysis = ExploratoryAnalysis(dataframe = df, target = 'Diabetes', ignore=['Name', 'Activity'])
    final_table = analysis.exploratory_table()
    print("Ignoring two columns: \n")
    print(final_table)

    # Using default value of "ignore" argument
    analysis = ExploratoryAnalysis(dataframe = df, target = 'Diabetes')
    final_table = analysis.exploratory_table()
    print("Default argument of ignore: \n")
    print(final_table)