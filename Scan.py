import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Movies')

response = table.scan()

items = response['Items']

for item in items:
    print(item)
    
