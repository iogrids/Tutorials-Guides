# Using Tailored dispatcher or custom dispatcher in cherrypy

# Refer this blog for further understanding and update this post

# https://appmecha.wordpress.com/?s=cherrypy&submit=Search
# https://appmecha.wordpress.com/2008/10/27/cherrypy-gae-routing-2/

```python

"""
If you look at the below code

you can call the generate() function like this http://localhost:8080/generate?length=10
what if we call the same function like this http://localhost:8080/GENERATE?length=8  (GENERATE in capital letters).
So in this case we want GENERATE to be converted as lowercase like generate. So before invoking the URL /generate another function should be called
as a hook before calling the generate() function. This hook is called a dispatcher in cherrypy which is runs prior to running the generate() function.
To use the dispatcher hook it should be mentioned in the conf{'request.dispatch': ForceLowerDispatcherURL()}
"""

"""
Check the function   def generate(self, length=8):   Have you ever wondered how does this function gets processed? This function has a single argument which is length and what if it has 
many other arguments like height, width, breadth. How does the processing function understand that it has only a single argument and if there are many arguments how does the processing
function know it has many arguments? The internal function in cherrypy which processes the generate() function is called as dispatcher. An example of dispatcher() function can be shown like this

def dispatcher(length, *args, **kwargs):
   // process args
   // process kwargs
   
   
When you call 

  generate(self, length = 8, 43, 45, 56, key1 = 'value1', key2 = 'value2', key3 = 'value3'):
  
     pass
     
  
8 in generate() function is passed to the length argument in dispatcher() function 
43, 45, 56 is passed to the *args in dispatcher() function
key1 = 'value1', key2 = 'value2', key3 = 'value3'  is passed to **kwargs in dispatcher() function

Note: *args    - Collects arguments into an array
      **kwargs - Collects arguments into a dictionary
"""

"""
Finally these are the basic set of arguments available in python

| ARGUMENT SPECIFICATION | INTERPRETATION |
| ------ | ------ |
| def fn(arg): | Mandatory positional or keyword argument |
| def fn(arg=value): | Optional positional or keyword argument with a default value |
| def fn(*args): | Collect positional arguments into an array |
| def fn(**args): | Collect keyword arguments into a dictionary |

"""


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