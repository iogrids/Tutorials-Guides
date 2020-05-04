# Cherrpy forms using server side rendering

Server side rendering meaning the FORM is rendered on the server side. 

In the below code the value is entered by the user in the form and the same value is recieved in the python function

```python
import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
            <head></head>
            <body>
                <form method="get" action="respond">
                    <input type="text" value="test" name="text_input" />
                    <button type="submit">Submit</button>
                </form>
            </body>
        </html>"""

    @cherrypy.expose
    # text_input is the name of the  <input type="text" > in the above form
    def respond(self, text_input='hello'):
        # %s is a format specifier in python. Similiarly %d - Integers, %f for float etc.
        msg = 'You sent me this text_input: %s' % text_input
        return msg


if __name__ == '__main__':
    conf = {'server.socket_host': '0.0.0.0'} 
    cherrypy.config.update(conf)
    cherrypy.quickstart(StringGenerator(),config={'/':conf})
```