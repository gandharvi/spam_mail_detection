from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json


app = FastAPI()
 
class model_input(BaseModel):
     Message: str      
        
# loading the saved model
mail_model = pickle.load(open('mail_data.sav', 'rb'))

@app.post('/mail_prediction')
def mail_predd(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    message = input_dictionary['Message']       
    
    prediction = mail_model.predict(message)
    
    if (prediction[0] == 0):
        return 'This is spam mail'
    else:
        return 'This is a ham mail'
 