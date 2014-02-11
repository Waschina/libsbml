/**
 * @cond doxygenLibsbmlInternal
 *
 * @file    ASTLambdaFunctionNode.cpp
 * @brief   Base Abstract Syntax Tree (AST) class.
 * @author  Sarah Keating
 * 
 * <!--------------------------------------------------------------------------
 * This file is part of libSBML.  Please visit http://sbml.org for more
 * information about SBML, and the latest version of libSBML.
 *
 * Copyright (C) 2009-2012 jointly by the following organizations: 
 *     1. California Institute of Technology, Pasadena, CA, USA
 *     2. EMBL European Bioinformatics Institute (EBML-EBI), Hinxton, UK
 *  
 * Copyright (C) 2006-2008 by the California Institute of Technology,
 *     Pasadena, CA, USA 
 *  
 * Copyright (C) 2002-2005 jointly by the following organizations: 
 *     1. California Institute of Technology, Pasadena, CA, USA
 *     2. Japan Science and Technology Agency, Japan
 * 
 * This library is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation.  A copy of the license agreement is provided
 * in the file named "LICENSE.txt" included with this software distribution and
 * also available online as http://sbml.org/software/libsbml/license.html
 * ------------------------------------------------------------------------ -->
 */

#include <sbml/math/ASTLambdaFunctionNode.h>
#include <sbml/math/ASTNaryFunctionNode.h>
#include <sbml/math/ASTNumber.h>
#include <sbml/math/ASTFunction.h>
#include <sbml/math/ASTNode.h>

/** @cond doxygen-ignored */

using namespace std;

/** @endcond */

LIBSBML_CPP_NAMESPACE_BEGIN

ASTLambdaFunctionNode::ASTLambdaFunctionNode (int type) :
  ASTNaryFunctionNode(type)
    , mNumBvars ( 0 )

{
}
  
  
  /**
   * Copy constructor
   */
ASTLambdaFunctionNode::ASTLambdaFunctionNode (const ASTLambdaFunctionNode& orig):
  ASTNaryFunctionNode(orig)
    , mNumBvars (orig.mNumBvars)
{
}
  /**
   * Assignment operator for ASTNode.
   */
ASTLambdaFunctionNode&
ASTLambdaFunctionNode::operator=(const ASTLambdaFunctionNode& rhs)
{
  if(&rhs!=this)
  {
    this->ASTNaryFunctionNode::operator =(rhs);
    mNumBvars = rhs.mNumBvars;
  }
  return *this;
}
  /**
   * Destroys this ASTNode, including any child nodes.
   */
ASTLambdaFunctionNode::~ASTLambdaFunctionNode ()
{
}

int
ASTLambdaFunctionNode::getTypeCode () const
{
  return AST_TYPECODE_FUNCTION_LAMBDA;
}


  /**
   * Creates a copy (clone).
   */
ASTLambdaFunctionNode*
ASTLambdaFunctionNode::deepCopy () const
{
  return new ASTLambdaFunctionNode(*this);
}

int
ASTLambdaFunctionNode::swapChildren(ASTFunction* that)
{
  if (that->getUnaryFunction() != NULL)
  {
    return ASTFunctionBase::swapChildren(that->getUnaryFunction());
  }
  else if (that->getBinaryFunction() != NULL)
  {
    return ASTFunctionBase::swapChildren(that->getBinaryFunction());
  }
  else if (that->getNaryFunction() != NULL)
  {
    return ASTFunctionBase::swapChildren(that->getNaryFunction());
  }
  else if (that->getUserFunction() != NULL)
  {
    return ASTFunctionBase::swapChildren(that->getUserFunction());
  }
  else if (that->getLambda() != NULL)
  {
    return ASTFunctionBase::swapChildren(that->getLambda());
  }
  else if (that->getPiecewise() != NULL)
  {
    return ASTFunctionBase::swapChildren(that->getPiecewise());
  }
  else if (that->getCSymbol() != NULL)
  {
    return ASTFunctionBase::swapChildren(that->getCSymbol()->getDelay());;
  }
  else if (that->getQualifier() != NULL)
  {
    return ASTFunctionBase::swapChildren(that->getQualifier());
  }
  else if (that->getSemantics() != NULL)
  {
    return ASTFunctionBase::swapChildren(that->getSemantics());
  }
  else
  {
    return LIBSBML_OPERATION_FAILED;
  }
}


unsigned int 
ASTLambdaFunctionNode::getNumBvars() const
{
  return mNumBvars;
}

  
  
