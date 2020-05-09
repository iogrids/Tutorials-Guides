# Example of GET, POST, PUT, DELETE, OPTIONS in python using mongodb

  ## TO access the resources you can use Postman

```python
import random
import string
import cherrypy
import cherrypy_cors
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps

@cherrypy.expose
class StringGeneratorWebService(object):    
    
    @cherrypy.tools.json_out()
    def GET(self):
        db = setup_database()
        results = dumps(db.collection.find({}))
        return results

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()  # If you do not provide this line JSON will not be returned
    def POST(self):
        #recieves the values from the form
        input_json = cherrypy.request.json
        print(input_json)     
        db = setup_database()
        db.collection.insert_one(input_json)
        return {'status': 'success', 'message': 'inserted'}
    
    @cherrypy.tools.json_out()
    def PUT(self):
        db = setup_database()
        db.collection.update_one({"_id": 53},{"$set":{"name":"craig"}})
        return {'status': 'success', 'message': 'updated'}

    @cherrypy.tools.json_out()
    def DELETE(self):
        db = setup_database()
        db.collection.delete_many({})
        return {'status': 'success', 'message': 'deleted'}

    def OPTIONS(self):
        # Browser makes a preflight request before accessing GET, POST, PUT, DELETE 
        cherrypy_cors.preflight(allowed_methods=['GET', 'POST', 'DELETE', 'PUT', 'OPTIONS'])


def setup_database():
    # pick what collection do you want to work with
    client = MongoClient('mongodb+srv://jeriljose:<password>@cluster0-jcy8l.mongodb.net/test?retryWrites=true&w=majority')
    # pick what database do you want to work with   
    db = client['playground']
    # create the collection in the database on server startup
    collection = db['users']
    # return the collection so that collection can be accessed in other functions 
    return collection

def cleanup_database():
    # Delete the collection in the database on server startup
    pass
    

           """" 
           Note: request.dispatch': cherrypy.dispatch.MethodDispatcher() might not be required here. cherrypy.dispatch.MethodDispatcher() tells cherrypy not to do routing for us and we will do the 
           routing ourselves. Here cherrypy does the routing for us since it automatically identifies which is GET request, which is POST request and responds automatically.
           So try removing this line and run the same application and check whether it works
           
           """
           
if __name__ == '__main__':
    cherrypy_cors.install()
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'cors.expose.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        }
    }
    cherrypy.engine.subscribe('start', setup_database)
    cherrypy.engine.subscribe('stop', cleanup_database)

    webapp = StringGeneratorWebService()
    webapp.generator = StringGeneratorWebService()

    cherrypy.quickstart(webapp, '/', conf)
```