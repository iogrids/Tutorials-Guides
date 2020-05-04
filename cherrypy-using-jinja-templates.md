# Python example using Jinja2 templates 

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

---

# Using For loop in jinja template to get values from the python dictionary

```html
<h1>{{ salutation }} {{ target }}</h1>

<ul>
    {% for galaxy in galaxies %}
    <li class="collection-item"><a href="#">{{galaxy}}</a></li>
    {% endfor %}
</ul>

```

---

# Using conditional statements in Jinja2

```html
<h2> Welcome to this blog </h2>

{% if target == 'jeril' %}
<p> Yes, available </p>
{% else %}
<p> Not available </p>
{% endif %}

```

# Template inheritance in jinja2. Click to play the video

[![Click to play video](http://img.youtube.com/vi/DxI4jnb5m1Q/0.jpg)](http://www.youtube.com/watch?v=DxI4jnb5m1Q "Python and Flask - Template Inheritance in Jinja2")
