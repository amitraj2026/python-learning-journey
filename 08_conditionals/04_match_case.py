a = int(input("Enter a lucky number between 1 to 10 "))


match a:
    case 1:
        print("You won a Phone")
    case 4:
        print("You won a camera")
    case 5:
        print("You won a earphone")
    case _:
        print("Better luck next time")
