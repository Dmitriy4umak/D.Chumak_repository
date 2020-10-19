import datetime

def countdown():
    a=str(datetime.timedelta(seconds=int(input("Введите отведенное колличество секунд: "))))
    print("До конца осталось:",a)

countdown()