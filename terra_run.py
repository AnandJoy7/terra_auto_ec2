import boto3

def describe_ec2_instances():
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.all()
    for instance in instances:
        print(f'ID: {instance.id}, State: {instance.state}, Type: {instance.instance_type}')

if __name__ == "__main__":
    describe_ec2_instances()
