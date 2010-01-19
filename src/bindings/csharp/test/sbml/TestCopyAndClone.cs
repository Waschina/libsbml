/// 
///  @file    TestCopyAndClone.cs
///  @brief   Read SBML unit tests
///  @author  Frank Bergmann (Csharp conversion)
///  @author  Akiya Jouraku (Csharp conversion)
///  @author  Ben Bornstein 
/// 
///  $Id$
///  $HeadURL$
/// 
///  This test file was converted from src/sbml/test/TestCopyAndClone.cpp
///  with the help of conversion sciprt (ctest_converter.pl).
/// 
/// <!---------------------------------------------------------------------------
///  This file is part of libSBML.  Please visit http://sbml.org for more
///  information about SBML, and the latest version of libSBML.
/// 
///  Copyright 2005-2009 California Institute of Technology.
///  Copyright 2002-2005 California Institute of Technology and
///                      Japan Science and Technology Corporation.
///  
///  This library is free software; you can redistribute it and/or modify it
///  under the terms of the GNU Lesser General Public License as published by
///  the Free Software Foundation.  A copy of the license agreement is provided
///  in the file named "LICENSE.txt" included with this software distribution
///  and also available online as http://sbml.org/software/libsbml/license.html
/// --------------------------------------------------------------------------->*/


namespace LibSBMLCSTest {

  using libsbml;

  using  System.IO;

  public class TestCopyAndClone {
    public class AssertionError : System.Exception 
    {
      public AssertionError() : base()
      {
        
      }
    }


    static void assertTrue(bool condition)
    {
      if (condition == true)
      {
        return;
      }
      throw new AssertionError();
    }

    static void assertEquals(object a, object b)
    {
      if ( (a == null) && (b == null) )
      {
        return;
      }
      else if ( (a == null) || (b == null) )
      {
        throw new AssertionError();
      }
      else if (a.Equals(b))
      {
        return;
      }
  
      throw new AssertionError();
    }

    static void assertNotEquals(object a, object b)
    {
      if ( (a == null) && (b == null) )
      {
        throw new AssertionError();
      }
      else if ( (a == null) || (b == null) )
      {
        return;
      }
      else if (a.Equals(b))
      {
        throw new AssertionError();
      }
    }

    static void assertEquals(bool a, bool b)
    {
      if ( a == b )
      {
        return;
      }
      throw new AssertionError();
    }

    static void assertNotEquals(bool a, bool b)
    {
      if ( a != b )
      {
        return;
      }
      throw new AssertionError();
    }

    static void assertEquals(int a, int b)
    {
      if ( a == b )
      {
        return;
      }
      throw new AssertionError();
    }

    static void assertNotEquals(int a, int b)
    {
      if ( a != b )
      {
        return;
      }
      throw new AssertionError();
    }


