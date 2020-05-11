# Nesting Cherrypy functions

```python

import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):        
        return 'This is index page'

    # Every time you call speak, it defines a new inner function whisper and then calls it immediately after. 
    # Functions can be nested as the speak() function.
    # speak() returns the output of whisper()   
    @cherrypy.expose
    def function_can_be_indexed(self):
        return speak('Hello, World')    

# This is an example of nested function
def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)


if __name__ == '__main__':    
    cherrypy.quickstart(HelloWorld())
    
```