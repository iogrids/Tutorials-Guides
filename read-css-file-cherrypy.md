```python
import cherrypy
from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader('templates'))


class Root:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('forms.html')
        """ self.get_galaxies is the function which is written below. We are also passing
            the function to the template. The function returns a list
        """
        print(os.path.abspath(os.getcwd()))
        return tmpl.render(salutation='Hello', target='Jeril')


if __name__ == '__main__':
    conf = {
        # This is the global configuration
        'global': {
            'server.socket_host': '127.0.0.1',
            'server.socket_port': 8080
        },
        # The below path can be accessed as -> http://localhost:8080/
        # This is the configuration for the root path (/)
        '/': {'tools.staticdir.root': os.path.abspath(os.getcwd())},
        # The below path can be accessed as -> http://localhost:8080/static/
        # The below is the configuration for /static path (/static)
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'public',  # Name of the folder where style.css is present
        }
    }
    cherrypy.quickstart(Root(), '/', conf)

```

## Now call the css file like This

```

<head >
    <meta charset = "UTF-8" >
    <meta name = "viewport" content = "width=device-width, initial-scale=1.0" >
    <meta http-equiv = "X-UA-Compatible" content = "ie=edge" >
    <title > Document < /title >
    <link href = "/static/style.css" rel = "stylesheet" >
</head >

```
