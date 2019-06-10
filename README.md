# PutObjectTaggingS3
Boto3 code to update tags on s3 objects.

S3 object tags are useful for several use cases for example cost tracking, billing, separating customers data etc. This code can be used in Lambda to ensure your s3 objects get tagged every time it gets uploaded/overwritten. It uses s3 event triggers to invoke Lambda, which in turn will put tags to your s3 objects. 

# services used 
1. Lambda
2. S3
3. CloudWatch logs for Lambda invocations 
