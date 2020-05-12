# Real usecase Example: 


Imagine you will have to display information like sex, state, physics_mark, chemistry_mark etc based on 
id and name where there is a drop-down box for id and name. The user selects the id and name from the
drop-down list. These values are passed to the python program.

These parameters should be parsed by python which is done using _cp_dispatch()

```
http://localhost:8080/?id=MKT01138
http://localhost:8080/students/?id=MKT01138&name=jeril
```

You cannot keep writing function for each passed value i.e 101011 & jeril. The _cp_dispatch() passes
the values to a function which then retrieves values like sex, state, physics_mark, chemistry_mark
etc from the database and returns the value as JSON.



# Basic explanation


The below code can create dynamic URL's like shown below

```
http://localhost:8080/nirvana/
http://localhost:8080/nirvana/albums/nevermind/
```

the above URL's is also the same as

```
http://localhost:8080/?artist=nirvana
http://localhost:8080/albums/?artist=nirvana&title=nevermind
```

1. ```_cp_dispatch``` is an inbuilt function in cherrypy which takes the URL and processes it
2. If the URL is ```http://localhost:8080/nirvana/albums/nevermind/``` ```_cp_dispatch``` processes the URL by 
   passing it to vpath. Now in vpath the values will be like this

   ```
   vpath[nirvana, albums, nevermind]
   vpath.pop() -  will remove the first value inserted to vpath
   
   Example: 
   vpath.pop(0) - will remove nirvana
   vpath.pop(1) - will remove albums
   ```

"""

import cherrypy

class Band(object):
    def __init__(self):
        self.albums = Album()

    def _cp_dispatch(self, vpath):
        if len(vpath) == 1:            
            cherrypy.request.params['name'] = vpath.pop()            
            return self             

        if len(vpath) == 3:
            cherrypy.request.params['artist'] = vpath.pop(0)  # /band name/
            vpath.pop(0) # /albums/
            cherrypy.request.params['title'] = vpath.pop(0) # /album title/
            return self.albums

        return vpath

    # this function is called if vpath parameter is only one eg: http://localhost:8080/nirvana/
    # Example vpath = [nirvana]
    # _cp_dispatch() function calls this function if vpath has single parameter i.e vpath = [nirvana]
    @cherrypy.expose
    def index(self, name):
        return 'About %s...' % name

# this function is called if vpath parameter is three eg: http://localhost:8080/nirvana/albums/nevermind/
# Example vpath = [nirvana, albums, nevermind]
# _cp_dispatch() function calls this function if vpath has 3 parameters i.e vpath = [nirvana, albums, nevermind]
class Album(object):
    @cherrypy.expose
    def index(self, artist, title):
        # can return values like shown below
        # Select * from table where author = artist & name = title
        return 'About %s by %s...' % (title, artist)

if __name__ == '__main__':
    cherrypy.quickstart(Band())