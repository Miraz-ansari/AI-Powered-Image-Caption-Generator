pythonCopy codeimport boto3from PIL import Imageimport io
# Initialize S3 clients3 = boto3.client('s3')
def lambda_handler(event, context):
    # Get the uploaded image from S3    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
        # Download image from S3    s3_response = s3.get_object(Bucket=bucket, Key=key)    image_content = s3_response['Body'].read()

    # Open image with PIL    image = Image.open(io.BytesIO(image_content))
        # Resize image (example: 256x256)    resized_image = image.resize((256, 256))

    # Save the image back to S3
    buffer = io.BytesIO()
    resized_image.save(buffer, 'JPEG')
    buffer.seek(0)

    s3.put_object(Bucket=bucket, Key=f"resized-{key}", Body=buffer)
    return {
        'statusCode': 200,
        'body': 'Image processed successfully'
    }
 
