# How to call another function in cherrypy

http://localhost:8080 - This would return apple
Functional style programming using cherrypy and python

Things like strings, lists, modules, and functions are all objects. 
There’s nothing particularly special about functions in Python. They’re also just objects.


```python

import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):        
        return 'This is index page'
    
    # Functions can be assigned to variables as shown below
    @cherrypy.expose
    def functions_assigned_to_variables_example(self):
        x = apple()
        return x
    
    # Functions are objects and can be directly called as shown below
    @cherrypy.expose
    def functions_are_objects_example(self):
        return apple()

    
def apple():
    return 'apple'


if __name__ == '__main__':    
    cherrypy.quickstart(HelloWorld())


```
