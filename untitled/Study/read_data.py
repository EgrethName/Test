text_data = open('Test_files/dataset_3363_4.txt', 'r')

data_str = text_data.readlines()
list_data = []
for i in range(len(data_str)):
    list_data.append(data_str[i].strip().split(';'))
for i in range(len(list_data)):
    del list_data[i][0]
for i in range(len(list_data)):
    for j in range(len(list_data[i])):
        list_data[i][j] = int(list_data[i][j])
    n = sum(list_data[i]) / 3
    print(n)
math = 0
phys = 0
rus = 0
for i in range(len(list_data)):
    math += list_data[i][0]
    phys += list_data[i][1]
    rus += list_data[i][2]
print(math / len(list_data), phys / len(list_data), rus / len(list_data))

text_data.close()
