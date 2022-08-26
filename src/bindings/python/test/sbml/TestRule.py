#
# @file    TestRule.py
# @brief   Rule unit tests
#
# @author  Akiya Jouraku (Python conversion)
# @author  Ben Bornstein 
# 
# ====== WARNING ===== WARNING ===== WARNING ===== WARNING ===== WARNING ======
#
# DO NOT EDIT THIS FILE.
#
# This file was generated automatically by converting the file located at
# src/sbml/test/TestRule.c
# using the conversion program dev/utilities/translateTests/translateTests.pl.
# Any changes made here will be lost the next time the file is regenerated.
#
# -----------------------------------------------------------------------------
# This file is part of libSBML.  Please visit http://sbml.org for more
# information about SBML, and the latest version of libSBML.
#
# Copyright 2005-2010 California Institute of Technology.
# Copyright 2002-2005 California Institute of Technology and
#                     Japan Science and Technology Corporation.
# 
# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation.  A copy of the license agreement is provided
# in the file named "LICENSE.txt" included with this software distribution
# and also available online as http://sbml.org/software/libsbml/license.html
# -----------------------------------------------------------------------------

import sys
import unittest
import libsbml


class TestRule(unittest.TestCase):

  global R
  R = None

  def setUp(self):
    self.R = libsbml.AlgebraicRule(2,4)
    if (self.R == None):
      pass    
    pass  

  def tearDown(self):
    _dummyList = [ self.R ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_Rule_init(self):
    self.assertTrue( self.R.getTypeCode() == libsbml.SBML_ALGEBRAIC_RULE )
    self.assertTrue( self.R.getMetaId() == "" )
    self.assertTrue( self.R.getNotes() == None )
    self.assertTrue( self.R.getAnnotation() == None )
    self.assertTrue( self.R.getFormula() == "" )
    self.assertTrue( self.R.getMath() == None )
    pass  

  def test_Rule_setFormula(self):
    formula =  "k1*X0";
    self.R.setFormula(formula)
    self.assertTrue(( formula == self.R.getFormula() ))
    self.assertTrue( self.R.isSetFormula() == True )
    if (self.R.getFormula() == formula):
      pass    
    self.R.setFormula(self.R.getFormula())
    self.assertTrue(( formula == self.R.getFormula() ))
    self.R.setFormula( "")
    self.assertTrue( self.R.isSetFormula() == False )
    if (self.R.getFormula() != None):
      pass    
    pass  

  def test_Rule_setMath(self):
    math = libsbml.parseFormula("1 + 1")
    self.R.setMath(math)
    self.assertTrue( self.R.getMath() != math )
    self.assertEqual( True, self.R.isSetMath() )
    self.R.setMath(self.R.getMath())
    self.assertTrue( self.R.getMath() != math )
    self.R.setMath(None)
    self.assertEqual( False, self.R.isSetMath() )
    if (self.R.getMath() != None):
      pass    
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestRule))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)
