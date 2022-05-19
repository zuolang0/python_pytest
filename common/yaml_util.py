import os.path
import importlib

import jinja2
import yaml
import os.path
import inspect
def get_obj_path():
    return os.path.dirname(__file__).split('common')[0]

def render_yaml(yamlpath,**kwargs):
    path,filename=os.path.split(get_obj_path()+yamlpath)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or "./")).get_template(filename).render(**kwargs)

def all_function():
    debug_module = importlib.import_module("debug")
    all_function = inspect.getmembers(debug_module, inspect.isfunction)
    return dict(all_function)

def read_yaml(yamlpath):
    r= render_yaml(yamlpath,**all_function())
    return yaml.safe_load(r)
    # function_model=importlib.import_module("debug")
    # all_function=inspect.getmembers(function_model,inspect.isfunction())
    # return dict(all_function)
    # with open(get_obj_path()+yamlpath,mode="r",encoding='utf-8') as f:
    #     value=yaml.load(stream=f,Loader=yaml.FullLoader)
    #     return value

def load_yaml(yamlpath):
    with open(get_obj_path()+yamlpath,mode="r",encoding='utf-8') as f:
        value=yaml.load(stream=f,Loader=yaml.FullLoader)
        yield value
def write_yaml(data,yamlpath):
    with open(get_obj_path()+yamlpath,encoding='utf-8',mode='w') as f:
        yaml.dump(data,stream=f,allow_unicode=True)
