#
# @file    TestL3Event.py
# @brief   L3 Event unit tests
#
# @author  Akiya Jouraku (Python conversion)
# @author  Sarah Keating 
#
# $Id$
# $HeadURL$
#
# This test file was converted from src/sbml/test/TestL3Event.c
# with the help of conversion sciprt (ctest_converter.pl).
#
#<!---------------------------------------------------------------------------
# This file is part of libSBML.  Please visit http://sbml.org for more
# information about SBML, and the latest version of libSBML.
#
# Copyright 2005-2009 California Institute of Technology.
# Copyright 2002-2005 California Institute of Technology and
#                     Japan Science and Technology Corporation.
# 
# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation.  A copy of the license agreement is provided
# in the file named "LICENSE.txt" included with this software distribution
# and also available online as http://sbml.org/software/libsbml/license.html
#--------------------------------------------------------------------------->*/
import sys
import unittest
import libsbml

class TestL3Event(unittest.TestCase):

  E = None

  def setUp(self):
    self.E = libsbml.Event(3,1)
    if (self.E == None):
      pass    
    pass  

  def tearDown(self):
    self.E = None
    pass  

  def test_L3_Event_NS(self):
    self.assert_( self.E.getNamespaces() != None )
    self.assert_( self.E.getNamespaces().getLength() == 1 )
    self.assert_((     "http://www.sbml.org/sbml/level3/version1/core" == self.E.getNamespaces().getURI(0) ))
    pass  

  def test_L3_Event_create(self):
    self.assert_( self.E.getTypeCode() == libsbml.SBML_EVENT )
    self.assert_( self.E.getMetaId() == "" )
    self.assert_( self.E.getNotes() == None )
    self.assert_( self.E.getAnnotation() == None )
    self.assert_( self.E.getId() == "" )
    self.assert_( self.E.getName() == "" )
    self.assert_( self.E.getUseValuesFromTriggerTime() == True )
    self.assertEqual( False, self.E.isSetId() )
    self.assertEqual( False, self.E.isSetName() )
    self.assertEqual( False, self.E.isSetUseValuesFromTriggerTime() )
    pass  

  def test_L3_Event_createWithNS(self):
    xmlns = libsbml.XMLNamespaces()
    xmlns.add( "http://www.sbml.org", "testsbml")
    sbmlns = libsbml.SBMLNamespaces(3,1)
    sbmlns.addNamespaces(xmlns)
    e = libsbml.Event(sbmlns)
    self.assert_( e.getTypeCode() == libsbml.SBML_EVENT )
    self.assert_( e.getMetaId() == "" )
    self.assert_( e.getNotes() == None )
    self.assert_( e.getAnnotation() == None )
    self.assert_( e.getLevel() == 3 )
    self.assert_( e.getVersion() == 1 )
    self.assert_( e.getNamespaces() != None )
    self.assert_( e.getNamespaces().getLength() == 2 )
    self.assert_( e.getId() == "" )
    self.assert_( e.getName() == "" )
    self.assert_( e.getUseValuesFromTriggerTime() == True )
    self.assertEqual( False, e.isSetId() )
    self.assertEqual( False, e.isSetName() )
    self.assertEqual( False, e.isSetUseValuesFromTriggerTime() )
    e = None
    pass  

  def test_L3_Event_free_NULL(self):
    pass  

  def test_L3_Event_hasRequiredAttributes(self):
    e = libsbml.Event(3,1)
    self.assertEqual( False, e.hasRequiredAttributes() )
    e.setUseValuesFromTriggerTime(True)
    self.assertEqual( True, e.hasRequiredAttributes() )
    e = None
    pass  

  def test_L3_Event_hasRequiredElements(self):
    e = libsbml.Event(3,1)
    self.assertEqual( False, e.hasRequiredElements() )
    t = libsbml.Trigger(3,1)
    e.setTrigger(t)
    self.assertEqual( True, e.hasRequiredElements() )
    e = None
    pass  

  def test_L3_Event_id(self):
    id =  "mitochondria";
    self.assertEqual( False, self.E.isSetId() )
    self.E.setId(id)
    self.assert_(( id == self.E.getId() ))
    self.assertEqual( True, self.E.isSetId() )
    if (self.E.getId() == id):
      pass    
    self.E.unsetId()
    self.assertEqual( False, self.E.isSetId() )
    if (self.E.getId() != None):
      pass    
    pass  

  def test_L3_Event_name(self):
    name =  "My_Favorite_Factory";
    self.assertEqual( False, self.E.isSetName() )
    self.E.setName(name)
    self.assert_(( name == self.E.getName() ))
    self.assertEqual( True, self.E.isSetName() )
    if (self.E.getName() == name):
      pass    
    self.E.unsetName()
    self.assertEqual( False, self.E.isSetName() )
    if (self.E.getName() != None):
      pass    
    pass  

  def test_L3_Event_useValuesFromTriggerTime(self):
    self.assert_( self.E.isSetUseValuesFromTriggerTime() == False )
    self.E.setUseValuesFromTriggerTime(True)
    self.assert_( self.E.getUseValuesFromTriggerTime() == True )
    self.assert_( self.E.isSetUseValuesFromTriggerTime() == True )
    self.E.setUseValuesFromTriggerTime(False)
    self.assert_( self.E.getUseValuesFromTriggerTime() == False )
    self.assert_( self.E.isSetUseValuesFromTriggerTime() == True )
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestL3Event))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)
