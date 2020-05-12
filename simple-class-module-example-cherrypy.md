# Example 1 of classes and objects in Cherrypy

```python
import cherrypy

class Root:
    @cherrypy.expose
    def index(self):
        return """
        <html>
        <head></head>
            <body>
                <a href = "admin">Admin </a>
            </body>
        </html>
        """ 

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"

if __name__ == '__main__':
    root = Root()  #Creating an instance of Root class
    cherrypy.quickstart(root)
    
```


# Example 2 of classes and objects in Cherrypy

```python

import cherrypy

class Fruits(object):
    def __init__(self):
        # Create an instance of Snacks class
        self.snacks = Snacks()
    
    # access like http://localhost:8080/chips
    @cherrypy.expose
    def chips(self):
        # Call functions of snacks class
        return self.snacks.chips()

    # access like http://localhost:8080/mango
    @cherrypy.expose
    def mango(self):
        # Call functions of snacks class
        return self.snacks.mango()

class Snacks(object):    
    def chips(self):
        return 'Are you eating chips'

    def mango(self):        
        return 'Are you eating mango'

if __name__ == '__main__':
    cherrypy.quickstart(Fruits())
```