
```
import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"

cherrypy.quickstart(HelloWorld())

```

cherrypy.quickstart() -> this is basically calling the below 4 lines or in other words the below 4 lines are replaced by a single line which is cherrypy.quickstart()

```
cherrypy.tree.mount(HelloWorld(), '/', conf)
cherrypy.server.socker_host = "127.0.0.1"
cherrypy.engine.start()
logging.info('Hello World started')
```

## So what is conf?

```
cherrypy.tree.mount(HelloWorld(), '/', conf)
```

conf is a dictionary which can be used like this


conf = {
    '/': {
        
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        'tools.response_headers.on': True,
        'tools.response_headers.headers': [
            ('content-type': 'application/json')
         ],
    }
}


# Basic Cherrypy Tutorial

```python
class Root:

  @cherrypy.expose
  def index(self):
    return self.dosome()

  def dosome(self):
    return "hello there"
    
cherrypy.tree.mount(Root(), '/')
```

In this example a request to /dosome would return a Not Found error because the method is not exposed even though it belongs to a published
object. The reason is that the dosome callable object is not exposed to the internal engine as a potential match for a URI.

---

## Cherrypy Engine:
  
Cherrypy has an internal engine called cherrypy engine. cherrypy engine handles the request and response objects

To start the engine you must issue the following call:

```python
cherrypy.engine.start()
```
---

## Cherrypy built in HTTP server

CherryPy comes with its own web (HTTP) server. To start the web server you have to make the following call:

```python
cherrypy.server.quickstart()
```

## Cherrypy configuration

You can pass configuration information to cherrypy engine when processing a URL.

You can pass global configuration information to cherrypy engine through ```python cherrypy.config.update()``` method and 
application specific configuration information via ```python cherrypy.tree.mount()``` method. You can also pass configuration
information which is path specific.

configuration information will be passed as python dictionaries which is shown below

```python
global_conf = {
  'global': {
  'server.socket_host': 'localhost',
  'server.socket_port': 8080,
  },
}
application_conf = {
  '/style.css': {
  'tools.staticfile.on': True,
  'tools.staticfile.filename': os.path.join(_curdir,
  'style.css'),
  }
}
```

configuration information can be passed as file also like shown below

```python
[global]
server.socket_host="localhost"
server.socket_port=8080

[/style.css]
tools.staticfile.on=True
tools.staticfile.filename="/full/path/to.style.css"
```

To notify CherryPy of our global settings we need to make the following call:
  
• With a dictionary
cherrypy.config.update(conf)
• With a file
cherrypy.config.update('/path/to/the/config/file')

To notify cherrypy of application specific settings we need to use cherry.tree.mount() method

• With a dictionary
cherrypy.tree.mount(application_instance, script_name, config=conf)

• With a file
cherrypy.tree.mount(application_instance, script_name, config='/path/to/config/file')
