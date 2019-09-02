import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data) #info is a list of dictionaries [dic1,dic2,dic3]
print('User count:', len(info))
#print(info)

for item in info:  #iterating thru each dictionary in the list
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
