import boto3

s3 = boto3.client('s3')

response = s3.generate_presigned_url('get_object', Params={'Bucket': "mjackson-boto3-942023", 'Key': "testyyyyyy.txt"}, ExpiresIn=300)

print(response)
                                                            
                                                   