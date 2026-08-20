text = input("Enter your text to check pelimdrome: ")

# 123454321

text = text.replace(" ", "") #For remove all white space
text = text.lower() #Convert all leters to lowercase

# Check pelindrome
text_len = len(text)
text_len = int(text_len/2)
pelimdrome = 1

for i in range(text_len):
    if(text[i] != text[-(i+1)]):
        pelimdrome = 0
        break

if(pelimdrome == 0):
    print("This is not pelimdrome!")
else:
    print("This a pelindrome text...")

# neveroddoreven
