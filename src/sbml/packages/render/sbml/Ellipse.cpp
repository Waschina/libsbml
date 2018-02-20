/**
 * @file    Ellipse.cpp
 * @brief Implementation of the Ellipse class.
 * @author  Ralph Gauges
 * @author  Frank T. Bergmann
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
 * Copyright (C) 2011-2013 jointly by the following organizations: 
 *     1. California Institute of Technology, Pasadena, CA, USA
 *     2. EMBL European Bioinformatics Institute (EMBL-EBI), Hinxton, UK
 *  
 * Copyright 2010 Ralph Gauges
 *     Group for the modeling of biological processes 
 *     University of Heidelberg
 *     Im Neuenheimer Feld 267
 *     69120 Heidelberg
 *     Germany
 *
 * This library is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation.  A copy of the license agreement is provided
 * in the file named "LICENSE.txt" included with this software distribution
 * and also available online as http://sbml.org/software/libsbml/license.html
 * ---------------------------------------------------------------------- -->*/

#include <sbml/packages/render/sbml/Ellipse.h>
#include <sbml/packages/render/validator/RenderSBMLError.h>

using namespace std;

#include <string>

#ifndef OMIT_DEPRECATED
#ifdef DEPRECATION_WARNINGS
#include <iostream>
#endif // DEPRECATION_WARNINGS
#endif // OMIT_DEPRECATED

#include <sbml/SBMLErrorLog.h>
#include <sbml/SBMLVisitor.h>
#include <sbml/xml/XMLNode.h>
#include <sbml/xml/XMLToken.h>
#include <sbml/xml/XMLAttributes.h>
#include <sbml/xml/XMLInputStream.h>
#include <sbml/xml/XMLOutputStream.h>

#include <sbml/packages/render/extension/RenderExtension.h>
#include <sbml/packages/layout/util/LayoutAnnotation.h>
#include <sbml/packages/layout/util/LayoutUtilities.h>

LIBSBML_CPP_NAMESPACE_BEGIN




#ifdef __cplusplus


/*
 * Creates a new Ellipse using the given SBML Level, Version and
 * &ldquo;render&rdquo; package version.
 */
Ellipse::Ellipse(unsigned int level,
                 unsigned int version,
                 unsigned int pkgVersion)
  : GraphicalPrimitive2D(level, version, pkgVersion)
  , mCX(0.0)
  , mCY(0.0)
  , mCZ(0.0)
  , mRX (0.0)
  , mRY (0.0)
  , mRatio(util_NaN())
  , mIsSetRatio(false)
{
  setSBMLNamespacesAndOwn(new RenderPkgNamespaces(level, version, pkgVersion));
  connectToChild();
}


/*
 * Creates a new Ellipse using the given RenderPkgNamespaces object.
 */
Ellipse::Ellipse(RenderPkgNamespaces *renderns)
  : GraphicalPrimitive2D(renderns)
  , mCX(0.0)
  , mCY(0.0)
  , mCZ(0.0)
  , mRX (0.0)
  , mRY (0.0)
  , mRatio (util_NaN())
  , mIsSetRatio (false)
{
  setElementNamespace(renderns->getURI());
  connectToChild();
  loadPlugins(renderns);
}


/*
 * Creates a new RadialGradient object from the given XMLNode object.
 * The XMLNode object has to contain a valid XML representation of a 
 * RadialGradient object as defined in the render extension specification.
 * This method is normally called when render information is read from a file and 
 * should normally not have to be called explicitly.
 *
 * @param node the XMLNode object reference that describes the RadialGradient
 * object to be instantiated.
 *
 * This constructor is deprecated. The new libsbml API only has
 * constructors which take the SBML level and version or one that takes
 * an SBMLNamespaces object.
 */
Ellipse::Ellipse(const XMLNode& node, unsigned int l2version)
  : GraphicalPrimitive2D(node, l2version)
  , mRatio(util_NaN())
  , mIsSetRatio(false)
{
    ExpectedAttributes ea;
    addExpectedAttributes(ea);
    this->readAttributes(node.getAttributes(), ea);

    
  setSBMLNamespacesAndOwn(new RenderPkgNamespaces(2,l2version));  

  connectToChild();
}
/** @endcond */


