while True:
    userInput = int(input("Enter your number: "))
    if(userInput < 10):
        print("sorry, your inputed number is less then 10")
    elif(userInput > 20):
        print("sorry, your inputed number is over 20")
    else:
        print("Great! your input is within 10 and 20.")