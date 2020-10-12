print("Введите два числа:")
a = int(input("Первое число:\n: "))
b = int(input("Второе число:\n: "))
print("Введите арифметическое действие:")
print("1 - суммирование")
print("2 - вычетание")
print("3 - умножение")
print("4 - деление")
x = int(input("Действие\n: "))
if (x>1 and x<3) : c=a-b
elif (x>2 and x<4) : c=a*b
elif (x>3 and x<5) : c=a/b
else : c=a+b
print ("Ответ: ", c)