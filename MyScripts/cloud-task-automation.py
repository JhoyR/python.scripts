import boto3
from botocore.exceptions import WaiterError

# Create a session with AWS credentials and region
session = boto3.Session(
    aws_access_key_id='SUA_ACCESS_KEY',
    aws_secret_access_key='SUA_SECRET_KEY',
    region_name='us-east-1'
)

# Create an EC2 client
ec2 = session.client('ec2')

# Define the instance details
instance_name = 'MinhaInstancia'
image_id = 'ami-0c55b159cbfafe1f0'
instance_type = 't2.micro'
key_name = 'my-key-pair'

# Create the instance
response = ec2.run_instances(
    ImageId=image_id,
    MinCount=1,
    MaxCount=1,
    InstanceType=instance_type,
    KeyName=key_name,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': instance_name,
                },
            ]
        },
    ]
)

# Get the instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f'Instance {instance_name} created with ID: {instance_id}')

# Wait for the instance to be in running state
waiter = ec2.get_waiter('instance_running')
try:
    waiter.wait(InstanceIds=[instance_id])
except WaiterError as e:
    print(f'Error while waiting for instance to be running: {e}')