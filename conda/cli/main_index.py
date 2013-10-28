# (c) 2012-2013 Continuum Analytics, Inc. / http://continuum.io
# All Rights Reserved
#
# conda is distributed under the terms of the BSD 3-clause license.
# Consult LICENSE.txt or http://opensource.org/licenses/BSD-3-Clause.

from __future__ import print_function, division, absolute_import


descr = "Creates (or updates) repodata.json in channel directories. (ADVANCED)"


def configure_parser(sub_parsers):
    p = sub_parsers.add_parser('index', description=descr, help=descr)

    p.add_argument(
        '-f', "--force",
        action = "store_true",
        help = "force reading all files",
    )
    p.add_argument(
        '-q', "--quiet",
        action = "store_true",
    )
    p.add_argument(
        'directories',
        metavar = 'DIRECTORIES',
        action = "store",
        nargs = '*',
    )
    p.set_defaults(func=execute)


def execute(args, parser):
    import os
    from os.path import abspath

    from conda.builder.index import update_index


    if len(args.directories) == 0:
        dir_paths = [os.getcwd()]
    else:
        dir_paths = [abspath(p) for p in args.directories]

    for path in dir_paths:
        update_index(path, verbose=not args.quiet, force=args.force)
