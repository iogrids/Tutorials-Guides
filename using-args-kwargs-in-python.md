# How to use *args  & **kwargs in Python?

How to create a function which accepts multiple arguments?

In situations where we do not know how many inputs we will recieve we can use *args and **kwargs.

Say for example we call a external API for Geo-location like state, city, pin-code. Tomorrow they may update the API with another value like population. To recieve these inputs we will have to create a function with state, city, pin-code, population as arguments and keep updating our arguments with their newest updates. In siutations like these where we do not know or can conclude on a predefined set of values recieved, we can use *args and **kwargs. 

Look at the code below

```python

  def generate(length = 10, *args, **kwargs):
    // process args
    // process kwargs
```
   
When you call 

```python
     generate(self, length = 8, 43, 45, 56, key1 = 'value1', key2 = 'value2', key3 = 'value3'):
       pass
```
     
  
* 8 in generate() function is passed to the length argument, so length = 10 
* 43, 45, 56 is passed to the *args parameter, so ```python *args = [43,45,56]```. You can add any amount of numbers like 23, 56, 67 and it will be captured in ```python *args```
* ```python key1 = 'value1', key2 = 'value2', key3 = 'value3' ```  is passed to **kwargs, so ``` python **kwargs = {"key1":"value1","key2":"value2","key3":"value3"}```

Note: 
*  *args    - Collects arguments into an array or tuple
*  **kwargs - Collects arguments into a dictionary


Finally these are the basic set of arguments available in python


| ARGUMENT SPECIFICATION | INTERPRETATION                                               |
|------------------------|--------------------------------------------------------------|
| def fn(arg):           | Mandatory positional or keyword argument                     |
| def fn(arg=value):     | Optional positional or keyword argument with a default value |
| def fn(*args):         | Collect positional arguments into an array                   |
| def fn(**args):        | Collect keyword arguments into a dictionary                  |
