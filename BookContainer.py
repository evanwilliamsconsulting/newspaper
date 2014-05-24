# -*- coding: utf-8 -*-
#
# File: BookContainer.py
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
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate
from Products.CMFCore.utils import getToolByName
from interfaces import IBookContainer
import interfaces

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    IntegerField(
	name='left',
	widget=IntegerField._properties['widget'](
	    label='left',
	    label_msgid='Newspaper_label_left',
	    i18n_domain='Newspaper',
	),
    ),
    IntegerField(
	name='top',
	widget=IntegerField._properties['widget'](
	    label='top',
	    label_msgid='Newspaper_label_top',
	    i18n_domain='Newspaper',
	),
    ),
    StringField(
        name='divid',
        widget=StringField._properties['widget'](
            label='Divid',
            label_msgid='Newspaper_label_divid',
            i18n_domain='Newspaper',
        ),
    ),
    StringField(
        name='class',
        widget=StringField._properties['widget'](
            label='Class',
            label_msgid='Newspaper_label_class',
            i18n_domain='Newspaper',
        ),
    ),
    TextField(
        name='markup',
        widget=TextAreaWidget(
            label='Markup',
            label_msgid='Newspaper_label_markup',
            i18n_domain='Newspaper',
        ),
    ),
    ReferenceField(
        name='pdfBlock',
        widget=ReferenceBrowserWidget(
            label='Broadsheets',
            label_msgid='Newspaper_label_containers',
            i18n_domain='Newspaper',
        ),
        allowed_types=('Broadsheet',),
        multiValued=1,
        relationship='containerLocation',
    ),
    ReferenceField(
        name='webBlock',
        widget=ReferenceBrowserWidget(
            label='Webpage',
            label_msgid='Newspaper_label_containers',
            i18n_domain='Newspaper',
        ),
        allowed_types=('Webpage',),
        multiValued=1,
        relationship='containerLocation',
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BookContainer_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BookContainer(OrderedBaseFolder,  BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IBookContainer)

    meta_type = 'BookContainer'
    _at_rename_after_creation = True

    schema = BookContainer_schema

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
	    theLink += "/topItem"
            return theLink

    security.declarePublic('showBookContainer')
    def showBookContainer(self):
            """
            TEST 
            """
    	    skin = self.portal_skins.newspaper_templates
	    showTemplate = skin.showBookContainer
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
	    justTemplate=skin.justBookContainer
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
	    topTemplate=skin.topBookContainer
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


    def web(self):
	    """
	    Test
	    """
	    result = ""
	    for item in self.listFolderContents():
		result += item.web()
	    return result



    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber):
	    """
	    Test
	    """
            print self.Title()
	    containers = self.listFolderContents()
	    x += self.getLeft()
	    y += self.getTop()
	    top = y
	    for container in containers:
		print container
		result=container.callPDFPDTBySameName(c,x,y,REQUEST,self,top,pagenumber)
	    	y += result[1]
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

    def listItems(self):
	"""
	hey
	"""
	parent = self.aq_inner.aq_parent
	items = parent.listFolderContents(contentFilter={"portal_type":"Broadsheet"})
	return items

    def left(self):
	"""
	getter
	"""
	return self.getLeft()

    def top(self):
	"""
	getter
	"""
	return self.getTop()

registerType(BookContainer, PROJECTNAME)
# end of class BookContainer

##code-section module-footer #fill in your manual code here
##/code-section module-footer

