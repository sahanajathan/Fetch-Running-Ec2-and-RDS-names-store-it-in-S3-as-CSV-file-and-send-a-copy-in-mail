import urllib
import datetime 
import boto3
from botocore.client import Config
import csv
def handler(event, context):
    dt=datetime.datetime.now().strftime('%I:%M%p %d-%m-%Y')
    print dt
    BUCKET_NAME = 'bucketname'
    FILE_NAME =  'File.csv';
    s3 = boto3.client('s3')
    s31 = boto3.resource('s3')
    s31.meta.client.download_file('bucketname', 'File.csv', '/tmp/' +FILE_NAME)
    region ='eu-west-1'
    client = boto3.client('ec2', region_name=region)
    response = client.describe_instances()
    for r in response['Reservations']:
        for i in r['Instances']:
            if i['State']['Name'] == 'running':
                            instances = [i['InstanceId']]
                            for tags in i['Tags']:
                                if tags['Key'] == 'Name':
                                    instancename = tags['Value']
                                    print instancename
                                    with open('/tmp/' +FILE_NAME, 'ab') as csvfile:
                                       spamwriter = csv.writer(csvfile,delimiter=',')
                                       spamwriter.writerow([instancename])
    client = boto3.client('rds')
    response = client.describe_db_instances()
    instance=response['DBInstances']
    for i in instance:
        name=i['DBInstanceIdentifier']
        status=i['DBInstanceStatus']
        if status=='available':
            print(name)
            with open('/tmp/' +FILE_NAME, 'ab') as csvfile:
                spamwriter = csv.writer(csvfile,delimiter=',')
                spamwriter.writerow([name])
    data = open('/tmp/' + FILE_NAME, 'r')
    s3.upload_file('/tmp/' +FILE_NAME, BUCKET_NAME, dt+'Report.csv')
    object_acl = s31.ObjectAcl('bucketnamet',dt+'Report.csv')