    public void test_CompartmentType_assignmentOperator()
    {
      CompartmentType o1 = new CompartmentType(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      CompartmentType o2 = new CompartmentType(2,4);
      o2 = o1;
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_CompartmentType_clone()
    {
      CompartmentType o1 = new CompartmentType(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      CompartmentType o2 = o1.clone();
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_CompartmentType_copyConstructor()
    {
      CompartmentType o1 = new CompartmentType(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      CompartmentType o2 = new CompartmentType(o1);
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Compartment_assignmentOperator()
    {
      Compartment o1 = new Compartment(2,4);
      o1.setId("c");
      o1.setOutside("c2");
      assertTrue( o1.getId() ==  "c" );
      assertTrue( o1.getOutside() ==  "c2" );
      Compartment o2 = new Compartment(2,4);
      o2 = o1;
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getOutside() ==  "c2" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Compartment_clone()
    {
      Compartment o1 = new Compartment(2,4);
      o1.setId("c");
      o1.setOutside("c2");
      assertTrue( o1.getId() ==  "c" );
      assertTrue( o1.getOutside() ==  "c2" );
      Compartment o2 = o1.clone();
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getOutside() ==  "c2" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Compartment_copyConstructor()
    {
      Compartment o1 = new Compartment(2,4);
      o1.setId("c");
      o1.setOutside("c2");
      assertTrue( o1.getId() ==  "c" );
      assertTrue( o1.getOutside() ==  "c2" );
      Compartment o2 = new Compartment(o1);
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getOutside() ==  "c2" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Constraint_assignmentOperator()
    {
      Constraint o1 = new Constraint(2,4);
      o1.setMetaId("c");
      assertTrue( o1.getMetaId() ==  "c" );
      XMLNode text = XMLNode.convertStringToXMLNode(" Some text ");
      XMLTriple triple = new XMLTriple("p", "http://www.w3.org/1999/xhtml", "");
      XMLAttributes att = new XMLAttributes();
      XMLNamespaces xmlns = new XMLNamespaces();
      xmlns.add("http://www.w3.org/1999/xhtml");
      XMLNode p = new XMLNode(triple,att,xmlns);
      p.addChild(text);
      XMLTriple triple1 = new XMLTriple("message", "", "");
      XMLAttributes att1 = new XMLAttributes();
      XMLNode message = new XMLNode(triple1,att1);
      message.addChild(p);
      ASTNode math = new ASTNode(libsbml.AST_CONSTANT_PI);
      o1.setMath(math);
      o1.setMessage(message);
      math = null;
      message = null;
      assertTrue( o1.getMath() != null );
      assertTrue( o1.getMessage() != null );
      Constraint o2 = new Constraint(2,4);
      o2 = o1;
      assertTrue( o2.getMetaId() ==  "c" );
      assertTrue( o1.getMath() != null );
      assertTrue( o1.getMessage() != null );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Constraint_clone()
    {
      Constraint o1 = new Constraint(2,4);
      o1.setMetaId("c");
      assertTrue( o1.getMetaId() ==  "c" );
      XMLNode text = XMLNode.convertStringToXMLNode(" Some text ");
      XMLTriple triple = new XMLTriple("p", "http://www.w3.org/1999/xhtml", "");
      XMLAttributes att = new XMLAttributes();
      XMLNamespaces xmlns = new XMLNamespaces();
      xmlns.add("http://www.w3.org/1999/xhtml");
      XMLNode p = new XMLNode(triple,att,xmlns);
      p.addChild(text);
      XMLTriple triple1 = new XMLTriple("message", "", "");
      XMLAttributes att1 = new XMLAttributes();
      XMLNode message = new XMLNode(triple1,att1);
      message.addChild(p);
      ASTNode math = new ASTNode(libsbml.AST_CONSTANT_PI);
      o1.setMath(math);
      o1.setMessage(message);
      math = null;
      message = null;
      assertTrue( o1.getMath() != null );
      assertTrue( o1.getMessage() != null );
      Constraint o2 = o1.clone();
      assertTrue( o2.getMetaId() ==  "c" );
      assertTrue( o1.getMath() != null );
      assertTrue( o1.getMessage() != null );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Constraint_copyConstructor()
    {
      Constraint o1 = new Constraint(2,4);
      o1.setMetaId("c");
      assertTrue( o1.getMetaId() ==  "c" );
      XMLNode text = XMLNode.convertStringToXMLNode(" Some text ");
      XMLTriple triple = new XMLTriple("p", "http://www.w3.org/1999/xhtml", "");
      XMLAttributes att = new XMLAttributes();
      XMLNamespaces xmlns = new XMLNamespaces();
      xmlns.add("http://www.w3.org/1999/xhtml");
      XMLNode p = new XMLNode(triple,att,xmlns);
      p.addChild(text);
      XMLTriple triple1 = new XMLTriple("message", "", "");
      XMLAttributes att1 = new XMLAttributes();
      XMLNode message = new XMLNode(triple1,att1);
      message.addChild(p);
      ASTNode math = new ASTNode(libsbml.AST_CONSTANT_PI);
      o1.setMath(math);
      o1.setMessage(message);
      math = null;
      message = null;
      assertTrue( o1.getMath() != null );
      assertTrue( o1.getMessage() != null );
      Constraint o2 = new Constraint(o1);
      assertTrue( o2.getMetaId() ==  "c" );
      assertTrue( o1.getMath() != null );
      assertTrue( o1.getMessage() != null );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Delay_assignmentOperator()
    {
      Delay o1 = new Delay(2,4);
      ASTNode node = new ASTNode(libsbml.AST_CONSTANT_PI);
      o1.setMath(node);
      node = null;
      assertTrue( o1.getMath() != null );
      Delay o2 = new Delay(2,4);
      o2 = o1;
      assertTrue( o1.getMath() != null );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Delay_clone()
    {
      Delay o1 = new Delay(2,4);
      ASTNode node = new ASTNode(libsbml.AST_CONSTANT_PI);
      o1.setMath(node);
      node = null;
      assertTrue( o1.getMath() != null );
      Delay o2 = o1.clone();
      assertTrue( o1.getMath() != null );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Delay_copyConstructor()
    {
      Delay o1 = new Delay(2,4);
      ASTNode node = new ASTNode(libsbml.AST_CONSTANT_PI);
      o1.setMath(node);
      node = null;
      assertTrue( o1.getMath() != null );
      Delay o2 = new Delay(o1);
      assertTrue( o2.getMath() != null );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_EventAssignment_assignmentOperator()
    {
      EventAssignment o1 = new EventAssignment(2,4);
      o1.setVariable("c2");
      assertTrue( o1.getVariable() ==  "c2" );
      ASTNode node = new ASTNode(libsbml.AST_CONSTANT_PI);
      o1.setMath(node);
      node = null;
      assertTrue( o1.getMath() != null );
      EventAssignment o2 = new EventAssignment(2,4);
      o2 = o1;
      assertTrue( o2.getVariable() ==  "c2" );
      assertTrue( o2.getMath() != null );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_EventAssignment_clone()
    {
      EventAssignment o1 = new EventAssignment(2,4);
      o1.setVariable("c2");
      assertTrue( o1.getVariable() ==  "c2" );
      ASTNode node = new ASTNode(libsbml.AST_CONSTANT_PI);
      o1.setMath(node);
      node = null;
      assertTrue( o1.getMath() != null );
      EventAssignment o2 = o1.clone();
      assertTrue( o2.getVariable() ==  "c2" );
      assertTrue( o2.getMath() != null );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_EventAssignment_copyConstructor()
    {
      EventAssignment o1 = new EventAssignment(2,4);
      o1.setVariable("c2");
      assertTrue( o1.getVariable() ==  "c2" );
      ASTNode node = new ASTNode(libsbml.AST_CONSTANT_PI);
      o1.setMath(node);
      node = null;
      assertTrue( o1.getMath() != null );
      EventAssignment o2 = new EventAssignment(o1);
      assertTrue( o2.getVariable() ==  "c2" );
      assertTrue( o2.getMath() != null );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Event_assignmentOperator()
    {
      Event o1 = new Event(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      Event o2 = new Event(2,4);
      o2 = o1;
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Event_clone()
    {
      Event o1 = new Event(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      Event o2 = o1.clone();
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Event_copyConstructor()
    {
      Event o1 = new Event(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      Event o2 = new Event(o1);
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_FunctionDefinition_assignmentOperator()
    {
      FunctionDefinition o1 = new FunctionDefinition(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      ASTNode node = new ASTNode(libsbml.AST_CONSTANT_PI);
      o1.setMath(node);
      node = null;
      assertTrue( o1.getMath() != null );
      FunctionDefinition o2 = new FunctionDefinition(2,4);
      o2 = o1;
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getMath() != null );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_FunctionDefinition_clone()
    {
      FunctionDefinition o1 = new FunctionDefinition(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      ASTNode node = new ASTNode(libsbml.AST_CONSTANT_PI);
      o1.setMath(node);
      node = null;
      assertTrue( o1.getMath() != null );
      FunctionDefinition o2 = o1.clone();
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getMath() != null );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_FunctionDefinition_copyConstructor()
    {
      FunctionDefinition o1 = new FunctionDefinition(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      ASTNode node = new ASTNode(libsbml.AST_CONSTANT_PI);
      o1.setMath(node);
      node = null;
      assertTrue( o1.getMath() != null );
      FunctionDefinition o2 = new FunctionDefinition(o1);
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getMath() != null );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_InitialAssignment_assignmentOperator()
    {
      InitialAssignment o1 = new InitialAssignment(2,4);
      o1.setSymbol("c");
      assertTrue( o1.getId() ==  "c" );
      InitialAssignment o2 = new InitialAssignment(2,4);
      o2 = o1;
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_InitialAssignment_clone()
    {
      InitialAssignment o1 = new InitialAssignment(2,4);
      o1.setSymbol("c");
      assertTrue( o1.getId() ==  "c" );
      InitialAssignment o2 = o1.clone();
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_InitialAssignment_copyConstructor()
    {
      InitialAssignment o1 = new InitialAssignment(2,4);
      o1.setSymbol("c");
      assertTrue( o1.getId() ==  "c" );
      InitialAssignment o2 = new InitialAssignment(o1);
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_KineticLaw_assignmentOperator()
    {
      KineticLaw o1 = new KineticLaw(2,4);
      Parameter p = new Parameter(2,4);
      p.setId("jake");
      o1.addParameter(p);
      p = null;
      assertTrue( o1.getNumParameters() == 1 );
      assertTrue( o1.getParameter(0).getId() ==  "jake" );
      KineticLaw o2 = new KineticLaw(2,4);
      o2 = o1;
      assertTrue( o2.getNumParameters() == 1 );
      assertTrue( o2.getParameter(0).getId() ==  "jake" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_KineticLaw_clone()
    {
      KineticLaw o1 = new KineticLaw(2,4);
      Parameter p = new Parameter(2,4);
      p.setId("jake");
      o1.addParameter(p);
      p = null;
      assertTrue( o1.getNumParameters() == 1 );
      assertTrue( o1.getParameter(0).getId() ==  "jake" );
      KineticLaw o2 = o1.clone();
      assertTrue( o2.getNumParameters() == 1 );
      assertTrue( o2.getParameter(0).getId() ==  "jake" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_KineticLaw_copyConstructor()
    {
      KineticLaw o1 = new KineticLaw(2,4);
      Parameter p = new Parameter(2,4);
      p.setId("jake");
      o1.addParameter(p);
      p = null;
      assertTrue( o1.getNumParameters() == 1 );
      assertTrue( o1.getParameter(0).getId() ==  "jake" );
      KineticLaw o2 = new KineticLaw(o1);
      assertTrue( o2.getNumParameters() == 1 );
      assertTrue( o2.getParameter(0).getId() ==  "jake" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_ListOf_assignmentOperator()
    {
      ListOf o1 = new ListOf();
      Species s = new Species(2,1);
      s.setId("species_1");
      o1.append(s);
      s = null;
      ListOf o2 = new ListOf();
      o2 = o1;
      assertTrue( o2.size() == 1 );
      assertTrue( ((Species) o2.get(0)).getId() ==  "species_1" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_ListOf_clone()
    {
      ListOf o1 = new ListOf();
      Species s = new Species(2,1);
      s.setId("species_1");
      o1.append(s);
      s = null;
      ListOf o2 = (ListOf) o1.clone();
      assertTrue( o2.size() == 1 );
      assertTrue( ((Species) o2.get(0)).getId() ==  "species_1" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_ListOf_copyConstructor()
    {
      ListOf o1 = new ListOf();
      Species s = new Species(2,1);
      s.setId("species_1");
      o1.append(s);
      s = null;
      ListOf o2 = new ListOf(o1);
      assertTrue( o2.size() == 1 );
      assertTrue( ((Species) o2.get(0)).getId() ==  "species_1" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Model_assignmentOperator()
    {
      Model o1 = new Model(2,4);
      o1.setId("c");
      Parameter p = new Parameter(2,4);
      p.setId("alex");
      o1.addParameter(p);
      p = null;
      assertTrue( o1.getId() ==  "c" );
      assertTrue( o1.getNumParameters() == 1 );
      assertTrue( o1.getParameter(0).getId() ==  "alex" );
      Model o2 = new Model(2,4);
      o2 = o1;
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getNumParameters() == 1 );
      assertTrue( o2.getParameter(0).getId() ==  "alex" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Model_clone()
    {
      Model o1 = new Model(2,4);
      o1.setId("c");
      Parameter p = new Parameter(2,4);
      p.setId("alex");
      o1.addParameter(p);
      p = null;
      assertTrue( o1.getId() ==  "c" );
      assertTrue( o1.getNumParameters() == 1 );
      assertTrue( o1.getParameter(0).getId() ==  "alex" );
      Model o2 = o1.clone();
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getNumParameters() == 1 );
      assertTrue( o2.getParameter(0).getId() ==  "alex" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Model_copyConstructor()
    {
      Model o1 = new Model(2,4);
      o1.setId("c");
      Parameter p = new Parameter(2,4);
      p.setId("alex");
      o1.addParameter(p);
      p = null;
      assertTrue( o1.getId() ==  "c" );
      assertTrue( o1.getNumParameters() == 1 );
      assertTrue( o1.getParameter(0).getId() ==  "alex" );
      Model o2 = new Model(o1);
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getNumParameters() == 1 );
      assertTrue( o2.getParameter(0).getId() ==  "alex" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Parameter_assignmentOperator()
    {
      Parameter o1 = new Parameter(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      Parameter o2 = new Parameter(2,4);
      o2 = o1;
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Parameter_clone()
    {
      Parameter o1 = new Parameter(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      Parameter o2 = o1.clone();
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Parameter_copyConstructor()
    {
      Parameter o1 = new Parameter(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      Parameter o2 = new Parameter(o1);
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Reaction_assignmentOperator()
    {
      Reaction o1 = new Reaction(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      KineticLaw kl = new KineticLaw(2,4);
      o1.setKineticLaw(kl);
      kl = null;
      assertTrue( o1.isSetKineticLaw() == true );
      assertNotEquals(o1.getKineticLaw(),null);
      Reaction o2 = new Reaction(2,4);
      o2 = o1;
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.isSetKineticLaw() == true );
      assertNotEquals(o2.getKineticLaw(),null);
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Reaction_clone()
    {
      Reaction o1 = new Reaction(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      KineticLaw kl = new KineticLaw(2,4);
      o1.setKineticLaw(kl);
      kl = null;
      assertTrue( o1.isSetKineticLaw() == true );
      assertNotEquals(o1.getKineticLaw(),null);
      Reaction o2 = o1.clone();
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.isSetKineticLaw() == true );
      assertNotEquals(o2.getKineticLaw(),null);
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Reaction_copyConstructor()
    {
      Reaction o1 = new Reaction(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      KineticLaw kl = new KineticLaw(2,4);
      o1.setKineticLaw(kl);
      kl = null;
      assertTrue( o1.isSetKineticLaw() == true );
      assertNotEquals(o1.getKineticLaw(),null);
      Reaction o2 = new Reaction(o1);
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.isSetKineticLaw() == true );
      assertNotEquals(o2.getKineticLaw(),null);
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Rule_assignmentOperator()
    {
      Rule o1 = new RateRule(2,4);
      o1.setVariable("a");
      assertTrue( o1.getVariable() ==  "a" );
      ASTNode node = new ASTNode(libsbml.AST_CONSTANT_PI);
      o1.setMath(node);
      node = null;
      assertTrue( o1.isSetMath() == true );
      Rule o2 = new RateRule(2,4);
      o2 = o1;
      assertTrue( o2.getVariable() ==  "a" );
      assertTrue( o2.isSetMath() == true );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Rule_clone()
    {
      Rule o1 = new RateRule(2,1);
      o1.setVariable("a");
      assertTrue( o1.getVariable() ==  "a" );
      ASTNode node = new ASTNode(libsbml.AST_CONSTANT_PI);
      o1.setMath(node);
      node = null;
      assertTrue( o1.isSetMath() == true );
      Rule o2 = o1.clone();
      assertTrue( o2.getVariable() ==  "a" );
      assertTrue( o2.isSetMath() == true );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Rule_copyConstructor()
    {
      Rule o1 = new RateRule(2,1);
      o1.setVariable("a");
      assertTrue( o1.getVariable() ==  "a" );
      ASTNode node = new ASTNode(libsbml.AST_CONSTANT_PI);
      o1.setMath(node);
      node = null;
      assertTrue( o1.isSetMath() == true );
      Rule o2 = new Rule(o1);
      assertTrue( o2.getVariable() ==  "a" );
      assertTrue( o2.isSetMath() == true );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_SBMLDocument_assignmentOperator()
    {
      SBMLDocument o1 = new SBMLDocument();
      o1.setLevelAndVersion(2,1,false);
      assertTrue( o1.getLevel() == 2 );
      assertTrue( o1.getVersion() == 1 );
      SBMLDocument o2 = new SBMLDocument();
      o2 = o1;
      assertTrue( o2.getLevel() == 2 );
      assertTrue( o2.getVersion() == 1 );
      o2 = null;
      o1 = null;
    }

    public void test_SBMLDocument_clone()
    {
      SBMLDocument o1 = new SBMLDocument();
      o1.setLevelAndVersion(1,1,false);
      Model m = new Model(1,1);
      m.setId("foo");
      o1.setModel(m);
      assertTrue( o1.getLevel() == 1 );
      assertTrue( o1.getVersion() == 1 );
      assertTrue( o1.getModel().getId() ==  "foo" );
      assertTrue( o1.getModel().getLevel() == 1 );
      assertTrue( o1.getModel().getVersion() == 1 );
      assertTrue( o1.getModel().getSBMLDocument() == o1 );
      SBMLDocument o2 = o1.clone();
      assertTrue( o2.getLevel() == 1 );
      assertTrue( o2.getVersion() == 1 );
      assertTrue( o2.getModel().getId() ==  "foo" );
      assertTrue( o2.getModel().getLevel() == 1 );
      assertTrue( o2.getModel().getVersion() == 1 );
      assertTrue( o2.getModel().getSBMLDocument() == o2 );
      o2 = null;
      o1 = null;
    }

    public void test_SBMLDocument_copyConstructor()
    {
      SBMLDocument o1 = new SBMLDocument();
      o1.setLevelAndVersion(2,1,false);
      assertTrue( o1.getLevel() == 2 );
      assertTrue( o1.getVersion() == 1 );
      SBMLDocument o2 = new SBMLDocument(o1);
      assertTrue( o2.getLevel() == 2 );
      assertTrue( o2.getVersion() == 1 );
      o2 = null;
      o1 = null;
    }

    public void test_SpeciesReference_assignmentOperator()
    {
      SpeciesReference o1 = new SpeciesReference(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      SpeciesReference o2 = new SpeciesReference(2,4);
      o2 = o1;
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_SpeciesReference_clone()
    {
      SpeciesReference o1 = new SpeciesReference(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      SpeciesReference o2 = o1.clone();
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_SpeciesReference_copyConstructor()
    {
      SpeciesReference o1 = new SpeciesReference(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      SpeciesReference o2 = new SpeciesReference(o1);
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_SpeciesType_assignmentOperator()
    {
      SpeciesType o1 = new SpeciesType(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      SpeciesType o2 = new SpeciesType(2,4);
      o2 = o1;
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_SpeciesType_clone()
    {
      SpeciesType o1 = new SpeciesType(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      SpeciesType o2 = o1.clone();
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_SpeciesType_copyConstructor()
    {
      SpeciesType o1 = new SpeciesType(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      SpeciesType o2 = new SpeciesType(o1);
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Species_assignmentOperator()
    {
      Species o1 = new Species(2,4);
      o1.setId("c");
      o1.setSpeciesType("c1");
      assertTrue( o1.getId() ==  "c" );
      assertEquals(o1.getSpeciesType(), "c1");
      Species o2 = new Species(2,4);
      o2 = o1;
      assertTrue( o2.getId() ==  "c" );
      assertEquals(o2.getSpeciesType(), "c1");
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Species_clone()
    {
      Species o1 = new Species(2,4);
      o1.setId("c");
      o1.setSpeciesType("c1");
      assertTrue( o1.getId() ==  "c" );
      assertEquals(o1.getSpeciesType(), "c1");
      Species o2 = o1.clone();
      assertTrue( o2.getId() ==  "c" );
      assertEquals(o2.getSpeciesType(), "c1");
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Species_copyConstructor()
    {
      Species o1 = new Species(2,4);
      o1.setId("c");
      o1.setSpeciesType("c1");
      assertTrue( o1.getId() ==  "c" );
      assertEquals(o1.getSpeciesType(), "c1");
      Species o2 = new Species(o1);
      assertTrue( o2.getId() ==  "c" );
      assertEquals(o2.getSpeciesType(), "c1");
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Trigger_assignmentOperator()
    {
      Trigger o1 = new Trigger(2,4);
      ASTNode node = new ASTNode(libsbml.AST_CONSTANT_PI);
      o1.setMath(node);
      node = null;
      assertTrue( o1.getMath() != null );
      Trigger o2 = new Trigger(2,4);
      o2 = o1;
      assertTrue( o1.getMath() != null );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Trigger_clone()
    {
      Trigger o1 = new Trigger(2,4);
      ASTNode node = new ASTNode(libsbml.AST_CONSTANT_PI);
      o1.setMath(node);
      node = null;
      assertTrue( o1.getMath() != null );
      Trigger o2 = o1.clone();
      assertTrue( o1.getMath() != null );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Trigger_copyConstructor()
    {
      Trigger o1 = new Trigger(2,4);
      ASTNode node = new ASTNode(libsbml.AST_CONSTANT_PI);
      o1.setMath(node);
      node = null;
      assertTrue( o1.getMath() != null );
      Trigger o2 = new Trigger(o1);
      assertTrue( o2.getMath() != null );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_UnitDefinition_assignmentOperator()
    {
      UnitDefinition o1 = new UnitDefinition(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      UnitDefinition o2 = new UnitDefinition(2,4);
      o2 = o1;
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_UnitDefinition_clone()
    {
      UnitDefinition o1 = new UnitDefinition(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      UnitDefinition o2 = o1.clone();
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_UnitDefinition_copyConstructor()
    {
      UnitDefinition o1 = new UnitDefinition(2,4);
      o1.setId("c");
      assertTrue( o1.getId() ==  "c" );
      UnitDefinition o2 = new UnitDefinition(o1);
      assertTrue( o2.getId() ==  "c" );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Unit_assignmentOperator()
    {
      Unit o1 = new Unit(2,4);
      o1.setKind(libsbml.UNIT_KIND_MOLE);
      assertTrue( o1.getKind() == libsbml.UNIT_KIND_MOLE );
      Unit o2 = new Unit(2,4);
      o2 = o1;
      assertTrue( o2.getKind() == libsbml.UNIT_KIND_MOLE );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Unit_clone()
    {
      Unit o1 = new Unit(2,4);
      o1.setKind(libsbml.UNIT_KIND_MOLE);
      assertTrue( o1.getKind() == libsbml.UNIT_KIND_MOLE );
      Unit o2 = o1.clone();
      assertTrue( o2.getKind() == libsbml.UNIT_KIND_MOLE );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

    public void test_Unit_copyConstructor()
    {
      Unit o1 = new Unit(2,4);
      o1.setKind(libsbml.UNIT_KIND_MOLE);
      assertTrue( o1.getKind() == libsbml.UNIT_KIND_MOLE );
      Unit o2 = new Unit(o1);
      assertTrue( o2.getKind() == libsbml.UNIT_KIND_MOLE );
      assertTrue( o2.getParentSBMLObject() == o1.getParentSBMLObject() );
      o2 = null;
      o1 = null;
    }

  }
}
