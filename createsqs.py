import boto3
import logging 

sqs = boto3.resource('sqs')

sqs_queue = sqs.create_queue(QueueName='NewQueue')

print(sqs_queue.url)
print(sqs_queue)