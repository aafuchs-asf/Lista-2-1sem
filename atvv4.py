anos = 0
a = 80000
b = 200000

while a < b:
    anos += 1
    a = a + a*0.03
    b = b + b*0.015
    print(a,b)

print(anos)