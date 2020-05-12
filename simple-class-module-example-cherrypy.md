# Simple example of Classes and objects in Cherrypy

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