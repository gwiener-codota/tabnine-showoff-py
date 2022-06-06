import boto3

bucket_name = 'experiments'
file_name = 'results.json'
region = 'us-east-1'

# read file from s3 bucket
response = boto3.client('s3', region_name=region).get_object(Bucket=bucket_name, Key=file_name)
print(response['Body'].read())

# upload a file to s3 bucket
response = boto3.client('s3', region_name=region).put_object(
    Bucket=bucket_name, File=file_name, ACL='public-read')