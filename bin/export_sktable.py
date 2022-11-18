#!/usr/bin/env python3
# ------------------------------------------------------------------------------#
#  ParAutomatik: Automatic parametrisation of force fields                     #
#  Copyright (C) 2019 - 2022  ParAutomatik developers group                             #
#                                                                              #
#  See the LICENSE file for terms of usage and distribution.                   #
# ------------------------------------------------------------------------------#

"""Command line wrapper for the ccs_export_table script."""


import sys
from ccs.common.exceptions import ScriptError
import ccs.scripts.ccs_export_sktable as ccs_export_sktable


try:
    ccs_export_sktable.main()
except ScriptError as exc:
    sys.stderr.write("ScriptError: " + str(exc) + "\n")
    sys.exit(1)
