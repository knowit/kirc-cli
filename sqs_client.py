import boto3
from consts import REGION, QUEUE_NAME, MESSAGE_GROUP_ID, COMMAND_PREFIX, COLORS, SIZES
from datetime import datetime, timezone
import uuid
import json

def send_queue_message(message: str):
    client = boto3.client('sqs', REGION)
    qurl = client.get_queue_url(QueueName=QUEUE_NAME)["QueueUrl"]
    response = client.send_message(QueueUrl=qurl, MessageBody=message, MessageGroupId=MESSAGE_GROUP_ID)
    return response


def main():
    print("Velkommen til verdens enkleste SQS-klient.")
    print("Klienten kan avsluttes når som helst ved å holde inne CTRL + C.")
    style = {}
    while True:
        print()
        print("Skriv inn meldingen du ønsker å sende til køen. For at meldingen faktisk skal bli sendt må du trykke på enter-tasten.")
        user_input = input()
        if user_input.startswith(COMMAND_PREFIX):
            command = user_input[len(COMMAND_PREFIX):]
            if command == 'clear':
                style = {}
            elif command in COLORS: # e.g. /red, /blue, /black
                style['color'] = command
            elif command in SIZES:
                style['font-size'] = SIZES[command]
            else:
                print(f'Unknown command {command}')
            continue
        id = str(uuid.uuid4())
        timestamp = datetime.now(timezone.utc).astimezone().isoformat()
        msg = {
            "message": user_input, 
            "id": id, 
            "timestamp": timestamp, 
            }
        if len(style) > 0:
            msg['style'] = ''.join([f'{key}: {value};' for key, value in style.items()])
        send_queue_message(json.dumps(msg))
        print("Melding sendt!")
        
if __name__ == '__main__':
    main()