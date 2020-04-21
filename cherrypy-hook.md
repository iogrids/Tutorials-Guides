Using cherrypy hook system. This would be useful if you want to execute a function before another function

```python

import cherrypy


class HookDemo(object):
    @cherrypy.tools.register('before_finalize')
    def hello():
        print("Hello printed")

    @cherrypy.tools.register('before_finalize')
    def welcome():
        print("welcome printed")

    @cherrypy.expose
    @cherrypy.tools.hello()
    @cherrypy.tools.welcome()
    def index(self):
        return 'OK'


if __name__ == '__main__':
    cherrypy.quickstart(HookDemo(), '/')
    
```

Result would be

* welcome printed
* Hello printed

OK will be printed when you access the root path -> http://localhost:8080/