#ifndef OMIT_DEPRECATED
/** @cond doxygenLibsbmlInternal */
/*
 * Instantiates a new ellipse object with the center set to 0,0,0
 * and the radii also set to 0.
 * The id is set to the given string.
 *
 * @param id the id of the ellipse.
 *
 * This constructor is deprecated. The new libsbml API only has
 * constructors which take the SBML level and version or one that takes
 * an SBMLNamespaces object.
 */
    Ellipse::Ellipse(RenderPkgNamespaces* renderns, const std::string& id)
 : GraphicalPrimitive2D(renderns,id)
 , mCX(0.0)
 , mCY(0.0)
 , mCZ(0.0)
 , mRatio(util_NaN())
 , mIsSetRatio(false)
{
#ifdef DEPRECATION_WARNINGS
    std::cerr << "Warning. Ellipse::Ellipse(const std::string& id) is deprecated." << std::endl;
#endif // DEPRECATION_WARNINGS
    setRadii(0.0,0.0);
        // set the element namespace of this object
  setElementNamespace(renderns->getURI());

  // connect child elements to this element.
  connectToChild();

  // load package extensions bound with this object (if any) 
  loadPlugins(renderns);
}
/** @endcond */
#endif // OMIT_DEPRECATED

#ifndef OMIT_DEPRECATED
/** @cond doxygenLibsbmlInternal */
/*
 * Constructor with 2D center and radius.
 * instantiates a new ellipse object with the center.
 * The z coordinate of the center is set to 0.
 * The id is unset and both radii are set to the given radius.
 *
 * @param cx x value of the center point 
 * @param cy y value of the center point 
 * @param r radius along both axis
 *
 * This constructor is deprecated. The new libsbml API only has
 * constructors which take the SBML level and version or one that takes
 * an SBMLNamespaces object.
 */
Ellipse::Ellipse(RenderPkgNamespaces* renderns, const RelAbsVector& cx,const RelAbsVector& cy,const RelAbsVector& r)
 : GraphicalPrimitive2D(renderns)
  , mCX(cx)
  , mCY(cy)
  , mCZ(RelAbsVector(0.0,50.0))
  , mRatio(util_NaN())
  , mIsSetRatio(false)
{
#ifdef DEPRECATION_WARNINGS
    std::cerr << "Warning. Ellipse::Ellipse(const RelAbsVector& cx,const RelAbsVector& cy,const RelAbsVector& r) is deprecated." << std::endl;
#endif // DEPRECATION_WARNINGS
    setRadii(r,r);
        // set the element namespace of this object
  setElementNamespace(renderns->getURI());

  // connect child elements to this element.
  connectToChild();

  // load package extensions bound with this object (if any) 
  loadPlugins(renderns);
}
/** @endcond */
#endif // OMIT_DEPRECATED

#ifndef OMIT_DEPRECATED
/** @cond doxygenLibsbmlInternal */
/*
 * Constructor with 2D center and radii.
 *
 * This constructor is deprecated. The new libsbml API only has
 * constructors which take the SBML level and version or one that takes
 * an SBMLNamespaces object.
 */
Ellipse::Ellipse(RenderPkgNamespaces* renderns, const RelAbsVector& cx,const RelAbsVector& cy,const RelAbsVector& rx,const RelAbsVector& ry)
 : GraphicalPrimitive2D(renderns)
 , mCX(cx)
 , mCY(cy)
 , mCZ(0.0)
 , mRatio(util_NaN())
 , mIsSetRatio(false)
{
#ifdef DEPRECATION_WARNINGS
    std::cerr << "Warning. Ellipse::Ellipse(const RelAbsVector& cx,const RelAbsVector& cy,const RelAbsVector& rx,const RelAbsVector& ry) is deprecated." << std::endl;
#endif // DEPRECATION_WARNINGS
    setRadii(rx,ry);
        // set the element namespace of this object
  setElementNamespace(renderns->getURI());

  // connect child elements to this element.
  connectToChild();

  // load package extensions bound with this object (if any) 
  loadPlugins(renderns);
}
/** @endcond */
#endif // OMIT_DEPRECATED

