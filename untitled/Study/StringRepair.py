
def is_number(s_int):
    try:
        int(s_int)
        return True
    except ValueError:
        return False


s = input()
list_s = []
temp_int = ''
for i in range(len(s)):
    if is_number(s[i]) is False:
        if temp_int != '':
            list_s.append(int(temp_int))
            temp_int = ''
        list_s.append(s[i])
    else:
        temp_int += s[i]
list_s.append(int(temp_int))
print(list_s)
s_fin = ''
for i in range(0, len(list_s), 2):
    s_fin += list_s[i] * list_s[i + 1]
print(s_fin)
