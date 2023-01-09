#!/usr/bin/env python3
# ------------------------------------------------------------------------------#
#  ParAutomatik: Automatic parametrisation of force fields                     #
#  Copyright (C) 2019 - 2022  ParAutomatik developers group                             #
#                                                                              #
#  See the LICENSE file for terms of usage and distribution.                   #
# ------------------------------------------------------------------------------#

"""Command line wrapper for the build_db script."""


import sys
from parautomatik.common.exceptions import ScriptError
import parautomatik.scripts.build_db as build_db


try:
    build_db.main()
except ScriptError as exc:
    sys.stderr.write("ScriptError: " + str(exc) + "\n")
    sys.exit(1)
