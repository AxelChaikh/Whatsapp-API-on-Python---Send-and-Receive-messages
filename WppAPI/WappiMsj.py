import requests
import json



def enviar(access_token, message_body):
    url = f"https://graph.facebook.com/v19.0/your_numberID/messages"

    headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
    }


    payload = {
        "messaging_product": "whatsapp",
        "to": "introduce_recipient",
        "type": "text",
        "text": {
        "body": message_body
        }
    }
    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Check the response
    if response.status_code == 200:
        print("Message sent successfully")
        print(response.json())
    else:
        print("Failed to send message")
        print(response.status_code, response.text)    


# Define the URL and the access token
phone_number_id = "your_numberID"
version = "v19.0"
access_token = "your_API_Key"

message_body =  input("Enter the message body: ")

enviar(access_token, message_body)
