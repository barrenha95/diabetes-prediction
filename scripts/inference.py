import json
import pandas as pd
import joblib
import category_encoders as ce

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

    def bmi_categorization(self, name = "BMI"):

        bmi_tmp = self.request[name]

        binInterval  = [0, 18.4, 24.9, 29.9, 34.9, 39.9, 100]
        binLabels= ['Underweight', 'Normal', 'Overweight', 'Obesity1', 'Obesity2', 'Obesity3']

        bmi_tmp = pd.cut(x=[float(bmi_tmp)], bins=binInterval, labels=binLabels) 

        tmp = self.request
        tmp[name] = bmi_tmp

        self.request_categorized = tmp
        
        return self.request_categorized
    
    def standardization(self):

        woe_encoder = joblib.load('./objects/woe_encoder.bin')
        sc = joblib.load('./objects/std_scaler.bin')
    
        tmp = pd.DataFrame.from_dict(self.request_categorized)

        #tmp2 = woe_encoder.transform(tmp)
        #self.X_train_std = self.sc.fit_transform(tmp)
        return self.request_categorized
        
        
        

"""Debug generating an generic small dataframe to check if the functions works properly"""
if __name__ == '__main__':

    rq1 = {           
           "Age":"9",
           "Income":"3",
           "PhysHlth":"15",
           "MentHlth":"18",
           "Education":"4",
           "GenHlth":"5",
           "BMI":"40",
           "HighBP":"1",
           "Smoker":"1",
           "Fruits":"0"
           }

    inference = InferenceEngine(request = rq1)
    inference.bmi_categorization()
    print(inference.standardization())