import boto3
import string


def fetchPostsForCategory(category: string):

    client = boto3.resource('dynamodb')
    table = client.Table('ML_Users')

    
    response = table.get_item(
        Key = {
            "userID": "ids"
        }
    )

    postIds = response["Item"][category]


    sectionItems = {
        "userPosts": []
    }

    table = client.Table('ML_Posts')

    for id in postIds:
        response = table.get_item(
            Key = {
                "postID": id
            }
        )
        sectionItems["userPosts"].append(response["Item"])

    return sectionItems
