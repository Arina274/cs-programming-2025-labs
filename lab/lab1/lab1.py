a1=12
b1=3.14
c="NOT"
d=True

Name="Арина"
Age="18"
print("Имя:",Name)
print("Возраст:",Age)

x1=342
x2=56.2
x3="43"
c=x1+x2+int(x3)
print("Сумма:",c)

a=3
b=8
d=(a+4*b)*(a-3*b)+a**2
print("Результат:",d)

x=int(input())
y=int(input())
S=x*y
P=(x+y)*2
print("Площадь:",S)
print("Площадь:",P)

f='Меня зовут '+Name+",мне "+Age+" лет."
print(f)

print("*   *   *")
print(" * * * *")
print('  *   *')

a=1
b=2
print('Арифметические операции:')
print(a+b)
print(a*b)
print(a-b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print('Операции сравнения:')
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

a1='Съешь еще '
b1="этих мягких "
c="французских булок, "
d="да выпей "
e="чаю"
print(a1+b1+c+d+e)

x="Нет! Да! "
print(x*4)

lll=input('Введи 3 числа через запятую')
l1,l2,l3=map(int,lll.split(','))
D=(l1+l3)//l2
print('Результат вычисления:',D)

d=input()
if len(d)>=10:
    print(d[:4])
    print(d[-2:])
    print(d[4:8])
    print(d[::-1])
else:
    print('Слово меньше')