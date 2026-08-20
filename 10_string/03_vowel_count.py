text = input("Enter your text here for vowels count: ")

# a, e, i, o, u ->vowel


# Vowel count
text_len = len(text)
vowel = 0
text = text.lower()
for i in range (text_len):
    letter = text[i]
    match letter:
        case 'a':
            vowel += 1
        
        case 'e':
            vowel += 1
        
        case 'i':
            vowel += 1
        
        case 'o':
            vowel += 1
        
        case 'u':
            vowel += 1
        case _:
            pass
        
print(f"Total number of vowels are: {vowel}")
