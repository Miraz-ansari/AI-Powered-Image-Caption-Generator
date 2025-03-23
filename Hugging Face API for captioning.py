pythonCopy codeimport boto3import requests

s3 = boto3.client('s3')

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"headers = {"Authorization": f"Bearer YOUR_HUGGINGFACE_API_TOKEN"}
def lambda_handler(event, context):
    # Get image from S3    bucket = "image-captioning-bucket"    key = "resized-" + event['image_key']
        image_obj = s3.get_object(Bucket=bucket, Key=key)    image_content = image_obj['Body'].read()

    # Send image to Hugging Face API    response = requests.post(API_URL, headers=headers, files={"file": image_content})
    caption = response.json()

    return {
        'statusCode': 200,
        'body': caption
    }
 
