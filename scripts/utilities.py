# General-purpose utility scripts or helper functions.

import pandas as pd

class ExploratoryAnalysis:
    """This class was created to turn exploratory analysis easier"""

    def __init__(self, dataframe, target):
        self.dataframe = dataframe
        self.target = target


"""Debug generating an generic small dataframe to check if the functions works properly"""
if __name__ == '__main__':
    data = [['tom', 'athletic','f',18, 0],['erika', 'sedentary','f',22, 0],['robert', 'sedentary','m',56, 1]]
    df = pd.DataFrame(data, columns=['Name', 'Activity', 'Sex', 'Age', 'Diabetes'])
    analysis = ExploratoryAnalysis(dataframe = df, target = 'Diabetes')
    print(analysis.dataframe)
    print(analysis.target)
