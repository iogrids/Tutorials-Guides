# Using python decorators with querystring

Python decorator which recieves value like this http://localhost:8080/?value=jeril 
Result - Passed value will be made bold

"""
 In the below code index() calls the decorator uppercase(). Now index() is automatically passed
 to uppercase(index) like so. 
 RESULT: jeril would be turned to JERIL
"""

```python

import cherrypy
from cherrypy import tools
from functools import wraps

# decorator for making the text bold
# *args - contains the function i.e index()
# **kw - contains the value passed to the function

def strong(func):    
    @wraps(func) 
    def wrapper(*args, **kw):
        return '<strong>' + func(*args, **kw) + '</strong>'
    return wrapper


class HelloWorld(object):
    @cherrypy.expose     
    @strong    
    def index(self, value):
        return value
        

if __name__ == '__main__':    
    cherrypy.quickstart(HelloWorld())
    
```