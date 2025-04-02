import json

f = open(r"auto_small.json",
         'r',
         encoding='utf8')
text = f.read()
print(text)
data = json.loads(text)
print(data)
