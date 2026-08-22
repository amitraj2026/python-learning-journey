'''
Write a function calculate_area(length, width=10) that returns the area of
a rectangle. Test it by calling the function with:
Both length and width
Only length (use default width)
'''


def area(length, width):
    a = length*width
    return a

print(area(5, 8))


def area1(length, width = 5):
    a = length*width
    return a 

print(area1(7))
