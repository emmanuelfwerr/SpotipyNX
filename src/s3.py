import boto3
from dotenv import load_dotenv

# maybe useful for later - REMOVE
#import time
#import random
#import string

# bucket_region = 'us-east-1' # not used by now

# need this to test the uploadS3() itself,
# but won't need it here for the app, since it is already loaded
load_dotenv()

def uploadS3(file_path, new_name, bucket_name='spotify-output'):
    try:
        s3 = boto3.resource('s3')
        s3.Bucket(bucket_name).upload_file(file_path, new_name)
        return 'nice! file uploaded to s3'
    except Exception as e:
        print(e)
        return 'error'

if __name__ == "__main__":
    file_path = '.gitignore' # test file
    new_name = 'test.txt'
    uploadS3(file_path, new_name)



