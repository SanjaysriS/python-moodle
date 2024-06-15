
letter = input().lower()

if letter in ['a', 'e', 'i', 'o', 'u']:
    print("It's a vowel.")
elif letter == 'y':
    print("Sometimes it's a vowel... Sometimes it's a consonant.")
else:
    print("It's a consonant.")
