# Cherry basic routing

```python
import cherrypy


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"


# http://localhost:8080/HelloWorld

    """
    You can also write like HelloWorld.exposed = True to expose a particular function
    instead of @cherrypy.expose. HelloWorld.exposed = True can also be called within a
    if loop like.. if the condition is true then expose this function
    """

    @cherrypy.expose
    def HelloWorld(self):
        return "Hello Jeril!"

    # def sum(self, a b) -> You can pass parameters like this
    # You can call the above like this -> http://localhost:8080/sum?a=5&b=10
    @cherrypy.expose
    def sum(self, a, b):
        """ simply returning the values will always be string. If a = 5 and b =10 the 
            return value would be a + b = 510. To avoid this you will have to mention
            the datatype i.e float(a) """
        return ' a + b = {}'.format(float(a) + float(b))


if __name__ == '__main__':
    """ 
     If you want to call the class function on a different path 
     # cherrypy.quickstart(HelloWorld(), '/differentpath')
    """
    cherrypy.quickstart(HelloWorld(), '/')

```
