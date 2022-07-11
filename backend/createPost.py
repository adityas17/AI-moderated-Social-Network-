import random
from re import M
import string
from urllib import response
import boto3
from dataclasses import dataclass

@dataclass
class ItemModel:
    title: string
    description: string
    category: string 
    imageKey: string
    postID: string


def createPost(itemModel: ItemModel,userID: string):

    client = boto3.resource('dynamodb')
    table = client.Table('ML_Posts')

    response = table.put_item(
        Item = {
            "title": itemModel.title,
            "description": itemModel.description,
            "categoryName": itemModel.category,
            "imageKey": itemModel.imageKey,
            "postID": itemModel.postID,
            "likes": 0,
            "dislikes": 0
        }
    )
    
    
    client = boto3.resource('dynamodb')
    table = client.Table('ML_Users')

    response = table.update_item(
        Key = {
            "userID": "ids"
        },
        UpdateExpression = "SET #arrayName = list_append(#arrayName, :myValue)",
        ExpressionAttributeValues = {
            ":myValue": [itemModel.postID]
        },
        ExpressionAttributeNames = {
              "#arrayName": itemModel.category
        },
        ReturnValues = "UPDATED_NEW"
    )

    response = table.update_item(
        Key = {
            "userID": userID
        },
        UpdateExpression = "SET posts = list_append(posts, :myValue)",
        ExpressionAttributeValues = {
            ":myValue": [itemModel.postID]
        },
        ReturnValues = "UPDATED_NEW"

    )

    
    return {"message": "post created"}

 


