from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import FileResponse

def home(req):
    return FileResponse("index.html")

def music(req):
    return FileResponse("music.html")

if __name__ == '__main__':

    with Configurator() as config:

        # Create a route called home (index)
        config.add_route('home','/')

        config.add_view(home, route_name='home')

        config.add_route('music', '/music')
        config.add_view(music, route_name='music')

        # Add static view
        # **NOTE: What this does is that it will now have the server bind the
        # static resources on the route “/” to the data in the “./public” folder.
        config.add_static_view(name='/', path='./public', cache_max_age=3600)

        app = config.make_wsgi_app()
    # This line is used to start serving on port 6543 on the localhost
    server = make_server('0.0.0.0', 6543, app) 
    server.serve_forever()