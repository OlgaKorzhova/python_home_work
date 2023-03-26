a = int(input("Введите число " ))
b = int(input("Введите степень " ))
def degree_num(a, b):
    if b == 0:
        return 1
    else:
        return a ** b
print(degree_num(a, b))