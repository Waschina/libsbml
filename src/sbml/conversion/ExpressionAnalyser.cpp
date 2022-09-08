
/**
 * @file    ExpressionAnalyser.cpp
 * @brief   Implementation of ExpressionAnalyser
 * @author  Sarah Keating
 * @author  Alessandro Felder
 *
 * <!--------------------------------------------------------------------------
 * This file is part of libSBML.  Please visit http://sbml.org for more
 * information about SBML, and the latest version of libSBML.
 *
 * Copyright (C) 2013-2018 jointly by the following organizations:
 *     1. California Institute of Technology, Pasadena, CA, USA
 *     2. EMBL European Bioinformatics Institute (EMBL-EBI), Hinxton, UK
 *     3. University of Heidelberg, Heidelberg, Germany
 *
 * Copyright (C) 2009-2013 jointly by the following organizations: 
 *     1. California Institute of Technology, Pasadena, CA, USA
 *     2. EMBL European Bioinformatics Institute (EMBL-EBI), Hinxton, UK
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
 * in the file named "LICENSE.txt" included with this software distribution
 * and also available online as http://sbml.org/software/libsbml/license.html
 * ------------------------------------------------------------------------ -->
 */


#include <sbml/conversion/ExpressionAnalyser.h>

#ifdef __cplusplus

#include <algorithm>
#include <string>
#include <vector>
#include <map>

using namespace std;

LIBSBML_CPP_NAMESPACE_BEGIN




ExpressionAnalyser::ExpressionAnalyser() :
   mODEs (NULL)
  ,mModel (NULL)
{
}

ExpressionAnalyser::ExpressionAnalyser(const ExpressionAnalyser& orig) :
   mODEs(NULL)
  , mModel(NULL)
{
}

/*
* Assignment operator for SBMLLevelVersionConverter.
*/
ExpressionAnalyser&
ExpressionAnalyser::operator=(const ExpressionAnalyser& rhs)
{
  if (&rhs != this)
  {
    mModel = rhs.mModel;
  }

  return *this;
}

ExpressionAnalyser* 
ExpressionAnalyser::clone() const
{
  return new ExpressionAnalyser(*this);
}

/*
 * Destroy this object.
 */
ExpressionAnalyser::~ExpressionAnalyser ()
{
  for (std::vector<std::pair<std::string, ASTNode*> >::iterator it = mODEs.begin(); it != mODEs.end(); ++it)
  {
    if (it->second != NULL)
    {
      delete it->second;
      it->second = NULL;
    }
  }
  mODEs.clear();
  SBMLTransforms::clearComponentValues();
}

/*
* Set ode pairs
*/
int
ExpressionAnalyser::setODEPairs(std::vector< std::pair< std::string, ASTNode*> > odes)
{
  mODEs = odes;
  return LIBSBML_OPERATION_SUCCESS;
}


/*
* Set ode model
*/
int
ExpressionAnalyser::setModel(Model* model)
{
  mModel = model;
  SBMLTransforms::mapComponentValues(model);
  return LIBSBML_OPERATION_SUCCESS;
}

