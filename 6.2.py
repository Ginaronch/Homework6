user_input = float(input("Введите число от 0 до 8640000: "))
sec = user_input
min = sec // 60
hours, min = divmod(min, 60)
days, hours = divmod(hours, 24)
days = int(days)
if user_input < 0 or user_input > 8640000 :
    print("Ошибка: Недопустимое значение")
else:
    if 11 <= days % 100 <= 14:
        end_days = "дней"
    elif days % 10 == 1:
        end_days = "день"
    elif 2 <= days % 10 <= 4:
        end_days = "дня"
    else:
        end_days = "дней"
    print(f"{days} {end_days}, {int(hours):02}:{int(min):02}:{int(sec) % 60:02}") # :02 - добавить ведущий ноль если значение меньше 10