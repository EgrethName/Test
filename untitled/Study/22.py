def is_exception_handled(element):
    for i in d[element]:
        if i in fin_list:
            return True
        else:
            result = is_exception_handled(i)
            if result:
                return True
    return False


n = int(input())
l = [input().split() for i in range(n)]
m = int(input())
l2 = [input() for j in range(m)]
d = {}
for i in l:
    d[i[0]] = []
    if len(i) > 1:
        del i[1]
        d[i[0]] = i[1:len(i) + 1]
    for j in i:
        if j not in d:
            d[j] = []

fin_list = []
for i in l2:
    fin_list.append(i)
    if i not in d:
        continue
    else:
        if not d[i]:
            continue
        else:
            exception_found = is_exception_handled(i)
            if exception_found:
                print(i)
print(l)
print(d)
print(l2)
print(fin_list)
