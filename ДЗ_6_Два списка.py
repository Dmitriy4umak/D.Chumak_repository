def unity():
    import random
    n1 = int(input("Введите колличество чисел в первом списке: "))
    min1 = int(input("Введите минимальное число в первом списке: "))
    max1 = int(input("Введите максимальное число в первом списке: "))
    print ("Первый список:")
    list1 = [random.randint(min1,max1) for _ in range(n1)]
    print(list1)
    n2 = int(input("Введите колличество чисел во втором списке: "))
    min2 = int(input("Введите минимальное число во втором списке: "))
    max2 = int(input("Введите максимальное число во втором списке: "))
    print ("Второй список:")
    list2 = [random.randint(min2,max2) for _ in range(n2)]
    print(list2)

    list3=list(set(list1) & set(list2))
    print("Новый список с одинаковыми числами из первых двух списков:")
    print(list3)

unity()