/*
* Check whether the expression has a parent expression which may already have been analysed 
* in which case we do not need to re analyse the child expression
* e.g. if we have k-x-y do not need to analyse k-x
*/
bool
ExpressionAnalyser::hasExpressionAlreadyRecorded(SubstitutionValues_t* value)
{
  for (unsigned int i = mExpressions.size(); i > 0; i--)
  {
    SubstitutionValues_t* exp = mExpressions.at(i - 1);
    switch (value->type)
    {
    case TYPE_K_MINUS_X_MINUS_Y:
      if (value->k_value == exp->k_value  &&
        value->x_value == exp->x_value &&
        value->y_value == exp->y_value &&
        value->dxdt_expression == exp->dxdt_expression &&
        value->dydt_expression == exp->dydt_expression)
      {
        return true;
      }
      break;
    case TYPE_K_PLUS_V_MINUS_X_MINUS_Y:
      if (value->k_value == exp->k_value  &&
        value->x_value == exp->x_value &&
        value->y_value == exp->y_value &&
        value->dxdt_expression == exp->dxdt_expression &&
        value->dydt_expression == exp->dydt_expression &&
        value->v_expression == exp->v_expression)
      {
        return true;
      }
      break;
    case TYPE_K_MINUS_X_PLUS_W_MINUS_Y:
      if (value->k_value == exp->k_value  &&
        value->x_value == exp->x_value &&
        value->y_value == exp->y_value &&
        value->dxdt_expression == exp->dxdt_expression &&
        value->dydt_expression == exp->dydt_expression &&
        value->w_expression == exp->w_expression)
      {
        return true;
      }
      break;
    case TYPE_K_MINUS_X:
      if (value->k_value == exp->k_value  &&
        value->x_value == exp->x_value &&
        value->dxdt_expression == exp->dxdt_expression)
      {
        return true;
      }
      break;
    case TYPE_K_PLUS_V_MINUS_X:
      if (value->k_value == exp->k_value  &&
        value->x_value == exp->x_value &&
        value->dxdt_expression == exp->dxdt_expression &&
        value->v_expression == exp->v_expression)
      {
        return true;
      }
      break;
    case TYPE_MINUS_X_PLUS_Y:
      if (value->x_value == exp->x_value &&
        value->y_value == exp->y_value &&
        value->dxdt_expression == exp->dxdt_expression &&
        value->dydt_expression == exp->dydt_expression)
      {
        return true;
      }
      break;
    default:
      break;
    }
  }
  return false;
}


bool
ExpressionAnalyser::analyseNode(ASTNode* node, SubstitutionValues_t *value)
{
  unsigned int numChildren = node->getNumChildren();
  ASTNodeType_t type = node->getType();
  ASTNode* rightChild = node->getRightChild();
  ASTNode* leftChild = node->getLeftChild();
  switch (type)
  {
  case AST_PLUS:
    //  -x+y node binary; plus; left child type minus; rightchild var/const
    //           +
    //        -     y
    //        x
    if (numChildren != 2 || rightChild->getType() != AST_NAME
      || leftChild->getType() != ASTNodeType_t::AST_MINUS
      || leftChild->getNumChildren() != 1)
      return false;

    // if we get to this point, the only thing left to check is 
    // whether the ->left->right grandchild (the x in -x+y) is a variable species.
    if (isVariableSpeciesOrParameter(leftChild->getChild(0)))
    {
      value->x_value = leftChild->getChild(0)->getName();
      value->y_value = rightChild->getName();
      value->dydt_expression = getODEFor(rightChild->getName());
      value->dxdt_expression = getODEFor(leftChild->getChild(0)->getName());
      value->type = TYPE_MINUS_X_PLUS_Y;
      value->current = node;
      return true;
    }
    break;

  case AST_MINUS:
    //          -                  -               -
    //        k   x             -     y        +      x
    //                        k   x         k     v
    //  k-x or k-x-y node binary; right child (x,y) is variable
    //  k+v-x; right child x var; left child plus node with left child k constant
    if (numChildren != 2 || !isVariableSpeciesOrParameter(rightChild))
      return false;
    // if left child is  numerical constant or a parameter, it IS k-x
    if (isNumericalConstantOrConstantParameter(leftChild))
    {
      value->k_value = leftChild->getName();
      value->x_value = rightChild->getName();
      value->dxdt_expression = getODEFor(rightChild->getName());
      value->dydt_expression = NULL;
      value->type = TYPE_K_MINUS_X;
      value->current = node;
      return true;
    }
    else if (leftChild->getType() == AST_PLUS 
      && isNumericalConstantOrConstantParameter(leftChild->getChild(0)))
    {
      value->k_value = leftChild->getChild(0)->getName();
      value->x_value = rightChild->getName();
      value->dxdt_expression = getODEFor(rightChild->getName());
      value->dydt_expression = NULL;
      value->v_expression = leftChild->getChild(1);
      value->type = TYPE_K_PLUS_V_MINUS_X;
      value->current = node;
      return true;
    }
    else
    {
      // if left child is k-x then we have k-x-y
      if (analyseNode(leftChild, value))
      {
        value->y_value = rightChild->getName();
        value->dydt_expression = getODEFor(rightChild->getName());
        value->type = TYPE_K_MINUS_X_MINUS_Y;
        value->current = node;
        return true;
      }
    }
    break;
  default:
    return false;
  }
  return false;
}

