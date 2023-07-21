from flask import Flask, url_for, send_from_directory
from routes.mainRoutes import *

class App:

    def __init__(self):
        self.app = Flask(__name__)
        self.routes()
        self.static()
    
    def routes(self):

        try:
            self.app.register_blueprint(mainRoutes)
            
        except:
            raise Exception('Não foi possível recuperar as rotas, principais')
    
    def static(self):
        
        @self.app.route('/static/css/<path:filename>')
        def css(filename):
            return send_from_directory('static/css', filename)
        
        @self.app.route('/static/js/<path:filename>')
        def js(filename):
            return send_from_directory('static/js', filename)

        @self.app.route('/static/img/<path:filename>')
        def img(filename):
            return send_from_directory('static/img', filename)
    
if __name__ == '__main__':
    app = App()
    app.app.run()