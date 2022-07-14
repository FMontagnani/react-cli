import os
import click

from src.templates.templates import TemplateFactory

@click.command()
@click.option('--component', '-c', help='Name of the Component you wish to create', required=True)
@click.option('--template', '-t', help='Name of the Template you want to use.', required=False, default='default')
def reactcli(component, template):
    '''
    Creates a React component folder given a defined template
    '''
    os.mkdir(component)

    component_maker = TemplateFactory(template)
    component_maker(component)
