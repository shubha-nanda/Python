def reverse_for_loop(s):
    if s == s[::-1]:
        return "palindrome"
    else:
        return "not palindrome"


if __name__ == "__main__":
    print(reverse_for_loop(input()))