/*
* Return the ODE for the given variable 
* or an ASTNode representing zero if there is no time derivative
*/
ASTNode*
ExpressionAnalyser::getODEFor(std::string name)
{
  for (unsigned int odeIndex = 0; odeIndex < mODEs.size(); odeIndex++)
  {
    std::pair<std::string, ASTNode*> ode = mODEs.at(odeIndex);
    if (name == ode.first)
    {
      return ode.second;
    }
  }
  ASTNode* zero = new ASTNode(AST_REAL);
  zero->setValue(0.0);
  return zero->deepCopy();
}
void
ExpressionAnalyser::analyse(bool minusXPlusYOnly)
{
  for (unsigned int odeIndex = 0; odeIndex < mODEs.size(); odeIndex++)
  {
    std::pair<std::string, ASTNode*> ode = mODEs.at(odeIndex);
    ASTNode* odeRHS = ode.second;
    odeRHS->reduceToBinary();
    List* operators = odeRHS->getListOfNodes((ASTNodePredicate)ASTNode_isOperator);
    ListIterator it = operators->begin();

    while (it != operators->end())
    {
      ASTNode* currentNode = (ASTNode*)*it;
      if (minusXPlusYOnly && currentNode->getType() != AST_PLUS)
      {
        it++;
        continue;
      }
      SubstitutionValues_t* value = new SubstitutionValues_t;
      value->type = TYPE_UNKNOWN;
      if (analyseNode(currentNode, value))
      {
        value->odeIndex = odeIndex;
        if (!hasExpressionAlreadyRecorded(value))
        {
          mExpressions.push_back(value);
        }
      }
      it++;
    }
  }
}

