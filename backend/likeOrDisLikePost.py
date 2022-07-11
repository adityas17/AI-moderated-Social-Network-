import boto3
import string



def likeOrDisLikePost(postID: string,likeDislikeType: string):
    
    client = boto3.resource('dynamodb')
    table = client.Table('ML_Posts')

    if likeDislikeType == "LIKE":
        response = table.update_item(
            Key = {
                "postID": postID
            },
            UpdateExpression = "SET likes = likes + :incrementValue",
            ExpressionAttributeValues = {
                ":incrementValue": 1
            },
            ReturnValues = "UPDATED_NEW"
        )
    else:
        response = table.update_item(
            Key = {
                "postID": postID
            },
            UpdateExpression = "SET dislikes = dislikes + :incrementValue",
            ExpressionAttributeValues = {
                ":incrementValue": 1
            },
            ReturnValues = "UPDATED_NEW"
        )

    return { 
        "message": "value updated"
     }


# response = table.update_item(
#     Key = {
#         "userID": model.userID
#     },
#     UpdateExpression = "SET totalVerbalReasoningQuestionsCompleted = totalVerbalReasoningQuestionsCompleted + :incrementValue",
#     ExpressionAttributeValues = {
#         ':incrementValue': model.totalVerbalReasoningQuestionsCompleted
#     },
#     ReturnValues = "UPDATED_NEW"
# )