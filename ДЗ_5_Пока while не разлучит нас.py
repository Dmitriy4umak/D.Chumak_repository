
a=int(input("Введите число А: "))
b=int(input("Введите число Б: "))
c=int(input("Введите число В: "))

print ("~~~~Помоги числу А превысить число Б!~~~~")
count=0
while a<b:
    count+=1
    print("Попытка",count,".","Значение А: ",a," - Подкинь еще чутка! :)")
    a+=c
    if a==b:
        count+=1
        print("Попытка",count,".","Значение А: ",a," - Ну вот, уже на ровне! :)")
        a+=c
    if a>b:
        count+=1
        print("Попытка",count,".","Значение А: ",a," - Это успех!!!")
print("Кол-во прибавлений числа В: ", count)