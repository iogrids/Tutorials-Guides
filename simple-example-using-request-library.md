# Simple example of using Requests library using Cherrypy

```python
import cherrypy
import requests

# The below is the json data
# https://reqres.in/api/users/2 json data is shown below

"""
{
   "data":{
      "id":2,
      "email":"janet.weaver@reqres.in",
      "first_name":"Janet",
      "last_name":"Weaver",
      "avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg"
   },
   "ad":{
      "company":"StatusCode Weekly",
      "url":"http://statuscode.org/",
      "text":"A weekly newsletter focusing on software development, infrastructure, the server, performance, and the stack end of things."
   }
}
"""

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        r = requests.get('https://reqres.in/api/users/2')
        json_data = r.json()
        return json_data['ad']['url']

cherrypy.quickstart(HelloWorld())
```