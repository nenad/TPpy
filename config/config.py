import json
import os

config_file = "../config.json"


def get(config_var):
    if not os.path.isfile(config_file):
        print "No config file found!"
        exit()

    json_config_object = json.loads(open(config_file, 'r'))
    return json_config_object[config_var]
