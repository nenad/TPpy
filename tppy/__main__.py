import importlib
import sys


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    module = importlib.import_module('tppy.namespaces.' + args[0])
    func = getattr(module, args[1])
    func()

if __name__ == "__main__":
    main()
