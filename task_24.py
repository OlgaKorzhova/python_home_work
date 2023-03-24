count=int(input("Введите количество кустов = "))
list_new=list(int(input(f" Введите количество ягод {i} куста = ")) for i in range(count))
print(list_new)
sum_max=list_new[0]+list_new[1]+list_new[count-1]
number_max=0
for i in range(1,count):
    if i!=count-1:
        sum_temp=list_new[i]+list_new[i-1]+list_new[i+1]
    else:
        sum_temp=list_new[i]+list_new[i-1]+list_new[0]
    if sum_temp>sum_max:
        sum_max=sum_temp
        number_max=i
print(f" Максимальная сумма ягод = {sum_max}  c {number_max} куста")