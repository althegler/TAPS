# -*- coding: utf-8 -*-
import os
from jinja2 import Environment, FileSystemLoader


THIS_DIR = os.path.dirname(os.path.abspath(__file__))

j_env = Environment(loader=FileSystemLoader(THIS_DIR + "/templates"), trim_blocks=True)

def templating():
    return j_env.get_template('cspm.j2').render(who={ 'name':'alberte' },
    list=["mig", "dig", "os"])
