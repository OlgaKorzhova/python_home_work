n = int(input("Введите число элементов массива =  "))
x = int(input("Введите число x =  "))
list = []
for i in range(n):
    list.append(int(input(f"Введите {i} элемент массива ")))
print(list)
uniq_number = set()
element = list[0]
diff = abs(list[0]-x)
for num in list[1:]:
    cur_diff = abs(num-x)
    if cur_diff < diff and num != x:
        element = num
        diff = cur_diff
        uniq_number.clear()
        uniq_number.add(element)
    elif cur_diff == diff and num != x:
        uniq_number.add(num)

print(f"Самые близкие числa к {x} :")
print(*uniq_number)