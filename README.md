# Fetch-Running-Ec2-and-RDS-names-store-it-in-S3-as-CSV-file-and-send-a-copy-in-mail
Fetch all the running instance details and dump it in CSV file store it in S3 and send a mail by attaching this file.

This python script does the following things

1. Fetch all the running instance name
2. Dump all the instance name to CSV file
3. Store this file in S3



Assumption made:
1.There are some servers running in the region.

Steps to achive this:
1. Login to AWS
2. create a lambda function (Python 2.7)
3. Create a S3 bucket
4. Create a blank CSV file in your local and upload to S3. (Example : File.csv)
5. Copy paste this code in lambda created , and make the respective modification to the code by giving your S3 bucket name, CSV File name,    Region Etc.
6. Add a Cloud watch watch event trigger if needed.
7. Create a IAM role with (S3 access,RDS Access) permissions and Give this role to Lambda.
8. Run the Lambda.


Expected Output:
1. CSV file in S3 should be updated with all the running server names.

******************************************************************************************************************
Mail.js

This Node.js  script does the following things
1. get the csv file which was updated in the previous lambda.
2. By using nodemailer , Email is sent to recepient with the  scv file attached.

* supportive packages is given in SendMail.zip *

steps to achieve sending mail using node.js.

1. download zip file
2. expand it.
3. Modify mail.js (Provide your mail id, password ect....)
4. Compress the files now.
5. create a lambda function (Node.js)
6. upload the Zip file and run the lambda function.


Output expected
Mail is sent to recepient with file attached.
