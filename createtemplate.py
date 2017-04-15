#!/usr/bin/env python
 
import os
import json
from pprint import pprint
from jinja2 import Environment, FileSystemLoader
 
PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)
 
 
def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)
 
 
def create_email_html():
    fname = "emailoutput.html"
    urls = ['http://example.com/1', 'http://example.com/2', 'http://example.com/3']
    context = {
        'urls': urls
    }

    with open('diff.json') as data_file:
        data = json.load(data_file)

    context = data
    title =  list(data["vpcs"].keys())[0]
    info = data["vpcs"][title]
    context["title"] = title
    context["info"] = info
    pprint(data['vpcs'][title])

    with open(fname, 'w') as f:
        html = render_template('email.html', context)
        f.write(html)
        f.close() 




def main():
    create_email_html()
 
########################################
 
if __name__ == "__main__":
    main()
