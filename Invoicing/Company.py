# -*- coding: utf-8 -*-
#
# File: Company.py
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


from plone.app.blob.field import BlobField, ImageField
from StringIO import StringIO
from PIL import *
from Products.CMFCore import permissions
from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate
from Products.CMFCore.utils import getToolByName

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Invoicing.config import *

from Products.Newspaper import interfaces as newspaper


import reportlab.pdfgen.canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
#import string, cStringIO
from PIL import *

from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter

import string 


from Products.Five.browser import BrowserView
import json
##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='Company',
        widget=StringField._properties['widget'](
            label='Company',
            label_msgid='Invoicing_label_Company',
            i18n_domain='Invoicing',
        ),
    ),
    StringField(
        name='Address1',
        widget=StringField._properties['widget'](
            label='Address1',
            label_msgid='Invoicing_label_Address1',
            i18n_domain='Invoicing',
        ),
    ),
    StringField(
        name='Address2',
        widget=StringField._properties['widget'](
            label='Address2',
            label_msgid='Invoicing_label_Address2',
            i18n_domain='Invoicing',
        ),
    ),
    StringField(
        name='City',
        widget=StringField._properties['widget'](
            label='City',
            label_msgid='Invoicing_label_City',
            i18n_domain='Invoicing',
        ),
    ),
    StringField(
        name='State',
        widget=StringField._properties['widget'](
            label='State',
            label_msgid='Invoicing_label_State',
            i18n_domain='Invoicing',
        ),
    ),
    StringField(
        name='PostalCode',
        widget=StringField._properties['widget'](
            label='Postalcode',
            label_msgid='Invoicing_label_PostalCode',
            i18n_domain='Invoicing',
        ),
    ),
    StringField(
        name='Telephone',
        widget=StringField._properties['widget'](
            label='Telephone',
            label_msgid='Invoicing_label_Telephone',
            i18n_domain='Invoicing',
        ),
    ),
    StringField(
        name='Fax',
        widget=StringField._properties['widget'](
            label='Fax',
            label_msgid='Invoicing_label_Fax',
            i18n_domain='Invoicing',
        ),
    ),
    StringField(
        name='email',
        widget=StringField._properties['widget'](
            label='Email',
            label_msgid='Invoicing_label_email',
            i18n_domain='Invoicing',
        ),
    ),
    StringField(
        name='website',
        widget=StringField._properties['widget'](
            label='Website',
            label_msgid='Invoicing_label_website',
            i18n_domain='Invoicing',
        ),
    ),
    FloatField(
	'price',
	default=40,
	required=True,
	widget=DecimalWidget(
		label= u'Price',
		description = u'Insertion Cost',
		size=8,
	),
    ),
    ReferenceField(
        name='displayAd',
        widget=InAndOutWidget(
            label='DisplayAd',
            label_msgid='Newspaper_label_displayad',
            i18n_domain='Newspaper',
        ),
        allowed_types=('Advertizement',),
        multiValued=1,
        relationship='containerLocation',
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Company_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class CompanyJSON(BrowserView):
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
	json_item['Company']=title
	attributes={}
	json_item['attributes']=attributes
	json_items={}
	items = self.context.listFolderContents()
	for item in items:
	    itemId = item.getId()
	    pos = self.context.getObjectPosition(itemId)
	    json_items[itemId]=item.getJSON()
	json_item['elements']=json_items
	pretty = json.dumps(json_item)    
	return pretty 

class Company(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ICompany,newspaper.IContainer)

    meta_type = 'Company'
    _at_rename_after_creation = True

    schema = Company_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def theId(self):
	    """
	    TEST
	    """
	    return self.getId()

    def theLinky(self):
            """
	    return a link to this container's standard view
            """
            theLink = self.absolute_url()
            return theLink

    security.declarePublic('showContainer')
    def showContainer(self):
            """
            TEST 
            """
    	    skin = self.portal_skins.newspaper_templates
	    showTemplate = skin.showContainer
	    return showTemplate()

    def contains(self): 
	    """
	    Test
	    """
	    items = self.listItems()
	    return items

    def toggleDivTagsOn(self):
	    """
            return true if Div Tags are on.
	    """
	    return self.getToggleDivTagsOn() 

    def just(self): 
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    justTemplate=skin.justContainer
	    return justTemplate()
    
    def getLines(self,columnid):
	    return self['columnid'].getLines()
	    
    def listColumns(self):
	    """
	    hey!
	    """
	    return self.returnInput()
    
    def topItem(self):
            """
            TEST
            """
    	    skin = self.portal_skins.newspaper_templates
	    topTemplate=skin.topContainer
	    return topTemplate()
	    
    def topList(self):
            """
            TEST
            """
    	    skin = self.portal_skins.newspaper_templates
	    topList=skin.topList
	    return topList()
	    

    def listKeys(self):
            """
            hey!
            """
	    returnObjects = []
	    keys = self.keys()
	    for key in keys:
		returnObjects.append(self[key])
	    return returnObjects

    def returnInput(self):
	    """
	    Test
	    """
	    stringValue = ""
	    items = self.listFolderContents(contentFilter={"portal_type":"Column"})
	    #items = self.contentItems()
	    #for item in items:
	    #    stringValue += item[1].just()
	    #return stringValue
	    #urls=[]
	    #for item in items:
	#	if item.getHeadline() == True:
	#            urls.append(item)
	#    for item in items:
	#	if item.getHeadline() == False:
	#            urls.append(item)
	    return items

    def getImage(self):
	   """
	   Test
	   """
	   items = self.listFolderContents(contentFilter={"portal_type":"Pix"})
	   return items[0].getPicture()


    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber):
	    """
	    Test
	    """
	    y = 1200 - y
	    self.left = x
	    self.top = y
            print self.Title()
	    self.pagenumber=pagenumber
            skinTool = getToolByName(self, 'portal_skins')
	    items = self.listFolderContents(contentFilter={"portal_type":"Advertizement"})
	    for ad in items:
		theImage = ad.getImage()
	        thePress = ImageReader(StringIO(str(theImage.data)))
		(width,height) = thePress.getSize()
	        c.drawImage(thePress,x,y,width,height)
	    return (x,y)

    def getXOffset(self):
            """
            Test
            """
            return 0

    def getYOffset(self):
            """
            Test
            """
            return 0

    def pdf(self):
            """
            PDF
            """
            return "PDF"

    def block(self):
	    """
	    BLOCK
            """
	    return "BLOCK"

    security.declarePublic(permissions.View,'getSnapshot')
    def getSnapshot(self,width,height):
	"""
	snapshot
	"""
	new_width = width * 1.2
	new_height = height * 1.2
	#items = self.listFolderContents(contentFilter={"portal_type":"Advertizement"})
	items = self.getDisplayAd()
	for ad in items:
	    return ad.getSnapshot(new_width,new_height)

    def listItems(self):
	"""
	hey
	"""
	parent = self.aq_inner.aq_parent
	items = parent.listFolderContents(contentFilter={"portal_type":"Broadsheet"})
	return items

    security.declarePublic(permissions.View,'getWidth')
    def getWidth(self):
	"""
	Return Width
	"""
	width = 0
	items = self.listFolderContents(contentFilter={"portal_type":"Advertizement"})
	for ad in items:
	    width=ad.getWidth()
	return width

    security.declarePublic(permissions.View,'getHeight')
    def getHeight(self):
	"""
	Return Height
	"""
	height = 0
	items = self.listFolderContents(contentFilter={"portal_type":"Advertizement"})
	for ad in items:
	    height=ad.getHeight()
	return height

    security.declarePublic(permissions.View,'web')
    def web(self):
	"""
	Return Web Content
        """
	#items = self.listFolderContents(contentFilter={"portal_type":"Advertizement"})
	items = self.getDisplayAd()
	theDiv = ""
	theDiv2 = ""
	for ad in items:
	    theImage = ad.getId()
	    theDiv2 = theImage
	    theDiv = "<div id='"
            theDiv += theImage
            theDiv += "' class='pix' style='margin-left:30px;position:relative;top:"
	    theDiv += str(0)
	    theDiv += "px;left:"
	    theDiv += str(0)
	    theDiv += "px;'"
            #theDiv += "style='border-color:blue;border-width:2px;border-style:solid;top:"
            left = 0
            width = ad.getWidth()
            height = ad.getHeight()
            theDiv += ">"
	    relativeUrl = ad.absolute_url(relative=1)
	    #relativeUrl = relativeUrl[3:]
	    fullUrl = "http://www.nhpress.net/" + relativeUrl
	    theTag = "<img width='"+str(ad.getWidth())+"' height='"+str(ad.getHeight())+"' src='"+fullUrl+"/imagecopy/'/>"
	    theDiv += theTag
	    theDiv += "</div>"
	return theDiv

    def getJSON(self,top,left):
	    """
	    Test
   	    """
	    json_item = {}
	    title = self.getId()
	    json_item['Company']=title
	    json_item['top']=top
	    json_item['left']=left
	    attributes={}
	    json_item['attributes']=attributes
	    items = self.listFolderContents()
	    json_items={}
	    for item in items:
		itemId = item.getId()
		json_items=item.getJSON()
	    json_item['elements']=json_items
	    return json_item 

##code-section module-footer #fill in your manual code here
##/code-section module-footer

registerType(Company, PROJECTNAME)
# end of class Company
