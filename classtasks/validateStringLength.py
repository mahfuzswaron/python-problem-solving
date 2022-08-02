while True:
    str = input("Enter your text here: ")
    length = len(str)
    if(length < 10 or length > 20):
        print("sorry, your inputed text's length must be within 10 to 20")
        print("your text is " , length, "character long" )
    else:
        print("great! your text is ",length, "character long")
    