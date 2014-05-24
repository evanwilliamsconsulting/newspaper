# -*- coding: utf-8 -*-
#
# File: Advertizement.py
#
# Copyright (c) 2012 by unknown <unknown>
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
from Products.CMFCore import permissions
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.Archetypes.public import BaseContent,registerType
#from Products.PloneGetPaid.interfaces import IBuyableMarker

from Products.Invoicing.config import *
from plone.app.blob.field import BlobField, ImageField


from Products.Five.browser import BrowserView
import json
##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ImageField(
        name='imagecopy',
        widget=ImageField._properties['widget'](
            label='imagecopy',
            label_msgid='Invoicing_label_imagecopy',
            i18n_domain='Invoicing',
        ),
	storage=AttributeStorage(),
    ),
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
	    label='height',
	    label_msgid='Newspaper_label_height',
	    i18n_domain='Newspaper',
	),
    ),
    IntegerField(
        name='numberOfInsertions',
        widget=IntegerField._properties['widget'](
            label='Numberofinsertions',
            label_msgid='Invoicing_label_numberOfInsertions',
            i18n_domain='Invoicing',
        ),
    ),
    FloatField(
	'price',
	required=True,
	widget=DecimalWidget(
		label= u'Price',
		description = u'Insertion Cost',
		size=8,
	),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Advertizement_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class AdvertizementJSON(BrowserView):
    """ JSON Encoded Issue """
    def __init__(self,context,request):
        """ Initialize context and request as view multiadaption parameters.

        Note that the BrowserView constructor does this for you.
        This step here is just to show how view receives its context and
        request parameter. You do not need to write __init__() for your
        views.
        """
        self.context = context
        self.request = request

    # by default call will call self.index() method which is mapped
    # to ViewPageTemplateFile specified in ZCML
    def __call__(self):
   	self.request.response.setHeader("Content-type","application/json")
	json_item = {}
	title = self.context.getId()
	json_item['Advertizement']=title
	attributes={}
	attributes['width']=self.context.getWidth()
	attributes['height']=self.context.getHeight()
	pixpath = self.context.absolute_url() + '/getImagecopy'
	attributes['adpath']=pixpath
	json_item['attributes']=attributes
	pretty = json.dumps(json_item)    
	return pretty 

class Advertizement(BaseContent):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IAdvertizement)

    meta_type = 'Advertizement'
    _at_rename_after_creation = True

    schema = Advertizement_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    security.declarePublic(permissions.View,'getImage');
    def getImage(self):
	"""
	"""
	theImage = self.getImagecopy()
	return theImage

    security.declarePublic(permissions.View,'getTheBlob');
    def getTheBlob(self):
	"""
	"""
	theImage = self.getImagecopy()
	return theImage.getBlob()

    security.declarePublic(permissions.View,'getSnapshot')
    def getSnapshot(self,width,height):
        """
        Test
        """
 	tag = self.getField('imagecopy').tag(self,height=height,width=width)
	return tag 

    security.declarePublic(permissions.View,'snapshot');
    def snapshot(self):
        """
	Test
	"""
	theImage = self.getId()
	theDiv = "<div id='"
        theDiv += theImage
        theDiv += "'>"
	theTag = "<img width='"+str(self.getWidth())+"' height='"+str(self.getHeight())+"' src='"+self.absolute_url()+"/imagecopy'/>"
	theDiv += theTag
	theDiv += "</div>"
	return theDiv

    def getJSON(self):
	    """
	    Test
   	    """
	    json_item = {}
	    title = self.getId()
	    json_item['Pix']=title
	    attributes={}
	    attributes['width']=self.getWidth()
	    attributes['height']=self.getHeight()
	    pixpath = self.absolute_url() + '/getImagecopy'
	    attributes['pixpath']=pixpath
	    json_item['attributes']=attributes
	    return json_item 

registerType(Advertizement, PROJECTNAME)
# end of class Advertizement

##code-section module-footer #fill in your manual code here
##/code-section module-footer

