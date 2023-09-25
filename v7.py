import math
a = float(input('Введите a: '))
z1 = math.cos(3/8*math.pi-a/4)**2 - math.cos(11/8*math.pi+a/4)**2
z2 = math.sqrt(2)/2*math.sin(a/2)
print(f'z1 = {z1}')
print(f'z2 = {z2}')