void
ExpressionAnalyser::detectHiddenSpecies(List * hiddenSpecies)
{
 analyse(true);
  //for (unsigned int odeIndex = 0; odeIndex < mODEs.size(); odeIndex++)
  //{
  //  std::pair<std::string, ASTNode*> ode = mODEs.at(odeIndex);
  //  ASTNode* odeRHS = ode.second;
  //  odeRHS->reduceToBinary();
  //  //      Step 1: iterative, in-place replacement of any -x+y terms with y-x terms
  reorderMinusXPlusYIteratively();
  mExpressions.clear();
  analyse();

  //  // Step 2 TODO
  //  List* operators = odeRHS->getListOfNodes((ASTNodePredicate)ASTNode_isOperator);
  //  ListIterator it = operators->begin();
  //  while (it != operators->end())
  //  {
  //    ASTNode* currentNode = (ASTNode*)*it;
  //    if (isKMinusXMinusY(currentNode))
  //    {
  //      currentNode->printMath();
  //      // (a) introduce z=k-x-y with dz/dt = -dx/dt-dy/dt (add to list of additional ODEs to add at the end)
  //      // TODO
  //      // (b) replace in ALL ODEs (not just current) k-x-y with z (interior loop over mODEs again?)
  //      // (c) replace in ALL ODEs (not just current) k+v-x-y with v+z
  //      // (d) replace in ALL ODEs (not just current) k-x+w-y with w+z
  //    }
  //    it++;
  //  }
    addHiddenVariablesForKMinusX(hiddenSpecies);
  //  // Step 3
  //  //it = operators->begin();
  //  //while (it != operators->end())
  //  //{
  //  //    ASTNode* currentNode = (ASTNode*)*it;
  //  //    if (isKMinusX(currentNode, mModel))
  //  //    {
  //  //        // remember x name for later, before we replace the current node
  //  //        std::string xName = std::string(currentNode->getRightChild()->getName());

  //  //        // (a)
  //  //        // introduce z=k-x
  //  //        Parameter* zParam = mModel->createParameter();
  //  //        const std::string zName = "z" + std::to_string(mModel->getNumParameters());
  //  //        zParam->setId(zName);
  //  //        zParam->setConstant(false);
  //  //        hiddenSpecies.add(zParam);

  //  //        // replace k - x with z in current ODE
  //  //        ASTNode* z = new ASTNode(ASTNodeType_t::AST_NAME);
  //  //        z->setName(zName.c_str());
  //  //        std::pair<ASTNode*, int> currentParentAndIndex = getParentNode(currentNode, odeRHS);
  //  //        ASTNode* currentParent = currentParentAndIndex.first;
  //  //        int index = currentParentAndIndex.second;
  //  //        if (currentParent != NULL)
  //  //        {
  //  //          currentParent->replaceChild(index, z, true);
  //  //          // intentionally, don't delete z as it's now owned by currentParent!
  //  //        }

  //  //        // add raterule defining dz/dt = -dxdt
  //  //        ASTNode* dxdt = odeRHS->deepCopy();
  //  //        RateRule* raterule = mModel->createRateRule();
  //  //        raterule->setVariable(zName);
  //  //        ASTNode* math = new ASTNode(ASTNodeType_t::AST_TIMES);
  //  //        ASTNode* minus1 = new ASTNode(ASTNodeType_t::AST_REAL);
  //  //        minus1->setValue(-1.0);
  //  //        math->addChild(minus1);
  //  //        math->addChild(dxdt);
  //  //        raterule->setMath(math);
  //  //        delete math; //its children dxdt and minus1 deleted as part of this.

  //  //        // TODO
  //  //        // (b) replace in ALL ODEs (not just current) k-x with z
  //  //        // (c) replace in ALL ODEs (not just current) k+v-x with v+z
  //  //    }
  //  //    it++;
  //  //}

  //}
  ////return hiddenSpecies;
}

/*
* Replace a child node within a node with the given replacement mode
*
* param node ASTNode * parent node containing node to be replaced
* param replaced ASTNode * node to be replaced if found in parent node
* param replacement
*/
void
ExpressionAnalyser::replaceExpressionInNodeWithNode(ASTNode* node, ASTNode* replaced, ASTNode* replacement)
{
  cout << "node: " << SBML_formulaToL3String(node) << endl;
  cout << "with: " << SBML_formulaToL3String(replaced) << endl;
  cout << "by: " << SBML_formulaToL3String(replacement) << endl;
  // we might be replcing the whole node
  if (node == replaced)
  {
    replaced = node->deepCopy();
    (*node) = *replacement;
  }
  else
  {
    std::pair<ASTNode*, int>currentParentAndIndex = make_pair((ASTNode*)NULL, (int)(NAN));
    ASTNode* currentParent;
    int index;
    do
    {
      currentParentAndIndex = getParentNode(replaced, node);
      currentParent = currentParentAndIndex.first;
      index = currentParentAndIndex.second;
      if (currentParent != NULL)
      {
        currentParent->replaceChild(index, replacement->deepCopy(), false);
        // intentionally, don't delete replacement as it's now owned by currentParent!
      }
    } while (currentParent != NULL);
  }
}

void
ExpressionAnalyser::replaceExpressionInNodeWithVar(ASTNode* node, ASTNode* replaced, std::string var)
{
  ASTNode* z = new ASTNode(ASTNodeType_t::AST_NAME);
  z->setName(var.c_str());
  replaceExpressionInNodeWithNode(node, replaced, z);
}

