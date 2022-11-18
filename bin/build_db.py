#!/usr/bin/env python3
#------------------------------------------------------------------------------#
#  ParAutomatik: Automatic parametrisation of force fields                     #
#  Copyright (C) 2019 - 2022  ParAutomatik developers group                             #
#                                                                              #
#  See the LICENSE file for terms of usage and distribution.                   #
#------------------------------------------------------------------------------#

'''Command line wrapper for the build_db script.'''


import sys
from ccs.common.exceptions import ScriptError
import ccs.scripts.ccs_build_db as ccs_build_db


try:
    ccs_build_db.main()
except ScriptError as exc:
    sys.stderr.write('ScriptError: ' + str(exc) + '\n')
    sys.exit(1)