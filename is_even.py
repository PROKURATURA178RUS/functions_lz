#Зададим число, которое проверяем на четность
b = float(input('Введите число:'))
#Зададим функцию, которая определяет четность числа
def even(a):
    if a % 2 == 1:
    #Вывод значения
        print('Нечетное')
    else:
    #Вывод значения
        print('Четное')
c = even(b)
print(c) 
    
