a = int(input('Введите число:'))
flag = 0
for i in range(2,a):
    if a % i == 0:
        flag += 1 
if flag != 0:
    print("число не простое")
else:
    print("число простое")
