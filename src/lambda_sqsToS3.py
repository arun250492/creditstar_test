import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'SQS_QUEUE_URL'

response = client.receive_message(
    QueueUrl='string',
    AttributeNames=[
        'All'|'Policy'|'VisibilityTimeout'|'MaximumMessageSize'|'MessageRetentionPeriod'|'ApproximateNumberOfMessages'|'ApproximateNumberOfMessagesNotVisible'|'CreatedTimestamp'|'LastModifiedTimestamp'|'QueueArn'|'ApproximateNumberOfMessagesDelayed'|'DelaySeconds'|'ReceiveMessageWaitTimeSeconds'|'RedrivePolicy'|'FifoQueue'|'ContentBasedDeduplication'|'KmsMasterKeyId'|'KmsDataKeyReusePeriodSeconds'|'DeduplicationScope'|'FifoThroughputLimit'|'RedriveAllowPolicy'|'SqsManagedSseEnabled',
    ],
    MessageAttributeNames=[
        'string',
    ],
    MaxNumberOfMessages=123,
    VisibilityTimeout=123,
    WaitTimeSeconds=123,
    ReceiveRequestAttemptId='string'
)

#Load sqs data to s3

s3_connection = boto.connect_s3()
bucket = s3_connection.get_bucket('your bucket name')
key = boto.s3.key.Key(bucket, 'response')
with open('some_file.zip') as f:
    key.send_file(f)
