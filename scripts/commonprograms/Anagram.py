
def Anagram(n,n1):
    # if sorted(n) == sorted(n1):
    #     return "anagram"
    # else:
    #     return "not anagram"


    # if len(n) == len(n1):
    #     res = [ i for i in n if i not in n1 ] + [ i for i in n1 if i not in n]

    #     if not res:
    #         print(res)
    #         return "anagram"
    #     else:
    #         return "not anagram"
    # else:
    #     return "not anagram"
    if len(n) != len(n1):
        return "not anagram"
        
    d={}
    d1={}

    for i in n:
        if i in d.keys():
            d[i]=d[i]+1
        else:
            d[i]=1
    
    for i in n1:
        if i in d1.keys():

            d1[i]=d1[i]+1
        else:
            d1[i]=1

    for i in d:
        if d[i] == d1[i]:
            if i not in d1.keys():
                return "not anagram"
        else:
            return "anagram"
               

if __name__ == "__main__":
    print("enter two strings")
    n=input()
    n1=input()
    print(Anagram(n,n1))
