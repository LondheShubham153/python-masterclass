import boto3

s3 = boto3.resource('s3')

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def upload_to_bucket(s3,file_name,bucket_name,key_name):
    print("Uploading file to S3")
    data = open(file_name, 'rb')
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("File uploaded to S3")

def download_from_bucket(s3,file_name,bucket_name,key_name):
    print("Downloading file from S3")
    s3.Bucket(bucket_name).download_file(key_name, file_name)
    print("File downloaded from S3")

download_from_bucket(s3,"thumbnail.png","trainwithshubham","thumbnail.png")