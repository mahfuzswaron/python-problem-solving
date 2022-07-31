while True:
    str = input("Enter your text here: ")
    length = len(str)
    if(length < 10 or length > 20):
        print("sorry, your inputed text is invalid")
    else:
        print("great!")
    