# Importing modules in python

Lets create a module called mymod.py with the below code

### mymod.py

```python
var = 10

def dothis():
	print("executing the dothis() function")
```

---

Lets create another python file and access the above function and variables in the below code

### importing the above module

```python

import mymod    # This imports the above python module mymod.py

print(mymod.var)      # This prints the variable declared in mymod.py var = 10
print(mymod.dothis)   # This calls the function mymod.py in mymod.py

```