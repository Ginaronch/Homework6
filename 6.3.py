user_input = input("Введите число: ")
answer = int(user_input)
while answer > 9:
    answer = 1
    for number in user_input:
        answer *= int(number)
        user_input = str(answer)
print("Ответ: ",answer)