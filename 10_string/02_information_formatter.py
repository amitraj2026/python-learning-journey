name = input("Enter your name: ")
name = name.strip()
name = name.title()

email = input("Enter your email: ")
email = email.strip()
email = email.lower()

city = input("Enter your city: ")
city = city.strip()
city = city.title()


print(f"Name:  {name}")
print(f"Email: {email}")
print(f"City:  {city}")
