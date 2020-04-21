# You can raise HTTP error and also mentioning error code using cherrypy.HTTPError. 

```python

""" raise cherrypy.HTTPError(403)
    raise cherrypy.HTTPError(
       "403 Forbidden", "You are not allowed to access this resource.") """
       
```

```python

import cherrypy

class ErrorDemo(object):

    @cherrypy.expose
    def index(self):
        return "Hello Jeril"

    @cherrypy.expose
    def simple(self):
        raise cherrypy.HTTPError(401,'Unauthorized access!')

    @cherrypy.expose
    def file(self, path):
        with cherrypy.HTTPError.handle(FileNotFoundError, 404):
            file = open(path)


if __name__ == '__main__':
    cherrypy.quickstart(ErrorDemo(), '/')
    
```