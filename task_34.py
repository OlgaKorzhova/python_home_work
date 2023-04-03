def count_str(list_1):
    counter=[]
    
    for phrase in list_1:
        count1=0
        for letter in phrase:
            if letter in russian_alphabet:
                count1+=1
        counter.append(count1)
        
       
    return counter
result=input("Введите строку ").lower().split()
print(result)
russian_alphabet={"а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы"}
result=count_str(result)
print(result)
result=set(result)
if len(result)==1:
    print("рифма есть")
else :
     print("рифмы нет")