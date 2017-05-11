import json
import cherrypy


class HtmlResponse:
    @cherrypy.expose()
    def index(self):
        return open('response.html')


class JsonResponse:
    @cherrypy.expose()
    def index(self, status=200):
        result = {'status': status,
                  'message': 'ALL OK'}

        return json.dumps(result)


class Form:
    @cherrypy.expose()
    def index(self, status=None, message=None):
        if cherrypy.request.method == 'POST':
            b = cherrypy.request.params
            print(b)
        else:
            return open('form.html')


cherrypy.tree.mount(HtmlResponse(), '/')
cherrypy.tree.mount(JsonResponse(), '/json')
cherrypy.tree.mount(Form(), '/form')

cherrypy.engine.start()
