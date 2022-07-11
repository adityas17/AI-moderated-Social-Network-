import boto3
import string 



def fetchPostImagePresignedURL(imageKey: string):

    s3 = boto3.client('s3')

    presigned_url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': 'ml-ap-mumbai-south-1',
            'Key': imageKey
            }
        )


    return {
        "presigned_url": presigned_url
    }
