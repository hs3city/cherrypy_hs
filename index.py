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

#TODO: fix
class Form:
    @cherrypy.expose()
    def index(self, status=None, message=None):
        if cherrypy.request.method == 'POST':
            result = {'status': status,
                      'message': message}

            return json.dumps(result)
        else:
            return open('form.html')


cherrypy.tree.mount(HtmlResponse(), '/html')
cherrypy.tree.mount(JsonResponse(), '/json')
cherrypy.tree.mount(Form(), '/form')

cherrypy.engine.start()
