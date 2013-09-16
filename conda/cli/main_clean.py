# (c) 2012-2013 Continuum Analytics, Inc. / http://continuum.io
# All Rights Reserved
#
# conda is distributed under the terms of the BSD 3-clause license.
# Consult LICENSE.txt or http://opensource.org/licenses/BSD-3-Clause.
from __future__ import print_function, division, absolute_import

from argparse import RawDescriptionHelpFormatter
import os
import sys

from conda.cli import common
import conda.config as config
from conda.utils import human_bytes

descr = """
Remove unused packages and caches
"""

example = """
examples:
    conda clean --tarballs
"""

def configure_parser(sub_parsers):
    p = sub_parsers.add_parser(
        'clean',
        formatter_class = RawDescriptionHelpFormatter,
        description = descr,
        help = descr,
        epilog = example,
    )

    common.add_parser_yes(p)
    p.add_argument(
        "-l", "--lock",
        action = "store_true",
        help = "remove all conda lock files",
    )
    p.add_argument(
        "-t", "--tarballs",
        action = "store_true",
        help = "remove cached package tarballs",
    )
    p.set_defaults(func=execute)


def rm_lock():
    from os.path import join

    from conda.lock import LOCKFN

    for root, dirs, files in os.walk(sys.prefix):
        for dn in dirs:
            if dn == LOCKFN:
                path = join(root, dn)
                print('removing: %s' % path)
                os.rmdir(path)


def rm_tarballs(args):
    from os.path import join, getsize

    print('Cache location: %s' % config.pkgs_dir)

    rmlist = []
    for fn in os.listdir(config.pkgs_dir):
        if fn.endswith('.tar.bz2') or fn.endswith('.tar.bz2.part'):
            rmlist.append(fn)

    if not rmlist:
        print("There are no tarballs to remove")
        sys.exit(0)

    print("Will remove the following tarballs:")
    print()
    totalsize = 0
    maxlen = len(max(rmlist, key=lambda x: len(str(x))))
    fmt = "%-40s %10s"
    for fn in rmlist:
        size = getsize(join(config.pkgs_dir, fn))
        totalsize += size
        print(fmt % (fn, human_bytes(size)))
    print('-' * (maxlen + 2 + 10))
    print(fmt % ('Total:', human_bytes(totalsize)))
    print()

    common.confirm_yn(args)

    for fn in rmlist:
        print("removing %s" % fn)
        os.unlink(os.path.join(config.pkgs_dir, fn))


def execute(args, parser):
    if args.lock:
        rm_lock()
    if args.tarballs:
        rm_tarballs(args)
