# Two type of modules in python, one is built in modules and second one is external modules 

# List of the the build in modules https://docs.python.org/3/py-modindex.html
import math
# import os
import myModule
import requests


print(math.sqrt(16))
myModule.hello()
r  = requests.get("https://www.google.com")
print(r.text)
