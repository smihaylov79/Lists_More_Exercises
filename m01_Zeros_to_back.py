lst1 = input().split(', ')
lst2 = []
lst3 = lst1.copy()
count = 0
for item in lst1:
    if int(item) == 0:
        lst3.remove(item)
        count += 1
    else:
        lst2.append(int(item))
for i in range(count):
    lst2.append(0)
print(lst2)
