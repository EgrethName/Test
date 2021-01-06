import csv

with open("Crimes.csv") as crimes:
    crimes_reader = csv.reader(crimes)
    crimes_list = []
    for row in crimes_reader:
        crimes_list.append(row)

crimes_2015 = []
crimes_types = set()
for i in crimes_list:
    crimes_types.add(i[5])
    if "/2015" in i[2]:
        crimes_2015.append(i)

cnt_crimes = dict.fromkeys(crimes_types, 0)
for i in crimes_types:
    for j in crimes_2015:
        if i == j[5]:
            cnt_crimes[i] += 1

output = max(cnt_crimes)

print(cnt_crimes)
print(max(cnt_crimes, key=cnt_crimes.get))