#ifndef OMIT_DEPRECATED
/** @cond doxygenLibsbmlInternal */
/*
 * Constructor with 3D center and radii.
 * instantiates a new ellipse object with the center and radii.
 * The id is unset.
 *
 * @param cx x value of the center point 
 * @param cy y value of the center point 
 * @param cz z value of the center point 
 * @param rx radius along the x axis
 * @param ry radius along the y axis
 *
 * This constructor is deprecated. The new libsbml API only has
 * constructors which take the SBML level and version or one that takes
 * an SBMLNamespaces object.
 */
Ellipse::Ellipse(RenderPkgNamespaces* renderns, const RelAbsVector& cx,const RelAbsVector& cy,const RelAbsVector& cz,const RelAbsVector& rx,const RelAbsVector& ry)
 : GraphicalPrimitive2D(renderns)
  , mCX(cx)
  , mCY(cy)
  , mCZ(cz)
  , mRatio(util_NaN())
  , mIsSetRatio(false)
{
#ifdef DEPRECATION_WARNINGS
    std::cerr << "Warning. Ellipse::Ellipse(const RelAbsVector& cx,const RelAbsVector& cy,const RelAbsVector& cz,const RelAbsVector& rx,const RelAbsVector& ry) is deprecated." << std::endl;
#endif // DEPRECATION_WARNINGS
    setRadii(rx,ry);
        // set the element namespace of this object
  setElementNamespace(renderns->getURI());

  // connect child elements to this element.
  connectToChild();

  // load package extensions bound with this object (if any) 
  loadPlugins(renderns);
}
/** @endcond */
#endif // OMIT_DEPRECATED

#ifndef OMIT_DEPRECATED
/** @cond doxygenLibsbmlInternal */
/*
 * Constructor with id, 2D center and radius.
 * instantiates a new ellipse object with the given @p id and center.
 * Both radii are set to the given radius r. This actually yields a circle.
 *
 * @param id id for the ellipse
 * @param cx x value of the center point 
 * @param cy y value of the center point 
 * @param r radius along both axis
 *
 * This constructor is deprecated. The new libsbml API only has
 * constructors which take the SBML level and version or one that takes
 * an SBMLNamespaces object.
 */
Ellipse::Ellipse(RenderPkgNamespaces* renderns, const std::string& id,const RelAbsVector& cx,const RelAbsVector& cy,const RelAbsVector& r)
 : GraphicalPrimitive2D(renderns,id)
  , mCX(cx)
  , mCY(cy)
  , mCZ(0.0)
  , mRatio(util_NaN())
  , mIsSetRatio(false)
{
#ifdef DEPRECATION_WARNINGS
    std::cerr << "Warning. Ellipse::Ellipse(const std::string& id,const RelAbsVector& cx,const RelAbsVector& cy,const RelAbsVector& r) is deprecated." << std::endl;
#endif // DEPRECATION_WARNINGS
    setRadii(r,r);
        // set the element namespace of this object
  setElementNamespace(renderns->getURI());

  // connect child elements to this element.
  connectToChild();

  // load package extensions bound with this object (if any) 
  loadPlugins(renderns);
}
/** @endcond */
#endif // OMIT_DEPRECATED

#ifndef OMIT_DEPRECATED
/** @cond doxygenLibsbmlInternal */
/*
 * Constructor with id, 2D center and radii.
 * instantiates a new ellipse object with the given @p id, center and radii.
 *
 * @param id id for the ellipse
 * @param cx x value of the center point 
 * @param cy y value of the center point 
 * @param rx radius along the x axis
 * @param ry radius along the y axis
 *
 *
 * This constructor is deprecated. The new libsbml API only has
 * constructors which take the SBML level and version or one that takes
 * an SBMLNamespaces object.
 */
Ellipse::Ellipse(RenderPkgNamespaces* renderns, const std::string& id,const RelAbsVector& cx,const RelAbsVector& cy,const RelAbsVector& rx,const RelAbsVector& ry)
 : GraphicalPrimitive2D(renderns,id)
 , mCX(cx)
 , mCY(cy)
 , mCZ(0.0)
 , mRatio(util_NaN())
 , mIsSetRatio(false)

