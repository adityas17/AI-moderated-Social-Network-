import boto3
import string


def fetchAllUserPosts(userID: string):
    
    client = boto3.resource('dynamodb')
    table = client.Table('ML_Users')

    response = table.get_item(
        Key = {
            "userID": userID
        }
    )

    itemIDS = response["Item"]["posts"]

    print("itemIDS: ",itemIDS)

    itemsForSale = []
    
    table = client.Table('ML_Posts')


    for id in itemIDS:
        response = table.get_item(
            Key = {
                "postID": id
            }
        )
        print("response: ",response)
        realItem = response["Item"]
        realItem["postID"] = id
        itemsForSale.append(realItem)


    return { "userPosts" :itemsForSale }
