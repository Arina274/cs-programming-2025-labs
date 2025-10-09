print('Задание 1')
Age=int(input('Введи свой возраст: '))
Name=input('Введи своё Имя: ')
for i in range(10):
    print('Меня зовут',Name,'и мне',Age,'лет')
print()

print('Задание 2')
X=int(input('Введи число от 1 до 9: '))
for i in range(1,11):
    R=X*i
    print(R)
print()
    
print('Задание 3')
for i in range(0,101,3):
    print(i,end=' ')
print()

print('Задание 4')
F=int(input('Введи число,для которого будет выведен факториал: '))
Fact=1
for i in range(1,F+1):
    Fact*=i
print(Fact)
print()

print('Задание 5')
k=20
while k>=0:
    print(k)
    k-=1
    
print()

print('Задание 6')
s=int(input('Введи предел для чисел фибонначи: '))
a,b=0,1
while a<=s:
    print(a)
    a,b=b,a+b
print()

print('Задание 7')
stroka=input('Введи строку: ')
s=''
for i in range(len(stroka)):
    s=s+stroka[i]+str(i+1)
print(s)
print()

print('Задание 8')
while True:
    m,n=input('Введи 2 числа через пробел: ').split()
    print('Сумма равна :',int(m)+int(n))