{
#ifdef DEPRECATION_WARNINGS
    std::cerr << "Warning. Ellipse::Ellipse(const std::string& id,const RelAbsVector& cx,const RelAbsVector& cy,const RelAbsVector& rx,const RelAbsVector& ry) is deprecated." << std::endl;
#endif // DEPRECATION_WARNINGS
    setRadii(rx,ry);
        // set the element namespace of this object
  setElementNamespace(renderns->getURI());

  // connect child elements to this element.
  connectToChild();

  // load package extensions bound with this object (if any) 
  loadPlugins(renderns);
}
/** @endcond */
#endif // OMIT_DEPRECATED

#ifndef OMIT_DEPRECATED
/** @cond doxygenLibsbmlInternal */
/*
 * Constructor with id, 3D center and radii.
 * instantiates a new ellipse object with the given @p id, center and radii.
 *
 * @param id id for the ellipse
 * @param cx x value of the center point 
 * @param cy y value of the center point 
 * @param cz z value of the center point 
 * @param rx radius along the x axis
 * @param ry radius along the y axis
 *
 *
 * This constructor is deprecated. The new libsbml API only has
 * constructors which take the SBML level and version or one that takes
 * an SBMLNamespaces object.
 */
Ellipse::Ellipse(RenderPkgNamespaces* renderns, const std::string& id,const RelAbsVector& cx,const RelAbsVector& cy,const RelAbsVector& cz,const RelAbsVector& rx,const RelAbsVector& ry)
 : GraphicalPrimitive2D(renderns, id)
 , mCX(cx)
 , mCY(cy)
 , mCZ(cz)
 , mRatio(util_NaN())
 , mIsSetRatio(false)
{
#ifdef DEPRECATION_WARNINGS
    std::cerr << "Warning. Ellipse::Ellipse(const std::string& id,const RelAbsVector& cx,const RelAbsVector& cy,const RelAbsVector& cz,const RelAbsVector& rx,const RelAbsVector& ry) is deprecated." << std::endl;
#endif // DEPRECATION_WARNINGS
    setRadii(rx,ry);
        // set the element namespace of this object
  setElementNamespace(renderns->getURI());

  // connect child elements to this element.
  connectToChild();

  // load package extensions bound with this object (if any) 
  loadPlugins(renderns);
}
/** @endcond */
#endif // OMIT_DEPRECATED


/*
 * Copy constructor for Ellipse.
 */
Ellipse::Ellipse(const Ellipse& orig)
  : GraphicalPrimitive2D( orig )
  , mCX ( orig.mCX )
  , mCY ( orig.mCY )
  , mCZ ( orig.mCZ )
  , mRX ( orig.mRX )
  , mRY ( orig.mRY )
  , mRatio ( orig.mRatio )
  , mIsSetRatio ( orig.mIsSetRatio )
{
  connectToChild();
}


/*
 * Assignment operator for Ellipse.
 */
Ellipse&
Ellipse::operator=(const Ellipse& rhs)
{
  if (&rhs != this)
  {
    GraphicalPrimitive2D::operator=(rhs);
    mCX = rhs.mCX;
    mCY = rhs.mCY;
    mCZ = rhs.mCZ;
    mRX = rhs.mRX;
    mRY = rhs.mRY;
    mRatio = rhs.mRatio;
    mIsSetRatio = rhs.mIsSetRatio;

    connectToChild();
  }

  return *this;
}


/*
 * Creates and returns a deep copy of this Ellipse object.
 */
Ellipse*
Ellipse::clone() const
{
  return new Ellipse(*this);
}


/*
 * Destructor for Ellipse.
 */
Ellipse::~Ellipse()
{
}


/*
 * Returns the value of the "ratio" attribute of this Ellipse.
 */
double
Ellipse::getRatio() const
{
  return mRatio;
}


/*
 * Predicate returning @c true if this Ellipse's "ratio" attribute is set.
 */
bool
Ellipse::isSetRatio() const
{
  return mIsSetRatio;
}


/*
 * Sets the value of the "ratio" attribute of this Ellipse.
 */
