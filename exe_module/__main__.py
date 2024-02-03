# -- use . to make relative path import (otherwise it will fail!)
from .myfun import get_function

# -- The __main__.py file makes the module executable
# you can directly run it with: python -m taille

print("Start the __main__.py file")

obj = get_function()
print(obj)
