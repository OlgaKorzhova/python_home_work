n = int(input("Введите число элементов массива =  "))
x = int(input("Введите число x =  "))
list = []
count = 0
for i in range(n):
    list.append(int(input(f"Введите {i} элемент массива ")))
    if x == list[i]:
        count +=1
print(list)
print(f"Число {x} встречается в массиве {count} раза")
