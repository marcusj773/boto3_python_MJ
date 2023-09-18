python import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = {'time': current_time}

    response = sqs.send_message(
        QueueUrl='https://sqs.us-west-1.amazonaws.com/469716034835/MO_SQS',
        MessageBody=time_date
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Sent message')
    }