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

        # Call namespaced class function with it's arguments
        argExpression = ''
        func = getattr(module, args[1])
        for i in range(0, len(args[2:])):
            argIndex = i + 2
            argExpression += 'args[' + argIndex.__str__() + '],'
        argExpression = argExpression[:-1]
        eval('func(' + argExpression + ')')


if __name__ == "__main__":
    main()
