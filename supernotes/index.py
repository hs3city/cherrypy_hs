import cherrypy

from supernotes.helpers import render_template


class Index:
    @cherrypy.expose
    def index(self):
        return render_template('index.html')


@cherrypy.expose
class Note:
    def GET(self):
        pass


@cherrypy.expose
class NoteList:
    def GET(self):
        pass


if __name__ == '__main__':
    cherrypy.tree.mount(Index(), '/')
    cherrypy.engine.start()
