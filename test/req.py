import requests

url = 'http://10.18.11.77:8895/yaml/show'
postdata = ""
p = requests.post(url, data=postdata)
print("get_yaml resp===", p.json())