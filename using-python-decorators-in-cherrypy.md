# Using python decorators in Cherrypy


```python

"""
 In the below code index() calls the decorator uppercase(). Now index() is automatically passed
 to uppercase(index) like so. 
 RESULT: jeril would be turned to JERIL
"""

import cherrypy
from cherrypy import tools
from functools import wraps

# just a plain Python decorator
# A decorator is called implicitly with the function it is decorating as the first argument.
# A decorator is simply a function which takes another function as a argument and returns another function as the return value
def uppercase(func):
    # wraps() is a decorator that is applied to the wrapper function of a decorator
    @wraps(func) #preserve function attributes, such as its name
    def wrapper(*args):
        original_result = func(*args)
        modified_result = original_result.upper()
        return modified_result
    return wrapper


class HelloWorld(object):
    @cherrypy.expose     
    @uppercase # decorated once, the exposed function is now uppercase(index) 
    def index(self):
        return 'jeril!'
        

if __name__ == '__main__':    
    cherrypy.quickstart(HelloWorld())
```