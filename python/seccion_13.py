

#ejercicio 1

x= int(input("ingresa un numero: "))
i=0
p=0
while i!=11:
    p=x*i
    print(p)
    i=i+1
    
#ejercicio 2

edad=int(input("edad: "))
e=1
while e!=edad+1:
    print(e, "años")
    e=e+1
    

#ejercicio 3

print("1,2,3,4,5,6,7,8,9,10")
x= int(input("ingresa un numero: "))
y= int(input("ingresa un segundo numero: "))

for i in range(x,y):
    print(i)
print(i+1)




#ejercicio 4

print("1,2,3,4,5,6,7,8,9,10")
w=int(input("ingresa un numero: "))
m=int(input("ingresa un segundo numero: "))


for j in range(w,m+1):
    if j%2 !=0:
        print(j)