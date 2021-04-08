import boto3
from consts import REGION, QUEUE_NAME, MESSAGE_GROUP_ID
from datetime import datetime, timezone
import uuid
import json

def send_queue_message(message: str):
    client = boto3.client('sqs', REGION)
    qurl = client.get_queue_url(QueueName=QUEUE_NAME)["QueueUrl"]
    response = client.send_message(QueueUrl=qurl, MessageBody=message, MessageGroupId=MESSAGE_GROUP_ID)
    return response


#"key1: value1; key2: value2;" osv., f.eks. "font-size: 48px; background-color: pink;"

def main():
    print("Velkommen til verdens enkleste SQS-klient.")
    print("Klienten kan avsluttes når som helst ved å holde inne CTRL + C.")

    shrek = 'https://media.tenor.com/images/5187ae066f8332352ca554484f0bc41f/tenor.gif'

    color = input("Hvilken bakgrunnsfarge skal teksten ha? ")
    size = input("Hvilken størrelse skal teksten ha i pixler? ")

    nickname = input("Skriv inn dit kallenavn:")
    while True:
        print()
        print("Skriv inn meldingen du ønsker å sende til køen. For at meldingen faktisk skal bli sendt må du trykke på enter-tasten.")
        user_input = input()
        id = str(uuid.uuid4())
        timestamp = datetime.now(timezone.utc).astimezone().isoformat()
        msg = {
            "message": user_input, 
            "id": id, 
            "nickname": nickname,
            "timestamp": timestamp, 
            "style": f"min-height: 100px; font-size: {size}px; background-image: url({shrek}); background-size: 100px 100px;"
            }
        send_queue_message(json.dumps(msg))
        print("Melding sendt!")
        
if __name__ == '__main__':
    main()

#"style": f"font-size: {size}px; background-color: {color}; "