std::string
ExpressionAnalyser::getUniqueNewParameterName()
{
  return "z" + std::to_string(mModel->getNumParameters());
}


void
ExpressionAnalyser::addParameterAndRateRule(List* hiddenSpecies, SubstitutionValues_t *exp)
{
  // introduce z
  Parameter* zParam = mModel->createParameter();
  zParam->setId(exp->z_value);
  zParam->setConstant(false);
  zParam->setValue(SBMLTransforms::evaluateASTNode(exp->current, mModel));
  hiddenSpecies->add(zParam);

  // add raterule defining dz/dt
  ASTNode* dxdt = exp->dxdt_expression->deepCopy(); 
  RateRule* raterule = mModel->createRateRule();
  raterule->setVariable(exp->z_value);
  ASTNode* math = new ASTNode(ASTNodeType_t::AST_TIMES);
  ASTNode* minus1 = new ASTNode(ASTNodeType_t::AST_REAL);
  minus1->setValue(-1.0);
  switch (exp->type)
  {
  case TYPE_K_MINUS_X:
  case TYPE_K_PLUS_V_MINUS_X:
    // dz/dt = -dx/dt
    math->addChild(minus1);
    math->addChild(dxdt);
    break;
  case TYPE_K_MINUS_X_MINUS_Y:
    // dz/dt = - (dx/dt + dy/dt)
    ASTNode* dydt = exp->dydt_expression->deepCopy();
    ASTNode* plus = new ASTNode(AST_PLUS);
    plus->addChild(dxdt);
    plus->addChild(dydt);
    math->addChild(minus1);
    math->addChild(plus);

    break;
  }
  raterule->setMath(math);
  delete math; //its children dxdt and minus1 deleted as part of this.

}

void
ExpressionAnalyser::replaceExpressionWithNewParameter(ASTNode* ode, SubstitutionValues_t* exp)
{
  if (exp->type == TYPE_K_MINUS_X || exp->type == TYPE_K_MINUS_X_MINUS_Y)
  {
    replaceExpressionInNodeWithVar(ode, exp->current, exp->z_value);
    if (exp->dxdt_expression != NULL)
    {
      replaceExpressionInNodeWithVar(exp->dxdt_expression, exp->current, exp->z_value);
    }
    if (exp->dydt_expression != NULL)
    {
      replaceExpressionInNodeWithVar(exp->dydt_expression, exp->current, exp->z_value);
    }

  }
  if (exp->type == TYPE_K_PLUS_V_MINUS_X)
  {
    ASTNode* replacement = new ASTNode(AST_PLUS);
    ASTNode* z = new ASTNode(ASTNodeType_t::AST_NAME);
    z->setName(exp->z_value.c_str());
    ASTNode *v = exp->v_expression->deepCopy();
    replacement->addChild(z);
    replacement->addChild(v);
    replaceExpressionInNodeWithNode(ode, exp->current, replacement);
    if (exp->dxdt_expression != NULL)
    {
      replaceExpressionInNodeWithNode(exp->dxdt_expression, exp->current, replacement);
    }
    if (exp->dydt_expression != NULL)
    {
      replaceExpressionInNodeWithNode(exp->dydt_expression, exp->current, replacement);
    }

  }
}


bool
ExpressionAnalyser::addHiddenVariablesForKMinusX(List* hiddenSpecies)
{
  for (unsigned int i = 0; i < mExpressions.size(); i++)
  {
    SubstitutionValues_t *exp = mExpressions.at(i);
    ASTNode* currentNode = exp->current;
    for (unsigned int j = 0; j < mODEs.size(); j++)
    {
      std::pair<std::string, ASTNode*> ode = mODEs.at(j);
      ASTNode* odeRHS = ode.second;
      std::string zName = parameterAlreadyCreated(exp);
      if (!zName.empty())
      {
        replaceExpressionWithNewParameter(odeRHS, exp);
      }
      else
      {
        std::string zName = getUniqueNewParameterName();
        exp->z_value = zName;

        replaceExpressionWithNewParameter(odeRHS, exp);
        addParameterAndRateRule(hiddenSpecies, exp);

      }
      cout << "ode: " << SBML_formulaToL3String(odeRHS) << endl;
    }
  } // end for
  return true;
}


