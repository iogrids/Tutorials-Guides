# How to handle javascript, CSS and images in Cherrypy

First, save the following stylesheet into a file named style.css and store into a local directory public/css.

```css
body {
 background-color: blue;
}
```

---

```python
import os
import os.path
import random
import string
import cherrypy


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
            <head>
            <link href="/static/css/style.css" rel="stylesheet">
            </head>
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
             'tools.sessions.on': True,
             'tools.staticdir.root': os.path.abspath(os.getcwd())
         },
         # With the below code all files inside public can be accessed as http://localhost/static/
         '/static': {
             'tools.staticdir.on': True,
             'tools.staticdir.dir': './public'
         }
     }
    cherrypy.quickstart(StringGenerator(), '/', conf)
```