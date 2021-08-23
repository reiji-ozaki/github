from google.cloud import vision
with open('./IMG_6971.jpg','rb')as image_file:
    content = image_file.read()

image = vision.Image(content=content)
annnotator_client = vision.ImageAnnotatorClient()
response_data = annnotator_client.label_detection(image=image)
labels = response_data.label_annotations

print('---result---')
for label in labels:
   print(label.description, ':' , round(label.score *100,2), '%')
print('---result---')
