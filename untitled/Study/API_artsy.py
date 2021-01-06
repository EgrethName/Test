import requests
import json

with open("Test_files/dataset_24476_4.txt", "r") as data_set:
    data_list = [str(row).strip() for row in data_set]

client_id = 'b822868ec4e1ed58edcc'
client_secret = '3f0736e93210227f4df3c07403c57f09'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
j = json.loads(r.text)
token = j["token"]

headers = {"X-Xapp-Token" : token}
pair_arts = []
for i in data_list:
    r = requests.get("https://api.artsy.net/api/artists/" + i, headers=headers)
    j = json.loads(r.text)
    pair = (j['sortable_name'], j['birthday'])
    pair_arts.append(pair)
k = sorted(pair_arts, key=lambda birthday: birthday[1])
for i in k:
    print(i[0])
