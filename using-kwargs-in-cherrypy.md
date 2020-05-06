# Using **kwargs in cherrypy

Say for example we call a external API for Geo-location like state, city, pin-code. Tomorrow they may update the API with another value like population. To recieve these inputs we will have to create a function with state, city, pin-code, population as arguments and keep updating our arguments with their newest updates.

So instead of creating multiple arguments like state, city, pin-code, population can we create a single argument in our function to capture all the values. We would get this done using **kwargs.
In siutations where we do not know or can conclude on the number of values recieved, we can use use **kwargs.

**kwargs = http://api.com/?state='kerala'&city='coimbatore'&pin-code='641011'&population=20000

```python
  import cherrypy
  
  class HelloWorld(object):
      @cherrypy.expose
      def index(self, **kwargs):
          if kwargs:
              print(kwargs)
          else:
              return "Hello World!"
  
  cherrypy.quickstart(HelloWorld())
  
```python

  Now call the above as

  http://localhost:8080/?a=10&b=20

  In the above example **kwargs = a=10&b=20