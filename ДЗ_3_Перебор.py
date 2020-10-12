
import random
a=[random.randint(0,10) for i in range(5)]
print(a)
b=int(input("Введите нужное число\n: "))
if b in a:
    print("Искомое число:", b)
    print("Ваше число под номером:", a.index(b)+1)
if b not in a:
    print("Искомое число:", b)
    print("Заданное число не найдено")
