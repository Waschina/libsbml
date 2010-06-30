#
# @file    TestReadSBML.rb
# @brief   Read SBML unit tests
#
# @author  Akiya Jouraku (Ruby conversion)
# @author  Ben Bornstein 
#
# $Id$
# $HeadURL$
#
# This test file was converted from src/sbml/test/TestReadSBML.cpp
# with the help of conversion sciprt (ctest_converter.pl).
#
#<!---------------------------------------------------------------------------
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
#--------------------------------------------------------------------------->*/
require 'test/unit'
require 'libSBML'

class TestReadSBML < Test::Unit::TestCase

  def SBML_FOOTER
    return "</model> </sbml>"
  end

  def SBML_HEADER_L1v1
    return "<sbml xmlns='http://www.sbml.org/sbml/level1' level='1' version='1'> <model name='m'>\n"
  end

  def SBML_HEADER_L1v2
    return "<sbml xmlns='http://www.sbml.org/sbml/level1' level='1' version='2'> <model name='m'>\n"
  end

  def SBML_HEADER_L2v1
    return "<sbml xmlns='http://www.sbml.org/sbml/level2' level='2' version='1'> <model name='m'>\n"
  end

  def SBML_HEADER_L2v2
    return "<sbml xmlns='http://www.sbml.org/sbml/level2/version2' level='2' version='2'> <model name='m'>\n"
  end

  def SBML_HEADER_L2v3
    return "<sbml xmlns='http://www.sbml.org/sbml/level2/version3' level='2' version='3'> <model name='m'>\n"
  end

  def XML_HEADER
    return "<?xml version='1.0' encoding='UTF-8'?>\n"
  end

  def wrapSBML_L1v1(s)
    r = XML_HEADER()
    r += SBML_HEADER_L1v1()
    r += s
    r += SBML_FOOTER()
    return r
  end

  def wrapSBML_L1v2(s)
    r = XML_HEADER()
    r += SBML_HEADER_L1v2()
    r += s
    r += SBML_FOOTER()
    return r
  end

  def wrapSBML_L2v1(s)
    r = XML_HEADER()
    r += SBML_HEADER_L2v1()
    r += s
    r += SBML_FOOTER()
    return r
  end

  def wrapSBML_L2v2(s)
    r = XML_HEADER()
    r += SBML_HEADER_L2v2()
    r += s
    r += SBML_FOOTER()
    return r
  end

  def wrapSBML_L2v3(s)
    r = XML_HEADER()
    r += SBML_HEADER_L2v3()
    r += s
    r += SBML_FOOTER()
    return r
  end

  def wrapXML(s)
    r = XML_HEADER()
    r += s
    return r
  end

  @@USE_LIBXML = 0
  @@USE_EXPAT  = 0
  @@USE_XERCES = 0

  def setXMLParser
    make_config = "../../../config/makefile-common-vars.mk"

    File.foreach(make_config) do |line|
      @@USE_EXPAT  = 1 if line =~ /^ USE_EXPAT  \s* = \s* 1/x
      @@USE_LIBXML = 1 if line =~ /^ USE_LIBXML \s* = \s* 1/x
      @@USE_XERCES = 1 if line =~ /^ USE_XERCES \s* = \s* 1/x
    end
  end

  def setup
    @@d = nil
  end

  def teardown
    @@d = nil
  end

  def test_ReadSBML_AlgebraicRule
    s = wrapSBML_L1v2("<listOfRules>" + 
    "  <algebraicRule formula='x + 1'/>" + 
    "</listOfRules>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumRules() == 1 )
    ar = @@m.getRule(0)
    assert ((  "x + 1" == ar.getFormula() ))
  end

  def test_ReadSBML_AlgebraicRule_L2
    s = wrapSBML_L2v1("<listOfRules>" + 
    "  <algebraicRule>" + 
    "    <math>" + 
    "      <apply>" + 
    "        <minus/>" + 
    "        <apply>" + 
    "          <plus/>" + 
    "            <ci> S1 </ci>" + 
    "            <ci> S2 </ci>" + 
    "        </apply>" + 
    "        <ci> T </ci>" + 
    "      </apply>" + 
    "    </math>" + 
    "  </algebraicRule>" + 
    "</listOfRules>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumRules() == 1 )
    ar = @@m.getRule(0)
    assert( ar != nil )
    assert_equal true, ar.isSetMath()
    math = ar.getMath()
    formula = ar.getFormula()
    assert( formula != nil )
    assert ((  "S1 + S2 - T" == formula ))
  end

  def test_ReadSBML_AssignmentRule
    s = wrapSBML_L2v1("<listOfRules>" + 
    "  <assignmentRule variable='k'>" + 
    "    <math>" + 
    "      <apply>" + 
    "        <divide/>" + 
    "        <ci> k3 </ci>" + 
    "        <ci> k2 </ci>" + 
    "      </apply>" + 
    "    </math>" + 
    "  </assignmentRule>" + 
    "</listOfRules>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumRules() == 1 )
    ar = @@m.getRule(0)
    assert( ar != nil )
    assert_equal true, ar.isSetMath()
    math = ar.getMath()
    formula = ar.getFormula()
    assert( formula != nil )
    assert ((  "k3 / k2" == formula ))
  end

  def test_ReadSBML_Compartment
    s = wrapSBML_L1v2("<listOfCompartments>" + 
    "  <compartment name='mitochondria' volume='.0001' units='milliliters'" + 
    "               outside='cell'/>" + 
    "</listOfCompartments>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumCompartments() == 1 )
    c = @@m.getCompartment(0)
    assert ((  "mitochondria"  == c.getId() ))
    assert ((  "milliliters"   == c.getUnits() ))
    assert ((  "cell"          == c.getOutside() ))
    assert( c.getVolume() == 0.0001 )
    assert_equal true, c.isSetVolume()
    assert_equal true, c.isSetSize()
  end

  def test_ReadSBML_CompartmentVolumeRule
    s = wrapSBML_L1v2("<listOfRules>" + 
    "  <compartmentVolumeRule compartment='A' formula='0.10 * t'/>" + 
    "</listOfRules>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumRules() == 1 )
    cvr = @@m.getRule(0)
    assert_equal true, cvr.isCompartmentVolume()
    assert ((  "A" == cvr.getVariable() ))
    assert ((  "0.10 * t"  == cvr.getFormula() ))
    assert( cvr.getType() == LibSBML::RULE_TYPE_SCALAR )
  end

  def test_ReadSBML_Compartment_L2
    s = wrapSBML_L2v1("<listOfCompartments>" + 
    "  <compartment id='membrane' size='.3' spatialDimensions='2'" + 
    "               units='area' outside='tissue' constant='false'/>" + 
    "</listOfCompartments>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumCompartments() == 1 )
    c = @@m.getCompartment(0)
    assert_equal true, c.isSetId()
    assert_equal false, c.isSetName()
    assert_equal true, c.isSetVolume()
    assert_equal true, c.isSetSize()
    assert_equal true, c.isSetUnits()
    assert_equal true, c.isSetOutside()
    assert ((  "membrane"  == c.getId() ))
    assert ((  "area"      == c.getUnits() ))
    assert ((  "tissue"    == c.getOutside() ))
    assert( c.getSpatialDimensions() == 2 )
    assert( c.getSize() == 0.3 )
  end

  def test_ReadSBML_Compartment_defaults
    s = wrapSBML_L1v2("<listOfCompartments> <compartment name='cell'/> </listOfCompartments>"  
    )
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumCompartments() == 1 )
    c = @@m.getCompartment(0)
    assert_equal true, c.isSetId()
    assert_equal true, c.isSetVolume()
    assert_equal false, c.isSetSize()
    assert_equal false, c.isSetUnits()
    assert_equal false, c.isSetOutside()
    assert ((  "cell"  == c.getId() ))
    assert( c.getVolume() == 1.0 )
  end

  def test_ReadSBML_Compartment_defaults_L2
    s = wrapSBML_L2v1("<listOfCompartments> <compartment id='cell'/> </listOfCompartments>"  
    )
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumCompartments() == 1 )
    c = @@m.getCompartment(0)
    assert_equal true, c.isSetId()
    assert_equal false, c.isSetName()
    assert_equal false, c.isSetSize()
    assert_equal false, c.isSetUnits()
    assert_equal false, c.isSetOutside()
    assert ((  "cell"  == c.getId() ))
    assert( c.getSpatialDimensions() == 3 )
    assert( c.getConstant() == true )
  end

  def test_ReadSBML_Event
    s = wrapSBML_L2v2("<listOfEvents>" + 
    "  <event id='e1' name='MyEvent' timeUnits='time'/>" + 
    "</listOfEvents>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumEvents() == 1 )
    e = @@m.getEvent(0)
    assert( e != nil )
    assert_equal true, e.isSetId()
    assert_equal true, e.isSetName()
    assert_equal true, e.isSetTimeUnits()
    assert_equal false, e.isSetTrigger()
    assert_equal false, e.isSetDelay()
    assert ((  "e1"       == e.getId() ))
    assert ((  "MyEvent"  == e.getName() ))
    assert ((  "time"     == e.getTimeUnits() ))
  end

  def test_ReadSBML_EventAssignment
    s = wrapSBML_L2v1("<listOfEvents>" + 
    "  <event>" + 
    "    <listOfEventAssignments>" + 
    "      <eventAssignment variable='k2'>" + 
    "        <math> <cn> 0 </cn> </math>" + 
    "      </eventAssignment>" + 
    "    </listOfEventAssignments>" + 
    "  </event>" + 
    "</listOfEvents>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumEvents() == 1 )
    e = @@m.getEvent(0)
    assert( e != nil )
    assert( e.getNumEventAssignments() == 1 )
    ea = e.getEventAssignment(0)
    assert( ea != nil )
    assert_equal true, ea.isSetVariable()
    assert ((  "k2" == ea.getVariable() ))
    assert_equal true, ea.isSetMath()
    math = ea.getMath()
    formula = LibSBML::formulaToString(math)
    assert( formula != nil )
    assert ((  "0" == formula ))
  end

  def test_ReadSBML_Event_delay
    s = wrapSBML_L2v1("<listOfEvents>" + 
    "  <event> <delay> <math> <cn> 5 </cn> </math> </delay> </event>" + 
    "</listOfEvents>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumEvents() == 1 )
    e = @@m.getEvent(0)
    assert( e != nil )
    assert_equal true, e.isSetDelay()
    assert_equal false, e.isSetTrigger()
    delay = e.getDelay()
    formula = LibSBML::formulaToString(delay.getMath())
    assert( formula != nil )
    assert ((  "5" == formula ))
  end

  def test_ReadSBML_Event_trigger
    s = wrapSBML_L2v1("<listOfEvents>" + 
    "  <event>" + 
    "    <trigger>" + 
    "      <math>" + 
    "        <apply>" + 
    "          <leq/>" + 
    "          <ci> P1 </ci>" + 
    "          <ci> t  </ci>" + 
    "        </apply>" + 
    "      </math>" + 
    "   </trigger>" + 
    "  </event>" + 
    "</listOfEvents>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumEvents() == 1 )
    e = @@m.getEvent(0)
    assert( e != nil )
    assert_equal false, e.isSetDelay()
    assert_equal true, e.isSetTrigger()
    trigger = e.getTrigger()
    formula = LibSBML::formulaToString(trigger.getMath())
    assert( formula != nil )
    assert ((  "leq(P1, t)" == formula ))
  end

  def test_ReadSBML_FunctionDefinition
    s = wrapSBML_L2v1("<listOfFunctionDefinitions>" + 
    "  <functionDefinition id='pow3' name='cubed'>" + 
    "    <math>" + 
    "      <lambda>" + 
    "        <bvar><ci> x </ci></bvar>" + 
    "        <apply>" + 
    "          <power/>" + 
    "          <ci> x </ci>" + 
    "          <cn> 3 </cn>" + 
    "        </apply>" + 
    "      </lambda>" + 
    "    </math>" + 
    "  </functionDefinition>" + 
    "</listOfFunctionDefinitions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumFunctionDefinitions() == 1 )
    fd = @@m.getFunctionDefinition(0)
    assert( fd != nil )
    assert_equal true, fd.isSetId()
    assert_equal true, fd.isSetName()
    assert ((  "pow3"   == fd.getId() ))
    assert ((  "cubed"  == fd.getName() ))
    assert_equal true, fd.isSetMath()
    math = fd.getMath()
    formula = LibSBML::formulaToString(math)
    assert( formula != nil )
    assert ((  "lambda(x, pow(x, 3))" == formula ))
  end

  def test_ReadSBML_KineticLaw
    s = wrapSBML_L1v2("<listOfReactions>" + 
    "  <reaction name='J1'>" + 
    "    <kineticLaw formula='k1*X0'/>" + 
    "  </reaction>" + 
    "</listOfReactions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumReactions() == 1 )
    r = @@m.getReaction(0)
    kl = r.getKineticLaw()
    assert ((  "k1*X0" == kl.getFormula() ))
  end

  def test_ReadSBML_KineticLaw_L2
    s = wrapSBML_L2v1("<listOfReactions>" + 
    "  <reaction id='J1'>" + 
    "    <kineticLaw>" + 
    "      <math>" + 
    "        <apply>" + 
    "          <times/>" + 
    "          <ci> k  </ci>" + 
    "          <ci> S2 </ci>" + 
    "          <ci> X0 </ci>" + 
    "        </apply>" + 
    "      </math>" + 
    "    </kineticLaw>" + 
    "  </reaction>" + 
    "</listOfReactions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumReactions() == 1 )
    r = @@m.getReaction(0)
    assert( r != nil )
    kl = r.getKineticLaw()
    assert( kl != nil )
    assert_equal true, kl.isSetMath()
    math = kl.getMath()
    formula = kl.getFormula()
    assert( formula != nil )
    assert ((  "k * S2 * X0" == formula ))
  end

  def test_ReadSBML_KineticLaw_Parameter
    s = wrapSBML_L1v2("<listOfReactions>" + 
    "  <reaction name='J1'>" + 
    "    <kineticLaw formula='k1*X0'>" + 
    "      <listOfParameters>" + 
    "        <parameter name='k1' value='0'/>" + 
    "      </listOfParameters>" + 
    "    </kineticLaw>" + 
    "  </reaction>" + 
    "</listOfReactions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumReactions() == 1 )
    r = @@m.getReaction(0)
    kl = r.getKineticLaw()
    assert ((  "k1*X0" == kl.getFormula() ))
    assert( kl.getNumParameters() == 1 )
    p = kl.getParameter(0)
    assert ((  "k1" == p.getId() ))
    assert( p.getValue() == 0 )
  end

  def test_ReadSBML_Model
    s = wrapXML("<sbml level='1' version='1'>" + 
    "  <model name='testModel'></model>" + 
    "</sbml>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert ((  "testModel" == @@m.getId() ))
  end

  def test_ReadSBML_Model_L2
    s = wrapXML("<sbml level='2' version='1'>" + 
    "  <model id='testModel'> </model>" + 
    "</sbml>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert_equal true, @@m.isSetId()
    assert_equal false, @@m.isSetName()
    assert ((  "testModel" == @@m.getId() ))
  end

  def test_ReadSBML_Parameter
    s = wrapSBML_L1v2("<listOfParameters>" + 
    "  <parameter name='Km1' value='2.3' units='second'/>" + 
    "</listOfParameters>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumParameters() == 1 )
    p = @@m.getParameter(0)
    assert ((  "Km1"     == p.getId() ))
    assert ((  "second"  == p.getUnits() ))
    assert( p.getValue() == 2.3 )
    assert( p.isSetValue() == true )
  end

  def test_ReadSBML_ParameterRule
    s = wrapSBML_L1v2("<listOfRules>" + 
    "  <parameterRule name='k' formula='k3/k2'/>" + 
    "</listOfRules>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumRules() == 1 )
    pr = @@m.getRule(0)
    assert_equal true, pr.isParameter()
    assert ((  "k" == pr.getVariable() ))
    assert ((  "k3/k2"  == pr.getFormula() ))
    assert( pr.getType() == LibSBML::RULE_TYPE_SCALAR )
  end

  def test_ReadSBML_Parameter_L2
    s = wrapSBML_L2v1("<listOfParameters>" + 
    "  <parameter id='T' value='4.6' units='Celsius' constant='false'/>" + 
    "</listOfParameters>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumParameters() == 1 )
    p = @@m.getParameter(0)
    assert_equal true, p.isSetId()
    assert_equal false, p.isSetName()
    assert_equal true, p.isSetValue()
    assert_equal true, p.isSetUnits()
    assert ((  "T"        == p.getId() ))
    assert ((  "Celsius"  == p.getUnits() ))
    assert( p.getValue() == 4.6 )
    assert( p.getConstant() == false )
  end

  def test_ReadSBML_Parameter_L2_defaults
    s = wrapSBML_L2v1("<listOfParameters> <parameter id='x'/> </listOfParameters>"  
    )
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumParameters() == 1 )
    p = @@m.getParameter(0)
    assert_equal true, p.isSetId()
    assert_equal false, p.isSetName()
    assert_equal false, p.isSetValue()
    assert_equal false, p.isSetUnits()
    assert ((  "x" == p.getId() ))
    assert( p.getConstant() == true )
  end

  def test_ReadSBML_RateRule
    s = wrapSBML_L2v1("<listOfRules>" + 
    "  <rateRule variable='x'>" + 
    "    <math>" + 
    "      <apply>" + 
    "        <times/>" + 
    "        <apply>" + 
    "          <minus/>" + 
    "          <cn> 1 </cn>" + 
    "          <ci> x </ci>" + 
    "        </apply>" + 
    "        <apply>" + 
    "          <ln/>" + 
    "          <ci> x </ci>" + 
    "        </apply>" + 
    "      </apply>" + 
    "    </math>" + 
    "  </rateRule>" + 
    "</listOfRules>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumRules() == 1 )
    rr = @@m.getRule(0)
    assert( rr != nil )
    assert_equal true, rr.isSetMath()
    math = rr.getMath()
    formula = rr.getFormula()
    assert( formula != nil )
    assert ((  "(1 - x) * log(x)" == formula ))
  end

  def test_ReadSBML_Reaction
    s = wrapSBML_L1v2("<listOfReactions>" + 
    "  <reaction name='reaction_1' reversible='false'/>" + 
    "</listOfReactions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumReactions() == 1 )
    r = @@m.getReaction(0)
    assert ((  "reaction_1" == r.getId() ))
    assert( r.getReversible() == false )
    assert( r.getFast() == false )
  end

  def test_ReadSBML_Reaction_L2
    s = wrapSBML_L2v1("<listOfReactions>" + 
    "  <reaction id='r1' reversible='false' fast='false'/>" + 
    "</listOfReactions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumReactions() == 1 )
    r = @@m.getReaction(0)
    assert_equal true, r.isSetId()
    assert_equal false, r.isSetName()
    assert_equal true, r.isSetFast()
    assert ((  "r1" == r.getId() ))
    assert( r.getReversible() == false )
    assert( r.getFast() == false )
  end

  def test_ReadSBML_Reaction_L2_defaults
    s = wrapSBML_L2v1("<listOfReactions> <reaction id='r1'/> </listOfReactions>"  
    )
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumReactions() == 1 )
    r = @@m.getReaction(0)
    assert_equal true, r.isSetId()
    assert_equal false, r.isSetName()
    assert_equal false, r.isSetFast()
    assert ((  "r1" == r.getId() ))
    assert( r.getReversible() == true )
  end

  def test_ReadSBML_Reaction_defaults
    s = wrapSBML_L1v2("<listOfReactions>" + 
    "  <reaction name='reaction_1'/>" + 
    "</listOfReactions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumReactions() == 1 )
    r = @@m.getReaction(0)
    assert ((  "reaction_1" == r.getId() ))
    assert( r.getReversible() != false )
    assert( r.getFast() == false )
  end

  def test_ReadSBML_SBML
    s = wrapXML("<sbml level='1' version='1'> </sbml>")
    @@d = LibSBML::readSBMLFromString(s)
    assert( @@d.getLevel() == 1 )
    assert( @@d.getVersion() == 1 )
  end

  def test_ReadSBML_Specie
    s = wrapSBML_L1v1("<listOfSpecie>" + 
    "  <specie name='Glucose' compartment='cell' initialAmount='4.1'" + 
    "          units='volume' boundaryCondition='false' charge='6'/>" + 
    "</listOfSpecie>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumSpecies() == 1 )
    sp = @@m.getSpecies(0)
    assert ((  "Glucose"  == sp.getId() ))
    assert ((  "cell"     == sp.getCompartment() ))
    assert ((  "volume"   == sp.getUnits() ))
    assert( sp.getInitialAmount() == 4.1 )
    assert( sp.getBoundaryCondition() == false )
    assert( sp.getCharge() == 6 )
    assert( sp.isSetInitialAmount() == true )
    assert( sp.isSetCharge() == true )
  end

  def test_ReadSBML_SpecieConcentrationRule
    s = wrapSBML_L1v1("<listOfRules>" + 
    "  <specieConcentrationRule specie='s2' formula='k * t/(1 + k)'/>" + 
    "</listOfRules>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumRules() == 1 )
    scr = @@m.getRule(0)
    assert_equal true, scr.isSpeciesConcentration()
    assert ((  "s2" == scr.getVariable() ))
    assert ((  "k * t/(1 + k)"  == scr.getFormula() ))
    assert( scr.getType() == LibSBML::RULE_TYPE_SCALAR )
  end

  def test_ReadSBML_SpecieConcentrationRule_rate
    s = wrapSBML_L1v1("<listOfRules>" + 
    "  <specieConcentrationRule specie='s2' formula='k * t/(1 + k)' " + 
    "                           type='rate'/>" + 
    "</listOfRules>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumRules() == 1 )
    scr = @@m.getRule(0)
    assert_equal true, scr.isSpeciesConcentration()
    assert ((  "s2" == scr.getVariable() ))
    assert ((  "k * t/(1 + k)"  == scr.getFormula() ))
    assert( scr.getType() == LibSBML::RULE_TYPE_RATE )
  end

  def test_ReadSBML_SpecieReference_Product
    s = wrapSBML_L1v1("<listOfReactions>" + 
    "  <reaction name='reaction_1' reversible='false'>" + 
    "    <listOfProducts>" + 
    "      <specieReference specie='S1' stoichiometry='1'/>" + 
    "    </listOfProducts>" + 
    "  </reaction>" + 
    "</listOfReactions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumReactions() == 1 )
    r = @@m.getReaction(0)
    assert ((  "reaction_1" == r.getId() ))
    assert( r.getReversible() == false )
    assert( r.getNumProducts() == 1 )
    sr = r.getProduct(0)
    assert ((  "S1" == sr.getSpecies() ))
    assert( sr.getStoichiometry() == 1 )
    assert( sr.getDenominator() == 1 )
  end

  def test_ReadSBML_SpecieReference_Reactant
    s = wrapSBML_L1v1("<listOfReactions>" + 
    "  <reaction name='reaction_1' reversible='false'>" + 
    "    <listOfReactants>" + 
    "      <specieReference specie='X0' stoichiometry='1'/>" + 
    "    </listOfReactants>" + 
    "  </reaction>" + 
    "</listOfReactions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumReactions() == 1 )
    r = @@m.getReaction(0)
    assert ((  "reaction_1" == r.getId() ))
    assert( r.getReversible() == false )
    assert( r.getNumReactants() == 1 )
    sr = r.getReactant(0)
    assert ((  "X0" == sr.getSpecies() ))
    assert( sr.getStoichiometry() == 1 )
    assert( sr.getDenominator() == 1 )
  end

  def test_ReadSBML_SpecieReference_defaults
    s = wrapSBML_L1v1("<listOfReactions>" + 
    "  <reaction name='reaction_1' reversible='false'>" + 
    "    <listOfReactants>" + 
    "      <specieReference specie='X0'/>" + 
    "    </listOfReactants>" + 
    "  </reaction>" + 
    "</listOfReactions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumReactions() == 1 )
    r = @@m.getReaction(0)
    assert ((  "reaction_1" == r.getId() ))
    assert( r.getReversible() == false )
    assert( r.getNumReactants() == 1 )
    sr = r.getReactant(0)
    assert ((  "X0" == sr.getSpecies() ))
    assert( sr.getStoichiometry() == 1 )
    assert( sr.getDenominator() == 1 )
  end

  def test_ReadSBML_Specie_defaults
    s = wrapSBML_L1v1("<listOfSpecie>" + 
    "  <specie name='Glucose' compartment='cell' initialAmount='1.0'/>" + 
    "</listOfSpecie>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumSpecies() == 1 )
    sp = @@m.getSpecies(0)
    assert ((  "Glucose"  == sp.getId() ))
    assert ((  "cell"     == sp.getCompartment() ))
    assert( sp.getInitialAmount() == 1.0 )
    assert( sp.getBoundaryCondition() == false )
    assert( sp.isSetInitialAmount() == true )
    assert( sp.isSetCharge() == false )
  end

  def test_ReadSBML_Species
    s = wrapSBML_L1v2("<listOfSpecies>" + 
    "  <species name='Glucose' compartment='cell' initialAmount='4.1'" + 
    "           units='volume' boundaryCondition='false' charge='6'/>" + 
    "</listOfSpecies>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumSpecies() == 1 )
    sp = @@m.getSpecies(0)
    assert ((  "Glucose"  == sp.getId() ))
    assert ((  "cell"     == sp.getCompartment() ))
    assert ((  "volume"   == sp.getUnits() ))
    assert( sp.getInitialAmount() == 4.1 )
    assert( sp.getBoundaryCondition() == false )
    assert( sp.getCharge() == 6 )
    assert( sp.isSetInitialAmount() == true )
    assert( sp.isSetCharge() == true )
  end

  def test_ReadSBML_SpeciesConcentrationRule
    s = wrapSBML_L1v2("<listOfRules>" + 
    "  <speciesConcentrationRule species='s2' formula='k * t/(1 + k)'/>" + 
    "</listOfRules>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumRules() == 1 )
    scr = @@m.getRule(0)
    assert_equal true, scr.isSpeciesConcentration()
    assert ((  "s2" == scr.getVariable() ))
    assert ((  "k * t/(1 + k)"  == scr.getFormula() ))
    assert( scr.getType() == LibSBML::RULE_TYPE_SCALAR )
  end

  def test_ReadSBML_SpeciesReference_StoichiometryMath_1
    s = wrapSBML_L2v1("<listOfReactions>" + 
    "  <reaction name='r1'>" + 
    "    <listOfReactants>" + 
    "      <speciesReference species='X0'>" + 
    "        <stoichiometryMath>" + 
    "          <math> <ci> x </ci> </math>" + 
    "        </stoichiometryMath>" + 
    "      </speciesReference>" + 
    "    </listOfReactants>" + 
    "  </reaction>" + 
    "</listOfReactions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumReactions() == 1 )
    r = @@m.getReaction(0)
    assert( r != nil )
    assert( r.getNumReactants() == 1 )
    sr = r.getReactant(0)
    assert( sr != nil )
    assert_equal true, sr.isSetStoichiometryMath()
    math = sr.getStoichiometryMath()
    formula = LibSBML::formulaToString(math.getMath())
    assert( formula != nil )
    assert ((  "x" == formula ))
  end

  def test_ReadSBML_SpeciesReference_StoichiometryMath_2
    s = wrapSBML_L2v1("<listOfReactions>" + 
    "  <reaction name='r1'>" + 
    "    <listOfReactants>" + 
    "      <speciesReference species='X0'>" + 
    "        <stoichiometryMath>" + 
    "          <math> <cn type='rational'> 3 <sep/> 2 </cn> </math>" + 
    "        </stoichiometryMath>" + 
    "      </speciesReference>" + 
    "    </listOfReactants>" + 
    "  </reaction>" + 
    "</listOfReactions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumReactions() == 1 )
    r = @@m.getReaction(0)
    assert( r != nil )
    assert( r.getNumReactants() == 1 )
    sr = r.getReactant(0)
    assert( sr != nil )
    assert_equal false, sr.isSetStoichiometryMath()
    assert( sr.getStoichiometry() == 3 )
    assert( sr.getDenominator() == 2 )
  end

  def test_ReadSBML_SpeciesReference_defaults
    s = wrapSBML_L1v2("<listOfReactions>" + 
    "  <reaction name='reaction_1' reversible='false'>" + 
    "    <listOfReactants>" + 
    "      <speciesReference species='X0'/>" + 
    "    </listOfReactants>" + 
    "  </reaction>" + 
    "</listOfReactions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumReactions() == 1 )
    r = @@m.getReaction(0)
    assert ((  "reaction_1" == r.getId() ))
    assert( r.getReversible() == false )
    assert( r.getNumReactants() == 1 )
    sr = r.getReactant(0)
    assert ((  "X0" == sr.getSpecies() ))
    assert( sr.getStoichiometry() == 1 )
    assert( sr.getDenominator() == 1 )
  end

  def test_ReadSBML_Species_L2_1
    s = wrapSBML_L2v1("<listOfSpecies>" + 
    "  <species id='Glucose' compartment='cell' initialConcentration='4.1'" + 
    "           substanceUnits='item' spatialSizeUnits='volume'" + 
    "           boundaryCondition='true' charge='6' constant='true'/>" + 
    "</listOfSpecies>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumSpecies() == 1 )
    sp = @@m.getSpecies(0)
    assert_equal true, sp.isSetId()
    assert_equal false, sp.isSetName()
    assert_equal true, sp.isSetCompartment()
    assert_equal false, sp.isSetInitialAmount()
    assert_equal true, sp.isSetInitialConcentration()
    assert_equal true, sp.isSetSubstanceUnits()
    assert_equal true, sp.isSetSpatialSizeUnits()
    assert_equal true, sp.isSetCharge()
    assert ((  "Glucose"  == sp.getId() ))
    assert ((  "cell"     == sp.getCompartment() ))
    assert ((  "item"     == sp.getSubstanceUnits() ))
    assert ((  "volume"   == sp.getSpatialSizeUnits() ))
    assert( sp.getInitialConcentration() == 4.1 )
    assert( sp.getHasOnlySubstanceUnits() == false )
    assert( sp.getBoundaryCondition() == true )
    assert( sp.getCharge() == 6 )
    assert( sp.getConstant() == true )
  end

  def test_ReadSBML_Species_L2_2
    s = wrapSBML_L2v1("<listOfSpecies>" + 
    "  <species id='s' compartment='c' hasOnlySubstanceUnits='true'/>" + 
    "</listOfSpecies>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumSpecies() == 1 )
    sp = @@m.getSpecies(0)
    assert_equal true, sp.isSetId()
    assert_equal false, sp.isSetName()
    assert_equal true, sp.isSetCompartment()
    assert_equal false, sp.isSetInitialAmount()
    assert_equal false, sp.isSetInitialConcentration()
    assert_equal false, sp.isSetSubstanceUnits()
    assert_equal false, sp.isSetSpatialSizeUnits()
    assert_equal false, sp.isSetCharge()
    assert ((  "s"  == sp.getId() ))
    assert ((  "c"  == sp.getCompartment() ))
    assert( sp.getHasOnlySubstanceUnits() == true )
    assert( sp.getBoundaryCondition() == false )
    assert( sp.getConstant() == false )
  end

  def test_ReadSBML_Species_L2_defaults
    s = wrapSBML_L2v1("<listOfSpecies>" + 
    "  <species id='Glucose_6_P' compartment='cell'/>" + 
    "</listOfSpecies>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumSpecies() == 1 )
    sp = @@m.getSpecies(0)
    assert_equal true, sp.isSetId()
    assert_equal false, sp.isSetName()
    assert_equal true, sp.isSetCompartment()
    assert_equal false, sp.isSetInitialAmount()
    assert_equal false, sp.isSetInitialConcentration()
    assert_equal false, sp.isSetSubstanceUnits()
    assert_equal false, sp.isSetSpatialSizeUnits()
    assert_equal false, sp.isSetCharge()
    assert ((  "Glucose_6_P"  == sp.getId() ))
    assert ((  "cell"         == sp.getCompartment() ))
    assert( sp.getHasOnlySubstanceUnits() == false )
    assert( sp.getBoundaryCondition() == false )
    assert( sp.getConstant() == false )
  end

  def test_ReadSBML_Unit
    s = wrapSBML_L1v2("<listOfUnitDefinitions>" + 
    "  <unitDefinition name='substance'>" + 
    "    <listOfUnits> <unit kind='mole' scale='-3'/> </listOfUnits>" + 
    "  </unitDefinition>" + 
    "</listOfUnitDefinitions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumUnitDefinitions() == 1 )
    ud = @@m.getUnitDefinition(0)
    assert ((  "substance" == ud.getId() ))
    assert( ud.getNumUnits() == 1 )
    u = ud.getUnit(0)
    assert( u.getKind() == LibSBML::UNIT_KIND_MOLE )
    assert( u.getExponent() == 1 )
    assert( u.getScale() == -3 )
  end

  def test_ReadSBML_UnitDefinition
    s = wrapSBML_L1v2("<listOfUnitDefinitions>" + 
    "  <unitDefinition name='mmls'/>" + 
    "</listOfUnitDefinitions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumUnitDefinitions() == 1 )
    ud = @@m.getUnitDefinition(0)
    assert ((  "mmls" == ud.getId() ))
  end

  def test_ReadSBML_UnitDefinition_L2
    s = wrapSBML_L2v1("<listOfUnitDefinitions>" + 
    "  <unitDefinition id='mmls' name='mmol/ls'/>" + 
    "</listOfUnitDefinitions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumUnitDefinitions() == 1 )
    ud = @@m.getUnitDefinition(0)
    assert_equal true, ud.isSetId()
    assert_equal true, ud.isSetName()
    assert ((  "mmls" == ud.getId() ))
    assert ((  "mmol/ls" == ud.getName() ))
  end

  def test_ReadSBML_Unit_L2
    s = wrapSBML_L2v1("<listOfUnitDefinitions>" + 
    "  <unitDefinition id='Fahrenheit'>" + 
    "    <listOfUnits>" + 
    "      <unit kind='Celsius' multiplier='1.8' offset='32'/>" + 
    "    </listOfUnits>" + 
    "  </unitDefinition>" + 
    "</listOfUnitDefinitions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumUnitDefinitions() == 1 )
    ud = @@m.getUnitDefinition(0)
    assert_equal true, ud.isSetId()
    assert ((  "Fahrenheit" == ud.getId() ))
    assert( ud.getNumUnits() == 1 )
    u = ud.getUnit(0)
    assert( u.getKind() == LibSBML::UNIT_KIND_CELSIUS )
    assert( u.getExponent() == 1 )
    assert( u.getScale() == 0 )
    assert( u.getMultiplier() == 1.8 )
    assert( u.getOffset() == 32 )
  end

  def test_ReadSBML_Unit_defaults_L1_L2
    s = wrapSBML_L1v2("<listOfUnitDefinitions>" + 
    "  <unitDefinition name='bogomips'>" + 
    "    <listOfUnits> <unit kind='second'/> </listOfUnits>" + 
    "  </unitDefinition>" + 
    "</listOfUnitDefinitions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNumUnitDefinitions() == 1 )
    ud = @@m.getUnitDefinition(0)
    assert ((  "bogomips" == ud.getId() ))
    assert( ud.getNumUnits() == 1 )
    u = ud.getUnit(0)
    assert( u.getKind() == LibSBML::UNIT_KIND_SECOND )
    assert( u.getExponent() == 1 )
    assert( u.getScale() == 0 )
    assert( u.getMultiplier() == 1.0 )
    assert( u.getOffset() == 0.0 )
  end

  def test_ReadSBML_annotation
    s = wrapSBML_L2v3("<annotation xmlns:mysim=\"http://www.mysim.org/ns\">" + 
    "  <mysim:nodecolors mysim:bgcolor=\"green\" mysim:fgcolor=\"white\">" + 
    "  </mysim:nodecolors>" + 
    "  <mysim:timestamp>2000-12-18 18:31 PST</mysim:timestamp>" + 
    "</annotation>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getAnnotation() != nil )
    ann = @@m.getAnnotation()
    assert( ann.getNumChildren() == 2 )
  end

  def test_ReadSBML_annotation_sbml
    s = wrapXML("<sbml level=\"1\" version=\"1\">" + 
    "  <annotation xmlns:jd = \"http://www.sys-bio.org/sbml\">" + 
    "    <jd:header>" + 
    "      <VersionHeader SBMLVersion = \"1.0\"/>" + 
    "    </jd:header>" + 
    "    <jd:display>" + 
    "      <SBMLGraphicsHeader BackGroundColor = \"15728639\"/>" + 
    "    </jd:display>" + 
    "  </annotation>" + 
    "</sbml>")
    @@d = LibSBML::readSBMLFromString(s)
    assert( @@d.getNumErrors() > 0 )
  end

  def test_ReadSBML_annotation_sbml_L2
    s = wrapXML("<sbml xmlns=\"http://www.sbml.org/sbml/level2\" level=\"2\" version=\"1\"> " + 
    "  <annotation>" + 
    "    <rdf xmlns=\"http://www.w3.org/1999/anything\">" + 
    "		 </rdf>" + 
    "	  </annotation>" + 
    "	  <model>" + 
    "   </model>" + 
    " </sbml>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@d.getNumErrors() == 0 )
  end

  def test_ReadSBML_invalid_default_namespace
    valid = wrapXML("<sbml xmlns=\"http://www.sbml.org/sbml/level2/version4\" level=\"2\" version=\"4\"> " + 
    "   <model>" + 
    "     <notes>" + 
    "       <p xmlns=\"http://www.w3.org/1999/xhtml\">Some text.</p>" + 
    "     </notes>" + 
    "     <annotation>" + 
    "       <example xmlns=\"http://www.example.org/\"/>" + 
    "     </annotation>" + 
    "     <listOfCompartments>" + 
    "       <compartment id=\"compartmentOne\" size=\"1\"/>" + 
    "     </listOfCompartments>" + 
    "     <listOfSpecies>" + 
    "       <species id=\"S1\" initialConcentration=\"1\" compartment=\"compartmentOne\"/>" + 
    "       <species id=\"S2\" initialConcentration=\"0\" compartment=\"compartmentOne\"/>" + 
    "     </listOfSpecies>" + 
    "     <listOfParameters>" + 
    "       <parameter id=\"t\" value = \"1\" units=\"second\"/>" + 
    "     </listOfParameters>" + 
    "     <listOfConstraints>" + 
    "       <constraint sboTerm=\"SBO:0000064\">" + 
    "         <math xmlns=\"http://www.w3.org/1998/Math/MathML\">" + 
    "           <apply>" + 
    "             <leq/>" + 
    "             <ci> S1 </ci>" + 
    "             <ci> t </ci>" + 
    "           </apply>" + 
    "         </math>" + 
    "         <message>" + 
    "           <p xmlns=\"http://www.w3.org/1999/xhtml\"> Species S1 is out of range </p>" + 
    "         </message>" + 
    "       </constraint>" + 
    "     </listOfConstraints>" + 
    "     <listOfReactions>" + 
    "       <reaction id=\"reaction_1\" reversible=\"false\">" + 
    "           <listOfReactants>" + 
    "             <speciesReference species=\"S1\"/>" + 
    "           </listOfReactants>" + 
    "           <listOfProducts>" + 
    "             <speciesReference species=\"S2\">" + 
    "             </speciesReference>" + 
    "           </listOfProducts>" + 
    "       </reaction>" + 
    "     </listOfReactions>" + 
    "   </model>" + 
    " </sbml>")
    invalid = wrapXML("<sbml xmlns=\"http://www.sbml.org/sbml/level2/version4\" level=\"2\" version=\"4\"> " + 
    "   <model xmlns=\"http://invalid/custom/default/uri\">" + 
    "     <notes xmlns=\"http://invalid/custom/default/uri/in/notes\">" + 
    "       <p xmlns=\"http://www.w3.org/1999/xhtml\">Some text.</p>" + 
    "     </notes>" + 
    "     <annotation xmlns=\"http://invalid/custom/default/uri/in/annotation\">" + 
    "       <example xmlns=\"http://www.example.org/\"/>" + 
    "     </annotation>" + 
    "     <listOfCompartments>" + 
    "       <compartment id=\"compartmentOne\" size=\"1\"/>" + 
    "     </listOfCompartments>" + 
    "     <listOfSpecies>" + 
    "       <notes xmlns=\"http://invalid/custom/default/uri/in/notes\">" + 
    "         <p xmlns=\"http://www.w3.org/1999/xhtml\">Some text.</p>" + 
    "       </notes>" + 
    "       <annotation xmlns=\"http://invalid/custom/default/uri/in/annotation\">" + 
    "         <example xmlns=\"http://www.example.org/\"/>" + 
    "       </annotation>" + 
    "       <species id=\"S1\" initialConcentration=\"1\" compartment=\"compartmentOne\"/>" + 
    "       <species id=\"S2\" initialConcentration=\"0\" compartment=\"compartmentOne\"/>" + 
    "     </listOfSpecies>" + 
    "     <listOfParameters>" + 
    "       <parameter id=\"t\" value = \"1\" units=\"second\"/>" + 
    "     </listOfParameters>" + 
    "     <listOfConstraints>" + 
    "       <constraint sboTerm=\"SBO:0000064\">" + 
    "         <math xmlns=\"http://www.w3.org/1998/Math/MathML\">" + 
    "           <apply>" + 
    "             <leq/>" + 
    "             <ci> S1 </ci>" + 
    "             <ci> t </ci>" + 
    "           </apply>" + 
    "         </math>" + 
    "         <message xmlns=\"http://invalid/custom/default/uri/in/message\">" + 
    "           <p xmlns=\"http://www.w3.org/1999/xhtml\"> Species S1 is out of range </p>" + 
    "         </message>" + 
    "       </constraint>" + 
    "     </listOfConstraints>" + 
    "     <listOfReactions>" + 
    "       <reaction id=\"reaction_1\" reversible=\"false\">" + 
    "           <listOfReactants>" + 
    "             <speciesReference xmlns=\"http://invalid/custom/default/uri\" species=\"S1\"/>" + 
    "           </listOfReactants>" + 
    "           <listOfProducts>" + 
    "             <speciesReference species=\"S2\">" + 
    "               <notes xmlns=\"http://invalid/custom/default/uri/in/notes\">" + 
    "                 <p xmlns=\"http://www.w3.org/1999/xhtml\">Some text.</p>" + 
    "               </notes>" + 
    "               <annotation xmlns=\"http://invalid/custom/default/uri/in/annotation\">" + 
    "                 <example xmlns=\"http://www.example.org/\"/>" + 
    "               </annotation>" + 
    "             </speciesReference>" + 
    "           </listOfProducts>" + 
    "       </reaction>" + 
    "     </listOfReactions>" + 
    "   </model>" + 
    " </sbml>")
    @@d = LibSBML::readSBMLFromString(valid)
    assert( @@d.getNumErrors() == 0 )
    @@d = nil
    @@d = LibSBML::readSBMLFromString(invalid)
    assert( @@d.getNumErrors() == 9 )
  end

  def test_ReadSBML_line_col_numbers
    setXMLParser

    s = "<?xml version='1.0' encoding='UTF-8'?>\n" + 
    "<sbml xmlns='http://www.sbml.org/sbml/level2' level='2' version='1'>\n" + 
    "  <model id='testModel' name='testModel'>\n" + 
    "    <listOfReactions> <reaction/> </listOfReactions>\n" + 
    "  </model>\n" + 
    "</sbml>\n"
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m != nil )
    sb = @@m
    sb = @@m.getListOfReactions()
    sb = @@m.getReaction(0)
  end

  def test_ReadSBML_metaid
    s = wrapSBML_L2v1("<listOfFunctionDefinitions>" + 
    "  <functionDefinition metaid='fd'/>" + 
    "</listOfFunctionDefinitions>" + 
    "<listOfUnitDefinitions>" + 
    "  <unitDefinition metaid='ud'/>" + 
    "</listOfUnitDefinitions>" + 
    "<listOfCompartments>" + 
    "  <compartment metaid='c'/>" + 
    "</listOfCompartments>" + 
    "<listOfSpecies>" + 
    "  <species metaid='s'/>" + 
    "</listOfSpecies>" + 
    "<listOfParameters>" + 
    "  <parameter metaid='p'/>" + 
    "</listOfParameters>" + 
    "<listOfRules>" + 
    "  <rateRule metaid='rr'/>" + 
    "</listOfRules>" + 
    "<listOfReactions>" + 
    "  <reaction metaid='rx'/>" + 
    "</listOfReactions>" + 
    "<listOfEvents>" + 
    " <event metaid='e'/>" + 
    "</listOfEvents>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m != nil )
    sb = @@m.getFunctionDefinition(0)
    assert_equal true, sb.isSetMetaId()
    assert ((  "fd" == sb.getMetaId() ))
    sb = @@m.getUnitDefinition(0)
    assert_equal true, sb.isSetMetaId()
    assert ((  "ud" == sb.getMetaId() ))
    sb = @@m.getCompartment(0)
    assert_equal true, sb.isSetMetaId()
    assert ((  "c" == sb.getMetaId() ))
    sb = @@m.getSpecies(0)
    assert_equal true, sb.isSetMetaId()
    assert ((  "s" == sb.getMetaId() ))
    sb = @@m.getParameter(0)
    assert_equal true, sb.isSetMetaId()
    assert ((  "p" == sb.getMetaId() ))
    sb = @@m.getRule(0)
    assert_equal true, sb.isSetMetaId()
    assert ((  "rr" == sb.getMetaId() ))
    sb = @@m.getReaction(0)
    assert_equal true, sb.isSetMetaId()
    assert ((  "rx" == sb.getMetaId() ))
    sb = @@m.getEvent(0)
    assert_equal true, sb.isSetMetaId()
    assert ((  "e" == sb.getMetaId() ))
  end

  def test_ReadSBML_metaid_Event
    s = wrapSBML_L2v1("<listOfEvents>" + 
    "  <event metaid='e'>" + 
    "    <listOfEventAssignments metaid='loea'>" + 
    "      <eventAssignment metaid='ea'/>" + 
    "    </listOfEventAssignments>" + 
    "  </event>" + 
    "</listOfEvents>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m != nil )
    e = @@m.getEvent(0)
    sb = e
    assert_equal true, sb.isSetMetaId()
    assert ((  "e" == sb.getMetaId() ))
    sb = e.getListOfEventAssignments()
    assert_equal true, sb.isSetMetaId()
    assert ((  "loea" == sb.getMetaId() ))
    sb = e.getEventAssignment(0)
    assert_equal true, sb.isSetMetaId()
    assert ((  "ea" == sb.getMetaId() ))
  end

  def test_ReadSBML_metaid_ListOf
    s = wrapSBML_L2v1("<listOfFunctionDefinitions metaid='lofd'/>" + 
    "<listOfUnitDefinitions     metaid='loud'/>" + 
    "<listOfCompartments        metaid='loc'/>" + 
    "<listOfSpecies             metaid='los'/>" + 
    "<listOfParameters          metaid='lop'/>" + 
    "<listOfRules               metaid='lor'/>" + 
    "<listOfReactions           metaid='lorx'/>" + 
    "<listOfEvents              metaid='loe'/>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m != nil )
    sb = @@m.getListOfFunctionDefinitions()
    assert_equal true, sb.isSetMetaId()
    assert ((  "lofd" == sb.getMetaId() ))
    sb = @@m.getListOfUnitDefinitions()
    assert_equal true, sb.isSetMetaId()
    assert ((  "loud" == sb.getMetaId() ))
    sb = @@m.getListOfCompartments()
    assert_equal true, sb.isSetMetaId()
    assert ((  "loc" == sb.getMetaId() ))
    sb = @@m.getListOfSpecies()
    assert_equal true, sb.isSetMetaId()
    assert ((  "los" == sb.getMetaId() ))
    sb = @@m.getListOfParameters()
    assert_equal true, sb.isSetMetaId()
    assert ((  "lop" == sb.getMetaId() ))
    sb = @@m.getListOfRules()
    assert_equal true, sb.isSetMetaId()
    assert ((  "lor" == sb.getMetaId() ))
    sb = @@m.getListOfReactions()
    assert_equal true, sb.isSetMetaId()
    assert ((  "lorx" == sb.getMetaId() ))
    sb = @@m.getListOfEvents()
    assert_equal true, sb.isSetMetaId()
    assert ((  "loe" == sb.getMetaId() ))
  end

  def test_ReadSBML_metaid_Reaction
    s = wrapSBML_L2v1("<listOfReactions>" + 
    "  <reaction metaid='r'>" + 
    "    <listOfReactants metaid='lor'>" + 
    "      <speciesReference metaid='sr1'/>" + 
    "    </listOfReactants>" + 
    "    <listOfProducts metaid='lop'>" + 
    "      <speciesReference metaid='sr2'/>" + 
    "    </listOfProducts>" + 
    "    <listOfModifiers metaid='lom'>" + 
    "      <modifierSpeciesReference metaid='msr'/>" + 
    "    </listOfModifiers>" + 
    "    <kineticLaw metaid='kl'/>" + 
    "  </reaction>" + 
    "</listOfReactions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m != nil )
    r = @@m.getReaction(0)
    sb = r
    assert_equal true, sb.isSetMetaId()
    assert ((  "r" == sb.getMetaId() ))
    sb = r.getListOfReactants()
    assert_equal true, sb.isSetMetaId()
    assert ((  "lor" == sb.getMetaId() ))
    sb = r.getReactant(0)
    assert_equal true, sb.isSetMetaId()
    assert ((  "sr1" == sb.getMetaId() ))
    sb = r.getListOfProducts()
    assert_equal true, sb.isSetMetaId()
    assert ((  "lop" == sb.getMetaId() ))
    sb = r.getProduct(0)
    assert_equal true, sb.isSetMetaId()
    assert ((  "sr2" == sb.getMetaId() ))
    sb = r.getListOfModifiers()
    assert_equal true, sb.isSetMetaId()
    assert ((  "lom" == sb.getMetaId() ))
    sb = r.getModifier(0)
    assert_equal true, sb.isSetMetaId()
    assert ((  "msr" == sb.getMetaId() ))
    sb = r.getKineticLaw()
    assert_equal true, sb.isSetMetaId()
    assert ((  "kl" == sb.getMetaId() ))
  end

  def test_ReadSBML_metaid_Unit
    s = wrapSBML_L2v1("<listOfUnitDefinitions>" + 
    "  <unitDefinition metaid='ud'>" + 
    "    <listOfUnits metaid='lou'>" + 
    "      <unit metaid='u'/>" + 
    "    </listOfUnits>" + 
    "  </unitDefinition>" + 
    "</listOfUnitDefinitions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m != nil )
    ud = @@m.getUnitDefinition(0)
    sb = ud
    assert_equal true, sb.isSetMetaId()
    assert ((  "ud" == sb.getMetaId() ))
    sb = ud.getListOfUnits()
    assert_equal true, sb.isSetMetaId()
    assert ((  "lou" == sb.getMetaId() ))
    sb = ud.getUnit(0)
    assert_equal true, sb.isSetMetaId()
    assert ((  "u" == sb.getMetaId() ))
  end

  def test_ReadSBML_notes
    s = wrapSBML_L2v3("<listOfReactions>" + 
    "<reaction name='J1'>" + 
    "  <kineticLaw formula='k1*X0'>" + 
    "    <notes>This is a test note.</notes>" + 
    "    <listOfParameters>" + 
    "      <parameter name='k1' value='0'/>" + 
    "    </listOfParameters>" + 
    "  </kineticLaw>" + 
    "</reaction>" + 
    "</listOfReactions>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    r = @@m.getReaction(0)
    kl = r.getKineticLaw()
    assert( kl.getNotes() != nil )
    notes = kl.getNotes().getChild(0).getCharacters()
    assert( (  "This is a test note." != notes ) == false )
  end

  def test_ReadSBML_notes_ListOf
    s = wrapSBML_L2v1("<listOfFunctionDefinitions>" + 
    "  <notes>My Functions</notes>" + 
    "  <functionDefinition/>" + 
    "</listOfFunctionDefinitions>" + 
    "<listOfUnitDefinitions>" + 
    "  <notes>My Units</notes>" + 
    "  <unitDefinition/>" + 
    "</listOfUnitDefinitions>" + 
    "<listOfCompartments>" + 
    "  <notes>My Compartments</notes>" + 
    "  <compartment/>" + 
    "</listOfCompartments>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m != nil )
    sb = @@m.getListOfFunctionDefinitions()
    assert_equal true, sb.isSetNotes()
    notes = sb.getNotes().getChild(0).getCharacters()
    assert( (  "My Functions" != notes ) == false )
    sb = @@m.getListOfUnitDefinitions()
    assert_equal true, sb.isSetNotes()
    notes = sb.getNotes().getChild(0).getCharacters()
    assert( (  "My Units" != notes ) == false )
    sb = @@m.getListOfCompartments()
    assert_equal true, sb.isSetNotes()
    notes = sb.getNotes().getChild(0).getCharacters()
    assert( (  "My Compartments" != notes ) == false )
  end

  def test_ReadSBML_notes_sbml
    s = wrapXML("<sbml level='1' version='1'>" + 
    "  <notes>Notes are not allowed as part of the SBML element.</notes>" + 
    "</sbml>")
    @@d = LibSBML::readSBMLFromString(s)
    assert( @@d.getNotes() != nil )
    notes = @@d.getNotes().getChild(0).getCharacters()
    assert( (  "Notes are not allowed as part of the SBML element." != notes ) == false )
    assert( @@d.getNumErrors() > 0 )
  end

  def test_ReadSBML_notes_sbml_L2
    s = wrapXML("<sbml xmlns=\"http://www.sbml.org/sbml/level2\" level=\"2\" version=\"1\"> " + 
    "  <notes>" + 
    "    <html xmlns=\"http://www.w3.org/1999/xhtml\">" + 
    "		 </html>" + 
    "	  </notes>" + 
    "	  <model>" + 
    "   </model>" + 
    " </sbml>")
    @@d = LibSBML::readSBMLFromString(s)
    assert( @@d.getNotes() != nil )
    assert( @@d.getNumErrors() == 0 )
  end

  def test_ReadSBML_notes_xmlns
    s = wrapSBML_L2v3("<notes>" + 
    "  <body xmlns=\"http://www.w3.org/1999/xhtml\">Some text.</body>" + 
    "</notes>")
    @@d = LibSBML::readSBMLFromString(s)
    @@m = @@d.getModel()
    assert( @@m.getNotes() != nil )
    ns = @@m.getNotes().getChild(0).getNamespaces()
    assert( ns.getLength() == 1 )
    assert ((  "http://www.w3.org/1999/xhtml" == ns.getURI(0) ))
    notes = @@m.getNotes().getChild(0).getChild(0).getCharacters()
    assert( (  "Some text." != notes ) == false )
  end

end
