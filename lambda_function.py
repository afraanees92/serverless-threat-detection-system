import json
import boto3
from datetime import datetime

# AWS Clients
sns = boto3.client('sns')
s3 = boto3.client('s3')

# Replace with your SNS Topic ARN
TOPIC_ARN = 'arn:aws:sns:us-east-1:YOUR_ACCOUNT_ID:security-alerts'

# Replace with your S3 Bucket Name
BUCKET_NAME = 'security-incident-logs-afra'


def lambda_handler(event, context):

    # Alert Message
    message = f"Suspicious activity detected at {datetime.now()}"

    # Send Email Alert using SNS
    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject='Security Alert',
        Message=message
    )

    # Save Incident Log in S3
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=f'incident-{datetime.now()}.txt',
        Body=message
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Incident handled successfully')
    }