You can access the below URL's and you will get the same content or the same resource of function will be called

http://localhost:8080/
http://localhost:8080/home
http://localhost:8080/whatever

```python

import cherrypy


class HandlerAlias(object):
    @cherrypy.expose(['index', 'home', 'whatever'])
    def index(self):
        return 'Handler alias demo!'


if __name__ == '__main__':
    cherrypy.quickstart(HandlerAlias(), '/')

```