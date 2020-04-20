```python
import cherrypy
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))


class Root:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('forms.html')
        """ self.get_galaxies is the function which is written below. We are also passing
            the function to the template. The function returns a list
         """
        return tmpl.render(salutation='Hello', target='Jeril', galaxies=self.get_galaxies())

     # This function returns a list
    def get_galaxies(self):
        galaxies = ["Messier 81", "StarBurst", "Black Eye", "Cosmos Redshift", "Sombrero",
                    "Hoags Object", "Andromeda", "Centarus A", "Whirlpool", "Canis Major Overdensity"]
        return galaxies


cherrypy.config.update({'server.socket_host': '127.0.0.1',
                        'server.socket_port': 8080,
                        })

cherrypy.quickstart(Root())

```

Using the variables from the python file in the HTML file

```
<h1>{{ salutation }} {{ target }}</h1>

<ul>
    {% for galaxy in galaxies %}
    <li class="collection-item"><a href="#">{{galaxy}}</a></li>
    {% endfor %}
</ul>

```