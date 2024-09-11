import json

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
        self.request = json.dumps(request)
        print(self.request)


"""Debug generating an generic small dataframe to check if the functions works properly"""
if __name__ == '__main__':

    rq1 = {"HighBP":"1", "HighChol":"0", "BMI":"1"}

    analysis = InferenceEngine(request = rq1)