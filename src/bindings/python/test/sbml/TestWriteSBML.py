#
# @file    TestWriteSBML.py
# @brief   Write SBML unit tests
#
# @author  Akiya Jouraku (Python conversion)
# @author  Ben Bornstein 
#
# $Id$
# $HeadURL$
#
# This test file was converted from src/sbml/test/TestWriteSBML.cpp
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

def util_NaN():
  z = 1e300
  z = z * z

  return z - z

def util_PosInf():
  z = 1e300
  z = z * z

  return z

def util_NegInf():
  z = 1e300
  z = z * z

  return -z 

def wrapString(s):
  return s
  pass

def LV_L1v1():
  return "level=\"1\" version=\"1\">\n"
  pass

def LV_L1v2():
  return "level=\"1\" version=\"2\">\n"
  pass

def LV_L2v1():
  return "level=\"2\" version=\"1\">\n"
  pass

def LV_L2v2():
  return "level=\"2\" version=\"2\">\n"
  pass

def LV_L2v3():
  return "level=\"2\" version=\"3\">\n"
  pass

def NS_L1():
  return "xmlns=\"http://www.sbml.org/sbml/level1\" "
  pass

def NS_L2v1():
  return "xmlns=\"http://www.sbml.org/sbml/level2\" "
  pass

def NS_L2v2():
  return "xmlns=\"http://www.sbml.org/sbml/level2/version2\" "
  pass

def NS_L2v3():
  return "xmlns=\"http://www.sbml.org/sbml/level2/version3\" "
  pass

def SBML_END():
  return "</sbml>\n"
  pass

def SBML_START():
  return "<sbml "
  pass

def XML_START():
  return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
  pass

def wrapSBML_L1v1(s):
  r = XML_START()
  r += SBML_START()
  r += NS_L1()
  r += LV_L1v1()
  r += s
  r += SBML_END()
  return r
  pass

def wrapSBML_L1v2(s):
  r = XML_START()
  r += SBML_START()
  r += NS_L1()
  r += LV_L1v2()
  r += s
  r += SBML_END()
  return r
  pass

def wrapSBML_L2v1(s):
  r = XML_START()
  r += SBML_START()
  r += NS_L2v1()
  r += LV_L2v1()
  r += s
  r += SBML_END()
  return r
  pass

def wrapSBML_L2v2(s):
  r = XML_START()
  r += SBML_START()
  r += NS_L2v2()
  r += LV_L2v2()
  r += s
  r += SBML_END()
  return r
  pass

def wrapSBML_L2v3(s):
  r = XML_START()
  r += SBML_START()
  r += NS_L2v3()
  r += LV_L2v3()
  r += s
  r += SBML_END()
  return r
  pass

def wrapXML(s):
  r = XML_START()
  r += s
  return r
  pass

