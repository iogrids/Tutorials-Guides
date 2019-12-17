import cherrypy
import os

class Product(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        return {
            'products': ['Ice cream', 'Chocolate', 'Fruit', 'Eggs']
        }
    

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'},)
    cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '80')),})
    cherrypy.quickstart(Product(),'/')
