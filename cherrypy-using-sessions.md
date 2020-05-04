# Using sessions in Cherrypy

HTTP is a stateless protocol. So if a value stored in a form should be shown in another page, we will have to store the value of the form in a session variable 
and in the other page we get the value from the session variable. Session variable is stateful and stores the value will the user is online or the browser window is open. Once if the user 
closes the window then session variable is lost.

The below code shows how to utilize session in cherrypy. 

In the /index page, a form is shown. index page calls the generate function
In the /generate function or page a random string is generated based on the string length provided in the index page. This value is then stored in the session variable
In the /display page, the value is displayed from the session variable


```python
import cherrypy

class StringGenerator(object):

    @cherrypy.expose
    def index(self):
        return """<html>         
        <head></head>
           <body>
               <form method="get" action="generate">
                   <input type="text" value="8" name="length" />
                   <button type="submit">Give it now!</button>
               </form>
           </body>
        </html>"""

    @cherrypy.expose
    def generate(self, length=8):
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session['mystring'] = some_string
        return some_string

    @cherrypy.expose
    def display(self):
        return cherrypy.session['mystring']


if __name__ == '__main__':
    conf = {
            '/': {
                'tools.sessions.on': True
                }
            }
    cherrypy.quickstart(StringGenerator(), '/', conf)

```

