# -*- coding: utf-8 -*-
#
# File: Broadsheet.py
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
from Products.Archetypes.Schema import Schema
from Products.Archetypes.Field import *
from Products.Archetypes.Widget import *
from Products.Archetypes.atapi import *
from zope.interface import implements
from plone.portlets.interfaces import ILocalPortletAssignable
import interfaces

from Products.Five.browser import BrowserView

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate


from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics

from reportlab.pdfbase.ttfonts import TTFont

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    IntegerField(
        name='pageNo',
        widget=IntegerField._properties['widget'](
            label='Pageno',
            label_msgid='Newspaper_label_pageNo',
            i18n_domain='Newspaper',
        ),
    ),
    IntegerField(
        name='pageWidth',
        widget=IntegerField._properties['widget'](
            label='Pagewidth',
            label_msgid='Newspaper_label_pageWidth',
            i18n_domain='Newspaper',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Broadsheet_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema
#class M_Broadsheet(NewsFolder.__class__): pass

class BlockView(BrowserView):
    """ A View of the Widget """
    def __init__(self, context, request):
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
    #def __call__():
    #
	
class EditView(BrowserView):
    """ A View of the Widget """
    def __init__(self, context, request):
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
    #def __call__():
    #

class Broadsheet(OrderedBaseFolder,ExtensibleMetadata,BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IBroadsheet,ILocalPortletAssignable)

    meta_type = 'Broadsheet'
    _at_rename_after_creation = True

    schema = Broadsheet_schema

    #__metaclass__=M_Broadsheet

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header
    something = 'ferf'
    top = 0
    left = 0
    width = 0
    height = 0
    
    # Methods

    def getIssueUrl(self):
	    """
 	    Test 
	    """
	    parent = self.aq_inner.aq_parent
	    #link = parent.getId()
	    link = "" 
	    return link

    def view(self,REQUEST):
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    showTemplate=skin.justBroadsheet
	    return showTemplate(REQUEST)

    def show(self): 
	    """
	    Test
	    """
	    return self.web()

    def pageNumber(self):
	    """
	    Return Page Number
            """
	    pageno = self.getPageNo()
            if pageno == 1:
		textValue = "One"
	    elif pageno == 2:
		textValue = "Two"
	    elif pageno == 3:
	        textValue = "Three"
            else:
		textValue = "Four"
	    theReturn = "<a href='"
	    theReturn += self.absolute_url()
	    theReturn += "'>"
            theReturn += textValue
	    theReturn += "</a>"
	    return theReturn

    def linky(self):
	    """
	    API Universal per product to return link to this pages's view
	    """
	    return self.absolute_url()

    def what(self,REQUEST):
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    showTemplate=skin.justBroadsheet
	    return showTemplate(REQUEST)

    def just(self): 
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    showTemplate=skin.justBroadsheet
	    return showTemplate()

    def blocks(self):
	    """
	    Test
	    """
	    blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
	    containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
	    return blocks

    def Blocks(self):
	    """
	    Test
	    """
	    Blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
	    Containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
	    All = self.listFolderContents()
	    return Containers 

    def listAllBlocks(self):
	    """
	    Test
	    """
	    Blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
	    Containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
	    ids = []
	    for block in Blocks:
		theId = block.getId()
		ids.append(theId)
	    for container in Containers:
	        theId = container.getId()
		ids.append(theId)
	    return ids

    def Pages(self):
	    """
	    Test
	    """
	    parent = self.aq_inner.aq_parent
	    return parent.pages()

    def listContainers(self):
	    """
	    """
	    return self.returnInput()

    def returnInput(self):
	    """
	    Test
	    """
	    stringValue = ""
	    items = self.listFolderContents(contentFilter={"portal_type":"Container"})
	    #items=self.contentItems()
	    return items
    
    def callPDTBySameName(self,show,REQUEST,parent,top,left):
	    """
	    Test
	    """
	    thePath = '/opt/development/newholland/press/products/Newspaper/skins/newspaper_templates/' + self.Title() + '.pd'
	    containercontainer = PDFPageTemplate(self.Title(),thePath)
	    showTemplate=containercontainer.continueWEB(REQUEST,parent,thePath,'0','0','0','0','0','0')
	    return showTemplate[0]

    def web(self):
	    """
	    """
	    blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
	    retval = "<div>"
	    for block in blocks:
		retval+=block.web()
	    retval += "</div>"
	    retval += "<div>"
	    containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
	    for container in containers:
		retval+=container.web()
	    retval += "</div>"
	    return retval

    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber):
	    """
	    Test
	    """
            #textobject = c.beginText()
            #textobject.setTextOrigin(x,y)
            #textobject.setFont('FilosBold',12)
            #textobject.textLine("Broadsheet")
	    #c.drawText(textobject)
            #print self.Title()
	    blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
	    for block in blocks:
		print block
		block.callPDFPDTBySameName(c,x,y,REQUEST,parent,top,pagenumber)
	    containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
	    for container in containers:
		print container
		container.callPDFPDTBySameName(c,x,y,REQUEST,parent,top,pagenumber)
	    wordy = self.listFolderContents(contentFilter={"portal_type":"Wordy"})
	    for word in wordy:
		word.callPDFPDTBySameName(c,x,y,REQUEST,parent,top,pagenumber)
	    return (x,y)

    def editsnap(self):
	    """
	    Test
	    """
	    blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
	    containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
	    items = []
	    for container in containers:
		items.append(container)
	    for block in blocks:
		items.append(block)
	    retval = "<div id='hFinderFiles'>"
	    red = 0x40;
	    green = 0x40;
	    blue = 0x40;
	    iter = 0;
	    for block in items:
		iter  += 1
		top=block.getTop()
		left=block.getLeft()
		width = block.getWidth()
		height = block.getHeight()
		width *= .4 
		height *= .4 
		top *= .4 
		left *= .4 
		someval = "<div "
		cssclass = "hFinderDirectory" + str(iter)
		someval += "class='" + cssclass + "' title='/"+block.id+"' id='" + block.id + "' "
		someval += "style='"
		rgb = format((blue<<16)|(green<<8)|red, '06x')
		blue += 40
		red += 40
		green += 40
		someval += "background-color:#"+rgb+";"
		someval += "position:absolute;"
		someval += "top:"+str(top)+"px;"
		someval += "left:"+str(left)+"px;"
		someval += "width:"+str(width)+"px;"
		someval += "height:"+str(height)+"px;"
		someval += "z-index:20;"
		someval += "border-style:solid;border-width:1px;"
		someval += "'>"
		someval += "<div>"
		width *= .8
		someval += block.getEditsnap(width,height)
		someval += "</div>"
		someval += "</div>"
		retval += someval
	    retval += "</div>"
	    retval += "<div id='hFinderEnd'></div>"
            return retval


    def listsnap(self):
	    """
	    Test
	    """
	    blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
	    containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
	    items = []
	    for container in containers:
		items.append(container)
	    for block in blocks:
		items.append(block)
	    retval = "<div id='hFinderFiles'>"
	    red = 0x40;
	    green = 0x40;
	    blue = 0x40;
	    iter = 0;
	    for block in items:
		iter  += 1
		top=block.getTop()
		left=block.getLeft()
		width = block.getWidth()
		height = block.getHeight()
		width *= .8 
		height *= .8 
		top *= .8 
		left *= .8 
		someval = "<div "
		cssclass = "hFinderDirectory" + str(iter)
		someval += "class='" + cssclass + "' title='/"+block.id+"' id='" + block.id + "' "
		someval += "style='"
		rgb = format((blue<<16)|(green<<8)|red, '06x')
		blue += 40
		red += 40
		green += 40
		someval += "background-color:#"+rgb+";"
		someval += "width:"+str(width)+"px;"
		someval += "height:"+str(height)+"px;"
		someval += "z-index:20;"
		someval += "border-style:solid;border-width:1px;"
		someval += "'>"
		someval += "<div>"
		snapWidth = width * .8
		snapHeight = height * .8
		someval += block.getEditsnap(snapWidth,snapHeight)
		someval += "</div>"
		someval += "</div>"
		someval += "<br/>"
		retval += someval
	    retval += "</div>"
	    retval += "<div id='hFinderEnd'></div>"
            return retval


registerType(Broadsheet, PROJECTNAME)
# end of class Broadsheet

##code-section module-footer #fill in your manual code here
##/code-section module-footer

