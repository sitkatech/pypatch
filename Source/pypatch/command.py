#!/usr/bin/env python
"""
    Wrapper around patch.py to allow command line execution and direct patching of python modules.

    Copyright: (c) 2013 Sitka Technology Group
    Author: Stryder Crown

    Available under the terms of MIT license (http://opensource.org/licenses/MIT as of 7/27/13)

    Project home: http://github.com/sitkatech/pypatch
"""

from __future__ import print_function

import sys
import argparse

import os
import traceback

from . import patch as pypatch


def apply_patch(args, debug=True):
    """
    Applies the contents of a unified diff file to a python module.
    """
    if debug:
        from logging import config

        logging_config = {
            'version': 1,
            'disable_existing_loggers': True,
            'formatters': {
                'simple': {
                    'format': '%(message)s'
                }
            },
            'handlers': {
                'console': {
                    'level': debug,
                    'class': 'logging.StreamHandler',
                    'formatter': 'simple'
                }
            },
            'loggers': {
                'pypatch.patch': {
                    'handlers': ['console'],
                    'level': debug,
                    'propagate': False
                }
            }
        }

        config.dictConfig(logging_config)

    try:
        module_path = get_module_path(args.module)
    except ImportError:
        msg = "Unable to locate module '%s'. Are you sure its installed?" % args.module
        raise argparse.ArgumentTypeError(msg)

    try:
        if not os.path.exists(args.patch_file):
            print("Unable to locate patch file '%s'" % args.patch_file)
            return

        patch_set = pypatch.fromfile(args.patch_file)
        os.chdir(module_path)
        result = patch_set.apply()

    except Exception as err:
        print("An unexpected error has occurred: %s" % err)
        traceback.print_exc()
        if hasattr(err, 'message'):
            print(err.message)
        sys.exit(1)
    if result:
        print("Module '%s' patched successfully!" % args.module)
    else:
        print("Unable to apply patch. Please verify the patch contents and python module.")
        sys.exit(1)


def get_module_path(module_name):
    """Gets the module path without importing anything. Avoids conflicts with package dependencies."""
    import imp
    path = sys.path
    for name in module_name.split('.'):
        file_pointer, path, desc = imp.find_module(name, path)
        path = [path, ]
        if file_pointer is not None:
            file_pointer.close()

    return path[0]


def main():
    """Parse args and execute function"""

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # Arguments for the apply action
    apply_patch_parser = subparsers.add_parser('apply', description='Apply a patch file to a python module.')

    apply_patch_parser.add_argument('patch_file',
                                    metavar='patch file',
                                    help='A unified diff/patch file to be applied to the python module.',
                                    type=str)

    apply_patch_parser.add_argument('module',
                                    metavar='python module',
                                    help='The name of the python module to be patched.',
                                    type=str)

    apply_patch_parser.add_argument('--debug',
                                    default='DEBUG',
                                    help='use debug logging',)

    apply_patch_parser.set_defaults(func=apply_patch)
    args = parser.parse_args()
    args.func(args, debug=args.debug.upper())


if __name__ == "__main__":
    main()
