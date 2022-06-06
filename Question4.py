n = input("Enter a word: \n")

rev = ''.join(reversed(n))

if n == rev:
    print("It is a palindrome")
else:
    print("Enter another word")
