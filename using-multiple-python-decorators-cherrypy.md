# Using multiple python decorators in Cherrpy


```python

"""
 In the below code index() calls the decorator uppercase(). Now index() is automatically passed
 to uppercase(index) like so. 
 RESULT: jeril would be turned to JERIL
"""

import cherrypy
from cherrypy import tools
from functools import wraps

# decorator for making the text bold
def strong(func):    
    @wraps(func) 
    def wrapper(*args):
        return '<strong>' + func(*args) + '</strong>'
    return wrapper

# decorator for making the text in italics
def emphasis(func):
    @wraps(func)
    def wrapper(*args):
        return '<em>' + func(*args) + '</em>'
    return wrapper


class HelloWorld(object):
    @cherrypy.expose     
    @strong
    @emphasis
    def index(self):
        return 'jeril!'
        

if __name__ == '__main__':    
    cherrypy.quickstart(HelloWorld())

```