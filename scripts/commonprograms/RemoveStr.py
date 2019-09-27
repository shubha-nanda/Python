def removeString(n,n1):
    s1 = ''
    for c in n:
        if c == n1:
            continue
        else:     
            s1 = s1 + c
         # appending chars in reverse order
    return s1


if __name__ == "__main__":
    print("enter the string")
    n=input()
    print("enter the char to remove")
    n1=input()
    print(removeString(n,n1))