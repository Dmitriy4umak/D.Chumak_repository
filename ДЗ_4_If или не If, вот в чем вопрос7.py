
def sravnenie():
    a=int(input("Введите первое сравниваемое число: "))
    b=int(input("Введите второе сравниваемое число: "))
    if a>b:
        print("True"," или ","Бобры - добры :)")
    elif a<b:
        print("False"," или ","Злюки бобры :(")
    else:
        print("Even"," или ","Победила дружба")

print ("~~~~Сравните два числа!~~~~")
sravnenie()