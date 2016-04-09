import importlib
import sys
import os

from configuration import config


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    config.loadProjectConfig()

    if len(args) == 0:
        print "You must specify module"
    elif len(args) == 1:
        module = importlib.import_module('tppy.namespaces.' + args[0])
        func = getattr(module, 'main')
        func()
    else:
        module = importlib.import_module('tppy.namespaces.' + args[0])
        func = getattr(module, args[1])
        if len(args[2:]) == 1:
            func(args[2])
        elif len(args[2:]) == 2:
            func(args[2], args[3])
        elif len(args[2:]) == 3:
            func(args[2], args[3], args[4])
        else:
            func()


if __name__ == "__main__":
    main()
