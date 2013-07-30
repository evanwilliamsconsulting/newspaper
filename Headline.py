# -*- coding: utf-8 -*-
#
# File: Headline.py
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

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='Headline',
        widget=StringField._properties['widget'](
            label='Headline',
            label_msgid='Newspaper_label_Headline',
            i18n_domain='Newspaper',
        ),
    ),
    IntegerField(
	name='width',
	widget=IntegerField._properties['widget'](
	    label='width',
	    label_msgid='Newspaper_label_width',
	    i18n_domain='Newspaper',
	),
    ),
    IntegerField(
        name='Fontsize',
        widget=IntegerField._properties['widget'](
            label='Fontsize',
            label_msgid='Newspaper_label_Fontsize',
            i18n_domain='Newspaper',
        ),
    ), 
    StringField(
        name='headlineclass',
	default='headlineclass',
        widget=StringField._properties['widget'](
            label='Headline Class',
            label_msgid='Newspaper_label_headclass',
            i18n_domain='Newspaper',
        ),
    ),
    BooleanField(
	name='italic',
	default=False,
        widget=BooleanField._properties['widget'](
	    label='italic',
	    label_msgid='Newspaper_label_italic',
	    i18n_domain='Newspaper',
	),
    ),
    BooleanField(
	name='glueX',
        widget=BooleanField._properties['widget'](
	    label='glueX',
	    label_msgid='Newspaper_label_glueX',
	    i18n_domain='Newspaper',
	),
    ),
    BooleanField(
	name='glueY',
        widget=BooleanField._properties['widget'](
	    label='glueY',
	    label_msgid='Newspaper_label_glueY',
	    i18n_domain='Newspaper',
	),
    ),
    BooleanField(
	name='offsetX',
        widget=BooleanField._properties['widget'](
	    label='offsetX',
	    label_msgid='Newspaper_label_offsetX',
	    i18n_domain='Newspaper',
	),
    ),
    BooleanField(
	name='resetY',
        widget=BooleanField._properties['widget'](
	    label='resetY',
	    label_msgid='Newspaper_label_resetY',
	    i18n_domain='Newspaper',
	),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Headline_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Headline(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IHeadline)

    meta_type = 'Headline'
    _at_rename_after_creation = True

    schema = Headline_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def contains(self): 
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    showTemplate=skin.showHeadline
	    return showTemplate()

    def just(self): 
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    justTemplate=skin.justLine
	    return justTemplate()

    def show(self):
	    """
            Show
            """
	    skin = self.portal_skins.newspaper_templates
            showTemplate = skin.showHeadline
	    return showTemplate()

    def web(self):
	    """
	    Web
	    """
	    return self.getHeadline()

    def solo(self):
	    """
	    Jam out the line.
            """
            return self.getHeadline()

    def formatted(self):
	    """
	    The line formatted
            """
	    return self.getHeadline()

    def getWidth(self):
	    """
	    Test
	    """
	    return 0

    def getHeight(self):
	    """
	    Test
	    """
	    return 70

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


    def callPDTBySameName(self,REQUEST,parent,top,left,width,height,start="",end=""):
	    """
	    Test
	    """
	    fontSize = str(3*self.getFontsize()/4)
            height = str(2*self.getFontsize())
            result = "<div id='"
	    result += self.getId()
	    result += "' class='headline' "
	    #result += "style='border-style:solid;border-color:purple;border-width:2px;font-size:"
	    result += "style='font-size:"
	    result += fontSize
	    result += "pt;"
            #result += "top:"
            #result += str(self.getTop()+int(top))
            #result += "px;"
            result += "position:relative;'>"
            #result += ">"
	    result += start
	    result += self.getHeadline()
            result += "</div>"
	    top = str(self.getTop()+int(top)+int(height))
	    return (result,top,left,width,height)

    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber):
	    """
	    Test
	    """
	    print "HEADLINE"
	    glueX = self.getGlueX()
            glueY = self.getGlueY()
    	    skin = self.portal_skins.newspaper_templates
	    theLine = self.getHeadline()
	    print theLine
	    textobject = c.beginText()
            parent = self.aq_inner.aq_parent
	    xorig = x
	    yorig = y
	    if glueX:
	        x = xorig + int(float(x)/2)
            else:
	        x = xorig
            if glueY:
		y += 0
            else:
                y = yorig
	    fontsize = self.getFontsize()
	    textobject.setTextOrigin(x,1185-(y+fontsize))
	    italic = self.getItalic()
	    if italic:
	    	textobject.setFont("Italic", fontsize)
	    else:
	    	textobject.setFont("Times-Roman", fontsize)
	    textobject.textLine(theLine)
	    c.drawText(textobject)
	    offsetX = self.getOffsetX()
            resetY = self.getResetY()
            if offsetX:
	        returnx = xorig
            else:
                returnx = x 
	    size = fontsize / 2
            returny = y + size
	    if not resetY:
		returny	= y + 2*size
	    return (returnx,returny)

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

    def getSkinName(self):
	    """
	    test
            """
	    return "showHeadline"

    def getSnapshot(self,width,height):
            """
	    Snapshot
	    """
	    fontSize = self.getFontsize()
	    fontSize /= 2
	    style = "font-size:"+str(fontSize)+"pt;font-weight:bold;"
	    headline = "<div class='headline' style='"+style+"'>"
	    headline += self.getHeadline()
	    headline += "</div>"
	    width = 0
	    height = 4 * fontSize / 3 
	    return (headline,width,height)

    def getType(self):
	    """
            Test
	    """
	    return "Headline"

    def getHeadlineClass(self):
	    """
	    Test
	    """
	    return self.getHeadlineclass()

    def publish(self,REQUEST):
            """
            Publish
            """
	    skin = self.portal_skins.newspaper_templates
	    showTemplate=skin.publishHeadline
	    return showTemplate()

registerType(Headline, PROJECTNAME)
# end of class Headline

##code-section module-footer #fill in your manual code here
##/code-section module-footer

