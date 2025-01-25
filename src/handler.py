import base64
from io import BytesIO
from PIL import Image
from transformers import pipeline

textpipe = pipeline("text-classification", model="skandavivek2/spam-classifier")
imagepipe = pipeline("image-classification", model="Wvolf/ViT_Deepfake_Detection")

def handler(job):
    """ Handler function that will be used to process jobs. """
    job_input = job['input']
    input_type = job_input["type"]

    print(f"Received job with input: {job_input}")
    
    if input_type == "text":
        return textpipe(job_input["text"])
    elif input_type == "image":
        image_data = base64.b64decode(job_input["image"])
        image = Image.open(BytesIO(image_data))
        return imagepipe(image)
    else:
        return {"error": "Invalid input type"}

import runpod
runpod.serverless.start({"handler": handler})
