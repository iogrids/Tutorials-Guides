# How to use external conf file in cherrypy

```python

import cherrypy


class AccessConfig(object):
    @cherrypy.expose
    def index(self):
        return 'user: {}, password : {}'.format(cherrypy.request.app.config['my_api']['api_user'], cherrypy.request.app.config['my_api']['api_password'])


if __name__ == '__main__':
    cherrypy.quickstart(AccessConfig(), '/', 'app.conf')
    
```


app.conf    (Create aoo.conf file in the root folder)

```
[my_api]
api_user = "admin"
api_password = "Start!123"

```