password = input("Enter your password")
pas_lenth = len(password)
if(pas_lenth<8):
    print("Not valid! Your password is below 8 characters.")

print(password.isalpha())
print(password.isdigit())
print(password.isalnum())
print(password.isspace())
# print(password.isalpha())
