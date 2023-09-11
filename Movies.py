import boto3 
import json


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
   
table = dynamodb.Table('Movies')

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'name': 'Friday',
            'rating': 'R'
        }
    )
    batch.put_item(
        Item={
            'name': 'Iron Man',
            'rating': 'PG'
        }
    )
    batch.put_item(
        Item={
            'name': 'Blade',
            'rating': 'R'
        }
    )
    batch.put_item(
        Item={
            'name': 'Dead Presidents',
            'rating': 'R'
        }
    )
    batch.put_item(
        Item={
            'name': 'Harry Potter and the Soucerors Stone',
            'rating': 'PG'
        }
    )
    batch.put_item(
        Item={
            'name': 'Maze Runner',
            'rating': 'PG-13'
        }
    )
    batch.put_item(
        Item={
            'name': 'Hunger Games',
            'rating': 'PG-13'
        }
    )
    batch.put_item(
        Item={
            'name': 'The Wash',
            'rating': 'R'
        }
    )
    batch.put_item(
        Item={
            'name': 'Ready Player One',
            'rating': 'PG-13'
        }
    )
    batch.put_item(
        Item={
            'name': 'Book of Eli',
            'rating': 'PG-13'
        }
    )