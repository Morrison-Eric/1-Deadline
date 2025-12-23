# 4.py

numbers_input = input("Введите 5 чисел через пробел: ")
numbers = list(map(float, numbers_input.split()))

min_num = min(numbers)
max_num = max(numbers)

print("Минимальное число:", min_num)
print("Максимальное число:", max_num)