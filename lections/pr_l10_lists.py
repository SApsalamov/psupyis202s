list1 = [10, 20, 30, 40, 50]
list2 = [11, 21, 22, 23, 24]
print("list1 = ", list1)
print("list2 = ", list2)
print(list1[1])
list2[-1] = 70
print(list2)
big_list = list1 + list2
print(big_list)

srez_big_list = big_list[3:-2]
print(srez_big_list)
srez_big_list.append(90)
srez_big_list.append(30)
print(srez_big_list)
