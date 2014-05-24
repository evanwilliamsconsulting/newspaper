# -*- coding: utf-8 -*-
#
# File: Line.py
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
import interfaces

from justifier import Justifier

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Newspaper.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='lineVerbage',
        widget=StringField._properties['widget'](
            label='Lineverbage',
            label_msgid='Newspaper_label_lineVerbage',
            i18n_domain='Newspaper',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Line_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Line(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ILine)

    meta_type = 'Line'
    _at_rename_after_creation = True

    schema = Line_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def show(self): 
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    showTemplate=skin.showLine
	    return showTemplate()

    def just(self): 
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    justTemplate=skin.justLine
	    return justTemplate()

    def getColumnWidth(self):
	    """ 
	    Test
	    """
	    theColumn=self.aq_inner.aq_parent
	    theWidth=theColumn.getColumnWidth()
	    return theWidth

    def setVerbage(self,verbage):
	    """
	    Test
	    """
	    self.setLineVerbage(verbage)

    def getLine(self):
	    """
	    Test
	    """
	    return self.getLineVerbage()


    def callPDTBySameName(self,REQUEST,parent,top,left,width,height,start,end):
	    """
	    Test
	    """
	    theLine = self.getLine()
	    newLine = ""
            carrot = True
            for aChar in theLine:
 		if aChar=='<':
      			carrot = False
                if carrot:
                	newLine += aChar
		if aChar=='>':
			carrot = True
	    return (theLine,top,left,width,height)

    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top):
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    theLine = self.getLine()
	    newLine = ""
            carrot = True
            for aChar in theLine:
 		if aChar=='<':
      			carrot = False
                if carrot:
                	newLine += aChar
		if aChar=='>':
			carrot = True
	    trimLine = newLine.strip()
	    textobject = c.beginText()
	    columnWidth = float(self.getColumnWidth()) 
	    #columnWidth = 180
	    words = trimLine.split()
            numWords = float(len(words))
            stringWidth = float(0)
	    wordX = x
            wordY = y 
            totalWords = float(0)
	    for word in words:
	        totalWords += c.stringWidth(word,"Times-Roman",11)
	    remainder = columnWidth - totalWords
            if numWords > 0:
	        spaceSize = remainder / numWords
            for word in words:
	        textobject.setTextOrigin(wordX,wordY)
                stringWidth = c.stringWidth(word,"Times-Roman",11)
		textobject.setFont("Times-Roman",11)
		textobject.textLine(word)
                wordX += stringWidth + spaceSize
            #spaces = float(numWords - 1)
	    #whiteSpace = columnWidth - stringWidth
            #if spaces > 0:
            #    wordSpace = whiteSpace / spaces
	    #    textobject.setWordSpace(wordSpace)
	    #textobject.setTextOrigin(x,y)
	    #textobject.setFont("Times-Roman", 11)
            #textobject.textLine(trimLine)
	    c.drawText(textobject)
            y+=12
	    return (x,y)

    def getXOffset(self):
            """
            test
            """
            return 0

    def getYOffset(self):
            """
            test
            """
            return 0

registerType(Line, PROJECTNAME)
# end of class Line

##code-section module-footer #fill in your manual code here
##/code-section module-footer

