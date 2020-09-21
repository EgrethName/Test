objects = [1, 2, 1, 2, 3, True, False, True, False, "true"]
objects_id = [id(i) for i in objects]
s = len(set(objects_id))
print(s)


