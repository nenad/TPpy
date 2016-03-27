import json
import os

config_file = os.path.dirname(__file__) + "/../config.json"


def get(config_var):
    if not os.path.isfile(config_file):
        print "No config file found!"
        exit()

    file_contents = open(config_file, 'r').read()

    json_config_object = json.loads(file_contents)
    return json_config_object[config_var]
