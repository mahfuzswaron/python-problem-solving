while True:
    n = int(input("enter a number to get factorial \n"))
    res = 1
    for i in range(1, n+1):
        res = res * i
    print("factorial = ", res)