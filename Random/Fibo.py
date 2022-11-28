n = int(input("please enter the length of fibo you want \n"))
a = 0
b = 1
c = 0
fibo = []
fibo.append(str(a))
fibo.append(str(b))
for i in range(2, n+1):
    c = a + b
    fibo.append(str(c))
    a = b
    b = c
result = ", ".join(fibo)
print("fibo = ", result )
