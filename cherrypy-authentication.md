There are various kinds of authentication like

* Basic authentication
* Digest authentication
* JWT authentication


"""
  Basic Authentication: If a visitor enters username and password, the entered username 
  and password send to the server is not encrypted. 
  Digest Authentication: If a visitor enters username and password, the entered username 
  and password send to the server is encrypted using a hash function. 
"""


This is an example of basic authentication in cherrypy

```python

import cherrypy
from cherrypy.lib import auth_basic


def validate_pass(realm, user, password):
    if user == 'admin' and password == 'Start!123':
        return True
    else:
        return False


class SecureApp(object):
    @cherrypy.expose
    def index(self):
        return 'Successfull authorization!'


if __name__ == '__main__':
    conf = {
        # On the main route which is / or http://localhost:8080/
        # If you want authentication for other routes copy and paste the same for those routes
        '/'	: {
            'tools.auth_basic.on': True,
            # Provide the domain name here instead of localhost if running on a domain
            'tools.auth_basic.realm': 'localhost',
            # validate_pass is a function
            'tools.auth_basic.checkpassword': validate_pass,
            'tools.auth_basic.accept_charset': 'UTF-8',
        }
    }
    cherrypy.quickstart(SecureApp(), '/', conf)

```

This is an example of digest authentication in cherrypy

```python

import cherrypy
from cherrypy.lib import auth_digest

USERS = {
    'admin': 'Start!123',
    'jeriljose': 'password123'
}


class SecureApp(object):
    @cherrypy.expose
    def index(self):
        return 'Successfull authentication!'


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.auth_digest.on': True,
            'tools.auth_digest.realm': 'localhost',
            # this function get_ha1_dict_plain() encrypts the entered usernamd and password
            'tools.auth_digest.get_ha1': auth_digest.get_ha1_dict_plain(USERS),
            'tools.auth_digest.key': 'a565c27146791cfb',
            'tools.auth_basic.accept_charset': 'UTF-8',
        }

    }
    cherrypy.quickstart(SecureApp(), '/', conf)


```
