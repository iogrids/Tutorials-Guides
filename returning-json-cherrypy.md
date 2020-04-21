# Returning Json using cherrypy. The decorator @cherrypy.tools.json_out() is used to return JSON as output

```python
import cherrypy


class JsonOut(object):
    @cherrypy.expose
    def index(self):
        return 'Weekly menu!'

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def menu(self):
        return {'weeklymenu': {'monday': {},
                               'tuesday': {},
                               'wednesday': {},
                               'thursday': {}}}


if __name__ == '__main__':
    cherrypy.quickstart(JsonOut(), '/')
    
```