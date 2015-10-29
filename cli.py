import logging
import argparse

from settings import TASKS
from utils.moduleimport import module_import


logger = logging.getLogger('cli')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='command line interface')

    parser.add_argument('-T', '--task', type=str,
                        help='run cookie: {}'.format(TASKS.keys()))

    args = parser.parse_args()

    if args.task:
        cls = module_import(TASKS[args.task])
        print(cls.__doc__)
        cls()
    else:
        print TASKS.keys()
