list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
list_2 = []
min_number = 6
max_number = 10
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i, end = ' ')