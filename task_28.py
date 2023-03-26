a = int(input("Введите первое число " ))
b = int(input("Введите второе число " ))
def sum_num(a, b):
    if a == 0:
        return b
    else:
        return sum_num(a - 1, b + 1)
print(sum_num(a, b))