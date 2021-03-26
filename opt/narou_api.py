import requests
import json
import pandas as pd

limit_item = 10

api = "https://api.syosetu.com/novelapi/api/?out=json&of=t-w-gf-gl&lim=" + str(limit_item) + "&order=old"
response = requests.get(api)
data = json.loads(response.text)
array = []

for i in data:
  array.append(i)

del array[0]

df = pd.DataFrame(data=array)

file_name = input("Please Enter File Name: ")
df.to_excel('./' + file_name + '.xlsx', index=False, header=False)