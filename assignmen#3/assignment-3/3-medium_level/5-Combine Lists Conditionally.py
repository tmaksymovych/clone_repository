l1 = [11, 45, 56, 12, 0, 23]
l2 = [34, 0, 67 ,89, 23]

for a in l2:
    if a not in l1:
        l1.append(a)
print(l1)