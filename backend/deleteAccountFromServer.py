import random
import string
import boto3
from dataclasses import dataclass

def deleteAccountFromServer(userID: string): 
    
    client = boto3.resource('dynamodb')
    table = client.Table('ML_Users')

    response = table.delete_item(
        Key={
            "userID": userID
        }
    )


    return {"message": "User Account Deleted"}