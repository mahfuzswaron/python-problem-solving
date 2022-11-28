string = str(input().upper()) ## DADE
# alphaVal = ['A', 'B', 'C', 'D', 'E']
alphaVal = 'ABCDE'
larger = 0 
for i in string: 
    if(alphaVal.index(i) > larger): 
        larger = alphaVal.index(i)
print(larger + 1)

