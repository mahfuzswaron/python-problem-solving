babyDictionary = {
    "do": "kora",
    "eat": "khawa",
    "read": "pora",
    "school": "jekhane porano hoy",
    "office": "jekhane kaj kora hoy",
    "institute": "protisthan",
    "polytechnic": "karigori",
    "educaion": "shikkha",
    "dictionary": "ovidhan",
    "book": "boi",
    "test": "porikkha",
    "computer": "adhunik gononakari jontro",
    "programming": "poricalona kora",
    "language": "vasha",
    "english": "ingraji",
    "bengali": "bangla",
    "write": "likha",
    "type": "dhoron, device er maddhome likha",
    "hello": "ohe",
    "python": "programming er vasha, 1 dhoroner sap"
}

def search(word):
    items = babyDictionary.items()
    
    result = []
    for x, y in items:
        if(word in x):
            result.append(y)
        elif(word in y):
            result.append(x)
        
    if(len(result) < 1):
        return "404 Not Found!"
    else:
        return ", ".join(result)
    
print("choose a option by number from the list below:")
print("1. English to Bengali")
print("2. Bengali to English")
while True:
    optionInput = int(input("option no : "))
    if(optionInput == 1):
        searchInput = str(input(("English : ")))
        print("Bengali: ", search(searchInput))
    elif(optionInput == 2):
        searchInput = str(input(("Bengali: ")))
        print("English: ", search(searchInput))
    else:
        print("sorry, please choose a valid option")
