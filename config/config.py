import json
import os

import sys

config_file = os.path.dirname(__file__) + "/../config.json"
project_vars = None


def get(config_var):
    if not os.path.isfile(config_file):
        print "No config file found!"
        exit()

    file_contents = open(config_file, 'r').read()

    json_config_object = json.loads(file_contents)
    return json_config_object[config_var]


def loadProjectConfig():
    global project_vars
    path = sys.path[1] + "/.tppy.json"
    print path
    if os.path.isfile(path):
        project_vars = json.loads(open(path).read())


def get_project_var(var):
    return project_vars[var]


def set_project_var(var, value):
    global project_vars
    project_vars[var] = value
