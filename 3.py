num = 0
while (int(num) < 1000 or int(num) > 9999):
    num = input("Введите чсило от 1000 до 10000 ")

if (int(num) == int(num[::-1])):
    print("Настоящее")
else:
    print("Кривое")
