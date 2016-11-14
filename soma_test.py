import pyoxford

data = open('m.jpg', 'rb').read()
api = pyoxford.vision("86a815e8435e43339f254b8c6b6de2f9")
#result = api.ocr("https://oxfordportal.blob.core.windows.net/vision/OpticalCharacterRecognition/1.jpg")
result = api.ocr(data)

doc = result.to_document()
for par in doc:
    print("\n".join(par))
