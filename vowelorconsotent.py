l = input("Enter a letter: ")

if l.isalpha() and len(l) == 1:  # Check if input is a single alphabetic character
    if l.lower() in 'aeiou':  # Check if the letter is a vowel
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")

c=input("enter a letter:")
