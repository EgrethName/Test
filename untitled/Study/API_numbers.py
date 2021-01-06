import requests

with open("dataset_24476_3 (2).txt", "r") as data_set:
    data_list = [str(row).strip() for row in data_set]

for i in data_list:
    res = requests.get("http://numbersapi.com/" + i + "/math?json=true")
    data = res.json()
    if data["found"]:
        print('Interesting')
    else:
        print('Boring')