std::string
ExpressionAnalyser::parameterAlreadyCreated(SubstitutionValues_t* exp)
{
  std::string renamed = "";
  bool match = false;
  unsigned int i = 0;
  while (!match && i < mExpressions.size())
  {
    if (mExpressions.at(i)->type == exp->type && mExpressions.at(i)->k_value == exp->k_value &&
      mExpressions.at(i)->x_value == exp->x_value && mExpressions.at(i)->z_value.empty() != true)
    {
      renamed = mExpressions.at(i)->z_value;
      match = true;
    }
    i++;
  }
  return renamed;
}

/*
 * Check whether for node is a name node representing species or a non constant parameter
*/
bool ExpressionAnalyser::isVariableSpeciesOrParameter(ASTNode* node)
{
    if (!node->isName()) // some nodes, like * operators, don't seem to have a name in the first place
        return false;
    Species* species = mModel->getSpecies(node->getName());
    Parameter* parameter = mModel->getParameter(node->getName()); // some species in rate rules may be defined as variable parameters
    bool isVariableSpeciesOrParameter = (species != NULL && !species->getConstant());
    bool isVariableParameter = (parameter!=NULL && !parameter->getConstant());
    return isVariableSpeciesOrParameter || isVariableParameter;
}

/*
* Check whether for node is a name node representing a constant parameter or a numerical node
*/
bool ExpressionAnalyser::isNumericalConstantOrConstantParameter(ASTNode* node)
{
    if (!node->isName()) // some nodes, like * operators, don't seem to have a name in the first place
        return false;
    Parameter* parameter = mModel->getParameter(node->getName());
    bool isConstantParameter = (parameter != NULL) && (parameter->getConstant());
    bool isNumericalConstant = node->isNumber() && node->isConstant();
    return isNumericalConstant || isConstantParameter;
}

/*
* Reorder any instance of - x + y with y - x in the set of ODEs.
* Fages Algorithm 3.1 Step 1
*/
void ExpressionAnalyser::reorderMinusXPlusYIteratively()
{
  for (unsigned int i = 0; i < mExpressions.size(); i++)
  {
    SubstitutionValues_t* exp = mExpressions.at(i);
    if (exp->type != TYPE_MINUS_X_PLUS_Y)
      continue;
    ASTNode* ode = (mODEs.at(exp->odeIndex)).second;
    ASTNode* replacement = new ASTNode(AST_MINUS);
    ASTNode* y = new ASTNode(AST_NAME);
    y->setName((exp->y_value).c_str());
    ASTNode* x = new ASTNode(AST_NAME);
    x->setName((exp->x_value).c_str());
    replacement->addChild(y);
    replacement->addChild(x);
    replaceExpressionInNodeWithNode(ode, exp->current, replacement);
  }
}

std::pair<ASTNode*, int> ExpressionAnalyser::getParentNode(const ASTNode* child, const ASTNode* root)
{
  for (unsigned int i = 0; i < root->getNumChildren(); i++)
    {
        if (root->getChild(i)->exactlyEqual(*(child)))
        {
            return std::pair<ASTNode*, int>(const_cast<ASTNode*>(root), i);
        }
    }
    for (unsigned int i = 0; i < root->getNumChildren(); i++)
    {
      std::pair<ASTNode*, int> parent = getParentNode(child, root->getChild(i));
      if (parent.first != NULL)
      {
        return parent;
      }
    }
    return std::pair<ASTNode*, int>(NULL, (int)(NAN));
}

/** @endcond */

LIBSBML_CPP_NAMESPACE_END

#endif  /* __cplusplus */


