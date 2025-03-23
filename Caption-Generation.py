pythonCopy codefrom transformers import BlipProcessor, BlipForConditionalGenerationfrom PIL import Image
# Load the model and processorprocessor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
def generate_caption(image_path):
    # Open the image    image = Image.open(image_path)

    # Process the image    inputs = processor(image, return_tensors="pt")

    # Generate caption    out = model.generate(**inputs)    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

# Example usage
caption = generate_caption("resized-image.jpg")
print(f"Generated caption: {caption}")
 
