#!/usr/bin/env python3
#------------------------------------------------------------------------------#
#  ParAutomatik: Automatic parametrisation of force fields                     #
#  Copyright (C) 2019 - 2022  ParAutomatik developers group                             #
#                                                                              #
#  See the LICENSE file for terms of usage and distribution.                   #
#------------------------------------------------------------------------------#

"""Common exceptions needed by the CCS project."""


class ScriptError(Exception):
    """Exception thrown by the command line scripts."""