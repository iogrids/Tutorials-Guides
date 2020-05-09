# How to call
# http://localhost:8080 - This would return apple


The function apple is a global function and is being called in the class HelloWorld

```python
import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        x = apple()
        return x

def apple():
    return 'orange'
    

if __name__ == '__main__':    
    cherrypy.quickstart(HelloWorld())

```