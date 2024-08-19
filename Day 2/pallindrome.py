word=input("Enter string that needs to be checked: ")
word_len=len(word)
rev_string=word[::-1]
if word==rev_string:
    print(f"{word} is pallindrome.")
else:
    print(f"{word} is not pallindrome.")