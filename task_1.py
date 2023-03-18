n = input('Введите трехзначное число:')
n = int(n)
first = n % 10
first1 = n // 10
second = first1 % 10
three = first1 // 10
print(first + second + three)