int 
ASTLambdaFunctionNode::setNumBvars(unsigned int numBvars)
{
  mNumBvars = numBvars;
  return LIBSBML_OPERATION_SUCCESS;

}
int
ASTLambdaFunctionNode::addChild(ASTBase* child, bool inRead)
{
  // now here what I want to do is just keep track of the number
  // of children being added so the mNumBvars 
  // variables can be given appropriate values

  // but not if we are reading a stream because then we already know

  bool bvar = (child->getType() == AST_QUALIFIER_BVAR);
  if (inRead == false)
  {
    if (bvar == true)
    {
      mNumBvars++;
      return ASTNaryFunctionNode::addChild(child);
    }
    else
    {
      return ASTNaryFunctionNode::addChild(child);
    }
  }

  return ASTNaryFunctionNode::addChild(child);
}

  
ASTBase* 
ASTLambdaFunctionNode::getChild (unsigned int n) const
{
  /* HACK TO REPLICATE OLD AST */
  /* do not return a node with teh bvar type
   * return the child of the bvar type
   */
  if (ASTFunctionBase::getNumChildren() <= n)
  {
    return NULL;
  }

  if (ASTFunctionBase::getChild(n)->getType() == AST_QUALIFIER_BVAR)
  {
    ASTBase * base = ASTFunctionBase::getChild(n);
    ASTNode * bvar = dynamic_cast<ASTNode*>(base);
    //if (base->getFunction() != NULL)
    //{
    //  bvar = static_cast<ASTFunction*>(base->getFunction());
    //}
    //else
    //{
    //  bvar = static_cast<ASTFunction*>(base);
    //}
    if (bvar != NULL)
    {
      if (bvar->getNumChildren() > 0)
      {
        return bvar->getChild(0);
      }
      else
      {
        return NULL;
      }
    }
    else
    {
      return NULL;
    }
  }
  else
  {
    return ASTFunctionBase::getChild(n);
  }
}

  


void
ASTLambdaFunctionNode::write(XMLOutputStream& stream) const
{
  if (&stream == NULL) return;

  ASTBase::writeStartElement(stream);

  /* HACK TO REPLICATE OLD AST */
  /* all but the last child will be wrapped as bvars
   * even if they are technically not
   */
  unsigned int numChildren = ASTFunctionBase::getNumChildren();
  for (unsigned int i = 0; i < numChildren; i++)
  {
    if (i < numChildren-1 && ASTFunctionBase::getChild(i)->getType() != AST_QUALIFIER_BVAR)
    {
      ASTQualifierNode * bvar = new ASTQualifierNode(AST_QUALIFIER_BVAR);
      bvar->addChild(ASTFunctionBase::getChild(i)->deepCopy());
      bvar->write(stream);
      delete bvar;
    }
    else
    {
      ASTFunctionBase::getChild(i)->write(stream);
    }
  }
    
  stream.endElement("lambda");
}

bool
ASTLambdaFunctionNode::read(XMLInputStream& stream, const std::string& reqd_prefix)
{
  bool read = false;
  ASTBase * child = NULL;
  const char*      name;

  unsigned int numBvars = getNumBvars();
  unsigned int numChildrenAdded = 0;
 
  // read in bvars
  // these are functions as they will be created as ASTQualifierNodes
  while(numChildrenAdded < numBvars)
  {
    child = new ASTFunction();
    read = child->read(stream, reqd_prefix);

    if (read == true && addChild(child, true) == LIBSBML_OPERATION_SUCCESS)
    {
      numChildrenAdded++;
    }
    else
    {
      read = false;
      break;
    }
  }

  // if we had no bvars to read mark read as true so we will continue
  if (numBvars == 0)
  {
    read = true;
  }

  while (read == true && stream.isGood() 
                      && numChildrenAdded < getExpectedNumChildren())
  {
    stream.skipText();

    name = stream.peek().getName().c_str();

    if (representsNumber(ASTBase::getTypeFromName(name)) == true)
    {
      child = new ASTNumber();
    }
    else 
    {
      child = new ASTFunction();
    }

    read = child->read(stream, reqd_prefix);

    stream.skipText();

    if (addChild(child) == LIBSBML_OPERATION_SUCCESS)
    {
      numChildrenAdded++;
      read = true;
    }
    else
    {
      read = false;
      break;
    }
  }

  return read;
}



bool 
ASTLambdaFunctionNode::hasCorrectNumberArguments() const
{
  bool correctNumArgs = true;

  if (getNumChildren() < 1)
  {
    correctNumArgs = false;
  }

  return correctNumArgs;
}




LIBSBML_CPP_NAMESPACE_END


/** @endcond */

