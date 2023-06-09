n = int(input("Введите порядковый номер месяца - "))
def month_to_season(n):
    if n >= 1 and n <= 2 or n == 12:
        print("Зима!")
    elif n >= 6 and n <= 8:
        print("Лето!")
    elif n >= 9 and n <= 11:
        print("Осень!")
    elif n >= 3 and n <= 5:
        print("Весна!")
    else:
        print("Такого месяца не существует :(")

month_to_season(n)

