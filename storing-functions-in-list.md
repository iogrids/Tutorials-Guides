# Storing functions in a list using cherrpy

```python

import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):        
        return 'This is index page'

    # Functions can be stored in datastructures like shown below. It is stored in list.
    # If you store the function in list you will have to iterate over the list
    # Return would only return a single value, hence would only call the first function
    @cherrypy.expose
    def functions_stored_in_data_structures_example(self):
        funcs = [apple, orange]
        for f in funcs:
            return f()  

def apple():
    return 'apple'

def orange():
    return 'orange'


if __name__ == '__main__':    
    cherrypy.quickstart(HelloWorld())
    
```