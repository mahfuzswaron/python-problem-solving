inputedStr = str(input())
length = len(inputedStr)
if length > 10:
    print("{a}{b}{c}".format(a = inputedStr[0], b= (len(inputedStr) - 2),c = inputedStr[length - 1] ))
else:
    print(inputedStr)