import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '86a815e8435e43339f254b8c6b6de2f9',
}

params = urllib.urlencode({
    # Request parameters
    'language': 'unk',
    'detectOrientation ': 'true',
})

data = open('m.jpg', 'rb').read()
conn = httplib.HTTPSConnection('api.projectoxford.ai')
conn.request("POST", "/vision/v1.0/ocr?%s" % params, data, headers)
response = conn.getresponse()
data = response.read()
print(data)
conn.close()
