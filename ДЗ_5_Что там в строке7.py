
stroka=input("Введите случайное предложение: ")
iskomoe=input("Введите символ, который необходимо найти: ")

count=0
for i in range(len(stroka)):
    if stroka[i]==iskomoe.lower() or stroka[i]==iskomoe.upper():
        count+=1

print("Буква", iskomoe, "встречается в тексте", count, "раз")