int
Ellipse::setRatio(double ratio)
{
  mRatio = ratio;
  mIsSetRatio = true;
  return LIBSBML_OPERATION_SUCCESS;
}


/*
 * Unsets the value of the "ratio" attribute of this Ellipse.
 */
int
Ellipse::unsetRatio()
{
  mRatio = util_NaN();
  mIsSetRatio = false;

  if (isSetRatio() == false)
  {
    return LIBSBML_OPERATION_SUCCESS;
  }
  else
  {
    return LIBSBML_OPERATION_FAILED;
  }
}


/*
 * Returns the x coordinate for the center point as a const reference.
 */
const RelAbsVector& 
Ellipse::getCX() const
{
    return this->mCX;
}


/*
* Returns the x coordinate for the center point as a const reference.
*/
RelAbsVector&
Ellipse::getCX()
{
  return this->mCX;
}


/*
 * Returns the y coordinate for the center point as a const reference.
 */
const RelAbsVector& 
Ellipse::getCY() const
{
    return this->mCY;
}


/*
* Returns the y coordinate for the center point as a const reference.
*/
RelAbsVector&
Ellipse::getCY()
{
  return this->mCY;
}


/*
 * Returns the z coordinate for the center point as a const reference.
 */
const RelAbsVector& 
Ellipse::getCZ() const
{
    return this->mCZ;
}


/*
* Returns the z coordinate for the center point as a const reference.
*/
RelAbsVector&
Ellipse::getCZ()
{
  return this->mCZ;
}


/*
 * Returns the radius along the x axis as a const reference.
 */
const RelAbsVector& 
Ellipse::getRX() const
{
    return this->mRX;
}


RelAbsVector&
Ellipse::getRX()
{
  return this->mRX;
}


/*
 * Returns the radius along the y axis as a const reference.
 */
const RelAbsVector& 
Ellipse::getRY() const
{
    return this->mRY;
}


RelAbsVector&
Ellipse::getRY()
{
  return this->mRY;
}


/*
 * Predicate returning @c true if this Ellipse's "cx" element is set.
 */
bool
Ellipse::isSetCX() const
{
  return mCX.isSetCoordinate();
}


/*
 * Predicate returning @c true if this Ellipse's "cy" element is set.
 */
bool
Ellipse::isSetCY() const
{
  return mCY.isSetCoordinate();
}


/*
 * Predicate returning @c true if this Ellipse's "cz" element is set.
 */
bool
Ellipse::isSetCZ() const
{
  return mCZ.isSetCoordinate();
}


/*
 * Predicate returning @c true if this Ellipse's "rx" element is set.
 */
bool
Ellipse::isSetRX() const
{
  return mRX.isSetCoordinate();
}


/*
 * Predicate returning @c true if this Ellipse's "ry" element is set.
 */
bool
Ellipse::isSetRY() const
{
  return mRY.isSetCoordinate();
}


/*
 * Sets the x coordinates for the center point.
 *
 * @param cx x value of the center point 
 */
void Ellipse::setCX(const RelAbsVector& cx)
{
    this->mCX=cx;
}


/*
 * Sets the y coordinates for the center point.
 *
 * @param cy y value of the center point 
 */
void Ellipse::setCY(const RelAbsVector& cy)
{
    this->mCY=cy;
}


/*
 * Sets the z coordinates for the center point.
 *
 * @param cz z value of the center point 
 */
void Ellipse::setCZ(const RelAbsVector& cz)
{
    this->mCZ=cz;
}

/*
 * Sets the radius along the x axis
 *
 * @param rx radius along the x axis
 */
void Ellipse::setRX(const RelAbsVector& rx)
{
    this->mRX=rx;
}


/*
 * Sets the radius along the y axis
 *
 * @param ry radius along the y axis
 */
void Ellipse::setRY(const RelAbsVector& ry)
{
    this->mRY=ry;
}


/*
 * Sets the 2D coordinates for the center point.
 */
void Ellipse::setCenter2D(const RelAbsVector& cx,const RelAbsVector& cy)
{
    this->mCX=cx;
    this->mCY=cy;
    this->mCZ=RelAbsVector(0.0,50.0);
}


/*
 * Sets the 3D coordinates for the center point.
 */
