import json
import uuid
from datetime import datetime, timezone
from consts import REGION, QUEUE_NAME, MESSAGE_GROUP_ID
import boto3


def send_queue_message(message: str):
    client = boto3.client('sqs', REGION)
    qurl = client.get_queue_url(QueueName=QUEUE_NAME)["QueueUrl"]
    response = client.send_message(
        QueueUrl=qurl, MessageBody=message, MessageGroupId=MESSAGE_GROUP_ID)
    return response


def main():
    print("Velkommen til verdens enkleste SQS-klient.")
    print("Klienten kan avsluttes når som helst ved å holde inne CTRL + C.")
    style = []
    nickname = "Guest"
    while True:
        print("Skriv inn meldingen du ønsker å sende til køen. For å legge til styling må du begynne meldingen med /style, og stylingen må være på formatet 'key1: value1;'. For at meldingen faktisk skal bli sendt må du trykke på enter-tasten.")
        user_input = input()
        message = ""

        # Set styling
        if user_input.startswith("/style"):
            style_values = user_input.split("/style")[1].split(";")
            for style_value in style_values:
                if len(style_value.split(": ")) == 2:
                    style.append(style_value + ";")

        # Remove styling
        elif user_input.startswith("/clear"):
            style = []
        # Set nickname
        elif user_input.startswith("/nickname"):
            nickname = user_input.split("/nickname")[1]
        # Write message
        else:
            message = user_input

        id = str(uuid.uuid4())
        timestamp = datetime.now(timezone.utc).astimezone().isoformat()
        # Send message without styling
        if not style:
            msg = {
                "message": message,
                "id": id,
                "timestamp": timestamp,
                "nickname": nickname
            }
        # Send message with styling
        else:
            msg = {
                "message": message,
                "id": id,
                "timestamp": timestamp,
                "style": "".join(style),
                "nickname": nickname

            }

        if len(message) > 0:
            send_queue_message(json.dumps(msg))
            print("Melding sendt!")


if __name__ == '__main__':
    main()
