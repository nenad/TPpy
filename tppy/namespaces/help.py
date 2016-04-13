import colorama
import importlib
import inspect
import os
from colorama import Fore, Style

from tppy.integrations.git import time
from tppy.namespaces import story


def main():
    colorama.init()
    print Fore.GREEN + "Available commands:" + Style.RESET_ALL
    _print_namespaces()
    _print_integrations()


def _print_namespaces():
    currentdir = os.path.dirname(__file__)
    for f in os.listdir(currentdir):
        if os.path.isfile(os.path.join(currentdir, f)):
            if _is_valid_file(f):
                module_name = f[:-3]
                print Fore.GREEN + module_name + Style.RESET_ALL
                m = importlib.import_module('tppy.namespaces.' + module_name)
                _print_namespace(m)


def _print_namespace(namespace):
    functions_list = [o for o in inspect.getmembers(namespace, inspect.isfunction)]
    for function in functions_list:
        function_name = function[0]
        if not _is_valid_function(function_name):
            continue
        function_ref = function[1]
        function_doc = inspect.getdoc(function_ref)
        function_args = inspect.getargspec(function_ref).args
        print Fore.YELLOW + "\t" + function_name + "(" + ",".join(function_args) + ")" + Style.RESET_ALL

        if function_doc:
            _get_formatted_doc(inspect.getdoc(function_ref))

        print ""


def _print_integrations():
    print Fore.GREEN + "Plugin commands:" + Style.RESET_ALL
    current_dir = os.path.dirname(__file__)
    plugin_dir = os.path.join(current_dir, '../integrations')
    for filedir in os.listdir(plugin_dir):
        fulldir = os.path.join(plugin_dir, filedir)
        if os.path.isdir(fulldir):
            _print_integration(filedir, fulldir)


def _print_integration(plugin, fulldir):
    print ""
    print Fore.RED + plugin + Style.RESET_ALL
    for module in os.listdir(fulldir):
        filepath = os.path.join(fulldir, module)
        if os.path.isfile(filepath):
            if _is_valid_file(module):
                module_name = module[:-3]
                print Fore.GREEN + module_name + Style.RESET_ALL
                m = importlib.import_module('tppy.integrations.' + plugin + '.' + module_name)
                _print_namespace(m)


def _is_valid_function(function_name):
    return not function_name.startswith('_')


def _get_formatted_doc(doc):
    for line in doc.splitlines():
        if line.startswith(':param'):
            print Fore.BLUE + '\t' + line[7:] + Style.RESET_ALL
        else:
            print '\t' + line


def _is_valid_file(filemodule):
    return not filemodule.startswith('_') and not filemodule.endswith('pyc')
