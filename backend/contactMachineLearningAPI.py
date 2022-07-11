import boto3
import string
from botocore.vendored import requests


def contactMachineLearningAPI(text: string):

    url = 'http://3.111.215.251/'
    
    myobj = {
    
        "message": text
    
    }
    
    res = requests.post(url, json = myobj).json()
    
    return res