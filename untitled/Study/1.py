text_data = open('Test_files/dataset_3363_3.txt', 'r')
data_str = text_data.read()
s = data_str.lower().split()
d = {}
for i in s:
    d[i] = s.count(i)
max_value = max(d.values())
d_list = list(d.items())
d_list_max = []
for i in range(len(d_list)):
    if d_list[i][1] == max_value:
        d_list_max.append(d_list[i])
ordered_list = sorted(d_list_max)
text_data.close()
print(*ordered_list[0])
