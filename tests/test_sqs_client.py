import sqs_client
import boto3
from moto import mock_sqs
import pytest
import os
from consts import REGION, QUEUE_NAME

@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'

@pytest.fixture(scope='function')
def sqs(aws_credentials):
    with mock_sqs():
        yield boto3.client('sqs', region_name=REGION)


def test_send_queue_message(sqs):
    msg = "Hello, World!"
    sqs.create_queue(QueueName=QUEUE_NAME)
    queue_url = sqs.get_queue_url(QueueName=QUEUE_NAME)["QueueUrl"]
    sqs_client.send_queue_message(msg)
    sqs_messages = sqs.receive_message(QueueUrl=queue_url)
    assert sqs_messages["Messages"][0]["Body"] == msg

