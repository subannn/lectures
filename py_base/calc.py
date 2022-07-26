first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
operation = input("Выберите операцию из следующих +-*/%**//: ")
ans = ""
if operation == '+': 
    ans = ans + "Ответ: " + str(first + second)
elif operation == '-': 
    ans = ans + "Ответ: " + str(first - second)
elif operation == '*': 
    ans = ans + "Ответ: " + str(first * second)
elif operation == '/': 
    ans = ans + "Ответ: " + str(first / second)
elif operation == '%': 
    ans = ans + "Ответ: " + str(first % second)
elif operation == '**': 
    ans = ans + "Ответ: " + str(first ** second)
elif operation == '//': 
    ans = ans + "Ответ: " + str(first // second)
else: ans = ans + "Ответ: Данной операции нет в системе"
print(ans)