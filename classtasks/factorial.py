def factorial(n):
        if( n == 1):
            return n
        if (n < 1):
            return "N/A"
        return n * factorial(n-1)

while True:
    number = int(input("Enter Number: "))
    print("factorial is", factorial(number))