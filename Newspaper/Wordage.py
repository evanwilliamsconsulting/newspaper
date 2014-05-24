# -*- coding: utf-8 -*-
#
# File: Wordage.py
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
from Products.Five.browser import BrowserView
from zope.interface import implements
import interfaces
from columnar import Columnar

import hyphenate 

from Products.CMFCore.utils import getToolByName

from browserdefault import BrowserDefaultMixin

from richly import RichColumnar

from Products.Newspaper.config import *

from Products.CMFCore.utils import getToolByName

from WordySchema import WordySchema


from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter

import string 
from cStringIO import StringIO


from zope.component import getMultiAdapter

##code-section module-header #fill in your manual code here
##/code-section module-header

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Wordage_schema = BaseSchema.copy() + \
	WordySchema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Wordage(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IWordage,interfaces.IContainer)

    meta_type = 'Wordage'
    _at_rename_after_creation = True

    schema = Wordage_schema
    containerChoice = None

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def submitColumnChoice(self,REQUEST):
	    """
	    Test
	    """
	    # Form's select_column contains the value of the column selected.
	    catalog = getToolByName(self, 'portal_catalog')
	    items = catalog.searchResults({'portal_type': 'Column'})
	    self.columnChoice = REQUEST["select_column"]
	    for item in items:
	        if item.id==self.columnChoice:
		    column=item.getObject()
	    if column is None:
		    return
	    skin = self.portal_skins.newspaper_templates
	    submitTemplate = skin.submit
	    i = 0
	    columnSize = self.getColumnSize()
	    verbage = self.getWordage()
	    col = Columnar(verbage,columnSize)
	    columns = col.getLines()
	    lineCount = col.countLines()
	    while i<=lineCount:
		lineid = str(i)
		if len(lineid) == 1:
		    lineid='0'+lineid
		portal_types = getToolByName(column, "portal_types")
		type_info = portal_types.getTypeInfo('Line')
		lineitem = type_info._constructInstance(column, lineid)
		lineitem.markCreationFlag()
	    	lineitem.setWordage(columns[i])
		i+=1
	    return submitTemplate()

    def selectedColumn(self,REQUEST):
	    """
	    return Selected Column
	    """
	    selectedColumn = REQUEST["select_column"]
	    return selectedColumn

    def applyWordageToIssue(self):
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    applyIssueTemplate=skin.applyIssue
	    return applyIssueTemplate()
    
    def submitIssueChoice(self):
	    """
	    Test
	    """
	    portal_url = getToolByName(self, "portal_url")
            portal = portal_url.getPortalObject()
	    issueChoice=self.REQUEST['select_issue']
	    issueChoice=issueChoice.split('-')
	    yearId = issueChoice[0]
	    monthId = issueChoice[1]
	    issueId = issueChoice[2]
	    
	    items = portal.listFolderContents(contentFilter={"portal_type":"Folder"})
	    for item in items:
		if item.id == "issues":
		    years=item.listFolderContents(contentFilter={"portal_type":"Folder"})
		    for year in years:
			if year.id == yearId:
			    months=year.listFolderContents(contentFilter={"portal_type":"Folder"})
			    for month in months:
                                if month.id == monthId:
			            issues = month.listFolderContents(contentFilter={"portal_type":"Issue"})
				    for issue in issues:
					if issue.id == issueId:
					     selectedIssue=issue
	    # Now Make a Container Here
	    #print selectedIssue
	    #print selectedIssue.id
	    #print selectedIssue.__dict__
	    #typestool = getToolByName(self,'portal_types')
	    #typestool.constructContent(type_name="Container",container=selectedIssue,title=self.id,id=self.id)
	    # does the content already exist?
	    if self.id not in selectedIssue:
	    	selectedIssue.invokeFactory(type_name="Container",id=self.id)
		# Now create a Headline and a Rich Column
		headlineId=self.id+"_headline"
		selectedIssue[self.id].invokeFactory(type_name="Headline",id=headlineId)
		richColumnId=self.id+"_rich"
		selectedIssue[self.id].invokeFactory(type_name="RichColumn",id=richColumnId)
		containerObject = selectedIssue[self.id]
		headlineObject = containerObject[headlineId]
		richColumnObject = containerObject[richColumnId]
		headlineObject.setHeadline(self.title)
		headlineObject.setFontsize(22)
		headlineObject.setWidth(0)
		wordage = self
		charsPerLine = self.getColumnSize()
		richColumnObject.setArticle(self)
		richColumnObject.setStartLine(0)
		richColumnObject.setEndLine(400)
		richColumnObject.setCharsPerLine(charsPerLine)
    
    def submitBroadsheetChoice(self):
	    """
	    Test
	    """
	    self.broadsheetChoice=self.REQUEST['select_broadsheet']
    	    skin = self.portal_skins.newspaper_templates
	    applyContainerTemplate=skin.applyContainer
	    return applyContainerTemplate()
    
    def submitContainerChoice(self):
	    """
	    Test
	    """
	    self.containerChoice=self.REQUEST['select_container']
    	    skin = self.portal_skins.newspaper_templates
	    applyColumnTemplate=skin.applyColumn
	    return applyColumnTemplate()
    
    def applyWordageToColumn(self):
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    applyColumnTemplate=skin.applyColumn
	    return applyColumnTemplate()
    
    def returnLine(self,lineid):
	    """
	    Trick
	    """
	    #Count Characters
	    lineWidth=35
	    lineStart=lineWidth*int(lineid)
	    lineEnd=lineWidth*int(lineid)+lineWidth
	    theWordage=self.getWordage()
	    return theWordage[lineStart:lineEnd]

    def returnColumn(self):
	    """
	    Test
	    """
	    catalog = getToolByName(self, 'portal_catalog')
	    items = catalog.searchResults({'portal_type': 'Container'})
	    for item in items:
	        if item.id==self.containerChoice:
		    issue=item.getObject()
	    broadsheets = issue.getFolderContents(contentFilter={'portal_type':'Column'})
	    stringValue = "<div id='instructions'>Please select a Column for issue: %s</div>" % issue.id
	    stringValue += "<form method='post' action=\"/" + self.id + "/submitColumnChoice\">"
	    for broadsheet in broadsheets:
		    sheet = broadsheet.getObject()
		    stringValue += "<input type=radio name='select_column' value='%s'>%s<BR/>" % (sheet.id,sheet.Title())
	    stringValue += "<input type='submit'/>"
	    stringValue += "</form>"
	    return stringValue

    def returnBroadsheet(self):
	    """
	    Test
	    """
	    catalog = getToolByName(self, 'portal_catalog')
	    items = catalog.searchResults({'portal_type': 'Issue'})
	    for item in items:
	        if item.id==self.issueChoice:
		    issue=item.getObject()
	    broadsheets = issue.getFolderContents(contentFilter={'portal_type':'Broadsheet'})
	    stringValue = "<div id='instructions'>Please select a Broadsheet for issue: %s</div>" % issue.id
	    stringValue += "<form method='post' action=\"/" + self.id + "/submitBroadsheetChoice\">"

	    for broadsheet in broadsheets:
		    sheet = broadsheet.getObject()
		    stringValue += "<input type=radio name='select_broadsheet' value='%s'>%s<BR/>" % (sheet.id,sheet.id)
	    stringValue += "<input type='submit'/>"
	    stringValue += "</form>"
	    return stringValue

    def returnContainer(self):
	    """
	    Test
	    """
	    catalog = getToolByName(self, 'portal_catalog')
	    items = catalog.searchResults({'portal_type': 'Broadsheet'})
	    for item in items:
	        if item.id==self.broadsheetChoice:
		    issue=item.getObject()
	    broadsheets = issue.getFolderContents(contentFilter={'portal_type':'Container'})
	    stringValue = "<div id='instructions'>Please select a Container for issue: %s</div>" % issue.id
	    stringValue += "<form method='post' action=\"/" + self.id + "/submitContainerChoice\">"

	    for broadsheet in broadsheets:
		    sheet = broadsheet.getObject()
		    stringValue += "<input type=radio name='select_container' value='%s'>%s<BR/>" % (sheet.id,sheet.id)
	    stringValue += "<input type='submit'/>"
	    stringValue += "</form>"
	    return stringValue

    def returnIssue(self):
	    """
	    Test
	    """
	    portal_url = getToolByName(self, "portal_url")
            portal = portal_url.getPortalObject()
	    thisPath = self.getPhysicalPath()
	    absoluteUrl='/'.join(thisPath)
	    items = portal.listFolderContents(contentFilter={"portal_type":"Folder"})
	    stringValue = "<div id='instructions'>Please select an Issue</div>"
	    stringValue += "<form method='post' action=\"" + absoluteUrl + "/submitIssueChoice"+ "\">"
	    for item in items:
		if item.id == "issues":
		    years=item.listFolderContents(contentFilter={"portal_type":"Folder"})
		    for year in years:
			months=year.listFolderContents(contentFilter={"portal_type":"Folder"})
			for month in months:
			    issues = month.listFolderContents(contentFilter={"portal_type":"Issue"})
			    for issue in issues:
				    print year.id
				    print month.id
				    print issue.id
				    issueLabel = "%s-%s-%s" % (year.id,month.id,issue.id)
				
	    			    stringValue += "<input type=radio name='select_issue' value='%s'>%s<BR/>" % (issueLabel,issueLabel)
	    stringValue += "<input type='submit'/>"
	    stringValue += "</form>"
	    return stringValue

    def showLines(self): 
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    showTemplate=skin.showWordage
	    return showTemplate()

    def returnText(self):
	    """
	    Test
	    """
	    return self.getWordage()

    def theWidth(self):
	    """
	    test
	    """
	    return "180"

    def theHeight(self):
	    """
	    Test
	    """
	    return "500"

    def wordage(self,REQUEST):
	    """
	    Return Wordage
	    """
	    return self.getWordage()

    def pdf(self,REQUEST): 
            """
   	    Test
            """
            skin = self.portal_skins.invoicing_templates
            showTemplate=skin.showIssue
	    output = StringIO()
	    c = canvas.Canvas(output,pagesize=letter,bottomup=0)
	    x=35
	    y=50
            textobject = c.beginText()
            textobject.setTextOrigin(x,y)
            textobject.setFont('Times-Roman',11)
	    xorig = x
	    yorig = y
	    xleft = 35
	    ytop = 35
	    ysave = y
	    width = self.getColumnSize() * 6
	    verbage = self.getWordage()
            theCarrotStart = False
            theCarrotEnd = False
            theTagOpen = True
            theTag = ""
            theWordage = " "
	    gotTheTag = False
	    nasty = 'Â'
	    verblen = len(verbage)
            m = -1
	    # while within a paragraph
	    total = 0
	    i = 0
	    while m < verblen-1:
		m += 1
		theChar = verbage[m]
		if theChar == '<':
		    theTag = ""
		    theCarrotStart = True
		    gotTheTag = True
                elif theChar == '/':
                    theTagOpen = False
		    theCarrotStart = False
		    gotTheTag = True
                elif theChar == '>':
                    theCarrotEnd = True
		    theCarrotStart = False
		    print "the tag %s" % theTag
		    gotTheTag = False 
		elif theCarrotStart and theChar != "<":
		    theTag += theChar
		    gotTheTag = True
		elif not gotTheTag:
		    if theChar != nasty:
		        theWordage += theChar
                if theCarrotEnd == True and theTagOpen == False:
		    theCarrotEnd = False
		    theTagOpen = True
		    just = RichColumnar(theWordage,self.getColumnSize())
		    lines = just.getLines()
		    totalLines = just.countLines()
		    p = 0 
		    while p <= totalLines and i<200:
			if i >=0:
			    theLine = just.returnLine(p)
			    self.drawALine(c,x,y,theLine)
			    y += 12 
			p += 1
			i += 1
		    theWordage = " "
		total += i
	    c.showPage()
	    c.save()
	    result = output.getvalue()
	    output.close()
	    response = REQUEST.RESPONSE
            response.setHeader('Content-type','application/pdf')
	    return result 

    def drawALine(self,c,x,y,theLine):
	    words = theLine.split()
	    totalWordLength = 0
	    for word in words:
		print "error"
		print word
		theWord = ""
		nasty = '\xC0\x82'
		for letter in word:
		    if letter <  nasty:
			theWord += letter
		theWord = theWord.decode('latin-1')
		totalWordLength += c.stringWidth(theWord,"Times-Roman",11)
	    lineLength = 5 * self.getColumnSize()
	    if len(words) > 2:
	        whiteSpace = (lineLength - totalWordLength) / (len(words) - 1)
            else:
		whiteSpace = 10
            textobject = c.beginText()
            textobject.setTextOrigin(x,y)
	    textobject.setFont("Times-Roman",11)
	    for word in words:
		theWord = ""
		nasty = '\xC0\x82'
		for letter in word:
		    if letter < nasty:
		        theWord += letter
		theWord = theWord.decode('latin-1')
		#theWord = unicode(word,'latin-1')
		stringWidth = c.stringWidth(theWord,"Times-Roman",11)
	        textobject.setTextOrigin(x,y)
	    	textobject.textLine(theWord)
		x += stringWidth
		x += whiteSpace 
	    c.drawText(textobject)
	    print "drawText"
	    print textobject
            y+=4
	    return (x,y)

    def publish(self,REQUEST):
            """
            Publish
            """
	    skin = self.portal_skins.newspaper_templates
	    showTemplate=skin.publishWordage
	    return showTemplate()

registerType(Wordage, PROJECTNAME)
# end of class Wordage

##code-section module-footer #fill in your manual code here
##/code-section module-footer
    
