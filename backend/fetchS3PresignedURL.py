import boto3
import string
import random


def fetchS3PresignedURL(userID: string):

    nameOfObject = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(50))

    s3 = boto3.client('s3')
    keyName = userID + '/' + nameOfObject + '.png'

    presigned_url = s3.generate_presigned_post(
        Bucket = "ml-ap-mumbai-south-1",
        Key = keyName,
    )

    return {
        "presigned_url": presigned_url,
        "nameOfObject": nameOfObject,
        "keyName": keyName
    }