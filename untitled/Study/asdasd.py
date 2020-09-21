def check(parent, child):
    if parent == child:
        return 'Yes'
    if not d.get(child):
        return "No"
    if child in d and parent in d[child]:
        return 'Yes'
    else:
        matched = "No"
        for i in d[child]:
            child = i
            matched = check(parent, child)
            if matched == "Yes":
                return matched
        return matched


n = int(input())
l = [input().split(" : ") for i in range(n)]
q = int(input())
l2 = [input().split() for j in range(q)]
d = {}
for i in l:
    if len(i) > 1:
        i[1] = i[1].split()
        d[i[0]] = i[1]
        for j in i[1]:
            if j not in d:
                d[j] = []
    else:
        d[i[0]] = []
for j in l2:
    print(check(j[0], j[1]))
