import json
import cherrypy
import jinja2

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates')
)


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


class SimpleTemplate:
    @cherrypy.expose()
    def index(self):
        template = env.get_template('simple.html')
        return template.render()


class Params:
    @cherrypy.expose()
    def index(self, param=None, counter=None):
        template = env.get_template('params.html')

        numbers = {'one': 1,
                 'two': 2,
                 'three': 3}

        return template.render(template_param=param,
                               counter=counter,
                               numbers=numbers)


cherrypy.tree.mount(SimpleTemplate(), '/simple')
cherrypy.tree.mount(Params(), '/params')
cherrypy.tree.mount(HtmlResponse(), '/')
cherrypy.tree.mount(JsonResponse(), '/json')
cherrypy.tree.mount(Form(), '/form')

cherrypy.engine.start()
