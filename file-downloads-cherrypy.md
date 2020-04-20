# File downloads using cherrypy

To implement this create a folder called downloads in the root folder and then you can polulate the folder with various files like zip, images, videos etc


```python

import cherrypy
import os
from cherrypy.lib.static import serve_file


class FileViewer(object):
    @cherrypy.expose
    def index(self):
        # os.getcwd() - This gives the current working directory
        # os.sep.join([os.getcwd(), 'downloads']) - concatenates multiple paths
        """ os.path.abspath(os.sep.join([os.getcwd(), 'downloads']))  
            simply removes things like . and .. from the provided path """
        # os.listdir - lists the files in the provided path
        # _blank - will open in new browser or window
        # {0} - is a placeholder for the format function which will be replaced by the first argument provided to the format function

        index_page = "<ul>"
        for item in os.listdir(os.path.abspath(os.sep.join([os.getcwd(), 'downloads']))):
            index_page += "<li><a href='/downloads/{0}' target='_blank'>{0}</a></li>".format(
                item)

        index_page += '</ul>'

        return index_page

    """ Set status, headers, and body in order to serve the given path """
    """ If the below function is not provided the content-type will be guessed
        by the browser but however it is a good practise to include the below 
        function. This function will be automatically called whenever /downloads is 
        accessed. """
    @cherrypy.expose
    def downloads(self, filepath):
        """ 
        application/x-download - this is a mime type which tells the client 
        what kind of data it is sending back. This tells it is of type attachment
        """
        # server_file is an inbuilt function of cherrypy
        return serve_file(filepath, 'application/x-download', 'attachment')


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/downloads': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'downloads',
        }
    }
    cherrypy.quickstart(FileViewer(), '/', conf)
    
```
