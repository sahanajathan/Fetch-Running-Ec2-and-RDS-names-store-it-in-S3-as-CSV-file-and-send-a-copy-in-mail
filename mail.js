exports.handler = (event, context, callback) => {
var nodemailer = require('nodemailer');

var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
     user: 'gmail_ID',
     pass: 'gmail_Pass'
  }
});
var dateTime = require('node-datetime');
var dt = dateTime.create();
var AWS = require('aws-sdk');
    var fs = require('fs');
    var s3 = new AWS.S3();
    var src_bkt = 'bucketname'
	var formatted = dt.format('d-m-Y');
	console.log(formatted);
    var src_key = 'Report.csv'

    var params = {   Bucket: src_bkt,   Key: src_key };  

s3.getObject(params, function(err, data){   if (err) {
    console.error(err.code, "-", err.message);
    return callback(err);   }

  fs.writeFile('/tmp/Report.csv',data.Body, function(err){
	  var mailOptions = {
  from: 'gmail_ID',
  to: 'gmail_ID_Recipient',
  subject: 'RUNNING SERVERS REPORT',
  text: 'Please find the attachment for the list all the running servers',
  attachments: [
        {  
            path: '/tmp/UIC_Report.csv'
        }]
};

transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});
    if(err)
      console.log(err.code, "-", err.message);

    return callback(err);   
  }); 
});

};