# -*- coding: utf-8 -*-
#
# File: Scripted.py
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
from ScriptishSchema import ScriptishSchema

from Products.Five.browser import BrowserView
from Acquisition import aq_inner,aq_parent

##code-section module-header #fill in your manual code here
##/code-section module-header

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Container_schema = OrderedBaseFolderSchema.copy() + \
			BlockishSchema.copy() + \
			ScriptishSchema.copy()
			
##code-section after-schema #fill in your manual code here
##/code-section after-schema

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
	A Scripted Block gets it's information for how to layout the container
	from a .pd file or the script text field.
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
	    containerWidth = int(float(width)/float(numberOfColumns))
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


    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber):
	    """
	    Test
	    """
	    if self.getIsBlockish():
	        showLink = self.getShowLink()
	        ll = self.getLeft()
                tt = self.getTop()
	        offset = tt
		return self.callNative(c,ll,offset,REQUEST,self,top,pagenumber)
	    else:
		return self.callNative(c,x,y,REQUEST,parent,top,pagenumber)
	    return (x,y)
	
    def callNative(self,c,x,y,REQUEST,parent,top,pagenumber):
	    """
		Native Version of callPDFPDTBySameName without Wrappers
	    """
	    y = y  + 40	
	    self.left = x
	    self.top = y
            print self.Title()
	    self.pagenumber=pagenumber
    	    #skin = self.portal_skins.newspaper_templates
            skinTool = getToolByName(self, 'portal_skins')
	    #containercontainer = skinTool.newspaper_templates.test.getPhysicalPath()
	    containercontainer = '/opt/development/newholland/press/products/Newspaper/skins/newspaper_templates/'+self.Title()
	    print containercontainer
	    obj = PDFPageTemplate(self.Title(),containercontainer)
	    print "Container: %s" % self.Title()
	    #y += self.getTop()
	    #x += self.getLeft()
	    # Here is where we replace the continuePDF
	    # Which loops through the items in the folder
	    # with a obj.processScript that uses the directions in the script
	    # to decide what to call next.
	    result=obj.continuePDF(c,x,y,REQUEST,parent,pagenumber)
	    x = result[0]
	    y = result[1]
	    return (x,y)

    def getTop(self):
	    return self.y

    def getLeft(self):
	    return self.x

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

    def width(self):
        """
        width
        """
        return 100;

    def height(self):
        """
        height
        """
        return 100;

    def snapshot(self):
	"""
	"""
	width = 800
	height = 1200
	return self.getSnapshot(800,1200)

    def getSnapshot(self,width,height):
        """
        snap content
        """
	snapshot = "<div>"
	items = self.listFolderContents(contentFilter={"portal_type":"Headline"})
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

