import boto3
import json

# Create a DynamoDB resource object using the specified region
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Create a table with the specified configuration
table = dynamodb.create_table(
    TableName='Movies',  # Specify the table name
    KeySchema=[
        {
            'AttributeName': 'name',  # Specify the primary key attribute name
            'KeyType': 'HASH'  # Specify the key type as HASH (for the partition key)
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'name',  # Define the attribute name for the primary key
            'AttributeType': 'S'  # Attribute type is String (S)
        }

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,  # Set the read capacity units
        'WriteCapacityUnits': 10  # Set the write capacity units
    }
)

# Print the status of the table
print("Table status:", table.table_status)
