##
## Filename    : setup.py
## Description : Python distutils code for libSBML Python module
## Author(s)   : Michael Hucka, Ben Bornstein, Ben Kovitz
## Created     : 2004-04-02
## Revision    : $Id$
## Source      : $Source$
##
## Copyright 2004 California Institute of Technology and
## Japan Science and Technology Corporation.
##
## This library is free software; you can redistribute it and/or modify it
## under the terms of the GNU Lesser General Public License as published
## by the Free Software Foundation; either version 2.1 of the License, or
## any later version.
##
## This library is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY, WITHOUT EVEN THE IMPLIED WARRANTY OF
## MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.  The software and
## documentation provided hereunder is on an "as is" basis, and the
## California Institute of Technology and Japan Science and Technology
## Corporation have no obligations to provide maintenance, support,
## updates, enhancements or modifications.  In no event shall the
## California Institute of Technology or the Japan Science and Technology
## Corporation be liable to any party for direct, indirect, special,
## incidental or consequential damages, including lost profits, arising
## out of the use of this software and its documentation, even if the
## California Institute of Technology and/or Japan Science and Technology
## Corporation have been advised of the possibility of such damage.  See
## the GNU Lesser General Public License for more details.
##
## You should have received a copy of the GNU Lesser General Public License
## along with this library; if not, write to the Free Software Foundation,
## Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA.
##
## The original code contained here was initially developed by:
##
##     Michael Hucka, Ben Bornstein and Ben Kovitz
##     
##     The SBML Team
##     Control and Dynamical Systems, MC 107-81
##     California Institute of Technology
##     Pasadena, CA, 91125, USA
##
##     http://sbml.org
##     mailto:sbml-team@caltech.edu
##
## Contributor(s):
##   Michael Hucka <mhucka@caltech.edu> Rewrote this to use it for installation


# This currently is only used for doing installations of what's built using
# the makefiles.  It's not being used for compiling or doing other things
# that distutils is capable of.
#
# While Python Distutils works with SWIG and C, it does not currently
# work with SWIG and C++ (it doesn't generate the appropriate
# compilation and link commands).  This is a known bug with Distutils.

# -----------------------------------------------------------------------------
# First read the current version number of libSBML.
# -----------------------------------------------------------------------------

import shlex

varsfile = open("../../config/makefile-common-vars.mk")
vars     = {}

while True:
    line = varsfile.readline()
    if not line:
        break
    if line.strip() == '' or line[0] in '#':
        continue
    lexer = shlex.shlex(line)
    lexer.whitespace = lexer.whitespace + '\x0c='
    lexer.wordchars = lexer.wordchars + '/@.$()-{}'
    key = lexer.get_token()
    val = lexer.get_token()
    vars[key] = val

# -----------------------------------------------------------------------------
# Now do the Python setup part.
# -----------------------------------------------------------------------------

from distutils.core import setup, Extension
from distutils import sysconfig

setup(name             = "libsbml", 
      version          = vars.get("PACKAGE_VERSION"),
      description      = "LibSBML Python API",
      long_description = ("LibSBML is a library for reading, writing and "+
                          "manipulating the Systems Biology Markup Language "+
                          "(SBML).  It is written in ISO C and C++, supports "+
                          "SBML Levels 1 and 2, and runs on Linux, Microsoft "+
                          "Windows, and Apple MacOS X.  For more information "+
                          "about SBML, please see http://sbml.org."),
      license          = "LGPL",
      author           = "SBML Team",
      author_email     = vars.get("PACKAGE_BUGREPORT"),
      url              = "http://sbml.org",
      py_modules       = ["libsbml"],
      ext_modules      = [Extension("_libsbml", 
                                    ["libsbml.i", "libsbml.cpp"],
                                    include_dirs="../../src")],
      data_files       = [(sysconfig.get_python_lib(), ["_libsbml.so"])]
)
      


# filter(lambda s: s[-13:] == 'site-packages', sys.path)
