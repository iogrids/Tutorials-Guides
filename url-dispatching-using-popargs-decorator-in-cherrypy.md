URL's can be dispatched using

OPTION 1: dispatch method - _cp_dispatch 
OPTION 2: The popargs decorator

This is an example using popargs decorator

```
import cherrypy

# takes the first segment and store it into a parameter named band_name
@cherrypy.popargs('band_name')
class Band(object):
    def __init__(self):
        self.albums = Album()              
    
    # http://localhost:8080/nirvana/
    @cherrypy.expose
    def index(self, band_name):
        return 'About %s...' % band_name

# take again the first segment (since we removed the previous first) and store it into a parameter named album_title
@cherrypy.popargs('album_title')
class Album(object):
    def __init__(self):
        self.tracks = Track()

    # http://localhost:8080/nirvana/albums/nevermind/
    @cherrypy.expose
    def index(self, band_name, album_title):
        return 'The album %s by %s...' % (album_title, band_name)

@cherrypy.popargs('track_num', 'track_title')
class Track(object):
    # http://localhost:8080/nirvana/albums/nevermind/tracks/06/polly/
    @cherrypy.expose
    def index(self, band_name, album_title, track_num, track_title):
        return 'Full title %s by %s ' % (track_num, track_title)

if __name__ == '__main__':
    cherrypy.quickstart(Band())
    
```