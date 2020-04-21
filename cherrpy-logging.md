How to use cherrypy logging functionality to log errors or to log accesses to specific routes or resources

```python
import cherrypy


class LogDemo(object):
    @cherrypy.expose
    def index(self):
        # use cherrpy.log if you want to log errors instead of print statement.
        # cherrpy.log will log all messages in error_logs.txt file
        cherrypy.log('The index page was hit!')
        return 'OK'

# the log files access_logs.txt and error_logs.txt will automatically be created
if __name__ == '__main__':
    conf = {
        '/': {
            'log.access_file': 'access_logs.txt',
            'log.error_file': 'error_logs.txt',
            'log.screen': False

        }
    }
    cherrypy.quickstart(LogDemo(), '/', conf)
```