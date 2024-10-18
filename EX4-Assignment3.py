def insert(sorted_list, value):
    for i in range(len(sorted_list)):
        if sorted_list[i] >= value:
            sorted_list.insert(i, value)
            return sorted_list
    sorted_list.append(value)
    return sorted_list


l1 = [1, 34, 56, 78, 89]
v1 = 77
l2 = [1, 3, 56, 234, 789]
v2 = -99
l3 = [1, 3, 56, 234, 789]
v3 = 789

print(insert(l1, v1))
print(insert(l2, v2))
print(insert(l3, v3))
