score = [2, 3, 6, 6, 5]
new_list = []
for i in score:
    if i not in new_list:
        new_list.append(i)
    else:
        continue
new_list.sort()
print(new_list[-2])