void Ellipse::setCenter3D(const RelAbsVector& cx,const RelAbsVector& cy,const RelAbsVector& cz)
{
    this->mCX=cx;
    this->mCY=cy;
    this->mCZ=cz;
}


/*
 * Sets the radii of the ellipse
 */
void Ellipse::setRadii(const RelAbsVector& rx,const RelAbsVector& ry)
{
    this->mRX=rx;
    this->mRY=ry;
}


/*
 * Unsets the value of the "cx" element of this Ellipse.
 */
int
Ellipse::unsetCX()
{
  mCX.unsetCoordinate();
  return LIBSBML_OPERATION_SUCCESS;
}


/*
 * Unsets the value of the "cy" element of this Ellipse.
 */
int
Ellipse::unsetCY()
{
  mCY.unsetCoordinate();
  return LIBSBML_OPERATION_SUCCESS;
}


/*
 * Unsets the value of the "cz" element of this Ellipse.
 */
int
Ellipse::unsetCZ()
{
  mCZ.unsetCoordinate();
  return LIBSBML_OPERATION_SUCCESS;
}


/*
 * Unsets the value of the "rx" element of this Ellipse.
 */
int
Ellipse::unsetRX()
{
  mRX.unsetCoordinate();
  return LIBSBML_OPERATION_SUCCESS;
}


/*
 * Unsets the value of the "ry" element of this Ellipse.
 */
int
Ellipse::unsetRY()
{
  mRY.unsetCoordinate();
  return LIBSBML_OPERATION_SUCCESS;
}


/*
 * Returns the XML element name of this Ellipse object.
 */
const std::string&
Ellipse::getElementName() const
{
  static const string name = "ellipse";
  return name;
}


/*
 * Returns the libSBML type code for this Ellipse object.
 */
int
Ellipse::getTypeCode() const
{
  return SBML_RENDER_ELLIPSE;
}


/*
 * Predicate returning @c true if all the required attributes for this Ellipse
 * object have been set.
 */
bool
Ellipse::hasRequiredAttributes() const
{
  //render - FIX_ME
  // old code used this to check that none of the values were NaN - but being
  bool allPresent = GraphicalPrimitive2D::hasRequiredAttributes();

  if (isSetCX() == false)
  {
    allPresent = false;
  }

  if (isSetCY() == false)
  {
    allPresent = false;
  }

  if (isSetRX() == false)
  {
    allPresent = false;
  }

  return allPresent;
}


/** @cond doxygenLibsbmlInternal */

/*
 * Write any contained elements
 */
void
Ellipse::writeElements(XMLOutputStream& stream) const
{
  GraphicalPrimitive2D::writeElements(stream);

  SBase::writeExtensionElements(stream);
}

/** @endcond */



/** @cond doxygenLibsbmlInternal */

/*
 * Accepts the given SBMLVisitor
 */
bool
Ellipse::accept(SBMLVisitor& v) const
{
  v.visit(*this);
  //render - FIX_ME
  //if (mCX != NULL)
  //{
  //  mCX.accept(v);
  //}

  //if (mCY != NULL)
  //{
  //  mCY.accept(v);
  //}

  //if (mCZ != NULL)
  //{
  //  mCZ.accept(v);
  //}

  //if (mRX != NULL)
  //{
  //  mRX.accept(v);
  //}

  //if (mRY != NULL)
  //{
  //  mRY.accept(v);
  //}

  v.leave(*this);
  return true;
}

/** @endcond */



/** @cond doxygenLibsbmlInternal */

/*
 * Sets the parent SBMLDocument
 */
void
Ellipse::setSBMLDocument(SBMLDocument* d)
{
  GraphicalPrimitive2D::setSBMLDocument(d);

}

/** @endcond */



/** @cond doxygenLibsbmlInternal */

/*
 * Connects to child elements
 */
void
Ellipse::connectToChild()
{
  GraphicalPrimitive2D::connectToChild();

}

/** @endcond */



/** @cond doxygenLibsbmlInternal */

/*
 * Enables/disables the given package with this element
 */
