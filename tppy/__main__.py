import importlib
import sys

from config import config


def main(args=None):
    print sys.argv[1:]

    if args is None:
        args = sys.argv[1:]

    config.loadProjectConfig()

    module = importlib.import_module('tppy.namespaces.' + args[0])
    func = getattr(module, args[1])
    if len(args[2:]) > 0:
        func(args[2])
    else:
        func()


if __name__ == "__main__":
    main()
