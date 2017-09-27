import cherrypy

from supernotes.helpers import render_template


class Index:
    @cherrypy.expose
    def index(self):
        return render_template('index.html')


if __name__ == '__main__':
    cherrypy.tree.mount(Index(), '/')
    cherrypy.engine.start()
