import boto3
import string



def savePost(postID: string,userID: string):

    client = boto3.resource('dynamodb')
    table = client.Table('ML_Users')

    response = table.update_item(
        Key = {
            "userID": userID
        },
        UpdateExpression = "SET savedPosts = list_append(savedPosts, :myValue)",
        ExpressionAttributeValues = {
            ":myValue": [postID]
        },
        ReturnValues = "UPDATED_NEW"
    )

    return {"message": "saved Post"}
