import json
import requests


url = 'https://4ba1-34-90-169-145.ngrok.io/mail_prediction'

input_data_for_model = {
    
     'Message': "I've been searching for the right words to thank you for this breather. I promise i wont take your help for granted and will fulfil my promise"
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)
print(response.text)