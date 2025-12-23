# 5.py

import math
operation = input("Введите операцию (пример: 5 + 3): ")
parts = operation.split()

if len(parts) != 3:
    print("Ошибка: нужно ввести два числа и знак операции")
else:
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Ошибка: деление на ноль")
            result = None
        else:
            result = num1 / num2
    elif operator == "%":
        result = num1 % num2
    elif operator == "//":
        if num2 == 0:
            print("Ошибка: деление на ноль")
            result = None
        else:
            result = num1 // num2
    elif operator == "**":
        result = num1 ** num2
    elif operator == "%%":
        result = num1 * num2 / 100
    elif operator == "/**":
        if num1 < 0:
            print("Ошибка: корень из отрицательного числа")
            result = None
        else:
            result = math.sqrt(num1)
    else:
        print("Ошибка: неверный оператор")
        result = None
    
    if result is not None:
        print(f"Результат: {result}")