vowels = ["a", 'e', "i", "o", "u"]
def killVowels(word):
    vLess=""
    for w in word:
        if(w not in vowels):
            vLess = vLess + w
    return vLess

while True:
    str = input("Enter your text here: ")
    length = len(str)
    if(length < 10):
        print("Error: sorry, input msut be minimum 10 characters")
    elif(length > 20):
        print("Error: sorry maximum character limit [20] is over. You may try", str[0:20])
    else:
        print("success: great! your text ( ", str , " ) is ", length, " character long" )
        print("without vowels the text is :", killVowels(str))
    