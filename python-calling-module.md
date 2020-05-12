# Importing modules in python

Lets create a module called mymod.py with the below code

### mymod.py


```python
var = 10

def dothis():
	print("executing the dothis() function")
```


### Importing the above module  - app.py


```python

import mymod    # This imports the above python module mymod.py

print(mymod.var)      # This prints the variable declared in mymod.py var = 10
print(mymod.dothis)   # This calls the function mymod.py in mymod.py

```

You can also call like this

```python

import mymod as mm    # This imports the above python module mymod.py

print(mm.var)      # This prints the variable declared in mymod.py var = 10
print(mm.dothis)   # This calls the function mymod.py in mymod.py

```

You can also import variable directly

```python

from mymod import var, dothis

print var
dothis()
```
