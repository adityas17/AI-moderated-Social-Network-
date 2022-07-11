import random
import string
import boto3
from dataclasses import dataclass


@dataclass
class UserModel:
    fullName: string
    email: string
    uniqueID: string
    keyName: string = "defaultProfilePhoto.jpeg"

def initialUserRegistration(userModel: UserModel):


    client = boto3.resource('dynamodb')
    table = client.Table('ML_Users')

    response = table.put_item(
        Item = {
            'userID': userModel.uniqueID,
            'email': userModel.email,
            'fullName': userModel.fullName,
            'keyName': userModel.keyName,
            'posts': [],
            'savedPosts': [],
        }
    )

    response = table.update_item(
        Key = {
            "userID": "ids"
        },
        UpdateExpression = "SET userIDs = list_append(userIDs, :myValue)",
        ExpressionAttributeValues = {
            ":myValue": [userModel.uniqueID]
        },
        ReturnValues = "UPDATED_NEW"
    )

    return {
        "message": "User Registered"
    }
    


