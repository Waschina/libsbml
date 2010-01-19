#
# @file    TestL3Compartment.py
# @brief   L3 Compartment unit tests
#
# @author  Akiya Jouraku (Python conversion)
# @author  Sarah Keating 
#
# $Id$
# $HeadURL$
#
# This test file was converted from src/sbml/test/TestL3Compartment.c
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

def isnan(x):
  return (x != x)
  pass
class TestL3Compartment(unittest.TestCase):

  C = None

  def setUp(self):
    self.C = libsbml.Compartment(3,1)
    if (self.C == None):
      pass    
    pass  

  def tearDown(self):
    self.C = None
    pass  

  def test_L3_Compartment_NS(self):
    self.assert_( self.C.getNamespaces() != None )
    self.assert_( self.C.getNamespaces().getLength() == 1 )
    self.assert_((     "http://www.sbml.org/sbml/level3/version1/core" == self.C.getNamespaces().getURI(0) ))
    pass  

  def test_L3_Compartment_constant(self):
    self.assert_( self.C.isSetConstant() == False )
    self.C.setConstant(True)
    self.assert_( self.C.getConstant() == True )
    self.assert_( self.C.isSetConstant() == True )
    self.C.setConstant(False)
    self.assert_( self.C.getConstant() == False )
    self.assert_( self.C.isSetConstant() == True )
    pass  

  def test_L3_Compartment_create(self):
    self.assert_( self.C.getTypeCode() == libsbml.SBML_COMPARTMENT )
    self.assert_( self.C.getMetaId() == "" )
    self.assert_( self.C.getNotes() == None )
    self.assert_( self.C.getAnnotation() == None )
    self.assert_( self.C.getId() == "" )
    self.assert_( self.C.getName() == "" )
    self.assert_( self.C.getUnits() == "" )
    self.assert_( self.C.getOutside() == "" )
    self.assertEqual( True, isnan(self.C.getSpatialDimensionsAsDouble()) )
    self.assertEqual( True, isnan(self.C.getVolume()) )
    self.assert_( self.C.getConstant() == True )
    self.assertEqual( False, self.C.isSetId() )
    self.assertEqual( False, self.C.isSetSpatialDimensions() )
    self.assertEqual( False, self.C.isSetName() )
    self.assertEqual( False, self.C.isSetSize() )
    self.assertEqual( False, self.C.isSetVolume() )
    self.assertEqual( False, self.C.isSetUnits() )
    self.assertEqual( False, self.C.isSetOutside() )
    self.assertEqual( False, self.C.isSetConstant() )
    pass  

  def test_L3_Compartment_createWithNS(self):
    xmlns = libsbml.XMLNamespaces()
    xmlns.add( "http://www.sbml.org", "testsbml")
    sbmlns = libsbml.SBMLNamespaces(3,1)
    sbmlns.addNamespaces(xmlns)
    c = libsbml.Compartment(sbmlns)
    self.assert_( c.getTypeCode() == libsbml.SBML_COMPARTMENT )
    self.assert_( c.getMetaId() == "" )
    self.assert_( c.getNotes() == None )
    self.assert_( c.getAnnotation() == None )
    self.assert_( c.getLevel() == 3 )
    self.assert_( c.getVersion() == 1 )
    self.assert_( c.getNamespaces() != None )
    self.assert_( c.getNamespaces().getLength() == 2 )
    self.assert_( c.getId() == "" )
    self.assert_( c.getName() == "" )
    self.assert_( c.getUnits() == "" )
    self.assert_( c.getOutside() == "" )
    self.assertEqual( True, isnan(c.getSpatialDimensionsAsDouble()) )
    self.assertEqual( True, isnan(c.getVolume()) )
    self.assert_( c.getConstant() == True )
    self.assertEqual( False, c.isSetId() )
    self.assertEqual( False, c.isSetSpatialDimensions() )
    self.assertEqual( False, c.isSetName() )
    self.assertEqual( False, c.isSetSize() )
    self.assertEqual( False, c.isSetVolume() )
    self.assertEqual( False, c.isSetUnits() )
    self.assertEqual( False, c.isSetOutside() )
    self.assertEqual( False, c.isSetConstant() )
    c = None
    pass  

  def test_L3_Compartment_free_NULL(self):
    pass  

  def test_L3_Compartment_hasRequiredAttributes(self):
    c = libsbml.Compartment(3,1)
    self.assertEqual( False, c.hasRequiredAttributes() )
    c.setId( "id")
    self.assertEqual( False, c.hasRequiredAttributes() )
    c.setConstant(False)
    self.assertEqual( True, c.hasRequiredAttributes() )
    c = None
    pass  

  def test_L3_Compartment_id(self):
    id =  "mitochondria";
    self.assertEqual( False, self.C.isSetId() )
    self.C.setId(id)
    self.assert_(( id == self.C.getId() ))
    self.assertEqual( True, self.C.isSetId() )
    if (self.C.getId() == id):
      pass    
    pass  

  def test_L3_Compartment_name(self):
    name =  "My_Favorite_Factory";
    self.assertEqual( False, self.C.isSetName() )
    self.C.setName(name)
    self.assert_(( name == self.C.getName() ))
    self.assertEqual( True, self.C.isSetName() )
    if (self.C.getName() == name):
      pass    
    self.C.unsetName()
    self.assertEqual( False, self.C.isSetName() )
    if (self.C.getName() != None):
      pass    
    pass  

  def test_L3_Compartment_size(self):
    size = 0.2
    self.assertEqual( False, self.C.isSetSize() )
    self.assertEqual( True, isnan(self.C.getSize()) )
    self.C.setSize(size)
    self.assert_( self.C.getSize() == size )
    self.assertEqual( True, self.C.isSetSize() )
    self.C.unsetSize()
    self.assertEqual( False, self.C.isSetSize() )
    self.assertEqual( True, isnan(self.C.getSize()) )
    pass  

  def test_L3_Compartment_spatialDimensions(self):
    self.assertEqual( False, self.C.isSetSpatialDimensions() )
    self.assertEqual( True, isnan(self.C.getSpatialDimensionsAsDouble()) )
    self.C.setSpatialDimensions(1.5)
    self.assertEqual( True, self.C.isSetSpatialDimensions() )
    self.assert_( self.C.getSpatialDimensionsAsDouble() == 1.5 )
    self.C.unsetSpatialDimensions()
    self.assertEqual( False, self.C.isSetSpatialDimensions() )
    self.assertEqual( True, isnan(self.C.getSpatialDimensionsAsDouble()) )
    pass  

  def test_L3_Compartment_units(self):
    units =  "volume";
    self.assertEqual( False, self.C.isSetUnits() )
    self.C.setUnits(units)
    self.assert_(( units == self.C.getUnits() ))
    self.assertEqual( True, self.C.isSetUnits() )
    if (self.C.getUnits() == units):
      pass    
    self.C.unsetUnits()
    self.assertEqual( False, self.C.isSetUnits() )
    if (self.C.getUnits() != None):
      pass    
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestL3Compartment))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)
