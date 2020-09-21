import os
unsorted_set = set()
for current_dir, dirs, files in os.walk(r"C:\Users\Egreth\Downloads\main"):
    for i in files:
        if i[-3:] == ".py":
            unsorted_set.add(current_dir)
unsorted_list = sorted(list(unsorted_set))
for i in unsorted_list:
    print(i[31:])
