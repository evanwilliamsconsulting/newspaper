# -*- coding: utf-8 -*-
#
# File: MultiColumn.py
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
from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate
from Products.CMFCore.utils import getToolByName
from interfaces import IMultiColumn,IBlock,IBoxMultiColumn
import interfaces
from BlockishSchema import BlockishSchema

from Products.Five.browser import BrowserView
from Acquisition import aq_inner,aq_parent

##code-section module-header #fill in your manual code here
##/code-section module-header

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

MultiColumn_schema = OrderedBaseFolderSchema.copy() + \
			BlockishSchema.copy()

BoxMultiColumn_schema = OrderedBaseFolderSchema.copy() + \
			BlockishSchema.copy()
			
##code-section after-schema #fill in your manual code here
##/code-section after-schema

class CodeMultiColumnView(BrowserView):
    """
    """
    def __init__(self,context,request):
        """
        """
        self.context = context
        self.request = request

class FullMultiColumnView(BrowserView):
    """
    """
    def __init__(self,context,request):
        """
        """
        self.context = context
        self.request = request

class MultiColumnView(BrowserView):
    """
    """
    def __init__(self,context,request):
	"""
	"""
	self.context = context
	self.request = request
	


class MultiColumn(OrderedBaseFolder,  BrowserDefaultMixin):
    """
	A container is itself a Block.
	Or a Block can Reference a MultiColumn that is elsewhere.
	Or a Block can Contain a MultiColumn.
    """
    x = 0
    y = 0
    security = ClassSecurityInfo()

    implements(interfaces.IMultiColumn,interfaces.IBlock)

    meta_type = 'MultiColumn'
    _at_rename_after_creation = True

    schema = MultiColumn_schema

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

    security.declarePublic('showMultiColumn')
    def showMultiColumn(self):
            """
            TEST 
            """
    	    skin = self.portal_skins.newspaper_templates
	    showTemplate = skin.showMultiColumn
	    return showTemplate()

    security.declarePublic('getWidth')
    def getWidth(self):
            """
            TEST
            """
	    width = 0
	    items = self.listFolderContents(contentFilter={"portal_type":"Pix"})
	    for item in items:
		width=item.getWidth()	
	        width *= 1.2
	    items = self.listFolderContents(contentFilter={"portal_type":"RichColumn"})
	    numberOfColumns = 0
	    for item in items:
		width+=item.getWidth()	
		numberOfColumns += 1
	    if numberOfColumns == 0:
	        numberOfColumns = 1
	    containerWidth = int(float(width)*0.7)
	    return containerWidth 
            
    security.declarePublic('getHeight')
    def getHeight(self):
            """
            TEST
            """
	    height = 0
	    items = self.listFolderContents()
	    for item in items:
	        height+=item.getHeight()	
	    return height
            
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
	    justTemplate=skin.justMultiColumn
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
	    topTemplate=skin.topMultiColumn
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
	    y = y  + 40	
	    left = self.getLeft()
	    top = self.getTop()
            print self.Title()
	    self.pagenumber=pagenumber
    	    #skin = self.portal_skins.newspaper_templates
            skinTool = getToolByName(self, 'portal_skins')
	    #containercontainer = skinTool.newspaper_templates.test.getPhysicalPath()
	    containercontainer = '/opt/development/newholland/press/products/Newspaper/skins/newspaper_templates/'+self.Title()
	    print containercontainer
	    obj = PDFPageTemplate(self.Title(),containercontainer)
	    print "MultiColumn: %s" % self.Title()
	    result=obj.continuePDF(c,left,top,REQUEST,self,pagenumber)
	    x = result[0]
	    y = result[1]
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

    def snapshot(self):
	"""
	"""
	width = self.getWidth()
	height = self.getHeight() 
	return self.getSnapshot(width,height)

    def getEditsnap(self,width,height):
        """
        snap content
        """
	top = self.getTop()
	left = self.getLeft()
	top = int(1.2 * float(top))
	left = int(1.2 * float(left))
	snapshot="<div class='snapcontents'>"
	items = self.listFolderContents(contentFilter={"portal_type":"Headline"})
	for item in items:
	    snapresult = item.getSnapshot(width,height)
	    snapshot += snapresult[0]
	items = self.listFolderContents(contentFilter={"portal_type":"TextColumn"})
	for item in items:
	    snapresult = item.getSnapshot(width,height)
	    snapshot += snapresult[0]
	items = self.listFolderContents(contentFilter={"portal_type":"RichColumn"})
	numberOfColumns = 0
	for item in items:
	    numberOfColumns += 1
	if numberOfColumns == 0:
	    numberOfColumns = 1
	widthOfOneColumn = float(width)/numberOfColumns
	for item in items:
	    snapresult = item.getSnapshot(width,height)
	    snapshot += snapresult[0]
	    break
	items = self.listFolderContents(contentFilter={"portal_type":"Pix"})
	for item in items:
	    snapresult = item.getSnapshot(width,height)
	    snapshot += snapresult[0]
	snapshot += "</div>"
	return snapshot

    
    def getSnapshot(self,width,height):
        """
        snap content
        """
	top = self.getTop()
	left = self.getLeft()
	top = int(1.2 * float(top))
	left = int(1.2 * float(left))
	snapshot = "<div style='position:absolute;top:"
	snapshot += str(top)
	snapshot += "px;left:"
	snapshot += str(left)
	snapshot += "px'>"
	items = self.listFolderContents(contentFilter={"portal_type":"Headline"})
	for item in items:
	    snapresult = item.getSnapshot(width,height)
	    snapshot += snapresult[0]
	items = self.listFolderContents(contentFilter={"portal_type":"TextColumn"})
	for item in items:
	    snapresult = item.getSnapshot(width,height)
	    snapshot += snapresult[0]
	items = self.listFolderContents(contentFilter={"portal_type":"RichColumn"})
	numberOfColumns = 0
	for item in items:
	    numberOfColumns += 1
	if numberOfColumns == 0:
	    numberOfColumns = 1
	widthOfOneColumn = float(width)/numberOfColumns
	for item in items:
	    snapresult = item.getSnapshot(width,height)
	    snapshot += snapresult[0]
	    break
	items = self.listFolderContents(contentFilter={"portal_type":"Pix"})
	for item in items:
	    snapresult = item.getSnapshot(width,height)
	    snapshot += snapresult[0]
	snapshot += "</div>"
	return snapshot

    security.declarePublic('full')
    def full(self):
        """
        snap content
        """
	width = 960
	height = 1120
	top = self.getTop()
	left = self.getLeft()
	top = int(1.2 * float(top))
	left = int(1.2 * float(left))
	top = 180
	snapshot = "<div style='position:absolute;top:"
	snapshot += str(top)
	snapshot += "px'>"
	items = self.listFolderContents(contentFilter={"portal_type":"Headline"})
	for item in items:
	    snapresult = item.getSnapshot(width,height)
	    snapshot += snapresult[0]
	items = self.listFolderContents(contentFilter={"portal_type":"TextColumn"})
	for item in items:
	    snapresult = item.getSnapshot(width,height)
	    snapshot += snapresult[0]
	items = self.listFolderContents(contentFilter={"portal_type":"RichColumn"})
	numberOfColumns = 0
	for item in items:
	    numberOfColumns += 1
	if numberOfColumns == 0:
	    numberOfColumns = 1
	widthOfOneColumn = float(width)/numberOfColumns
	for item in items:
	    snapresult = item.alltext(width,height)
	    snapshot += snapresult
	    break
	items = self.listFolderContents(contentFilter={"portal_type":"Pix"})
	for item in items:
	    snapresult = item.getSnapshot(width,height)
	    snapshot += snapresult[0]
	snapshot += "</div>"
	return snapshot

#    
#    def getSnapshot(self,width,height):
#	"""
#	snapshot
#	"""
#	snapshot = "<div class='container'>"
#	for item in self.listFolderContents():
#	    (snap,returnWidth,returnHeight) = item.getSnapshot(width,height)
#	    snapshot += snap
#	    height -= returnHeight
#	    if height <= 0:
#	        break
#	    snapshot += "<br/>"
#	snapshot += "</div>"
#	return snapshot

class BoxMultiColumn(MultiColumn):
    """
	This is a MultiColumn that has a box around it.
	A container is itself a Block.
	Or a Block can Reference a MultiColumn that is elsewhere.
	Or a Block can Contain a MultiColumn.
    """
    implements(interfaces.IMultiColumn,interfaces.IBlock,interfaces.IBoxMultiColumn)

    meta_type = 'BoxMultiColumn'
    _at_rename_after_creation = True

    schema = BoxMultiColumn_schema

    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber):
	    """
	    Test
	    """
	    return super(BoxMultiColumn,self).callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber)

registerType(MultiColumn, PROJECTNAME)
registerType(BoxMultiColumn, PROJECTNAME)
# end of class MultiColumn

##code-section module-footer #fill in your manual code here
##/code-section module-footer

