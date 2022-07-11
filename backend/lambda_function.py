import json
from initialUserRegistration import *
from deleteAccountFromServer import *
from fetchS3PresignedURL import *
from createPost import *
from fetchAllUserPosts import *
from fetchPostImagePresignedURL import *
from likeOrDisLikePost import *
from savePost import *
from fetchAllSavedPosts import *
from fetchPostsForCategory import *
from contactMachineLearningAPI import *

def lambda_handler(event, context):
    # TODO implement

    requestBody = event

    requestType = requestBody["requestType"]

    if requestType == "initialUserRegistration":
        fullName = requestBody["fullName"]
        email = requestBody["email"]
        uniqueID = requestBody["uniqueID"]
        userModel = UserModel(fullName=fullName,email=email,uniqueID=uniqueID)
        res = initialUserRegistration(userModel=userModel)
    elif requestType == "deleteAccountFromServer":
        userID = requestBody["userID"]
        res = deleteAccountFromServer(userID=userID)
    elif requestType == "fetchS3PresignedURL":
        userID = requestBody["userID"]
        res = fetchS3PresignedURL(userID=userID)
    elif requestType == "createPost":
        userID = requestBody["userID"]
        title = requestBody["title"]
        description = requestBody["description"]
        category = requestBody["category"]
        imageKey = requestBody["imageKey"]
        postID = requestBody["postID"]
        itemModel = ItemModel(title=title,description=description,category=category,imageKey=imageKey,postID=postID)
        res = createPost(itemModel=itemModel,userID=userID) 
    elif requestType == "fetchAllUserPosts":
        userID = requestBody["userID"]
        res = fetchAllUserPosts(userID=userID)
    elif requestType == "fetchPostImagePresignedURL":
        imageKey = requestBody["imageKey"]
        res = fetchPostImagePresignedURL(imageKey=imageKey)
    elif requestType == "likeOrDisLikePost":
        postID = requestBody["postID"]
        likeDislikeType = requestBody["type"]
        res = likeOrDisLikePost(postID=postID,likeDislikeType=likeDislikeType)
    elif requestType == "savePost":
        postID = requestBody["postID"]
        userID = requestBody["userID"]
        res = savePost(postID=postID,userID=userID)
    elif requestType == "fetchAllSavedPosts":
        userID = requestBody["userID"]
        res = fetchAllSavedPosts(userID=userID)
    elif requestType == "fetchPostsForCategory":
        category = requestBody["category"]
        res = fetchPostsForCategory(category=category)
    else:
        res = {"message": "Something went wrong, check your request-type"}

    return {
        'statusCode': 200,
        'body': res
    }
