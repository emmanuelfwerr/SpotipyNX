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

"""
this function reads a file and uploads it to a S3 bucket
"""
def uploadS3(file_path, new_name, bucket_name='spotify-output'):
    # upload to S3 bucket:
    try:
        s3 = boto3.resource('s3')
        s3.Bucket(bucket_name).upload_file(file_path, new_name)
        print('nice! file uploaded to s3')
    except Exception as e:
        print(e)
        return 'error'

    # generate public temporal URL
    try:
        url = boto3.client('s3').generate_presigned_url(
            ClientMethod='get_object',
            Params={'Bucket': bucket_name, 'Key': new_name},
            ExpiresIn=3600
        )
        print(url)
        return url
    except Exception as e:
        print(e)


"""
send an email notification using Amazon SNS
not possible to attach files :(
it is send to us, not to the user :(
"""
def sendEmail(message, subject):
    try:
        sns = boto3.client('sns')
        sns.publish(
            TopicArn='arn:aws:sns:us-east-1:619628291786:spotify-send-email:5855775a-d7f2-4761-acf6-7a90ab9e904b',
            Message=message,
            Subject=subject
        )
    except Exception as e:
        print(e)


if __name__ == "__main__":
    file_path = '.gitignore' # test file
    new_name = 'test.txt'
    uploadS3(file_path, new_name)