void
Ellipse::enablePackageInternal(const std::string& pkgURI,
                               const std::string& pkgPrefix,
                               bool flag)
{
  GraphicalPrimitive2D::enablePackageInternal(pkgURI, pkgPrefix, flag);

}

/** @endcond */


/** @cond doxygenLibsbmlInternal */
/*
 * Creates an XMLNode object from this Ellipse object.
 *
 * @return the XMLNode with the XML representation for the 
 * Ellipse object.
 */
XMLNode Ellipse::toXML() const
{
  return getXmlNodeForSBase(this);
}
/** @endcond */


/** @cond doxygenLibsbmlInternal */
void
Ellipse::addExpectedAttributes(ExpectedAttributes& attributes)
{
  GraphicalPrimitive2D::addExpectedAttributes(attributes);

  attributes.add("cx");
  attributes.add("cy");
  attributes.add("cz");
  attributes.add("rx");
  attributes.add("ry");
  attributes.add("rz");
  attributes.add("ratio");
}
/** @endcond */

/** @cond doxygenLibsbmlInternal */
void Ellipse::readAttributes (const XMLAttributes& attributes, 
                              const ExpectedAttributes& expectedAttributes)
{
    unsigned int level = getLevel();
    unsigned int version = getVersion();
    unsigned int pkgVersion = getPackageVersion();
    unsigned int numErrs;
    bool assigned = false;
    SBMLErrorLog* log = getErrorLog();

    GraphicalPrimitive2D::readAttributes(attributes, expectedAttributes);

    if (log)
    {
      numErrs = log->getNumErrors();

      for (int n = numErrs-1; n >= 0; n--)
      {
        if (log->getError(n)->getErrorId() == UnknownPackageAttribute)
        {
          const std::string details = log->getError(n)->getMessage();
          log->remove(UnknownPackageAttribute);
          log->logPackageError("render", RenderEllipseAllowedAttributes,
            pkgVersion, level, version, details);
        }
        else if (log->getError(n)->getErrorId() == UnknownCoreAttribute)
        {
          const std::string details = log->getError(n)->getMessage();
          log->remove(UnknownCoreAttribute);
          log->logPackageError("render", RenderEllipseAllowedCoreAttributes,
            pkgVersion, level, version, details);
        }
      }
    }

    string elplusid = "<ellipse> element";
    if (!getId().empty()) {
      elplusid += " with the id '" + mId + "'";
    }
    // 
    // ratio double (use = "optional" )
    // 

    if (log) numErrs = log->getNumErrors();
    mIsSetRatio = attributes.readInto("ratio", mRatio);

    if ( mIsSetRatio == false && log)
    {
      if (log->getNumErrors() == numErrs + 1 &&
        log->contains(XMLAttributeTypeMismatch))
      {
        log->remove(XMLAttributeTypeMismatch);
        std::string message = "Render attribute 'ratio' from the " + elplusid +
          " must be a double.";
        log->logPackageError("render", RenderEllipseRatioMustBeDouble,
          pkgVersion, level, version, message);
      }
    }

    std::string s;
    RelAbsVector v = RelAbsVector();

    //render - FIX_ME
    // look at this wrt to errors
    //
    // cx RelAbsVector (use = required) 
    //
    assigned = attributes.readInto("cx", s,this->getErrorLog(),false, getLine(), getColumn());
    if (!assigned && log) 
    {
      std::string message = "The required attribute 'cx' is missing from the "
        + elplusid + ".";
      log->logPackageError("render", RenderEllipseAllowedAttributes,
        pkgVersion, level, version, message);
    }
    else
    {
      v.setCoordinate(s);
      if (!v.empty() && log) 
      {
        std::string message = "The syntax '" + s + "' of the attribute 'cx' on the "
          + elplusid + " does not conform to the syntax of a RelAbsVector type.";
        log->logPackageError("render", RenderEllipseCxMustBeString,
          pkgVersion, level, version, message);

      }
      else
      {
        this->setCX(v);
      }
      v.erase();
    }
    //
    // cy RelAbsVector (use = required) 
    //
    s="";
    assigned = attributes.readInto("cy", s, this->getErrorLog(), false, getLine(), getColumn());
    if (!assigned && log)
    {
      std::string message = "The required attribute 'cy' is missing from the "
        + elplusid + ".";
      log->logPackageError("render", RenderEllipseAllowedAttributes,
        pkgVersion, level, version, message);
    }
    else
    {
      v.setCoordinate(s);
      if (!v.empty() && log)
      {
        std::string message = "The syntax '" + s + "' of the attribute 'cy' on the "
          + elplusid + " does not conform to the syntax of a RelAbsVector type.";
        log->logPackageError("render", RenderEllipseCyMustBeString,
          pkgVersion, level, version, message);

      }
      else
      {
        this->setCY(v);
      }
      v.erase();
    }

    //
    // cz RelAbsVector (use = optional) 
    //

    s="";
    assigned = attributes.readInto("cz", s, getErrorLog(), false, getLine(), getColumn());
    if (!assigned)
    {
        this->mCZ=RelAbsVector(0.0,0.0);
    }
    else
    {
      v.setCoordinate(s);
      if (!v.empty() && log)
      {
        std::string message = "The syntax '" + s + "' of the attribute 'cz' on the "
          + elplusid + " does not conform to the syntax of a RelAbsVector type.";
        log->logPackageError("render", RenderEllipseCzMustBeString,
          pkgVersion, level, version, message);

      }
      else
      {
        this->setCZ(v);
      }
      v.erase();
    }

    //
    // rx RelAbsVector (use = required) 
    //

    s="";
    assigned = attributes.readInto("rx", s, this->getErrorLog(), false, getLine(), getColumn());
    if (!assigned && log)
    {
      std::string message = "The required attribute 'rx' is missing from the "
        + elplusid + ".";
      log->logPackageError("render", RenderEllipseAllowedAttributes,
        pkgVersion, level, version, message);
    }
    else
    {    
        v.setCoordinate(s);
        if (!v.empty() && log)
        {
          std::string message = "The syntax '" + s + "' of the attribute 'rx' on the "
            + elplusid + " does not conform to the syntax of a RelAbsVector type.";
          log->logPackageError("render", RenderEllipseRxMustBeString,
            pkgVersion, level, version, message);

        }
        else
        {
          this->setRX(v);
        }
        v.erase();
    }

    //
    // ry RelAbsVector (use = optional) 
    //

    s="";
    assigned = attributes.readInto("ry", s, getErrorLog(), false, getLine(), getColumn());
    if (!assigned)
    {
      if (isSetRX())
      {
        setRY(getRX());
      }
      else
      {
        this->mRY = RelAbsVector(0.0, 0.0);
      }
    }
    else
    {
      v.setCoordinate(s);
      if (!v.empty() && log)
      {
        std::string message = "The syntax '" + s + "' of the attribute 'ry' on the "
          + elplusid + " does not conform to the syntax of a RelAbsVector type.";
        log->logPackageError("render", RenderEllipseRyMustBeString,
          pkgVersion, level, version, message);

      }
      else
      {
        this->setRY(v);
      }
      v.erase();
    }
}
/** @endcond */

/** @cond doxygenLibsbmlInternal */

/*
 * Writes the attributes to the stream
 */
void
Ellipse::writeAttributes(XMLOutputStream& stream) const
{
  GraphicalPrimitive2D::writeAttributes(stream);

  if (isSetRatio() == true)
  {
    stream.writeAttribute("ratio", getPrefix(), mRatio);
  }

    std::ostringstream os;
    os << mCX;
    stream.writeAttribute("cx",getPrefix(), os.str());
    os.str("");
    os << mCY;
    stream.writeAttribute("cy",getPrefix(), os.str());
    if(this->mCZ!=RelAbsVector(0.0,0.0))
    {
        os.str("");  
        os << mCZ;
        stream.writeAttribute("cz",getPrefix(), os.str());
    }
    os.str("");
    os << mRX;
    stream.writeAttribute("rx",getPrefix(), os.str());
    if(this->mRY!=this->mRX)
    {
        os.str("");  
        os << mRY;
        stream.writeAttribute("ry",getPrefix(), os.str());
    }

  SBase::writeExtensionAttributes(stream);
}
/** @endcond */










#endif /* __cplusplus */
LIBSBML_CPP_NAMESPACE_END
