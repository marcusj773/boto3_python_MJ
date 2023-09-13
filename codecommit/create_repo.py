import json
import boto3
import uuid

def lambda_handler(event, context):
    # Create a CodeCommit client
    codecommit = boto3.client('codecommit')

    # Create a new CodeCommit repository with the specified name
    response = codecommit.create_repository(
    repositoryName='luit-silver-2023-{}'.format(str(uuid.uuid4()))
    )

    # Print the response from the repository creation
    print(response)
    
    del response["repositoryMetadata"]["lastModifiedDate"]
    del response["repositoryMetadata"]["creationDate"]
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
