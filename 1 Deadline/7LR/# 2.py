# 2.py

password = input("Создайте пароль: ")
confirm = input("Подтвердите пароль: ")

if password == confirm:
    print("Пароль создан")
else:
    print("Пароли не совпадают")
    exit()

login_password = input("Введите пароль для входа: ")

if login_password == password:
    print("Access")
else:
    print("Denied")