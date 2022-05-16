import os
import random

import yaml

def get_obj_path():
    return os.path.dirname(__file__).split(__file__)[0]
def get_rand_num(min,max):
    return random.randint(int(min),int(max))
def read_tag_yaml(path):
    print(get_obj_path()+path)
    with open(get_obj_path()+path,mode="r",encoding='utf-8') as f:
        value=yaml.load(stream=f,Loader=yaml.FullLoader)
    return value
