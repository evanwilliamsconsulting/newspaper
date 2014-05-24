# -*- coding: utf-8 -*-
#
# File: Container.py
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
from interfaces import IContainer,IBlock
import interfaces
from BlockishSchema import BlockishSchema

from Products.Five.browser import BrowserView
from Acquisition import aq_inner,aq_parent

import json
##code-section module-header #fill in your manual code here
##/code-section module-header

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Container_schema = OrderedBaseFolderSchema.copy() + \
    BlockishSchema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class ContainerJSON(BrowserView):
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
	json_item['Container']=title
	items = self.context.listFolderContents()
	json_items = {}
	for item in items:
		itemId = item.getId()
		pos = item.getObjectPosition(itemId)
		json_items[pos]=item.getJSON()
	json_item['Items']=sorted(json_items,reverse=True)
	pretty = json.dumps(json_item)    
	return pretty 

class ContainerDiagnostics(BrowserView):
    """
    """
    def __init__(self,context,request):
        """
        """
        self.context = context
        self.request = request

class FullContainerView(BrowserView):
    """
    """
    def __init__(self,context,request):
        """
        """
        self.context = context
        self.request = request

class ContainerView(BrowserView):
    """
    """
    def __init__(self,context,request):
        """
        """
        self.context = context
        self.request = request



class Container(OrderedBaseFolder,  BrowserDefaultMixin):
    """
    A container is itself a Block.
    Or a Block can Reference a Container that is elsewhere.
    Or a Block can Contain a Container.
    """
    x = 0
    y = 0
    security = ClassSecurityInfo()

    implements(interfaces.IContainer,interfaces.IBlock)

    meta_type = 'Container'
    _at_rename_after_creation = True

    schema = Container_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def getPreviousElement(self,currentId):
	"""
	Returns the ID of the previous element
	"""
	ids = self.getObjectIds()
	previousId = None
	for id in ids:
	    if id == currentId:
		return previousId
	    else:
		previousId = id
	return None

    def getJSON(self):
	"""
	test
	"""
	json_result = {}
	json_item = {}
	elements = {}
	title = self.getId()
	items = self.listFolderContents()
	json_items = {}
	#
	broadsheet = self.aq_inner.aq_parent
	(bT,bL,bW,bH,bB,bR) = broadsheet.getBoundingBox(self.id)
	# New Container must be positioned outside of Bounding Box.
	
        top = self.getTop()
        left = self.getLeft()
	width = self.getWidth()
	height = self.getHeight()
	# test bounding box
	freeSpaces = broadsheet.getFreeSpaces(self.id,1200,0)
	print "free Spaces"
	print freeSpaces
	# use first Free Space
	top = bT
	left = bL
	# if first choose first
	for freeSpace in freeSpaces:
	    fT=freeSpace[0]
	    fL=freeSpace[1]
	    fW=freeSpace[2]
	    fH=freeSpace[3]
	    if fW == 0:
#		if fH > height:
		top = fT
		left =fL
		break 
	    if fH == 0:
	#	if fW > width:
		top = fT
		left = fL
		break
	# update top and left with new coordinates
	# so that bounding box will be recomputed
	# with new position
	broadsheet.updateBoundingBox(self.id,top,left+100,width,height)	
	#
	for item in items:
		itemId = item.getId()
		#json_items[itemId]=item.getJSON()
		pos = self.getObjectPosition(itemId)
		json_items[pos]=item.getJSON()
	json_item['elements']=json_items
	#json_item['top']=self.getTop()
	#json_item['left']=self.getLeft()
	json_item['top']=top
	json_item['left']=left
	json_result['Container']=json_item
	return json_result
	
    def theId(self):
        """
        TEST
        """
        return self.getId()

    def style(self):
	"""
	TEST
	"""
	style="position:relative"
	return style

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

    def getElements(self):
	"""
	Returns a list of elements in the container
	"""
	elements = self.listFolderContents() 
	return elements

    def getPreviousElement(self,givenElement):
	"""
	Returns previous element in the list
	"""
	previousElement = None
	for element in self.getElements():
	    if element==givenElement:
		return previousElement
	    previousElement=element
	return None

    security.declarePublic('setWidth')
    def setWidth(self,width):
	"""
	TEST
	"""
	self.width=width

    security.declarePublic('setHeight')
    def setWidth(self,height):
	"""
	TEST
	"""
	self.height=height

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


    def web(self):
        """
        Test
        """
        result = ""
        for item in self.listFolderContents():
            result += item.web()
        return result

    def getPosition(self):
	"""
	Returns the position of the Container.
	"""
	left = self.getLeft()
	top = self.getTop()
	return (left,top)


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
        print "Container: %s" % self.Title()
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
	    item.setNumberOfColumns(numberOfColumns)
            snapresult = item.getSnapshot(width,height)
            snapshot += snapresult[0]
            break
        items = self.listFolderContents(contentFilter={"portal_type":"Pix"})
        for item in items:
            snapresult = item.getSnapshot(width,height)
            snapshot += snapresult[0]
        snapshot += "</div>"
        return snapshot


    def getDimensions(self):
	"""
	returns the system given position
	"""
	top = self.getTop()
	left = self.getLeft()
	width = self.getWidth()
	height = self.getHeight()
	return top, left, width, height

    def getSnapshot(self,width,height):
        """
        snap content
        """
	broadsheet = self.aq_inner.aq_parent
	(bT,bL,bW,bH,bB,bR) = broadsheet.getBoundingBox(self.id)
	# New Container must be positioned outside of Bounding Box.
	
        top = self.getTop()
        left = self.getLeft()
	width = self.getWidth()
	height = self.getHeight()
	# test bounding box
	freeSpaces = broadsheet.getFreeSpaces(self.id,1200,0)
	print "free Spaces"
	print freeSpaces
	# use first Free Space
	top = bT
	left = bL
	# if first choose first
	for freeSpace in freeSpaces:
	    fT=freeSpace[0]
	    fL=freeSpace[1]
	    fW=freeSpace[2]
	    fH=freeSpace[3]
	    if fW == 0:
#		if fH > height:
		top = fT
		left =fL
		break 
	    if fH == 0:
	#	if fW > width:
		top = fT
		left = fL
		break
	# update top and left with new coordinates
	# so that bounding box will be recomputed
	# with new position
	broadsheet.updateBoundingBox(self.id,top,left+100,width,height)	

        snapshot = "<div style='position:absolute;top:"
        snapshot += str(top)
        snapshot += "px;left:"
        snapshot += str(left)
        snapshot += "px'>"
        items = self.listFolderContents(contentFilter={"portal_type":"Headline"})
        for item in items:
            snapresult = item.getSnapshot(width,height)
            snapshot += snapresult[0]
	    #snapshot += "HEADLINE"
        items = self.listFolderContents(contentFilter={"portal_type":"TextColumn"})
        for item in items:
            snapresult = item.getSnapshot(width,height)
            snapshot += snapresult[0]
        items = self.listFolderContents(contentFilter={"portal_type":"RichColumn"})
        numberOfColumns = 0
        for item in items:
            numberOfColumns += 1
        widthOfOneColumn = float(width)
        for item in items:
        	snapresult = item.getSnapshot(width,height)
        	snapshot += snapresult[0]
            	break
    #snapshot += "RICH"
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

registerType(Container, PROJECTNAME)
# end of class Container

##code-section module-footer #fill in your manual code here
##/code-section module-footer
