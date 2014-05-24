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

from Products.Five.browser import BrowserView

import json
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


class BroadsheetJSON(BrowserView):
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
	json_item['Broadsheet']=title
	items = self.context.listFolderContents()
	json_items = {}
	for item in items:
		itemId = item.getId()
		pos = self.context.getObjectPosition(itemId)
		json_items[pos]=item.getJSON()
	json_item['Items']=json_items
	pretty = json.dumps(json_item)    
	return pretty 

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

    # for Update bounding box
    nT = nL = nW = nH = nB = nR = 0
    nName = ""

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
        return All 

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

    def listpos(self):
	"""
	TEST
	"""
	# Where is box in relation to previous bounding box?
	isBelow = False
	isRight = False
	isAbove = False
	isLeft = False
	additionalBottom = additionalTop = additionalLeft = additionalRight = 0
	# Previous coordinates
	pT = pL = pR = pB = pW = pH = 0

	hOverlap = vOverlap = Overlap = False
        blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
        containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
        items = []
	retval = "<div>";
	retval += "<table><tr>"
	retval += "<td>Id</td><td>Top</td><td>Left</td><td>Width</td><td>Height</td><td>Right</td><td>Bottom</td><td>Overlap</td>"
	retval += "<td>pTop</td><td>pLeft</td><td>pWidth</td><td>pHeight</td><td>pRight</td><td>pBottom</td>"
	retval += "<td>bTop</td><td>bLeft</td><td>bWidth</td><td>bHeight</td><td>bRight</td><td>bBottom</td>"
	retval += "</tr>"
        for container in containers:
            items.append(container)
        for block in blocks:
            items.append(block)
	firstTime = True
	additionalX = additionalY = 0
	# Bounding coordinates
	bT = bL = bR = bB = bW = bH = 0
	for block in items:
		isBelow = False
		isRight = False
		isAbove = False
		isLeft = False
		additionalBottom = additionalTop = additionalLeft = additionalRight = 0
		top = block.getTop()
		left = block.getLeft()
		width = block.getWidth()
		height = block.getHeight()
		right = left + width
		bottom = top + height
		#if left >= pL and left <= pR:
		#	hOverlap = True
		#if right <= pR and right >= pL:
		#	hOverlap = True
		#if top >= pT and top <= pB:
		#	vOverlap = True
		#if bottom <= pB and bottom >= pT:
		#	vOverlap = True
		#if hOverlap and vOverlap:
		#	Overlap = True
		#if Overlap == True:
		#       |-------------------|
		#	|                   |
		#       |           |-----------|
		#	|	    |       |   |
                #       |           |       |   |
		#       |-----------|-------|---|
		#                   |           |
		#                   |-----------|
		#	additionalY = height - (bB - top)
		#	additionalX = width - (bR - left)
		#else:
			# There is no overlap.
			# That's great!
			# Determine for each dimension
			# if new box is above or below or left or right
			# prior to recalculating bounding box.
			
			# First vertical.
			# if height + top is greater than the previous bounding bottom
			# then new box is below old bounding box.
		    
			# If we are doing all this do we also need isOverlap
			# Yes but maybe not to calculate as above!
		if (height + top) > bB:
		    isBelow = True
		    additionalBottom = height + top - bB
		if top < bT:
		    isAbove = True
		    additionalTop = bT - top
		if (width + left) > bR:
		    isRight = True
		    additionalRight = width + left - bR
		if left < bL:
		    isLeft = True
		    additionalLeft = bL - left
		if isRight:
		    bW += additionalRight
		    bR = right
		if isLeft:
		    bW += additionalLeft
		    bL = left
		if isAbove:
		    bH += additionalTop
		    bT = top
		if isBelow:
		    bH += additionalBottom
		    bB = bottom
		retval += "<tr>"
		retval += "<td>"
		retval += block.id
		retval += "</td>"
		retval += "<td>"
		retval += str(block.getTop())
		retval += "</td>"
		retval += "<td>"
		retval += str(block.getLeft())
		retval += "</td>"
		retval += "<td>"
		retval += str(block.getWidth())
		retval += "</td>"
		retval += "<td>"
		retval += str(block.getHeight())
		retval += "</td>"
		retval += "<td>"
		retval += str(right)
		retval += "</td>"
		retval += "<td>"
		retval += str(bottom)
		retval += "</td>"
		retval += "<td>"
		if Overlap == True:
			retval += "Overlap"	
		retval += "</td>"
		if firstTime:
			firstTime = False
			bL = left
			bT = top
		retval += "<td>"
		retval += str(pT)
		retval += "</td>"
		retval += "<td>"
		retval += str(pL)
		retval += "</td>"
		retval += "<td>"
		retval += str(pW)
		retval += "</td>"
		retval += "<td>"
		retval += str(pH)
		retval += "</td>"
		retval += "<td>"
		retval += str(pR)
		retval += "</td>"
		retval += "<td>"
		retval += str(pB)
		retval += "</td>"
		retval += "<td>"
		retval += str(bT)
		retval += "</td>"
		retval += "<td>"
		retval += str(bL)
		retval += "</td>"
		retval += "<td>"
		retval += str(bW)
		retval += "</td>"
		retval += "<td>"
		retval += str(bH)
		retval += "</td>"
		retval += "<td>"
		retval += str(bR)
		retval += "</td>"
		retval += "<td>"
		retval += str(bB)
		retval += "</td>"
		freeSpaces = self.getFreeSpaces(block.id,1500,0)
		retval += "</tr>"
		retval += "<td>Free Space</td><td colspan='19'>"
		retval += "%s" % freeSpaces
		retval += "</td>"
		retval += "</tr>"
		pH = height
		pL = left
		pB = bottom
		pT = top
		pR = right
		pW = width
	retval += "</table>"
	retval += "</div>"
	return retval

    def updateBoundingBox(self,name,nT,nL,nW,nH):
	"""
	TEST
	"""
	self.nT = nT
	self.nL = nL
	self.nW = nW
	self.nH = nH
	self.nName = name
	self.nB = nT + nH
	self.nR = nL + nW

    def getPreviousBoundingBox(self,name):
	"""
	TEST
	"""
	# Where is box in relation to previous bounding box?
	isBelow = False
	isRight = False
	isAbove = False
	isLeft = False
	additionalBottom = additionalTop = additionalLeft = additionalRight = 0
	# Previous coordinates
	pT = pL = pR = pB = pW = pH = 0

	hOverlap = vOverlap = Overlap = False
        blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
        containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
        items = []
	retval = (0,0,0,0,0,0)
        for container in containers:
            items.append(container)
        for block in blocks:
            items.append(block)
	firstTime = True
	additionalX = additionalY = 0
	# Bounding coordinates
	bT = bL = bR = bB = bW = bH = 0
	# Previous Bounding Box
	pbT = pbL = pbR = pbB = pbW = pbH = 0
	for block in items:
		pbT = bT
		pbR = bR
		pbL = bL
		pbH = bH
		pbW = bW
		pbB = bB
		isBelow = False
		isRight = False
		isAbove = False
		isLeft = False
		additionalBottom = additionalTop = additionalLeft = additionalRight = 0
		top = block.getTop()
		left = block.getLeft()
		width = block.getWidth()
		height = block.getHeight()
		right = left + width
		bottom = top + height
		#if left >= pL and left <= pR:
		#	hOverlap = True
		#if right <= pR and right >= pL:
		#	hOverlap = True
		#if top >= pT and top <= pB:
		#	vOverlap = True
		#if bottom <= pB and bottom >= pT:
		#	vOverlap = True
		#if hOverlap and vOverlap:
		#	Overlap = True
		#if Overlap == True:
		#       |-------------------|
		#	|                   |
		#       |           |-----------|
		#	|	    |       |   |
                #       |           |       |   |
		#       |-----------|-------|---|
		#                   |           |
		#                   |-----------|
		#	additionalY = height - (bB - top)
		#	additionalX = width - (bR - left)
		#else:
			# There is no overlap.
			# That's great!
			# Determine for each dimension
			# if new box is above or below or left or right
			# prior to recalculating bounding box.
			
			# First vertical.
			# if height + top is greater than the previous bounding bottom
			# then new box is below old bounding box.
		    
			# If we are doing all this do we also need isOverlap
			# Yes but maybe not to calculate as above!
		if (height + top) > bB:
		    isBelow = True
		    additionalBottom = height + top - bB
		if top < bT:
		    isAbove = True
		    additionalTop = bT - top
		if (width + left) > bR:
		    isRight = True
		    additionalRight = width + left - bR
		if left < bL:
		    isLeft = True
		    additionalLeft = bL - left
		if isRight:
		    bW += additionalRight
		    bR = right
		if isLeft:
		    bW += additionalLeft
		    bL = left
		if isAbove:
		    bH += additionalTop
		    bT = top
		if isBelow:
		    bH += additionalBottom
		    bB = bottom
		if block.id == name:
		    retval = (pbT,pbL,pbW,pbH,pbB,pbR)
		    return retval
	return (0,0,0,0,0,0)

    def getBoundingBox(self,name):
	"""
	TEST
	"""
	# Where is box in relation to previous bounding box?
	isBelow = False
	isRight = False
	isAbove = False
	isLeft = False
	additionalBottom = additionalTop = additionalLeft = additionalRight = 0
	# Previous coordinates
	pT = pL = pR = pB = pW = pH = 0

	hOverlap = vOverlap = Overlap = False
        blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
        containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
        items = []
	retval = (0,0,0,0,0,0)
        for container in containers:
            items.append(container)
        for block in blocks:
            items.append(block)
	firstTime = True
	additionalX = additionalY = 0
	# Bounding coordinates
	bT = bL = bR = bB = bW = bH = 0
	for block in items:
		isBelow = False
		isRight = False
		isAbove = False
		isLeft = False
		additionalBottom = additionalTop = additionalLeft = additionalRight = 0
		if self.nName == block.id:
			top = self.nT
			left = self.nL
			width = self.nW
			height = self.nH
			right = self.nR
			bottom = self.nR
		else:
			top = block.getTop()
			left = block.getLeft()
			width = block.getWidth()
			height = block.getHeight()
			right = left + width
			bottom = top + height
		#if left >= pL and left <= pR:
		#	hOverlap = True
		#if right <= pR and right >= pL:
		#	hOverlap = True
		#if top >= pT and top <= pB:
		#	vOverlap = True
		#if bottom <= pB and bottom >= pT:
		#	vOverlap = True
		#if hOverlap and vOverlap:
		#	Overlap = True
		#if Overlap == True:
		#       |-------------------|
		#	|                   |
		#       |           |-----------|
		#	|	    |       |   |
                #       |           |       |   |
		#       |-----------|-------|---|
		#                   |           |
		#                   |-----------|
		#	additionalY = height - (bB - top)
		#	additionalX = width - (bR - left)
		#else:
			# There is no overlap.
			# That's great!
			# Determine for each dimension
			# if new box is above or below or left or right
			# prior to recalculating bounding box.
			
			# First vertical.
			# if height + top is greater than the previous bounding bottom
			# then new box is below old bounding box.
		    
			# If we are doing all this do we also need isOverlap
			# Yes but maybe not to calculate as above!
		if (height + top) > bB:
		    isBelow = True
		    additionalBottom = height + top - bB
		if top < bT:
		    isAbove = True
		    additionalTop = bT - top
		if (width + left) > bR:
		    isRight = True
		    additionalRight = width + left - bR
		if left < bL:
		    isLeft = True
		    additionalLeft = bL - left
		if isRight:
		    bW += additionalRight
		    bR = right
		if isLeft:
		    bW += additionalLeft
		    bL = left
		if isAbove:
		    bH += additionalTop
		    bT = top
		if isBelow:
		    bH += additionalBottom
		    bB = bottom
		if block.id == name:
		    retval = (bT,bL,bW,bH,bB,bR)
		    return retval
	return (0,0,0,0,0,0)

    def getFreeSpaces(self,name,widthMax=0,heightMax=0):
	# returns a list of (T,L,W,H) representing Free Space
	# W or H is 0 if infinite to right or bottom.
	# say you already have a bounding box
	# that is a previous bounding box
	# and the current box used to expand the
	# previous bounding box to the current bounding box
	# 
	# There are likely to be empty spaces
	# as well as the spaces around the new bounding box
	# the free space list
	# is the difference between the new bounding box
	# and the old bounding box
	# with respect to the infinite space around
	# the new bounding box.
	#
	#  _____________________________ 
	# |                 |           |
	# |      prev       |           |
	# -------------------           |
	# |                             |
	# |__________current____________|
	#
	#
	# There are a number of ways that the space can be
	# listed: free space will list from top to bottom as follows:
	#
	#                   ____________
	#                   |           |
	# and 
	#
	# _______________________________
	# |                              |
        #
	# and
	#
	# ________________________________
	# |
	# |_______________________________
	#  
	#                   ______________
	#                   |
	#                   |
	#                   |
	#                   |_____________
	#
	# this is all great except that we have made a top left assumption again
	# also depending on whether the page is to be
	# right expansive or bottom expansive this may include only two
	# of the four cases
	(bT,bL,bW,bH,bB,bR) = self.getBoundingBox(name)
	(pbT,pbL,pbW,pbH,pbB,pbR) = self.getPreviousBoundingBox(name)
	# how do we then compute the symmetric difference as above?
	# bounding box always completely includes the previous bounding box
	sL = abs(bL - pbL)
	sR = abs(bR - pbR)
	sT = abs(bT - pbT)
	sL = abs(bL - pbL)
	# List of open spaces
	freeSpace = []
	# Assume that we are going vertical right now!
	if sT > 0: # There is space at the top
	    freeSpaceTop = (bT,bL,0,sT)
	    if bL <= widthMax:
		freeSpace.append(freeSpaceTop)
	elif sL > 0: # There is space at the left
	    freeSpaceLeft = (bT,bL,sL,0)
	    if bL <= widthMax:
		freeSpace.append(freeSpaceLeft)
	else: # There has to be free space at the right
	    freeSpaceRight = (pbT,bR,0,bH)
	    if bR <= widthMax:
		freeSpace.append(freeSpaceRight)
	# List the space to the bottom and the right anyway
	freeSpaceBottom = (bB,bL,0,bW)
	if bL <= widthMax:
	    freeSpace.append(freeSpaceBottom)
	freeSpaceRight = (bB,bR,bH,0)
	if bR <= widthMax:
	    freeSpace.append(freeSpaceRight)
	return freeSpace
	
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
