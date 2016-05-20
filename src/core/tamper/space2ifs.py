#!/usr/bin/env python
# encoding: UTF-8

"""
This file is part of commix (@commixproject) tool.
Copyright (c) 2014-2016 Anastasios Stasinopoulos (@ancst).
https://github.com/stasinopoulos/commix

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

For more see the file 'readme/COPYING' for copying permission.
"""

from src.utils import settings

"""
The internal field separator (abbreviated IFS) refers to a variable 
which defines the character or characters used to separate a pattern 
into tokens for some operations.
"""

if settings.TARGET_OS == "unix":
  settings.TAMPER_SCRIPTS['space2ifs'] = True
  settings.WHITESPACE[0] = "${IFS}" 
else:
  warn_msg = "Windows target host(s), does not support the (Bash) $IFS variable."
  print settings.print_warning_msg(warn_msg)

#eof 