import importlib
import sys
import os

from configuration import config


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    currentDir = os.path.dirname(__file__)
    config.loadProjectConfig()

    if len(args) == 0:
        print "You must specify module"
    elif len(args) == 1:
        module = importlib.import_module('tppy.namespaces.' + args[0])
        func = getattr(module, 'main')
        func()
    else:
        module = None
        startingParam = 1
        if os.path.isfile(os.path.join(currentDir, 'integrations/' + args[0] + '/' + args[1] + '.py')):
            module = importlib.import_module('tppy.integrations.' + args[0] + '.' + args[1])
            startingParam = 2
        else:
            module = importlib.import_module('tppy.namespaces.' + args[0])

        # Call namespaced class function with it's arguments
        argExpression = ''
        func = getattr(module, args[startingParam])
        for i in range(0, len(args[startingParam + 1:])):
            argIndex = i + startingParam + 1
            argExpression += 'args[' + argIndex.__str__() + '],'
        argExpression = argExpression[:-1]
        try:
            eval('func(' + argExpression + ')')
        except KeyboardInterrupt:
            print "\nExited"


if __name__ == "__main__":
    main()
