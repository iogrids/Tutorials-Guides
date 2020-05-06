# Dispatcher

There are 3 kinds of dispatcher in cherrypy

- Routes Dispatcher - class in cherypy library   
- Method Dispatcher - class in cherrypy library
- Dispatcher        - class in cherrypy library

* The below code is an example of routes dispatcher - 'request.dispatch': ForceLowerDispatcherURL() 

* In routes dispatcher we map the URL to a specific method

* The below is an example use-case of in what scenerios we can use routes dispatcher


If you look at the below code

```python

   def generate(self, length=8):
      pass
```

* you can call the generate() function like this http://localhost:8080/generate?length=10
* what if we call the same function like this http://localhost:8080/GENERATE?length=8  (GENERATE in capital letters). We will get error because there is no GENERATE URL
* So in this case we want GENERATE to be converted as lowercase like generate. So before invoking the URL /generate another function should be called as a hook before calling the generate() function. 
* This hook is called a dispatcher in cherrypy, which runs prior to running the generate() function.
* To use the dispatcher hook it should be mentioned in the conf{'request.dispatch': ForceLowerDispatcherURL()}


```python

import random
import string

import cherrypy
from cherrypy._cpdispatch import Dispatcher

class StringGenerator(object):
   @cherrypy.expose
   def generate(self, length=8):
       return ''.join(random.sample(string.hexdigits, int(length)))

# Dispatcher is another class. We are inheriting functions, methods of Dispatcher in our custom class ForceLowerDispatcherURL.
# The class Dispatcher will be having a function called __Call__ which takes the parameter path_info. path_info contains the URL which the user enters in the browser i.e /generate
# lower() makes the path to lower case
# In cherrypy Dispatcher class or Dispatcher object is called before calling the page handler i.e dispatcher is called before calling the generate page handler.
# Dispatcher is called by cherrypy internally to understand the arrangment of handlers, to understand the config entried which are passed to every handler etc
class ForceLowerDispatcherURL(Dispatcher):
    def __call__(self, path_info):
        return Dispatcher.__call__(self, path_info.lower())

if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': ForceLowerDispatcherURL(),
        }
    }
    cherrypy.quickstart(StringGenerator(), '/', conf)
    
```