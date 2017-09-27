import jinja2

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates')
)


def render_template(template_name, context=None):
    template = env.get_template(template_name)
    rendered_template = template.render(context)
    return rendered_template
