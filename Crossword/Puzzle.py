# -*- coding: utf-8 -*-
#
# File: Puzzle.py
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
from reportlab.lib.colors import black,white
import interfaces
import string

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Crossword.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    IntegerField(
        name='top',
        widget=IntegerField._properties['widget'](
            label='Top',
            label_msgid='YouCanBox_label_top',
            i18n_domain='YouCanBox',
        ),
    ),
    IntegerField(
        name='left',
        widget=IntegerField._properties['widget'](
            label='Left',
            label_msgid='YouCanBox_label_left',
            i18n_domain='YouCanBox',
        ),
    ),
    StringField(
        name='Caption',
        widget=StringField._properties['widget'](
            label='Caption',
            label_msgid='Crossword_label_Caption',
            i18n_domain='Crossword',
        ),
    ),
    StringField(
        name='Author',
        widget=StringField._properties['widget'](
            label='Author',
            label_msgid='Crossword_label_Author',
            i18n_domain='Crossword',
        ),
    ),
    DateTimeField(
        name='DateOfPublication',
        widget=DateTimeField._properties['widget'](
            label='Dateofpublication',
            label_msgid='Crossword_label_DateOfPublication',
            i18n_domain='Crossword',
        ),
    ),
    TextField(
        name='Objective',
        widget=TextAreaWidget(
            label='Objective',
            label_msgid='Crossword_label_Objective',
            i18n_domain='Crossword',
        ),
    ),
    IntegerField(
        name='gridpx',
        widget=IntegerField._properties['widget'](
            label='Gridpx',
            label_msgid='Crossword_label_gridpx',
            i18n_domain='Crossword',
        ),
    ),
    IntegerField(
        name='gridwide',
        widget=IntegerField._properties['widget'](
            label='Gridwide',
            label_msgid='Crossword_label_gridwide',
            i18n_domain='Crossword',
        ),
    ),
    IntegerField(
        name='gridhigh',
        widget=IntegerField._properties['widget'](
            label='Gridhigh',
            label_msgid='Crossword_label_gridhigh',
            i18n_domain='Crossword',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Puzzle_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Puzzle(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IPuzzle)

    meta_type = 'Puzzle'
    _at_rename_after_creation = True

    schema = Puzzle_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header
    def helloWorld(self):
	"""
		Say Hello
	"""
	width = self.gridpx * (self.gridwide+3)
	height = self.gridpx * (self.gridhigh+3)

	widthtext = str(width) + "px"
	heighttext = str(height) + "px"

	thewidth = str(width)
	theheight = str (height)

	svgheader = '<svg width="%s" height="%s">' % (widthtext,heighttext)
	bigrect = '<rect x="10" y="10" width="%s" height="%s" style="fill: #000000"/>' % (thewidth,theheight)
	svgbottom = '</svg>'

	svgtext = svgheader + bigrect 

	for someItem in self.listFolderContents(contentFilter={"portal_type" : "Clue"}):
		theAnswer = someItem.Answer
		theOrientation = someItem.Orientation
		answerCount = len(theAnswer)
		theClue = someItem.title
		theClueX = 10+someItem.X*self.gridpx
		theClueY = 10+someItem.Y*self.gridpx
		if theOrientation:
			gridWide= str(self.gridpx*answerCount)+"px"
			gridHigh= str(self.gridpx)+"px"
		else:
			gridWide= str(self.gridpx)+"px"
			gridHigh= str(self.gridpx*answerCount)+"px"
		smallWidth = str(theClueX)
		smallHeight = str(theClueY)	
		smallWidthText = smallWidth + "px"
		smallHeightText = smallHeight + "px"
		smallrect = '<rect x="%s" y="%s" width="%s" height="%s" style="fill: #FFFFFF" />' % (smallWidth,smallHeight,gridWide,gridHigh)
		svgtext += smallrect	
		# Let me put in the letters
		nextLetter=1
		for aLetter in theAnswer:
			letterWidth=nextLetter*self.gridpx
			if theOrientation:
				textWidth = 10 + theClueX+self.gridpx*(nextLetter-1)
		    		textHeight=theClueY+0.8*self.gridpx
			else:
				textWidth = 20+self.gridpx*someItem.X
		    		textHeight=theClueY+(nextLetter-1)*self.gridpx+self.gridpx*0.8
			textWidth=str(textWidth)
			textHeight=str(textHeight)
			nextLetter+=1
			thetext = '<text x="%s" y="%s" style="font-weight:bold">%s</text>' % (textWidth,textHeight,aLetter)
			svgtext += thetext	


	svgtext += svgbottom

	return svgtext

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header
    def haveAClue(self):
	"""
		Say Hello
	"""
	width = self.gridpx * (self.gridwide+2)
	height = self.gridpx * (self.gridhigh+2)

	widthtext = str(width) + "px"
	heighttext = str(height) + "px"

	thewidth = str(width)
	theheight = str (height)

	svgheader = '<svg width="%s" height="%s">' % (widthtext,heighttext)
	bigrect = '<rect x="10" y="10" width="%s" height="%s" style="fill: #000000"/>' % (thewidth,theheight)
	svgbottom = '</svg>'

	svgtext = svgheader + bigrect 

	nextQuestion = 1
	theKey = (0,0)
	theSet = set(theKey)
	for someItem in self.listFolderContents(contentFilter={"portal_type" : "Clue"}):
		theKey = (someItem.X,someItem.Y)
		theAnswer = someItem.Answer
		theOrientation = someItem.Orientation
		answerCount = len(theAnswer)
		theClue = someItem.title
		theClueX = 10+someItem.X*self.gridpx
		theClueY = 10+someItem.Y*self.gridpx
		if theOrientation:
			gridWide= str(self.gridpx*answerCount)+"px"
			gridHigh= str(self.gridpx)+"px"
		else:
			gridWide= str(self.gridpx)+"px"
			gridHigh= str(self.gridpx*answerCount)+"px"
		smallWidth = str(theClueX)
		smallHeight = str(theClueY)	
		smallWidthText = smallWidth + "px"
		smallHeightText = smallHeight + "px"
		smallrect = '<rect x="%s" y="%s" width="%s" height="%s" style="fill: #FFFFFF" />' % (smallWidth,smallHeight,gridWide,gridHigh)
		svgtext += smallrect	
		# Let me put in the letters
		nextLetter=1
		firstLetter = True
		for aLetter in theAnswer:
			letterWidth=nextLetter*self.gridpx
			if theOrientation:
				textWidth = 10 + theClueX+self.gridpx*(nextLetter-1)
		    		textHeight=theClueY+0.8*self.gridpx
			else:
				textWidth = 20+self.gridpx*someItem.X
		    		textHeight=theClueY+(nextLetter-1)*self.gridpx+self.gridpx*0.8
			textWidth=str(textWidth)
			textHeight=str(textHeight)
			nextLetter+=1
			questionNumber=someItem.ItemNo
			if firstLetter:
				theQuestion = str(someItem.X) + " " + str(someItem.Y)
				thetext = '<text x="%s" y="%s" style="font-size:7pt">%s</text>' % (textWidth,textHeight,theQuestion)
				svgtext += thetext	
			firstLetter=False
		nextQuestion += 1
		theSet.add(theKey)
	svgtext += svgbottom

	return svgtext

    # Methods
    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber):
        """
        Test
	"""
	y = 1170 - y
	xorig = self.getLeft()
	yorig = y
	x = xorig + 40
	y = 1170 - yorig
	savex = x
	savey = y
	textobject = c.beginText()
	textobject.setFont("Times-Roman",22)
	textobject.setTextOrigin(x,y)
	textobject.textLine(self.getCaption())
	y -= 25
	textobject.setFont("Times-Roman",11)
	textobject.setTextOrigin(x,y)
	i = 1
	for someItem in self.listFolderContents(contentFilter={"portal_type" : "Clue"}):
	    theOrientation = someItem.Orientation
	    theAnswer = someItem.Answer
	    question = someItem.title
	    if theOrientation:
		across = "ACROSS"
	    else:
		across = "UP"
	    theOutputLine = str(i) + " " + across + ": " + question
	    y -= 14
	    i += 1
	    textobject.setTextOrigin(x,y)
	    textobject.textLine(theOutputLine)
	c.drawText(textobject)
	y -= 30
	savey = y
	gridsize = int(float(self.getGridpx())/2)
	widthx = gridsize * (self.getGridwide()+3)
	heighty = gridsize * (self.getGridhigh()+3)
	c.setStrokeColor(black)
	c.setFillColor(black)
	newy = y - 300
	newx = x 
	c.rect(newx,newy,widthx,heighty,stroke=1,fill=1)
	i = 1
	for someItem in self.listFolderContents(contentFilter={"portal_type" : "Clue"}):
		theAnswer = someItem.Answer
		theOrientation = someItem.Orientation
		answerCount = len(theAnswer)
		startx = newx + someItem.X * gridsize
		starty = newy + someItem.Y * gridsize
		if theOrientation:
			gridWide= gridsize*answerCount
			gridHigh= gridsize 
		else:
			gridWide= gridsize
			gridHigh= gridsize*answerCount
		c.setStrokeColor(white)
		c.setFillColor(white)
		c.rect(startx,starty,gridWide,gridHigh,stroke=1,fill=1)
		if theOrientation:
		    c.drawString(startx-10*len(str(i)),starty+10,str(i))
		else:
		    c.drawString(startx,starty-gridsize,str(i))
		i += 1
	# Now for the clues (on the side)
	textobject = c.beginText()
	x = savex + 2*widthx + 30
	y = savey
	textobject.setTextOrigin(x,y)
	textobject.textLine("DOWN")
	c.drawText(textobject)
	return (x,y)

registerType(Puzzle, PROJECTNAME)
# end of class Puzzle

##code-section module-footer #fill in your manual code here
##/code-section module-footer

