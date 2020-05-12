# Example of inheritance in Cherrypy

class HelloWorld inherits class Page. Once inherited class HelloWorld can call all the methods 
and variables of class Page

```python

import cherrypy

class Page:
    title = 'This is the title'

    def header(self):
        return """
        <html>
        <head></head>
            <body>
                <a href = "header">This is the header </a>
            </body>
        </html>
        """

    def footer(self):
        return """
        <html>
        <head></head>
            <body>
                <a href = "footer">This is the footer </a>
            </body>
        </html>
            """

class HelloWorld(Page):
    @cherrypy.expose
    def index(self):
        # return self.title - To return the title      
        return self.header() + self.footer()  # returning multiple values
        

if __name__ == '__main__':    
    cherrypy.quickstart(HelloWorld())
```
    