import json
import pandas as pd

class InferenceEngine:
    '''
    The objective of this class is to automate the process of making inferences.
    This class can be called from:
        - Notebooks to make tests manually
        - From pipelines

    Operations:
    - Preprocessing to Json input
    - Apply std_scaler
    - Apply model and return results

    Parameters:
    request (JSON object): The JSON with the request data.
    
    '''

    def __init__(self, request):
        

        # Handling JSON input
        ## If come as a JSON convert to Dict and save
        ## If come as Dict just save
        try:
            json.dumps(request) 
            self.request = request
        except:
            self.request = json.loads(request)

        self.df = pd.json_normalize(self.request, max_level=0)

    def bmi_categorization(self, name = "BMI"):
        self.df['BMI'] = pd.cut(x=float(self.df['BMI']), bins=[0, 18.4
                                       , 24.9
                                       , 29.9
                                       , 34.9
                                       , 39.9,100], 
                   labels=['Underweight'
                          , 'Normal'
                          , 'Overweight'
                          , 'Obesity1'
                          , 'Obesity2'
                          , 'Obesity3']) 
        
        return self.df["BMI"]
        
        

"""Debug generating an generic small dataframe to check if the functions works properly"""
if __name__ == '__main__':

    rq1 = {"HighBP":"1",
           "HighChol":"0",
           "BMI":"30",
           "HeartDiseaseorAttack":"1",
           "PhysActivity":"1",
           "DiffWalk":"1",
           "Age":"1",
           "Education":"1",
           "Income":"1"
           }
    
    inference = InferenceEngine(request = rq1)
    
    print(inference.bmi_categorization())