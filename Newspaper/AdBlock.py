# -*- coding: utf-8 -*-
#
# File: Block.py
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
from interfaces import IBlock
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
        name='containers',
        widget=ReferenceBrowserWidget(
            label='Containers',
            label_msgid='Newspaper_label_containers',
            i18n_domain='Newspaper',
        ),
        allowed_types=('Container',),
        multiValued=1,
        relationship='containerLocation',
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Block_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Block(OrderedBaseFolder,  BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IBlock)

    meta_type = 'Block'
    _at_rename_after_creation = True

    schema = Block_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def show(self): 
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    showTemplate=skin.showBlock
	    return showTemplate()

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
	    justTemplate=skin.justBlock
	    return justTemplate()
    
    def getLines(self,columnid):
	    return self['columnid'].getLines()
	    
    def listColumns(self):
	    """
	    hey!
	    """
	    return self.returnInput()

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


    def callPDTBySameName(self,REQUEST,parent,top='0',left='0',width='0',height='0',start="",end=""):
	    """
	    Test
	    """
	    print "Block"
	    print self.Title()
            style3="'"
	    containercontainer = '/opt/development/newholland/press/products/Newspaper/skins/newspaper_templates/'+self.Title()+'.pd'
	    result = PDFPageTemplate(self.Title(),containercontainer)
	    theDiv = self.getDivid()
            theClass = self.getClass()


	    style2="'"
            theLeft = self.getLeft()
            if theLeft is not None:
		style2 += "left:"
                style2 += str(theLeft)
		style2 += "px"
                style2 += ";"
		style3 += "left:"
                style3 += str(theLeft)
		style3 += "px"
                style3 += ";"
                left = theLeft
            else:
                left = 0
            style2 += "position:relative;"
	    output = "<div style='position:absolute;left:0px;top:"
	    output += str(top)
	    output += "px'><div id='"
	    output += self.getId()
            output += "' class='"
            output += "container'"

	    start = "<div class='"
	    start += "name"
	    start += "' onmouseover="
	    start += '"'
	    start += "this.style.cursor='hand'"
	    start += '"'
	    style3 += "display:none;position:relative;background-color:rgba(0,255,0,0.5);color:red;'"
	    start += " style="
	    start += style3
	    start += ">"
	    start += self.getId()
	    start += "</div>"
            start = "<div style='clear:both;'></div>"


            
	    output2 = result.continueWEB(REQUEST,parent,containercontainer,start)
	    style2 += "top:"
	    style2 += str(2*int(output2[1]))
   	    style2 += "px;"
	    style2 += "'"
            output += "style="
	    output += style2
            output += ">"
	    output += output2[0]
	    output += "</div><br/>"


            height = 0
	    return (output,top,left,width,height)


    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top):
	    """
	    Test
	    """
	    print "Block"
	    obj = self.getContainers()
	    x += self.getLeft()
            y += self.getTop()
	    for item in obj:
		item.callPDFPDTBySameName(c,x,y,REQUEST,item,top)
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

    def web(self):
            """
            WEB
            """
            return "WEB"

registerType(Block, PROJECTNAME)
# end of class Block

##code-section module-footer #fill in your manual code here
##/code-section module-footer

