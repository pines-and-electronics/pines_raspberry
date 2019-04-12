import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

for root, dirs, files in os.walk('/images'):
    for file in files:
        if file.endswith('.jpeg'):
            print(os.path.join(root, file))
            file_name = os.path.join(root,file)
         # Loads the image into memory
            with io.open(file_name, 'rb') as image_file:
             content = image_
             file.read()

            image = types.Image(content=content)

         # Performs label detection on the image file
            response = client.label_detection(image=image)
            labels = response.label_annotations

            print('Labels:')
            for label in labels:
                print(label.description)
