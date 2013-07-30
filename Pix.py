# -*- coding: utf-8 -*-
#
# File: Pix.py
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
from plone.app.blob.field import BlobField, ImageField
from zope.interface import implements
import interfaces
import string 
from StringIO import StringIO
import reportlab.pdfgen.canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from PIL import *

from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter


from reportlab.lib.colors import yellow,red,black,white
from reportlab.lib.units import inch

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Newspaper.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    IntegerField(
	name='top',
	widget=IntegerField._properties['widget'](
	    label='top',
	    label_msgid='Newspaper_label_top',
	    i18n_domain='Newspaper',
	),
    ),
    IntegerField(
	name='left',
	widget=IntegerField._properties['widget'](
	    label='left',
	    label_msgid='Newspaper_label_left',
	    i18n_domain='Newspaper',
	),
    ),
    IntegerField(
	name='width',
	default=275,
	widget=IntegerField._properties['widget'](
	    label='width',
	    label_msgid='Newspaper_label_width',
	    i18n_domain='Newspaper',
	),
    ),
    IntegerField(
	name='height',
	default=350,
	widget=IntegerField._properties['widget'](
	    label='height',
	    label_msgid='Newspaper_label_height',
	    i18n_domain='Newspaper',
	),
    ),
    StringField(
        name='caption',
        widget=StringField._properties['widget'](
            label='Caption',
            label_msgid='Newspaper_label_caption',
            i18n_domain='Newspaper',
        ),
    ),
    StringField(
        name='credit',
        widget=StringField._properties['widget'](
            label='Credit',
            label_msgid='Newspaper_label_caption',
            i18n_domain='Newspaper',
        ),
    ),
    StringField(
        name='pixclass',
	default='pixclass',
        widget=StringField._properties['widget'](
            label='Pix class',
            label_msgid='Newspaper_label_pixclass',
            i18n_domain='Newspaper',
        ),
    ),
    ImageField(
        name='picture',
        widget=ImageField._properties['widget'](
            label='Pix',
            label_msgid='Newspaper_label_picture',
            i18n_domain='Newspaper',
        ),
        storage=AttributeStorage(),
    ),
    ImageField(
	name='bylineImage',
	widget=ImageField._properties['widget'](
	    label='Pix',
	    label_msgid='Newspaper_label_bylineImage',
	    i18n_domain='Newspaper',
	),
	storage=AttributeStorage(),
    ),
    BooleanField(
	name='useBylineImage',
        widget=BooleanField._properties['widget'](
	    label='useBylineImage',
	    label_msgid='Newspaper_label_useBylineImage',
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
	name='resetX',
        widget=BooleanField._properties['widget'](
	    label='resetX',
	    label_msgid='Newspaper_label_resetX',
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
    BooleanField(
	name='topMargin',
	widget=BooleanField._properties['widget'](
		label='topMargin',
		label_msgid='Newspaper_label_topMargin',
		i18n_domain='Newspaper',
	),
    ),
    IntegerField(
	name='offsetXWidth',
	default=0,
	widget=IntegerField._properties['widget'](
            label='X Column Offset',
	    label_msgid='Newspaper_label_offsetXWidth',
	    i18n_domain='Newspaper',
	),
    ),
    IntegerField(
	name='offsetYHeight',
	default=0,
	widget=IntegerField._properties['widget'](
            label='Y Column Offset',
	    label_msgid='Newspaper_label_offsetYHeight',
	    i18n_domain='Newspaper',
	),
    ),
    IntegerField(
	name='offsetYCaption',
	default=0,
	widget=IntegerField._properties['widget'](
            label='Y Caption Offset',
	    label_msgid='Newspaper_label_offsetYCaption',
	    i18n_domain='Newspaper',
	),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Pix_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Pix(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IPix)

    meta_type = 'Pix'
    _at_rename_after_creation = True

    schema = Pix_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def returnPix(self):
	    """
	    Test
	    """
	    theImage = self.getId()
	    theDiv = "<div id='"
            theDiv += theImage
	    theClass = self.getPixclass()
            theDiv += "' class='"
	    theDiv += theClass
	    theDiv += "' style='margin:10px;'"
            theDiv += ">"
	    theTag = "<img width='"+str(self.getWidth())+"' height='"+str(self.getHeight())+"' src='"+self.absolute_url()+"/picture'/>"
	    theDiv += theTag
	    theDiv += "</div>"
	    return theDiv

    def web(self):
	    """
	    Test
	    """
	    theImage = self.getId()
	    theDiv = "<div id='"
            theDiv += theImage
	    theClass = self.getPixclass()
            theDiv += "' class='"
	    theDiv += theClass
	    theDiv += "' style='margin:10px;'"
            theDiv += ">"
	    theDiv += self.pixHTML()
	    theDiv += "</div>"
	    return theDiv
        

    def pixHTML(self):
	    """
	    Test
	    """
	    theImage = self.getId()
	    theDiv = "<div id='"
            theDiv += theImage
            theDiv += "' class='pix' style='margin-left:30px;position:absolute;top:"
	    theDiv += str(self.getTop())
	    theDiv += "px;left:0"
	    theDiv += "px;'"
            #theDiv += "style='border-color:blue;border-width:2px;border-style:solid;top:"
            left = self.getLeft()
	    top = self.getTop()
            width = self.getWidth()
            height = self.getHeight()
            theDiv += ">"
	    theTag = "<img width='"+str(self.getWidth())+"' height='"+str(self.getHeight())+"' src='"+self.absolute_url()+"/picture'/>"
	    theDiv += theTag
	    theDiv += "</div>"
	    left += width
	    return theDiv

    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber):
	    """
	    Test
	    """
	    yorig = y
            height = self.getHeight()
	    y = 1200 - height - y
	
	    y -= 10
	    if self.getTopMargin():
		y -= 40
            print 'here'
            print self.Title()
    	    #skin = self.portal_skins.newspaper_templates
	    #containercontainer = skin[self.Title()]
	    #result=containercontainer.continuePDF(c,x,y,REQUEST,parent,pagenumber)
	    #return (result[0],result[1])
	    glueX = self.getGlueX()
	    glueY = self.getGlueY()
	    xorig = x
	    offsetYHeight = self.getOffsetYHeight()
	    offsetXWidth = self.getOffsetXWidth()
	    x += offsetXWidth
	    y -= offsetYHeight
	    theImage=self.getPicture()
	    theBlob = theImage.getBlob()
	    theString = theBlob.open().read()
	    theStringIO=StringIO(str(theString))
	    #theStringIO=StringIO(theImage.data)
	    #data = theImage.data
	    #leng = len(data)
	    im = Image.open(theStringIO)
	    im2 = im.transpose(1)
            theStringIO2=StringIO(str(im2.tostring()))		
            parent = self.aq_inner.aq_parent
            width = self.getWidth()
            height = self.getHeight()
	    if self.getTopMargin():
		y+=25
	    #c.drawImage(ImageReader(im2),x,y,width,height,anchor='ne')
	    c.drawImage(ImageReader(StringIO(theString)),x,y,width,height)
	    caption = self.getCaption()
	    offsetYCaption = self.getOffsetYCaption()
	    if caption is not None:
	        textobject = c.beginText()
		textobject.setFillColorRGB(0,0,0)
		h = self.getHeight()
		if h is None:
			h = 400
		captionY = y - 30 + offsetYCaption
	        textobject.setTextOrigin(x,captionY)
	        fontsize = 12
	        textobject.setFont("Times-Roman", fontsize)
	        textobject.textLine(caption)
	        c.drawText(textobject)
	    credit = self.getCredit()
	    if credit is not None:
	        textobject = c.beginText()
		h = self.getHeight()
		w = self.getWidth()
		w = w - 120
		if h is None:
			h = 400
		creditY = y - 15 + offsetYCaption
	        textobject.setTextOrigin(x+w-100,creditY)
	        fontsize = 11
	        textobject.setFont("Times-Roman", fontsize)
	        textobject.textLine(credit)
	        c.drawText(textobject)
		useBylineImage=self.getUseBylineImage()
		if useBylineImage:
	            theImage=self.getBylineImage()
	            theBlob = theImage.getBlob()
	            theString = theBlob.open().read()
	            theStringIO=StringIO(str(theString))
	    	    im = Image.open(theStringIO)
	            im2 = im.transpose(1)
                    theStringIO2=StringIO(str(im2.tostring()))		
                    parent = self.aq_inner.aq_parent
                    width = 35 
                    height = 35
	            c.drawImage(ImageReader(StringIO(theString)),x+w+10,creditY-20,width,height)
	    resetX = self.getResetX()
	    resetY = self.getResetY()
	    if resetY:
	    	returny = yorig
	    else:
		returny = y + h - 100
	    offsetX = self.getOffsetX()
            if offsetX:
	        returnx = x + int(float(self.getWidth())*1.1) 
            else:
                returnx = xorig 
	    return (returnx,returny)

    def getSkinName(self):
	   """
           TEST
           """
           return "showPix"

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
	    theImage=self.getPicture()
	    theImageData = StringIO()
	    theImageUsage = theImage.file._read_data(theImageData)
	    theImageReader = ImageReader(theImageUsage)
	    (width,height) = theImageReader.getSize()
            parent = self.aq_inner.aq_parent
            width = self.getWidth()
            height = self.getHeight()
	    if self.getTopMargin():
		y+=15
	    c.drawImage(theImageReader,x,y,width,height,anchor='ne')
	    caption = self.getCaption()
	    credit = self.getCredit()
	    pdfmetrics.registerFont(TTFont('FilosBold','FilosBol.ttf'))
	    pdfmetrics.registerFont(TTFont('FilosReg','FilosReg.ttf'))
	    if caption is not None:
	        textobject = c.beginText()
		h = self.getHeight()
		if h is None:
			h = 400
	        textobject.setTextOrigin(x,y+h+30)
	        fontsize = 14
	        textobject.setFont("FilosReg", fontsize)
	        textobject.textLine(caption)
	        c.drawText(textobject)
            if credit is not None:
                textobject = c.beginText()
                h = self.getHeight()
                if h is None:
                    h = 400
                w = self.getWidth()
                w = w - 100
                textobject.setTextOrigin(x-w,y+h+15)
                fontsize = 11
                textobject.setFont("FilosReg",fontsize)
                textobject.textLine(credit)
                c.drawText(textobject)
	    c.showPage()
	    c.save()
	    result = output.getvalue()
	    output.close()
	    response = REQUEST.RESPONSE
            response.setHeader('Content-type','application/pdf')
	    return result 

    def publish(self,REQUEST):
            """
            Publish
            """
	    skin = self.portal_skins.newspaper_templates
	    showTemplate=skin.publishPix
	    return showTemplate()

    def getSnapshot(self,width,height):
	    """
	    Snapshot
	    """
	    retcode = "<div id='pix'>"
	    actualWidth = 1.2 * width
	    actualHeight = 1.2 * height
 	    tag = self.getField('picture').tag(self,height=actualHeight,width=actualWidth)
	    caption = self.getCaption()
	    retcode += tag
	    retcode += "<div style='color:B6546D;'>"
	    retcode += caption
	    retcode += "</div>"	
	    retcode += "</div>"	
	    return (retcode,width,height)

    def getType(self):
	    """
	    Test
   	    """
	    return "Pix"

registerType(Pix, PROJECTNAME)
# end of class Image

##code-section module-footer #fill in your manual code here
##/code-section module-footer

