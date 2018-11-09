# -*- coding: utf-8 -*-
import os
from jinja2 import Environment, FileSystemLoader


THIS_DIR = os.path.dirname(os.path.abspath(__file__))

j_env = Environment(loader=FileSystemLoader(THIS_DIR + "/templates"),
        trim_blocks=True, lstrip_blocks=True)
j_test_env = Environment(loader=FileSystemLoader(THIS_DIR + "/templates/minimal"),
             trim_blocks=True, lstrip_blocks=True)

def templating(data):
    return j_env.get_template('cspm.j2').render(data=data)


def test_templating(data):
    return j_test_env.get_template('cspm.j2').render(data=data)
