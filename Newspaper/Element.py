# -*- coding: utf-8 -*-
#
# File: Headline.py
#
# Copyright (c) 2011 by unknown <unknown>
# Generator: ArchGenXML Version 2.6
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.Five.browser import BrowserView
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate


##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    IntegerField(
        name='width',
        widget=IntegerField._properties['widget'](
            label='width',
            label_msgid='Newspaper_label_width',
            i18n_domain='Newspaper',
            ),
        ),
    IntegerField(
        name='height',
        widget=IntegerField._properties['widget'](
            label='Height',
            label_msgid='Newspaper_label_Height',
            i18n_domain='Newspaper',
            ),
        ), 
    BooleanField(
        name='glueX',
        widget=BooleanField._properties['widget'](
            label='glueX',
            label_msgid='Newspaper_label_glueX',
            i18n_domain='Newspaper',
            ),
        ),
    BooleanField(
        name='glueY',
        widget=BooleanField._properties['widget'](
            label='glueY',
            label_msgid='Newspaper_label_glueY',
            i18n_domain='Newspaper',
            ),
        ),
    BooleanField(
        name='prevX',
        widget=BooleanField._properties['widget'](
            label='prevX',
            label_msgid='Newspaper_label_prevX',
            i18n_domain='Newspaper',
            ),
        ),
    BooleanField(
        name='prevY',
        widget=BooleanField._properties['widget'](
            label='prevY',
            label_msgid='Newspaper_label_prevY',
            i18n_domain='Newspaper',
            ),
        ),
    BooleanField(
        name='resetX',
        widget=BooleanField._properties['widget'](
            label='resetX',
            label_msgid='Newspaper_label_resetX',
            i18n_domain='Newspaper',
            ),
        ),
    BooleanField(
        name='resetY',
        widget=BooleanField._properties['widget'](
            label='resetY',
            label_msgid='Newspaper_label_resetY',
            i18n_domain='Newspaper',
            ),
        ),
    BooleanField(
        name='drift',
	default=True,
        widget=BooleanField._properties['widget'](
            label='drift',
            label_msgid='Newspaper_label_drift',
            i18n_domain='Newspaper',
            ),
        ),
    BooleanField(
        name='gravity',
	default=True,
        widget=BooleanField._properties['widget'](
            label='gravity',
            label_msgid='Newspaper_label_gravity',
            i18n_domain='Newspaper',
            ),
        ),
    IntegerField(
        name='offsetX',
	default=5,
        widget=IntegerField._properties['widget'](
            label='offsetX',
            label_msgid='Newspaper_label_offsetX',
            i18n_domain='Newspaper',
            ),
        ),
    IntegerField(
        name='offsetY',
	default=5,
        widget=IntegerField._properties['widget'](
            label='OffsetY',
            label_msgid='Newspaper_label_OffsetY',
            i18n_domain='Newspaper',
            ),
        ), 
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Element_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema
class Element(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IElement,interfaces.IPositionable)

    meta_type = 'Element'
    _at_rename_after_creation = True

    schema = Element_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def getSchema(self):
	"""
	returns Schema so derived Classes can use it
	"""
	return schema

    def getContainer(self):
	"""
	Through Acquisition, returns Container of this element
	"""
	aqContainer = self.aq_inner.aq_parent
	return aqContainer

    def getPosition(self):
	"""
	Returns Element Position (left,top)
	Applies Rules to previous Element to determine
	Current element position
	"""
	pLeft = pTop = nLeft = nTop = 0
	container = self.getContainer()
	previousElement = container.getPreviousElement(self)
	# retrieve Previous width and height
	if previousElement == None:
		pWidth = 0
		pHeight = 0
		(pLeft,pTop) = container.getPosition()
		pResetY = False
	else:
		pWidth = previousElement.getWidth()
		pHeight = previousElement.getHeight()	
		pResetY = previousElement.getResetY()
		# retrieve Previous left and top
		(pLeft,pTop) = previousElement.getPosition()
	# apply rules
	# getDrift
	# getGravity
	# glueX
	## if glueX is on then glue to right of previous
	## unless previous element reset X
	beforePreviousElement = container.getPreviousElement(previousElement)
	if self.getPrevX():
		(bLeft,bTop) = beforePreviousElement.getPosition()
		while beforePreviousElement != None and bLeft == bTop:
			beforePreviousElement = container.getPreviousElement(beforePreviousElement)
			(bLeft,bTop) = beforePreviousElement.getPosition()
		nLeft = bLeft + pWidth
	elif self.getGlueX() and not previousElement.getResetX():
	    nLeft = pLeft + pWidth
	else: # if Drift is on then drift to right of previous
	    if self.getDrift(): #or not previousElement.getResetX():
		nLeft = pLeft + pWidth
	    else: # no glue no Drift: overlay
		nLeft = pLeft	
	# glueY 
	## if glueY is on then glue to bottom of Previous
	## unless previous element reset Y
	beforePreviousElement = container.getPreviousElement(previousElement)
	if self.getPrevY():
		(bLeft,bTop) = beforePreviousElement.getPosition()
		while pTop  == bTop and  None != beforePreviousElement:
			beforePreviousElement = container.getPreviousElement(beforePreviousElement)
			(bLeft,bTop) = beforePreviousElement.getPosition()
		#nTop = bTop + pHeight
		nTop = bTop + pHeight
	elif self.getGlueY() and not pResetY:
	    nTop = pTop + pHeight
	else: # if Gravity is on then glue to bottom of Previous
	    if self.getGravity() or pResetY:
		nTop = pTop 
	    else: # no glue no gravity: overlay
		nTop = pTop 
	## if there are offsets add them
	nLeft += self.getOffsetX()
	nTop += self.getOffsetY() 
	return (nLeft,nTop)
 
    def getSize(self):
	"""
	Returns Element Dimensions (width,height)
	"""
	return (self.getWidth(),self.getHeight()) 

    def getJSON(self):
	attributes = {}
        attributes['width']=self.getWidth()
        attributes['height']=self.getHeight()
        attributes['glueX']=self.getGlueX()
        attributes['glueY']=self.getGlueY()
        attributes['prevX']=self.getPrevX()
        attributes['prevY']=self.getPrevY()
	attributes['resetX']=self.getResetX()
	attributes['resetY']=self.getResetY()
	attributes['drift']=self.getDrift()
	attributes['gravity']=self.getGravity()
	attributes['offsetX']=self.getOffsetX()
	attributes['offsetY']=self.getOffsetY()
	return attributes

##code-section after-local-

registerType(Element, PROJECTNAME)
# end of class Headline

##code-section module-footer #fill in your manual code here
##/code-section module-footer
