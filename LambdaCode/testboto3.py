import json
import boto3

ec2client = boto3.client('ec2')
snsclient = boto3.client('sns')

def lambda_handler(event, context):
    # TODO implement
    ec2_instance_id=event['detail']['instance-id']
    tag_response = ec2client.describe_tags(
    Filters=[
        {
            'Name': 'resource-id',
            'Values': [ec2_instance_id],
        },
    ]
    )
    print(tag_response)   

    alltags=tag_response['Tags']
    flag='STOP'
    for tag in alltags:
        print(tag['Key'])
        if tag['Key']=='SPECIAL':
            flag='DONOT_STOP'
            break
    print(flag)
    if flag=='STOP':
        response=ec2client.stop_instances(InstanceIds=[ec2_instance_id])
        snsresponse=snsclient.publish(TopicArn='arn:aws:sns:ap-south-1:637423393571:ec2_stop',
                                      Message='Instance with id '+ec2_instance_id+' has been stopped',
                                      Subject='EC2 Violated!!!!')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
