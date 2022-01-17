# Harshit Agrawal
# https://github.com/iamharshit13


#START

#anagram checking function
def checkanagram(s1,s2):
    ls1=len(s1)
    ls2=len(s2)
    if(ls1!=ls2):
        return 0
    
    ss1=sorted(s1)
    ss2=sorted(s2)

    for i in range(0,ls1):
        if ss1[i]!=ss2[i]:
            return 0
    return 1
#user input and function calling 
s1 = input("Enter the first string:")
s2 = input("Enter the second string:")

if(checkanagram(s1,s2)):
    print("The strings are in anagram")
else:
    print("The strings are not in anagram")

#END


# Harshit Agrawal
# https://github.com/iamharshit13