class TestWriteSBML(unittest.TestCase):

  S = None
  D = None

  def equals(self, *x):
    if len(x) == 2:
      return x[0] == x[1]
    elif len(x) == 1:
      return x[0] == self.OSS.str()

  def setUp(self):
    self.D = libsbml.SBMLDocument()
    self.S = 0
    pass  

  def tearDown(self):
    self.D = None
    self.S = None
    pass  

  def test_SBMLWriter_create(self):
    w = libsbml.SBMLWriter()
    self.assert_( w != None )
    w = None
    pass  

  def test_SBMLWriter_setProgramName(self):
    w = libsbml.SBMLWriter()
    self.assert_( w != None )
    i = w.setProgramName( "sss")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    i = w.setProgramName("")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    w = None
    pass  

  def test_SBMLWriter_setProgramVersion(self):
    w = libsbml.SBMLWriter()
    self.assert_( w != None )
    i = w.setProgramVersion( "sss")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    i = w.setProgramVersion("")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    w = None
    pass  

  def test_WriteSBML_AlgebraicRule(self):
    self.D.setLevelAndVersion(1,1,False)
    expected =  "<algebraicRule formula=\"x + 1\"/>";
    r = self.D.createModel().createAlgebraicRule()
    r.setFormula("x + 1")
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_AlgebraicRule_L2v1(self):
    self.D.setLevelAndVersion(2,1,False)
    expected = wrapString("<algebraicRule>\n" + 
    "  <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "    <apply>\n" + 
    "      <plus/>\n" + 
    "      <ci> x </ci>\n" + 
    "      <cn type=\"integer\"> 1 </cn>\n" + 
    "    </apply>\n" + 
    "  </math>\n" + 
    "</algebraicRule>")
    r = self.D.createModel().createAlgebraicRule()
    r.setFormula("x + 1")
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_AlgebraicRule_L2v2(self):
    self.D.setLevelAndVersion(2,2,False)
    expected = wrapString("<algebraicRule sboTerm=\"SBO:0000004\">\n" + 
    "  <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "    <apply>\n" + 
    "      <plus/>\n" + 
    "      <ci> x </ci>\n" + 
    "      <cn type=\"integer\"> 1 </cn>\n" + 
    "    </apply>\n" + 
    "  </math>\n" + 
    "</algebraicRule>")
    r = self.D.createModel().createAlgebraicRule()
    r.setFormula("x + 1")
    r.setSBOTerm(4)
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_Compartment(self):
    self.D.setLevelAndVersion(1,2,False)
    expected =  "<compartment name=\"A\" volume=\"2.1\" outside=\"B\"/>";
    c = self.D.createModel().createCompartment()
    c.setId("A")
    c.setSize(2.1)
    c.setOutside("B")
    self.assertEqual( True, self.equals(expected,c.toSBML()) )
    pass  

  def test_WriteSBML_CompartmentType(self):
    self.D.setLevelAndVersion(2,2,False)
    expected =  "<compartmentType id=\"ct\"/>";
    ct = self.D.createModel().createCompartmentType()
    ct.setId("ct")
    ct.setSBOTerm(4)
    self.assertEqual( True, self.equals(expected,ct.toSBML()) )
    pass  

  def test_WriteSBML_CompartmentType_withSBO(self):
    self.D.setLevelAndVersion(2,3,False)
    expected =  "<compartmentType id=\"ct\" sboTerm=\"SBO:0000004\"/>";
    ct = self.D.createModel().createCompartmentType()
    ct.setId("ct")
    ct.setSBOTerm(4)
    self.assertEqual( True, self.equals(expected,ct.toSBML()) )
    pass  

  def test_WriteSBML_CompartmentVolumeRule(self):
    self.D.setLevelAndVersion(1,1,False)
    expected = wrapString("<compartmentVolumeRule " + "formula=\"v + c\" type=\"rate\" compartment=\"c\"/>")
    self.D.createModel()
    self.D.getModel().createCompartment().setId("c")
    r = self.D.getModel().createRateRule()
    r.setVariable("c")
    r.setFormula("v + c")
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_CompartmentVolumeRule_L2v1(self):
    self.D.setLevelAndVersion(2,1,False)
    expected = wrapString("<assignmentRule variable=\"c\">\n" + 
    "  <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "    <apply>\n" + 
    "      <plus/>\n" + 
    "      <ci> v </ci>\n" + 
    "      <ci> c </ci>\n" + 
    "    </apply>\n" + 
    "  </math>\n" + 
    "</assignmentRule>")
    self.D.createModel()
    self.D.getModel().createCompartment().setId("c")
    r = self.D.getModel().createAssignmentRule()
    r.setVariable("c")
    r.setFormula("v + c")
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_CompartmentVolumeRule_L2v2(self):
    self.D.setLevelAndVersion(2,2,False)
    expected = wrapString("<assignmentRule variable=\"c\" sboTerm=\"SBO:0000005\">\n" + 
    "  <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "    <apply>\n" + 
    "      <plus/>\n" + 
    "      <ci> v </ci>\n" + 
    "      <ci> c </ci>\n" + 
    "    </apply>\n" + 
    "  </math>\n" + 
    "</assignmentRule>")
    self.D.createModel()
    self.D.getModel().createCompartment().setId("c")
    r = self.D.getModel().createAssignmentRule()
    r.setVariable("c")
    r.setFormula("v + c")
    r.setSBOTerm(5)
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_CompartmentVolumeRule_defaults(self):
    self.D.setLevelAndVersion(1,1,False)
    expected =  "<compartmentVolumeRule formula=\"v + c\" compartment=\"c\"/>";
    self.D.createModel()
    self.D.getModel().createCompartment().setId("c")
    r = self.D.getModel().createAssignmentRule()
    r.setVariable("c")
    r.setFormula("v + c")
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_Compartment_L2v1(self):
    self.D.setLevelAndVersion(2,1,False)
    expected =  "<compartment id=\"M\" spatialDimensions=\"2\" size=\"2.5\"/>";
    c = self.D.createModel().createCompartment()
    c.setId("M")
    c.setSize(2.5)
    c.setSpatialDimensions(2)
    self.assertEqual( True, self.equals(expected,c.toSBML()) )
    pass  

  def test_WriteSBML_Compartment_L2v1_constant(self):
    self.D.setLevelAndVersion(2,1,False)
    expected =  "<compartment id=\"cell\" size=\"1.2\" constant=\"false\"/>";
    c = self.D.createModel().createCompartment()
    c.setId("cell")
    c.setSize(1.2)
    c.setConstant(False)
    self.assertEqual( True, self.equals(expected,c.toSBML()) )
    pass  

  def test_WriteSBML_Compartment_L2v1_unsetSize(self):
    self.D.setLevelAndVersion(2,1,False)
    expected =  "<compartment id=\"A\"/>";
    c = self.D.createModel().createCompartment()
    c.setId("A")
    c.unsetSize()
    self.assertEqual( True, self.equals(expected,c.toSBML()) )
    pass  

  def test_WriteSBML_Compartment_L2v2_compartmentType(self):
    self.D.setLevelAndVersion(2,2,False)
    expected =  "<compartment id=\"cell\" compartmentType=\"ct\"/>";
    c = self.D.createModel().createCompartment()
    c.setId("cell")
    c.setCompartmentType("ct")
    self.assertEqual( True, self.equals(expected,c.toSBML()) )
    pass  

  def test_WriteSBML_Compartment_L2v3_SBO(self):
    self.D.setLevelAndVersion(2,3,False)
    expected =  "<compartment id=\"cell\" sboTerm=\"SBO:0000005\"/>";
    c = self.D.createModel().createCompartment()
    c.setId("cell")
    c.setSBOTerm(5)
    self.assertEqual( True, self.equals(expected,c.toSBML()) )
    pass  

  def test_WriteSBML_Compartment_unsetVolume(self):
    self.D.setLevelAndVersion(1,2,False)
    expected =  "<compartment name=\"A\"/>";
    c = self.D.createModel().createCompartment()
    c.setId("A")
    c.unsetVolume()
    self.assertEqual( True, self.equals(expected,c.toSBML()) )
    pass  

  def test_WriteSBML_Constraint(self):
    self.D.setLevelAndVersion(2,2,False)
    expected =  "<constraint sboTerm=\"SBO:0000064\"/>";
    ct = self.D.createModel().createConstraint()
    ct.setSBOTerm(64)
    self.assertEqual( True, self.equals(expected,ct.toSBML()) )
    pass  

  def test_WriteSBML_Constraint_full(self):
    self.D.setLevelAndVersion(2,2,False)
    expected = wrapString("<constraint sboTerm=\"SBO:0000064\">\n" + 
    "  <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "    <apply>\n" + 
    "      <leq/>\n" + 
    "      <ci> P1 </ci>\n" + 
    "      <ci> t </ci>\n" + 
    "    </apply>\n" + 
    "  </math>\n" + 
    "  <message>\n" + 
    "    <p xmlns=\"http://www.w3.org/1999/xhtml\"> Species P1 is out of range </p>\n" + 
    "  </message>\n" + 
    "</constraint>")
    c = self.D.createModel().createConstraint()
    node = libsbml.parseFormula("leq(P1,t)")
    c.setMath(node)
    c.setSBOTerm(64)
    text = libsbml.XMLNode.convertStringToXMLNode(" Species P1 is out of range ")
    triple = libsbml.XMLTriple("p", "http://www.w3.org/1999/xhtml", "")
    att = libsbml.XMLAttributes()
    xmlns = libsbml.XMLNamespaces()
    xmlns.add("http://www.w3.org/1999/xhtml")
    p = libsbml.XMLNode(triple,att,xmlns)
    p.addChild(text)
    triple1 = libsbml.XMLTriple("message", "", "")
    att1 = libsbml.XMLAttributes()
    message = libsbml.XMLNode(triple1,att1)
    message.addChild(p)
    c.setMessage(message)
    self.assertEqual( True, self.equals(expected,c.toSBML()) )
    pass  

  def test_WriteSBML_Constraint_math(self):
    self.D.setLevelAndVersion(2,2,False)
    expected = wrapString("<constraint>\n" + 
    "  <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "    <apply>\n" + 
    "      <leq/>\n" + 
    "      <ci> P1 </ci>\n" + 
    "      <ci> t </ci>\n" + 
    "    </apply>\n" + 
    "  </math>\n" + 
    "</constraint>")
    c = self.D.createModel().createConstraint()
    node = libsbml.parseFormula("leq(P1,t)")
    c.setMath(node)
    self.assertEqual( True, self.equals(expected,c.toSBML()) )
    pass  

  def test_WriteSBML_Event(self):
    self.D.setLevelAndVersion(2,1,False)
    expected =  "<event id=\"e\"/>";
    e = self.D.createModel().createEvent()
    e.setId("e")
    self.assertEqual( True, self.equals(expected,e.toSBML()) )
    pass  

  def test_WriteSBML_Event_WithSBO(self):
    self.D.setLevelAndVersion(2,3,False)
    expected =  "<event id=\"e\" sboTerm=\"SBO:0000076\"/>";
    e = self.D.createModel().createEvent()
    e.setId("e")
    e.setSBOTerm(76)
    self.assertEqual( True, self.equals(expected,e.toSBML()) )
    pass  

  def test_WriteSBML_Event_WithUseValuesFromTriggerTime(self):
    expected =  "<event id=\"e\" useValuesFromTriggerTime=\"false\"/>";
    self.D.setLevelAndVersion(2,4,False)
    e = self.D.createModel().createEvent()
    e.setId("e")
    e.setUseValuesFromTriggerTime(False)
    self.assertEqual( True, self.equals(expected,e.toSBML()) )
    pass  

  def test_WriteSBML_Event_both(self):
    expected = wrapString("<event id=\"e\">\n" + 
    "  <trigger>\n" + 
    "    <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "      <apply>\n" + 
    "        <leq/>\n" + 
    "        <ci> P1 </ci>\n" + 
    "        <ci> t </ci>\n" + 
    "      </apply>\n" + 
    "    </math>\n" + 
    "  </trigger>\n" + 
    "  <delay>\n" + 
    "    <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "      <cn type=\"integer\"> 5 </cn>\n" + 
    "    </math>\n" + 
    "  </delay>\n" + 
    "</event>")
    self.D.setLevelAndVersion(2,1,False)
    e = self.D.createModel().createEvent()
    e.setId("e")
    node1 = libsbml.parseFormula("leq(P1,t)")
    t = libsbml.Trigger( 2,1 )
    t.setMath(node1)
    node = libsbml.parseFormula("5")
    d = libsbml.Delay( 2,1 )
    d.setMath(node)
    e.setDelay(d)
    e.setTrigger(t)
    self.assertEqual( True, self.equals(expected,e.toSBML()) )
    pass  

  def test_WriteSBML_Event_delay(self):
    expected = wrapString("<event id=\"e\">\n" + 
    "  <delay>\n" + 
    "    <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "      <cn type=\"integer\"> 5 </cn>\n" + 
    "    </math>\n" + 
    "  </delay>\n" + 
    "</event>")
    self.D.setLevelAndVersion(2,1,False)
    e = self.D.createModel().createEvent()
    e.setId("e")
    node = libsbml.parseFormula("5")
    d = libsbml.Delay( 2,1 )
    d.setMath(node)
    e.setDelay(d)
    self.assertEqual( True, self.equals(expected,e.toSBML()) )
    pass  

  def test_WriteSBML_Event_delayWithSBO(self):
    expected = wrapString("<event id=\"e\">\n" + 
    "  <delay sboTerm=\"SBO:0000064\">\n" + 
    "    <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "      <cn type=\"integer\"> 5 </cn>\n" + 
    "    </math>\n" + 
    "  </delay>\n" + 
    "</event>")
    self.D.setLevelAndVersion(2,3,False)
    e = self.D.createModel().createEvent()
    e.setId("e")
    node = libsbml.parseFormula("5")
    d = libsbml.Delay( 2,3 )
    d.setMath(node)
    d.setSBOTerm(64)
    e.setDelay(d)
    self.assertEqual( True, self.equals(expected,e.toSBML()) )
    pass  

  def test_WriteSBML_Event_full(self):
    expected = wrapString("<event id=\"e\">\n" + 
    "  <trigger>\n" + 
    "    <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "      <apply>\n" + 
    "        <leq/>\n" + 
    "        <ci> P1 </ci>\n" + 
    "        <ci> t </ci>\n" + 
    "      </apply>\n" + 
    "    </math>\n" + 
    "  </trigger>\n" + 
    "  <listOfEventAssignments>\n" + 
    "    <eventAssignment variable=\"k2\" sboTerm=\"SBO:0000064\">\n" + 
    "      <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "        <cn type=\"integer\"> 0 </cn>\n" + 
    "      </math>\n" + 
    "    </eventAssignment>\n" + 
    "  </listOfEventAssignments>\n" + 
    "</event>")
    self.D.setLevelAndVersion(2,3,False)
    e = self.D.createModel().createEvent()
    e.setId("e")
    node = libsbml.parseFormula("leq(P1,t)")
    t = libsbml.Trigger( 2,3 )
    t.setMath(node)
    math = libsbml.parseFormula("0")
    ea = libsbml.EventAssignment( 2,3 )
    ea.setVariable("k2")
    ea.setMath(math)
    ea.setSBOTerm(64)
    e.setTrigger(t)
    e.addEventAssignment(ea)
    self.assertEqual( True, self.equals(expected,e.toSBML()) )
    pass  

  def test_WriteSBML_Event_trigger(self):
    expected = wrapString("<event id=\"e\">\n" + 
    "  <trigger>\n" + 
    "    <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "      <apply>\n" + 
    "        <leq/>\n" + 
    "        <ci> P1 </ci>\n" + 
    "        <ci> t </ci>\n" + 
    "      </apply>\n" + 
    "    </math>\n" + 
    "  </trigger>\n" + 
    "</event>")
    self.D.setLevelAndVersion(2,1,False)
    e = self.D.createModel().createEvent()
    e.setId("e")
    node = libsbml.parseFormula("leq(P1,t)")
    t = libsbml.Trigger( 2,1 )
    t.setMath(node)
    e.setTrigger(t)
    self.assertEqual( True, self.equals(expected,e.toSBML()) )
    pass  

  def test_WriteSBML_Event_trigger_withSBO(self):
    expected = wrapString("<event id=\"e\">\n" + 
    "  <trigger sboTerm=\"SBO:0000064\">\n" + 
    "    <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "      <apply>\n" + 
    "        <leq/>\n" + 
    "        <ci> P1 </ci>\n" + 
    "        <ci> t </ci>\n" + 
    "      </apply>\n" + 
    "    </math>\n" + 
    "  </trigger>\n" + 
    "</event>")
    self.D.setLevelAndVersion(2,3,False)
    e = self.D.createModel().createEvent()
    e.setId("e")
    node = libsbml.parseFormula("leq(P1,t)")
    t = libsbml.Trigger( 2,3 )
    t.setMath(node)
    t.setSBOTerm(64)
    e.setTrigger(t)
    self.assertEqual( True, self.equals(expected,e.toSBML()) )
    pass  

  def test_WriteSBML_FunctionDefinition(self):
    expected = wrapString("<functionDefinition id=\"pow3\">\n" + 
    "  <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "    <lambda>\n" + 
    "      <bvar>\n" + 
    "        <ci> x </ci>\n" + 
    "      </bvar>\n" + 
    "      <apply>\n" + 
    "        <power/>\n" + 
    "        <ci> x </ci>\n" + 
    "        <cn type=\"integer\"> 3 </cn>\n" + 
    "      </apply>\n" + 
    "    </lambda>\n" + 
    "  </math>\n" + 
    "</functionDefinition>")
    fd = libsbml.FunctionDefinition( 2,4 )
    fd.setId("pow3")
    fd.setMath(libsbml.parseFormula("lambda(x, x^3)"))
    self.assertEqual( True, self.equals(expected,fd.toSBML()) )
    pass  

  def test_WriteSBML_FunctionDefinition_withSBO(self):
    expected = wrapString("<functionDefinition id=\"pow3\" sboTerm=\"SBO:0000064\">\n" + 
    "  <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "    <lambda>\n" + 
    "      <bvar>\n" + 
    "        <ci> x </ci>\n" + 
    "      </bvar>\n" + 
    "      <apply>\n" + 
    "        <power/>\n" + 
    "        <ci> x </ci>\n" + 
    "        <cn type=\"integer\"> 3 </cn>\n" + 
    "      </apply>\n" + 
    "    </lambda>\n" + 
    "  </math>\n" + 
    "</functionDefinition>")
    fd = libsbml.FunctionDefinition( 2,4 )
    fd.setId("pow3")
    fd.setMath(libsbml.parseFormula("lambda(x, x^3)"))
    fd.setSBOTerm(64)
    self.assertEqual( True, self.equals(expected,fd.toSBML()) )
    pass  

  def test_WriteSBML_INF(self):
    expected =  "<parameter id=\"p\" value=\"INF\"/>";
    p = self.D.createModel().createParameter()
    p.setId("p")
    p.setValue(util_PosInf())
    self.assertEqual( True, self.equals(expected,p.toSBML()) )
    pass  

  def test_WriteSBML_InitialAssignment(self):
    self.D.setLevelAndVersion(2,2,False)
    expected =  "<initialAssignment symbol=\"c\" sboTerm=\"SBO:0000064\"/>";
    ia = self.D.createModel().createInitialAssignment()
    ia.setSBOTerm(64)
    ia.setSymbol("c")
    self.assertEqual( True, self.equals(expected,ia.toSBML()) )
    pass  

  def test_WriteSBML_InitialAssignment_math(self):
    expected = wrapString("<initialAssignment symbol=\"c\">\n" + 
    "  <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "    <apply>\n" + 
    "      <plus/>\n" + 
    "      <ci> a </ci>\n" + 
    "      <ci> b </ci>\n" + 
    "    </apply>\n" + 
    "  </math>\n" + 
    "</initialAssignment>")
    ia = self.D.createModel().createInitialAssignment()
    node = libsbml.parseFormula("a + b")
    ia.setMath(node)
    ia.setSymbol("c")
    self.assertEqual( True, self.equals(expected,ia.toSBML()) )
    pass  

  def test_WriteSBML_KineticLaw(self):
    self.D.setLevelAndVersion(1,2,False)
    expected = wrapString("<kineticLaw formula=\"k * e\" timeUnits=\"second\" " + "substanceUnits=\"item\"/>")
    kl = self.D.createModel().createReaction().createKineticLaw()
    kl.setFormula("k * e")
    kl.setTimeUnits("second")
    kl.setSubstanceUnits("item")
    self.assertEqual( True, self.equals(expected,kl.toSBML()) )
    pass  

  def test_WriteSBML_KineticLaw_ListOfParameters(self):
    self.D.setLevelAndVersion(1,2,False)
    expected = wrapString("<kineticLaw formula=\"nk * e\" timeUnits=\"second\" " + 
    "substanceUnits=\"item\">\n" + 
    "  <listOfParameters>\n" + 
    "    <parameter name=\"n\" value=\"1.2\"/>\n" + 
    "  </listOfParameters>\n" + 
    "</kineticLaw>")
    kl = self.D.createModel().createReaction().createKineticLaw()
    kl.setFormula("nk * e")
    kl.setTimeUnits("second")
    kl.setSubstanceUnits("item")
    p = kl.createParameter()
    p.setName("n")
    p.setValue(1.2)
    self.assertEqual( True, self.equals(expected,kl.toSBML()) )
    pass  

  def test_WriteSBML_KineticLaw_l2v1(self):
    self.D.setLevelAndVersion(2,1,False)
    expected = wrapString("<kineticLaw timeUnits=\"second\" substanceUnits=\"item\">\n" + 
    "  <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "    <apply>\n" + 
    "      <divide/>\n" + 
    "      <apply>\n" + 
    "        <times/>\n" + 
    "        <ci> vm </ci>\n" + 
    "        <ci> s1 </ci>\n" + 
    "      </apply>\n" + 
    "      <apply>\n" + 
    "        <plus/>\n" + 
    "        <ci> km </ci>\n" + 
    "        <ci> s1 </ci>\n" + 
    "      </apply>\n" + 
    "    </apply>\n" + 
    "  </math>\n" + 
    "</kineticLaw>")
    kl = self.D.createModel().createReaction().createKineticLaw()
    kl.setTimeUnits("second")
    kl.setSubstanceUnits("item")
    kl.setFormula("(vm * s1)/(km + s1)")
    self.assertEqual( True, self.equals(expected,kl.toSBML()) )
    pass  

  def test_WriteSBML_KineticLaw_skipOptional(self):
    self.D.setLevelAndVersion(1,2,False)
    expected =  "<kineticLaw formula=\"k * e\"/>";
    kl = self.D.createModel().createReaction().createKineticLaw()
    kl.setFormula("k * e")
    self.assertEqual( True, self.equals(expected,kl.toSBML()) )
    pass  

  def test_WriteSBML_KineticLaw_withSBO(self):
    self.D.setLevelAndVersion(2,2,False)
    expected = wrapString("<kineticLaw sboTerm=\"SBO:0000001\">\n" + 
    "  <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "    <apply>\n" + 
    "      <divide/>\n" + 
    "      <apply>\n" + 
    "        <times/>\n" + 
    "        <ci> vm </ci>\n" + 
    "        <ci> s1 </ci>\n" + 
    "      </apply>\n" + 
    "      <apply>\n" + 
    "        <plus/>\n" + 
    "        <ci> km </ci>\n" + 
    "        <ci> s1 </ci>\n" + 
    "      </apply>\n" + 
    "    </apply>\n" + 
    "  </math>\n" + 
    "</kineticLaw>")
    kl = self.D.createModel().createReaction().createKineticLaw()
    kl.setFormula("(vm * s1)/(km + s1)")
    kl.setSBOTerm(1)
    self.assertEqual( True, self.equals(expected,kl.toSBML()) )
    pass  

  def test_WriteSBML_Model(self):
    self.D.setLevelAndVersion(1,1,False)
    expected = wrapSBML_L1v1("  <model name=\"Branch\"/>\n")
    self.D.createModel("Branch")
    self.S = libsbml.writeSBMLToString(self.D)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_WriteSBML_Model_L2v1(self):
    self.D.setLevelAndVersion(2,1,False)
    expected = wrapSBML_L2v1("  <model id=\"Branch\"/>\n")
    self.D.createModel("Branch")
    self.S = libsbml.writeSBMLToString(self.D)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_WriteSBML_Model_L2v1_skipOptional(self):
    self.D.setLevelAndVersion(2,1,False)
    expected = wrapSBML_L2v1("  <model/>\n")
    self.D.createModel()
    self.S = libsbml.writeSBMLToString(self.D)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_WriteSBML_Model_L2v2(self):
    self.D.setLevelAndVersion(2,2,False)
    expected = wrapSBML_L2v2("  <model id=\"Branch\" sboTerm=\"SBO:0000004\"/>\n")
    m = self.D.createModel("Branch")
    m.setSBOTerm(4)
    self.S = libsbml.writeSBMLToString(self.D)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_WriteSBML_Model_skipOptional(self):
    self.D.setLevelAndVersion(1,2,False)
    expected = wrapSBML_L1v2("  <model/>\n")
    self.D.createModel()
    self.S = libsbml.writeSBMLToString(self.D)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_WriteSBML_NaN(self):
    expected =  "<parameter id=\"p\" value=\"NaN\"/>";
    p = self.D.createModel().createParameter()
    p.setId("p")
    p.setValue(util_NaN())
    self.assertEqual( True, self.equals(expected,p.toSBML()) )
    pass  

  def test_WriteSBML_NegINF(self):
    expected =  "<parameter id=\"p\" value=\"-INF\"/>";
    p = self.D.createModel().createParameter()
    p.setId("p")
    p.setValue(util_NegInf())
    self.assertEqual( True, self.equals(expected,p.toSBML()) )
    pass  

  def test_WriteSBML_Parameter(self):
    self.D.setLevelAndVersion(1,2,False)
    expected =  "<parameter name=\"Km1\" value=\"2.3\" units=\"second\"/>";
    p = self.D.createModel().createParameter()
    p.setId("Km1")
    p.setValue(2.3)
    p.setUnits("second")
    self.assertEqual( True, self.equals(expected,p.toSBML()) )
    pass  

  def test_WriteSBML_ParameterRule(self):
    self.D.setLevelAndVersion(1,1,False)
    expected = wrapString("<parameterRule " + "formula=\"p * t\" type=\"rate\" name=\"p\"/>")
    self.D.createModel()
    self.D.getModel().createParameter().setId("p")
    r = self.D.getModel().createRateRule()
    r.setVariable("p")
    r.setFormula("p * t")
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_ParameterRule_L2v1(self):
    self.D.setLevelAndVersion(2,1,False)
    expected = wrapString("<rateRule variable=\"p\">\n" + 
    "  <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "    <apply>\n" + 
    "      <times/>\n" + 
    "      <ci> p </ci>\n" + 
    "      <ci> t </ci>\n" + 
    "    </apply>\n" + 
    "  </math>\n" + 
    "</rateRule>")
    self.D.createModel()
    self.D.getModel().createParameter().setId("p")
    r = self.D.getModel().createRateRule()
    r.setVariable("p")
    r.setFormula("p * t")
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_ParameterRule_L2v2(self):
    self.D.setLevelAndVersion(2,2,False)
    expected = wrapString("<rateRule variable=\"p\" sboTerm=\"SBO:0000007\">\n" + 
    "  <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "    <apply>\n" + 
    "      <times/>\n" + 
    "      <ci> p </ci>\n" + 
    "      <ci> t </ci>\n" + 
    "    </apply>\n" + 
    "  </math>\n" + 
    "</rateRule>")
    self.D.createModel()
    self.D.getModel().createParameter().setId("p")
    r = self.D.getModel().createRateRule()
    r.setVariable("p")
    r.setFormula("p * t")
    r.setSBOTerm(7)
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_ParameterRule_defaults(self):
    self.D.setLevelAndVersion(1,1,False)
    expected =  "<parameterRule formula=\"p * t\" name=\"p\"/>";
    self.D.createModel()
    self.D.getModel().createParameter().setId("p")
    r = self.D.getModel().createAssignmentRule()
    r.setVariable("p")
    r.setFormula("p * t")
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_Parameter_L1v1_required(self):
    self.D.setLevelAndVersion(1,1,False)
    expected =  "<parameter name=\"Km1\" value=\"NaN\"/>";
    p = self.D.createModel().createParameter()
    p.setId("Km1")
    p.unsetValue()
    self.assertEqual( True, self.equals(expected,p.toSBML()) )
    pass  

  def test_WriteSBML_Parameter_L1v2_skipOptional(self):
    self.D.setLevelAndVersion(1,2,False)
    expected =  "<parameter name=\"Km1\"/>";
    p = self.D.createModel().createParameter()
    p.setId("Km1")
    p.unsetValue()
    self.assertEqual( True, self.equals(expected,p.toSBML()) )
    pass  

  def test_WriteSBML_Parameter_L2v1(self):
    self.D.setLevelAndVersion(2,1,False)
    expected =  "<parameter id=\"Km1\" value=\"2.3\" units=\"second\"/>";
    p = self.D.createModel().createParameter()
    p.setId("Km1")
    p.setValue(2.3)
    p.setUnits("second")
    self.assertEqual( True, self.equals(expected,p.toSBML()) )
    pass  

  def test_WriteSBML_Parameter_L2v1_constant(self):
    self.D.setLevelAndVersion(2,1,False)
    expected =  "<parameter id=\"x\" constant=\"false\"/>";
    p = self.D.createModel().createParameter()
    p.setId("x")
    p.setConstant(False)
    self.assertEqual( True, self.equals(expected,p.toSBML()) )
    pass  

  def test_WriteSBML_Parameter_L2v1_skipOptional(self):
    self.D.setLevelAndVersion(2,1,False)
    expected =  "<parameter id=\"Km1\"/>";
    p = self.D.createModel().createParameter()
    p.setId("Km1")
    self.assertEqual( True, self.equals(expected,p.toSBML()) )
    pass  

  def test_WriteSBML_Parameter_L2v2(self):
    self.D.setLevelAndVersion(2,2,False)
    expected =  "<parameter id=\"Km1\" value=\"2.3\" units=\"second\" sboTerm=\"SBO:0000002\"/>";
    p = self.D.createModel().createParameter()
    p.setId("Km1")
    p.setValue(2.3)
    p.setUnits("second")
    p.setSBOTerm(2)
    self.assertEqual( True, self.equals(expected,p.toSBML()) )
    pass  

  def test_WriteSBML_Reaction(self):
    self.D.setLevelAndVersion(1,2,False)
    expected =  "<reaction name=\"r\" reversible=\"false\" fast=\"true\"/>";
    r = self.D.createModel().createReaction()
    r.setId("r")
    r.setReversible(False)
    r.setFast(True)
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_Reaction_L2v1(self):
    self.D.setLevelAndVersion(2,1,False)
    expected =  "<reaction id=\"r\" reversible=\"false\"/>";
    r = self.D.createModel().createReaction()
    r.setId("r")
    r.setReversible(False)
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_Reaction_L2v1_full(self):
    self.D.setLevelAndVersion(2,1,False)
    expected = wrapString("<reaction id=\"v1\">\n" + 
    "  <listOfReactants>\n" + 
    "    <speciesReference species=\"x0\"/>\n" + 
    "  </listOfReactants>\n" + 
    "  <listOfProducts>\n" + 
    "    <speciesReference species=\"s1\"/>\n" + 
    "  </listOfProducts>\n" + 
    "  <listOfModifiers>\n" + 
    "    <modifierSpeciesReference species=\"m1\"/>\n" + 
    "  </listOfModifiers>\n" + 
    "  <kineticLaw>\n" + 
    "    <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "      <apply>\n" + 
    "        <divide/>\n" + 
    "        <apply>\n" + 
    "          <times/>\n" + 
    "          <ci> vm </ci>\n" + 
    "          <ci> s1 </ci>\n" + 
    "        </apply>\n" + 
    "        <apply>\n" + 
    "          <plus/>\n" + 
    "          <ci> km </ci>\n" + 
    "          <ci> s1 </ci>\n" + 
    "        </apply>\n" + 
    "      </apply>\n" + 
    "    </math>\n" + 
    "  </kineticLaw>\n" + 
    "</reaction>")
    self.D.createModel()
    r = self.D.getModel().createReaction()
    r.setId("v1")
    r.setReversible(True)
    r.createReactant().setSpecies("x0")
    r.createProduct().setSpecies("s1")
    r.createModifier().setSpecies("m1")
    r.createKineticLaw().setFormula("(vm * s1)/(km + s1)")
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_Reaction_L2v2(self):
    self.D.setLevelAndVersion(2,2,False)
    expected =  "<reaction id=\"r\" name=\"r1\" reversible=\"false\" fast=\"true\" sboTerm=\"SBO:0000064\"/>";
    r = self.D.createModel().createReaction()
    r.setId("r")
    r.setName("r1")
    r.setReversible(False)
    r.setFast(True)
    r.setSBOTerm(64)
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_Reaction_defaults(self):
    self.D.setLevelAndVersion(1,2,False)
    expected =  "<reaction name=\"r\"/>";
    r = self.D.createModel().createReaction()
    r.setId("r")
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_Reaction_full(self):
    self.D.setLevelAndVersion(1,2,False)
    expected = wrapString("<reaction name=\"v1\">\n" + 
    "  <listOfReactants>\n" + 
    "    <speciesReference species=\"x0\"/>\n" + 
    "  </listOfReactants>\n" + 
    "  <listOfProducts>\n" + 
    "    <speciesReference species=\"s1\"/>\n" + 
    "  </listOfProducts>\n" + 
    "  <kineticLaw formula=\"(vm * s1)/(km + s1)\"/>\n" + 
    "</reaction>")
    self.D.createModel()
    r = self.D.getModel().createReaction()
    r.setId("v1")
    r.setReversible(True)
    r.createReactant().setSpecies("x0")
    r.createProduct().setSpecies("s1")
    r.createKineticLaw().setFormula("(vm * s1)/(km + s1)")
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_SBMLDocument_L1v1(self):
    self.D.setLevelAndVersion(1,1,False)
    expected = wrapXML("<sbml xmlns=\"http://www.sbml.org/sbml/level1\" " + "level=\"1\" version=\"1\"/>\n")
    self.S = libsbml.writeSBMLToString(self.D)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_WriteSBML_SBMLDocument_L1v2(self):
    self.D.setLevelAndVersion(1,2,False)
    expected = wrapXML("<sbml xmlns=\"http://www.sbml.org/sbml/level1\" " + "level=\"1\" version=\"2\"/>\n")
    self.S = libsbml.writeSBMLToString(self.D)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_WriteSBML_SBMLDocument_L2v1(self):
    self.D.setLevelAndVersion(2,1,False)
    expected = wrapXML("<sbml xmlns=\"http://www.sbml.org/sbml/level2\" " + "level=\"2\" version=\"1\"/>\n")
    self.S = libsbml.writeSBMLToString(self.D)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_WriteSBML_SBMLDocument_L2v2(self):
    self.D.setLevelAndVersion(2,2,False)
    expected = wrapXML("<sbml xmlns=\"http://www.sbml.org/sbml/level2/version2\" " + "level=\"2\" version=\"2\"/>\n")
    self.S = libsbml.writeSBMLToString(self.D)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_WriteSBML_Species(self):
    self.D.setLevelAndVersion(1,2,False)
    expected = wrapString("<species name=\"Ca2\" compartment=\"cell\" initialAmount=\"0.7\"" + " units=\"mole\" boundaryCondition=\"true\" charge=\"2\"/>")
    s = self.D.createModel().createSpecies()
    s.setName("Ca2")
    s.setCompartment("cell")
    s.setInitialAmount(0.7)
    s.setUnits("mole")
    s.setBoundaryCondition(True)
    s.setCharge(2)
    self.assertEqual( True, self.equals(expected,s.toSBML()) )
    pass  

  def test_WriteSBML_SpeciesConcentrationRule(self):
    self.D.setLevelAndVersion(1,2,False)
    expected = wrapString("<speciesConcentrationRule " + "formula=\"t * s\" type=\"rate\" species=\"s\"/>")
    self.D.createModel()
    self.D.getModel().createSpecies().setId("s")
    r = self.D.getModel().createRateRule()
    r.setVariable("s")
    r.setFormula("t * s")
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_SpeciesConcentrationRule_L1v1(self):
    self.D.setLevelAndVersion(1,1,False)
    expected =  "<specieConcentrationRule formula=\"t * s\" specie=\"s\"/>";
    self.D.createModel()
    self.D.getModel().createSpecies().setId("s")
    r = self.D.getModel().createAssignmentRule()
    r.setVariable("s")
    r.setFormula("t * s")
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_SpeciesConcentrationRule_L2v1(self):
    self.D.setLevelAndVersion(2,1,False)
    expected = wrapString("<assignmentRule variable=\"s\">\n" + 
    "  <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "    <apply>\n" + 
    "      <times/>\n" + 
    "      <ci> t </ci>\n" + 
    "      <ci> s </ci>\n" + 
    "    </apply>\n" + 
    "  </math>\n" + 
    "</assignmentRule>")
    self.D.createModel()
    self.D.getModel().createSpecies().setId("s")
    r = self.D.getModel().createAssignmentRule()
    r.setVariable("s")
    r.setFormula("t * s")
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_SpeciesConcentrationRule_L2v2(self):
    self.D.setLevelAndVersion(2,2,False)
    expected = wrapString("<assignmentRule variable=\"s\" sboTerm=\"SBO:0000006\">\n" + 
    "  <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "    <apply>\n" + 
    "      <times/>\n" + 
    "      <ci> t </ci>\n" + 
    "      <ci> s </ci>\n" + 
    "    </apply>\n" + 
    "  </math>\n" + 
    "</assignmentRule>")
    self.D.createModel()
    self.D.getModel().createSpecies().setId("s")
    r = self.D.getModel().createAssignmentRule()
    r.setVariable("s")
    r.setFormula("t * s")
    r.setSBOTerm(6)
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_SpeciesConcentrationRule_defaults(self):
    self.D.setLevelAndVersion(1,2,False)
    expected =  "<speciesConcentrationRule formula=\"t * s\" species=\"s\"/>";
    self.D.createModel()
    self.D.getModel().createSpecies().setId("s")
    r = self.D.getModel().createAssignmentRule()
    r.setVariable("s")
    r.setFormula("t * s")
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteSBML_SpeciesReference(self):
    self.D.setLevelAndVersion(1,2,False)
    expected =  "<speciesReference species=\"s\" stoichiometry=\"3\" denominator=\"2\"/>";
    sr = self.D.createModel().createReaction().createReactant()
    sr.setSpecies("s")
    sr.setStoichiometry(3)
    sr.setDenominator(2)
    self.assertEqual( True, self.equals(expected,sr.toSBML()) )
    pass  

  def test_WriteSBML_SpeciesReference_L1v1(self):
    self.D.setLevelAndVersion(1,1,False)
    expected =  "<specieReference specie=\"s\" stoichiometry=\"3\" denominator=\"2\"/>";
    sr = self.D.createModel().createReaction().createReactant()
    sr.setSpecies("s")
    sr.setStoichiometry(3)
    sr.setDenominator(2)
    self.assertEqual( True, self.equals(expected,sr.toSBML()) )
    pass  

  def test_WriteSBML_SpeciesReference_L2v1_1(self):
    self.D.setLevelAndVersion(2,1,False)
    expected = wrapString("<speciesReference species=\"s\">\n" + 
    "  <stoichiometryMath>\n" + 
    "    <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "      <cn type=\"rational\"> 3 <sep/> 2 </cn>\n" + 
    "    </math>\n" + 
    "  </stoichiometryMath>\n" + 
    "</speciesReference>")
    sr = self.D.createModel().createReaction().createReactant()
    sr.setSpecies("s")
    sr.setStoichiometry(3)
    sr.setDenominator(2)
    self.assertEqual( True, self.equals(expected,sr.toSBML()) )
    pass  

  def test_WriteSBML_SpeciesReference_L2v1_2(self):
    self.D.setLevelAndVersion(2,1,False)
    expected =  "<speciesReference species=\"s\" stoichiometry=\"3.2\"/>";
    sr = self.D.createModel().createReaction().createReactant()
    sr.setSpecies("s")
    sr.setStoichiometry(3.2)
    self.assertEqual( True, self.equals(expected,sr.toSBML()) )
    pass  

  def test_WriteSBML_SpeciesReference_L2v1_3(self):
    self.D.setLevelAndVersion(2,1,False)
    expected = wrapString("<speciesReference species=\"s\">\n" + 
    "  <stoichiometryMath>\n" + 
    "    <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "      <apply>\n" + 
    "        <divide/>\n" + 
    "        <cn type=\"integer\"> 1 </cn>\n" + 
    "        <ci> d </ci>\n" + 
    "      </apply>\n" + 
    "    </math>\n" + 
    "  </stoichiometryMath>\n" + 
    "</speciesReference>")
    sr = self.D.createModel().createReaction().createReactant()
    sr.setSpecies("s")
    math = libsbml.parseFormula("1/d")
    stoich = sr.createStoichiometryMath()
    stoich.setMath(math)
    sr.setStoichiometryMath(stoich)
    self.assertEqual( True, self.equals(expected,sr.toSBML()) )
    pass  

  def test_WriteSBML_SpeciesReference_L2v2_1(self):
    self.D.setLevelAndVersion(2,2,False)
    expected = wrapString("<speciesReference id=\"ss\" name=\"odd\" sboTerm=\"SBO:0000009\" species=\"s\">\n" + 
    "  <stoichiometryMath>\n" + 
    "    <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "      <cn type=\"rational\"> 3 <sep/> 2 </cn>\n" + 
    "    </math>\n" + 
    "  </stoichiometryMath>\n" + 
    "</speciesReference>")
    sr = self.D.createModel().createReaction().createReactant()
    sr.setSpecies("s")
    sr.setStoichiometry(3)
    sr.setDenominator(2)
    sr.setId("ss")
    sr.setName("odd")
    sr.setSBOTerm(9)
    sr.setId("ss")
    sr.setName("odd")
    sr.setSBOTerm(9)
    self.assertEqual( True, self.equals(expected,sr.toSBML()) )
    pass  

  def test_WriteSBML_SpeciesReference_L2v3_1(self):
    self.D.setLevelAndVersion(2,3,False)
    expected =  "<speciesReference id=\"ss\" name=\"odd\" sboTerm=\"SBO:0000009\" species=\"s\" stoichiometry=\"3.2\"/>";
    sr = self.D.createModel().createReaction().createReactant()
    sr.setSpecies("s")
    sr.setStoichiometry(3.2)
    sr.setId("ss")
    sr.setName("odd")
    sr.setSBOTerm(9)
    self.assertEqual( True, self.equals(expected,sr.toSBML()) )
    pass  

  def test_WriteSBML_SpeciesReference_defaults(self):
    self.D.setLevelAndVersion(1,2,False)
    expected =  "<speciesReference species=\"s\"/>";
    sr = self.D.createModel().createReaction().createReactant()
    sr.setSpecies("s")
    self.assertEqual( True, self.equals(expected,sr.toSBML()) )
    pass  

  def test_WriteSBML_SpeciesType(self):
    self.D.setLevelAndVersion(2,2,False)
    expected =  "<speciesType id=\"st\"/>";
    st = self.D.createModel().createSpeciesType()
    st.setId("st")
    st.setSBOTerm(4)
    self.assertEqual( True, self.equals(expected,st.toSBML()) )
    pass  

  def test_WriteSBML_SpeciesType_withSBO(self):
    self.D.setLevelAndVersion(2,3,False)
    expected =  "<speciesType id=\"st\" sboTerm=\"SBO:0000004\"/>";
    st = self.D.createModel().createSpeciesType()
    st.setId("st")
    st.setSBOTerm(4)
    self.assertEqual( True, self.equals(expected,st.toSBML()) )
    pass  

  def test_WriteSBML_Species_L1v1(self):
    self.D.setLevelAndVersion(1,1,False)
    expected = wrapString("<specie name=\"Ca2\" compartment=\"cell\" initialAmount=\"0.7\"" + " units=\"mole\" boundaryCondition=\"true\" charge=\"2\"/>")
    s = self.D.createModel().createSpecies()
    s.setName("Ca2")
    s.setCompartment("cell")
    s.setInitialAmount(0.7)
    s.setUnits("mole")
    s.setBoundaryCondition(True)
    s.setCharge(2)
    self.assertEqual( True, self.equals(expected,s.toSBML()) )
    pass  

  def test_WriteSBML_Species_L2v1(self):
    self.D.setLevelAndVersion(2,1,False)
    expected = wrapString("<species id=\"Ca2\" compartment=\"cell\" initialAmount=\"0.7\" " + "substanceUnits=\"mole\" constant=\"true\"/>")
    s = self.D.createModel().createSpecies()
    s.setId("Ca2")
    s.setCompartment("cell")
    s.setInitialAmount(0.7)
    s.setSubstanceUnits("mole")
    s.setConstant(True)
    self.assertEqual( True, self.equals(expected,s.toSBML()) )
    pass  

  def test_WriteSBML_Species_L2v1_skipOptional(self):
    self.D.setLevelAndVersion(2,1,False)
    expected =  "<species id=\"Ca2\" compartment=\"cell\"/>";
    s = self.D.createModel().createSpecies()
    s.setId("Ca2")
    s.setCompartment("cell")
    self.assertEqual( True, self.equals(expected,s.toSBML()) )
    pass  

  def test_WriteSBML_Species_L2v2(self):
    self.D.setLevelAndVersion(2,2,False)
    expected = wrapString("<species id=\"Ca2\" speciesType=\"st\" compartment=\"cell\" initialAmount=\"0.7\" " + "substanceUnits=\"mole\" constant=\"true\"/>")
    s = self.D.createModel().createSpecies()
    s.setId("Ca2")
    s.setCompartment("cell")
    s.setInitialAmount(0.7)
    s.setSubstanceUnits("mole")
    s.setConstant(True)
    s.setSpeciesType("st")
    self.assertEqual( True, self.equals(expected,s.toSBML()) )
    pass  

  def test_WriteSBML_Species_L2v3(self):
    self.D.setLevelAndVersion(2,3,False)
    expected =  "<species id=\"Ca2\" compartment=\"cell\" sboTerm=\"SBO:0000007\"/>";
    s = self.D.createModel().createSpecies()
    s.setId("Ca2")
    s.setCompartment("cell")
    s.setSBOTerm(7)
    self.assertEqual( True, self.equals(expected,s.toSBML()) )
    pass  

  def test_WriteSBML_Species_defaults(self):
    self.D.setLevelAndVersion(1,2,False)
    expected = wrapString("<species name=\"Ca2\" compartment=\"cell\" initialAmount=\"0.7\"" + " units=\"mole\" charge=\"2\"/>")
    s = self.D.createModel().createSpecies()
    s.setName("Ca2")
    s.setCompartment("cell")
    s.setInitialAmount(0.7)
    s.setUnits("mole")
    s.setCharge(2)
    self.assertEqual( True, self.equals(expected,s.toSBML()) )
    pass  

  def test_WriteSBML_Species_skipOptional(self):
    self.D.setLevelAndVersion(1,2,False)
    expected =  "<species name=\"Ca2\" compartment=\"cell\" initialAmount=\"0.7\"/>";
    s = self.D.createModel().createSpecies()
    s.setId("Ca2")
    s.setCompartment("cell")
    s.setInitialAmount(0.7)
    self.assertEqual( True, self.equals(expected,s.toSBML()) )
    pass  

  def test_WriteSBML_StoichiometryMath(self):
    self.D.setLevelAndVersion(2,1,False)
    expected = wrapString("<stoichiometryMath>\n" + 
    "  <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "    <apply>\n" + 
    "      <divide/>\n" + 
    "      <cn type=\"integer\"> 1 </cn>\n" + 
    "      <ci> d </ci>\n" + 
    "    </apply>\n" + 
    "  </math>\n" + 
    "</stoichiometryMath>")
    math = libsbml.parseFormula("1/d")
    stoich = self.D.createModel().createReaction().createReactant().createStoichiometryMath()
    stoich.setMath(math)
    self.assertEqual( True, self.equals(expected,stoich.toSBML()) )
    pass  

  def test_WriteSBML_StoichiometryMath_withSBO(self):
    self.D.setLevelAndVersion(2,3,False)
    expected = wrapString("<stoichiometryMath sboTerm=\"SBO:0000333\">\n" + 
    "  <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "    <apply>\n" + 
    "      <divide/>\n" + 
    "      <cn type=\"integer\"> 1 </cn>\n" + 
    "      <ci> d </ci>\n" + 
    "    </apply>\n" + 
    "  </math>\n" + 
    "</stoichiometryMath>")
    math = libsbml.parseFormula("1/d")
    stoich = self.D.createModel().createReaction().createReactant().createStoichiometryMath()
    stoich.setMath(math)
    stoich.setSBOTerm(333)
    self.assertEqual( True, self.equals(expected,stoich.toSBML()) )
    pass  

  def test_WriteSBML_Unit(self):
    self.D.setLevelAndVersion(2,4,False)
    expected =  "<unit kind=\"kilogram\" exponent=\"2\" scale=\"-3\"/>";
    u = self.D.createModel().createUnitDefinition().createUnit()
    u.setKind(libsbml.UNIT_KIND_KILOGRAM)
    u.setExponent(2)
    u.setScale(-3)
    self.assertEqual( True, self.equals(expected,u.toSBML()) )
    pass  

  def test_WriteSBML_UnitDefinition(self):
    self.D.setLevelAndVersion(1,2,False)
    expected =  "<unitDefinition name=\"mmls\"/>";
    ud = self.D.createModel().createUnitDefinition()
    ud.setId("mmls")
    self.assertEqual( True, self.equals(expected,ud.toSBML()) )
    pass  

  def test_WriteSBML_UnitDefinition_L2v1(self):
    self.D.setLevelAndVersion(2,1,False)
    expected =  "<unitDefinition id=\"mmls\"/>";
    ud = self.D.createModel().createUnitDefinition()
    ud.setId("mmls")
    self.assertEqual( True, self.equals(expected,ud.toSBML()) )
    pass  

  def test_WriteSBML_UnitDefinition_L2v1_full(self):
    self.D.setLevelAndVersion(2,1,False)
    expected = wrapString("<unitDefinition id=\"Fahrenheit\">\n" + 
    "  <listOfUnits>\n" + 
    "    <unit kind=\"Celsius\" multiplier=\"1.8\" offset=\"32\"/>\n" + 
    "  </listOfUnits>\n" + 
    "</unitDefinition>")
    ud = self.D.createModel().createUnitDefinition()
    ud.setId("Fahrenheit")
    u1 = ud.createUnit()
    u1.setKind(libsbml.UnitKind_forName("Celsius"))
    u1.setMultiplier(1.8)
    u1.setOffset(32)
    self.assertEqual( True, self.equals(expected,ud.toSBML()) )
    pass  

  def test_WriteSBML_UnitDefinition_full(self):
    self.D.setLevelAndVersion(1,2,False)
    expected = wrapString("<unitDefinition name=\"mmls\">\n" + 
    "  <listOfUnits>\n" + 
    "    <unit kind=\"mole\" scale=\"-3\"/>\n" + 
    "    <unit kind=\"liter\" exponent=\"-1\"/>\n" + 
    "    <unit kind=\"second\" exponent=\"-1\"/>\n" + 
    "  </listOfUnits>\n" + 
    "</unitDefinition>")
    ud = self.D.createModel().createUnitDefinition()
    ud.setId("mmls")
    u1 = ud.createUnit()
    u1.setKind(libsbml.UNIT_KIND_MOLE)
    u1.setScale(-3)
    u2 = ud.createUnit()
    u2.setKind(libsbml.UNIT_KIND_LITER)
    u2.setExponent(-1)
    u3 = ud.createUnit()
    u3.setKind(libsbml.UNIT_KIND_SECOND)
    u3.setExponent(-1)
    self.assertEqual( True, self.equals(expected,ud.toSBML()) )
    pass  

  def test_WriteSBML_Unit_L2v1(self):
    self.D.setLevelAndVersion(2,1,False)
    expected =  "<unit kind=\"Celsius\" multiplier=\"1.8\" offset=\"32\"/>";
    u = self.D.createModel().createUnitDefinition().createUnit()
    u.setKind(libsbml.UnitKind_forName("Celsius"))
    u.setMultiplier(1.8)
    u.setOffset(32)
    self.assertEqual( True, self.equals(expected,u.toSBML()) )
    pass  

  def test_WriteSBML_Unit_defaults(self):
    self.D.setLevelAndVersion(1,2,False)
    expected =  "<unit kind=\"kilogram\"/>";
    u = self.D.createModel().createUnitDefinition().createUnit()
    u.setKind(libsbml.UNIT_KIND_KILOGRAM)
    self.assertEqual( True, self.equals(expected,u.toSBML()) )
    pass  

  def test_WriteSBML_Unit_l2v3(self):
    self.D.setLevelAndVersion(2,3,False)
    expected =  "<unit kind=\"kilogram\" exponent=\"2\" scale=\"-3\"/>";
    u = self.D.createModel().createUnitDefinition().createUnit()
    u.setKind(libsbml.UNIT_KIND_KILOGRAM)
    u.setExponent(2)
    u.setScale(-3)
    u.setOffset(32)
    self.assertEqual( True, self.equals(expected,u.toSBML()) )
    pass  

  def test_WriteSBML_bzip2(self):
    file = []
    file.append("../../../examples/sample-models/from-spec/level-2/algebraicrules.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/assignmentrules.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/boundarycondition.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/delay.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/dimerization.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/enzymekinetics.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/events.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/functiondef.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/multicomp.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/overdetermined.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/twodimensional.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/units.xml")

    bz2file = "test.xml.bz2"
    for f in file:
      d = libsbml.readSBML(f)
      self.assert_( d != None )
      if not libsbml.SBMLWriter.hasBzip2():
        self.assert_( libsbml.writeSBML(d,bz2file) == 0 )
        d = None
        continue
      result = libsbml.writeSBML(d,bz2file)
      self.assertEqual( 1, result )
      dg = libsbml.readSBML(bz2file)
      self.assert_( dg != None )
      self.assert_( ( dg.toSBML() != d.toSBML() ) == False )
      d = None
      dg = None
    pass


  def test_WriteSBML_elements_L1v2(self):
    self.D.setLevelAndVersion(1,2,False)
    expected = wrapSBML_L1v2("  <model>\n" + 
    "    <listOfUnitDefinitions>\n" + 
    "      <unitDefinition/>\n" + 
    "    </listOfUnitDefinitions>\n" + 
    "    <listOfCompartments>\n" + 
    "      <compartment/>\n" + 
    "    </listOfCompartments>\n" + 
    "    <listOfSpecies>\n" + 
    "      <species initialAmount=\"0\"/>\n" + 
    "    </listOfSpecies>\n" + 
    "    <listOfParameters>\n" + 
    "      <parameter/>\n" + 
    "    </listOfParameters>\n" + 
    "    <listOfRules>\n" + 
    "      <algebraicRule/>\n" + 
    "    </listOfRules>\n" + 
    "    <listOfReactions>\n" + 
    "      <reaction/>\n" + 
    "    </listOfReactions>\n" + 
    "  </model>\n")
    m = self.D.createModel()
    m.createUnitDefinition()
    m.createCompartment()
    m.createParameter()
    m.createAlgebraicRule()
    m.createReaction()
    m.createSpecies()
    self.S = libsbml.writeSBMLToString(self.D)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_WriteSBML_elements_L2v1(self):
    self.D.setLevelAndVersion(2,1,False)
    expected = wrapSBML_L2v1("  <model>\n" + 
    "    <listOfFunctionDefinitions>\n" + 
    "      <functionDefinition/>\n" + 
    "    </listOfFunctionDefinitions>\n" + 
    "    <listOfUnitDefinitions>\n" + 
    "      <unitDefinition/>\n" + 
    "    </listOfUnitDefinitions>\n" + 
    "    <listOfCompartments>\n" + 
    "      <compartment/>\n" + 
    "    </listOfCompartments>\n" + 
    "    <listOfSpecies>\n" + 
    "      <species/>\n" + 
    "    </listOfSpecies>\n" + 
    "    <listOfParameters>\n" + 
    "      <parameter/>\n" + 
    "    </listOfParameters>\n" + 
    "    <listOfRules>\n" + 
    "      <algebraicRule/>\n" + 
    "    </listOfRules>\n" + 
    "    <listOfReactions>\n" + 
    "      <reaction/>\n" + 
    "    </listOfReactions>\n" + 
    "    <listOfEvents>\n" + 
    "      <event/>\n" + 
    "    </listOfEvents>\n" + 
    "  </model>\n")
    m = self.D.createModel()
    m.createUnitDefinition()
    m.createFunctionDefinition()
    m.createCompartment()
    m.createEvent()
    m.createParameter()
    m.createAlgebraicRule()
    m.createInitialAssignment()
    m.createConstraint()
    m.createReaction()
    m.createSpecies()
    self.S = libsbml.writeSBMLToString(self.D)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_WriteSBML_elements_L2v2(self):
    self.D.setLevelAndVersion(2,2,False)
    expected = wrapSBML_L2v2("  <model>\n" + 
    "    <listOfFunctionDefinitions>\n" + 
    "      <functionDefinition/>\n" + 
    "    </listOfFunctionDefinitions>\n" + 
    "    <listOfUnitDefinitions>\n" + 
    "      <unitDefinition/>\n" + 
    "    </listOfUnitDefinitions>\n" + 
    "    <listOfCompartmentTypes>\n" + 
    "      <compartmentType/>\n" + 
    "    </listOfCompartmentTypes>\n" + 
    "    <listOfSpeciesTypes>\n" + 
    "      <speciesType/>\n" + 
    "    </listOfSpeciesTypes>\n" + 
    "    <listOfCompartments>\n" + 
    "      <compartment/>\n" + 
    "    </listOfCompartments>\n" + 
    "    <listOfSpecies>\n" + 
    "      <species/>\n" + 
    "    </listOfSpecies>\n" + 
    "    <listOfParameters>\n" + 
    "      <parameter/>\n" + 
    "    </listOfParameters>\n" + 
    "    <listOfInitialAssignments>\n" + 
    "      <initialAssignment/>\n" + 
    "    </listOfInitialAssignments>\n" + 
    "    <listOfRules>\n" + 
    "      <algebraicRule/>\n" + 
    "    </listOfRules>\n" + 
    "    <listOfConstraints>\n" + 
    "      <constraint/>\n" + 
    "    </listOfConstraints>\n" + 
    "    <listOfReactions>\n" + 
    "      <reaction/>\n" + 
    "    </listOfReactions>\n" + 
    "    <listOfEvents>\n" + 
    "      <event/>\n" + 
    "    </listOfEvents>\n" + 
    "  </model>\n")
    m = self.D.createModel()
    m.createUnitDefinition()
    m.createFunctionDefinition()
    m.createCompartmentType()
    m.createSpeciesType()
    m.createCompartment()
    m.createEvent()
    m.createParameter()
    m.createAlgebraicRule()
    m.createInitialAssignment()
    m.createConstraint()
    m.createReaction()
    m.createSpecies()
    self.S = libsbml.writeSBMLToString(self.D)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_WriteSBML_error(self):
    d = libsbml.SBMLDocument()
    w = libsbml.SBMLWriter()
    self.assertEqual( False, w.writeSBML(d, "/tmp/impossible/path/should/fail") )
    self.assert_( d.getNumErrors() == 1 )
    self.assert_( d.getError(0).getErrorId() == libsbml.XMLFileUnwritable )
    d = None
    w = None
    pass  

  def test_WriteSBML_gzip(self):
    file = []
    file.append("../../../examples/sample-models/from-spec/level-2/algebraicrules.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/assignmentrules.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/boundarycondition.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/delay.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/dimerization.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/enzymekinetics.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/events.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/functiondef.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/multicomp.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/overdetermined.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/twodimensional.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/units.xml")

    gzfile = "test.xml.gz"
    for f in file:
      d = libsbml.readSBML(f)
      self.assert_( d != None )
      if not libsbml.SBMLWriter.hasZlib():
        self.assert_( libsbml.writeSBML(d,gzfile) == 0 )
        d = None
        continue
      result = libsbml.writeSBML(d,gzfile)
      self.assertEqual( 1, result )
      dg = libsbml.readSBML(gzfile)
      self.assert_( dg != None )
      self.assert_( ( dg.toSBML() != d.toSBML() ) == False )
      d = None
      dg = None
    pass


  def test_WriteSBML_locale(self):
    expected =  "<parameter id=\"p\" value=\"3.31\"/>";
    p = self.D.createModel().createParameter()
    p.setId("p")
    p.setValue(3.31)
    self.assertEqual( True, self.equals(expected,p.toSBML()) )
    pass  

  def test_WriteSBML_zip(self):
    file = []
    file.append("../../../examples/sample-models/from-spec/level-2/algebraicrules.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/assignmentrules.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/boundarycondition.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/delay.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/dimerization.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/enzymekinetics.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/events.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/functiondef.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/multicomp.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/overdetermined.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/twodimensional.xml")
    file.append("../../../examples/sample-models/from-spec/level-2/units.xml")

    zipfile = "test.xml.zip"
    for f in file:
      d = libsbml.readSBML(f)
      self.assert_( d != None )
      if not libsbml.SBMLWriter.hasZlib():
        self.assert_( libsbml.writeSBML(d,zipfile) == 0 )
        d = None
        continue
      result = libsbml.writeSBML(d,zipfile)
      self.assertEqual( 1, result )
      dg = libsbml.readSBML(zipfile)
      self.assert_( dg != None )
      self.assert_( ( dg.toSBML() != d.toSBML() ) == False )
      d = None
      dg = None
    pass


def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestWriteSBML))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)
