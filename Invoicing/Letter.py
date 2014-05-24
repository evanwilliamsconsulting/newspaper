# -*- coding: utf-8 -*-
#
# File: Letter.py
#
# Copyright (c) 2012 by unknown <unknown>
# Generator: ArchGenXML Version 2.6
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.Archetypes.Widget import ReferenceWidget
from zope.interface import implements
import interfaces
import locale

from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter

import string 
from cStringIO import StringIO

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Invoicing.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    DateTimeField(
        name='dateOfLetter',
        widget=DateTimeField._properties['widget'](
            label='Date of Letter',
            label_msgid='Invoicing_label_dateOfLetter',
            i18n_domain='Invoicing',
	    show_hm = 0,
        ),
    ),
    ReferenceField(
        name='Company',
	relationship='Company',
        allowed_types=('Company'),
        widget=ReferenceWidget(
            label='Company',
            label_msgid='Invoicing_label_Company',
            i18n_domain='Invoicing',
        ),
    ),
    ReferenceField(
        name='PrimaryContact',
	relationship='Contact',
	allowed_types=('Contact'),
        widget=ReferenceWidget(
            label='Primarycontact',
            label_msgid='Invoicing_label_PrimaryContact',
            i18n_domain='Invoicing',
        ),
    ),
    BooleanField(
        name='sent',
        widget=BooleanField._properties['widget'](
            label='Sent',
            label_msgid='Invoicing_label_sent',
            i18n_domain='Invoicing',
        ),
    ),
    FixedPointField(
        name='offerprice',
        widget=FixedPointField._properties['widget'](
            label='Offer Price',
            label_msgid='Invoicing_label_offerprice',
            i18n_domain='Invoicing',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Letter_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Letter(BaseFolder):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ILetter)

    meta_type = 'Letter'
    _at_rename_after_creation = True

    schema = Letter_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    aliases = {
        '(Default)'	:	PROJECTNAME.lower() + '_view',
	'view'		:	PROJECTNAME.lower() + '_view',
	'edit'		:	'base_edit',
	'base'	        :       'base_view',
	'form'		:	'form_view',
        'letter'	:	'letter_view',
        'test'		:	'test_view',
	}

    # Methods
    def letter(self,REQUEST): 
        """
        Test
        """
        skin = self.portal_skins.invoicing_templates
        showTemplate=skin.showIssue
	output = StringIO()
	c = canvas.Canvas(output,pagesize=letter,bottomup=0)
	x=35
	y=50
	#self.renderMasthead(c,x,y)
        textobject = c.beginText()
        textobject.setTextOrigin(x,y)
	pdfmetrics.registerFont(TTFont('FilosBold','FilosBol.ttf'))
	pdfmetrics.registerFont(TTFont('FilosReg','FilosReg.ttf'))
        textobject.setFont('FilosBold',40)
	textobject.textLine("New Holland Press - INVOICE")
        y+=20	
        textobject.setFont('FilosReg',18)
        textobject.textLine("21 Lincoln Ave. Princeton, NJ 08540")
	y+=50
	parent = self.aq_inner.aq_parent
	company = parent.getCompany()
	address1 = parent.getAddress1()
	city = parent.getCity()
	state = parent.getState()
	postalcode = parent.getPostalCode()
        textobject.setFont('FilosBold',12)
	textobject.setTextOrigin(x,y)
	textobject.textLine("Date:")
	x += 50
	textobject.setTextOrigin(x,y)
	textobject.setFont('FilosReg',12)
	dateOfLetter = self.getDateOfLetter()
	theDate=((str(dateOfLetter)).split(' '))[0]
	textobject.textLine(str(theDate))
	x = 35
	y += 50
	billto = "Bill to:"
        textobject.setFont('FilosBold',12)
	textobject.setTextOrigin(x,y)
	textobject.textLine("Bill to:")
	x += 50
	textobject.setTextOrigin(x,y)
	textobject.setFont('FilosReg',12)
	textobject.textLine(company)
	y+=20
	textobject.setTextOrigin(x,y)
	textobject.textLine(address1)
	y+=20
	textobject.setTextOrigin(x,y)
	textobject.textLine(city)
	x+=50
	textobject.setTextOrigin(x,y)
	textobject.textLine(state)
	x+=50
	textobject.setTextOrigin(x,y)
	textobject.textLine(postalcode)
	x = 35
	y += 50
	textobject.setTextOrigin(x,y)
        textobject.setFont('FilosReg',12)
	textobject.textLine("Line Item")
	x+=150
	textobject.setTextOrigin(x,y)
	textobject.textLine("Qty.")
	x+=50
	textobject.setTextOrigin(x,y)
	textobject.textLine("Rate")
	x+=50
        isDiscount = False
	for aLine in self.listFolderContents():
	    if aLine.getDiscount() > 0:
                isDiscount = True
        if isDiscount:
	    textobject.setTextOrigin(x,y)
            textobject.setFont('FilosReg',12)
	    textobject.textLine("Discount")
	x+=50
	textobject.setTextOrigin(x,y)
        textobject.setFont('FilosBold',12)
	textobject.textLine("Total")
	c.drawText(textobject)
	y+=20
	x=35
	invoiceTotal = 0
	xlocation = 0 
	for aLine in self.listFolderContents():
                textobject = c.beginText()
		theId = aLine.getId()
		textobject.setTextOrigin(x,y)
                textobject.setFont('FilosReg',12)
		textobject.textLine(theId)
		insertions = aLine.getInsertions()
		rate = aLine.getRate()
		extension = float(insertions) * float(rate)
		discount = aLine.getDiscount()
		total = (extension *  (float(50) - float(discount))) / 50
		extension = round(extension,3)
		total = round(total,3)
		x+=150
		textobject.setTextOrigin(x,y)
		textobject.textLine(str(insertions))
		x+=50
		textobject.setTextOrigin(x,y)
		textobject.textLine(str(rate))
		x+=50
		#textobject.setTextOrigin(x,y)
                #textobject.setFont('FilosBold',12)
		#currency = "$" + locale.format('%.2f',extension)
		#textobject.textLine(currency)
		x+=50
                if isDiscount:
		    textobject.setTextOrigin(x,y)
                    textobject.setFont('FilosReg',12)
		    percentage = str(discount)  + "%"
		    textobject.textLine(percentage)
		x+=50
		xlocation=x
		textobject.setTextOrigin(x,y)
                textobject.setFont('FilosBold',12)
		currency = "$" + locale.format('%.2f',total)
		textobject.textLine(currency)
		invoiceTotal += total
		y+=20
		x=35
	        c.drawText(textobject)
		theAds = aLine.listFolderContents()
		for theAd in theAds:
		    someAd = theAd.aq_inner
		    theTitle= someAd.Title()
		    theImage = theAd.getImage()
	            thePress = ImageReader(StringIO(str(theImage.data)))
		    (width,height) = thePress.getSize()
		    aspect = float(height)/float(width)
		    width = 150
		    height = aspect * width 
	            c.drawImage(thePress,100,400,width,height)
	x = 300
	y += 50
        textobject = c.beginText()
	textobject.setTextOrigin(x,y)
	textobject.setFont('FilosBold',12)
	textobject.textLine("Total:")
	x = xlocation
	textobject.setTextOrigin(x,y)
	currency = "$" + locale.format('%.2f',invoiceTotal)
	textobject.textLine(currency)
        c.drawText(textobject)
	c.showPage()
	c.save()
	result = output.getvalue()
	output.close()
	response = REQUEST.RESPONSE
        response.setHeader('Content-type','application/pdf')
	return result 

    def renderMasthead(self,c,x,y):
        textobject = c.beginText()
        textobject.setTextOrigin(x,y)
	pdfmetrics.registerFont(TTFont('FilosBold','FilosBol.ttf'))
	pdfmetrics.registerFont(TTFont('FilosReg','FilosReg.ttf'))
        textobject.setFont('FilosBold',40)
	textobject.textLine("New Holland Press")
	textobject.setTextOrigin(x,y+30)
        textobject.setFont("FilosReg",16)
        textobject.textLine("A Paper Of Discussion")
        textobject.setTextOrigin(x,y-60)
        textobject.textLine("www.newhollandpress.com")
        textobject.setTextOrigin(x+300,y-60)
        textobject.setFont("FilosBold",16)
        textobject.textLine("INVOICE")
	textobject.setTextOrigin(x+320,y+30)
        textobject.setFont("FilosReg",16)
        textobject.textLine("Tuesday, February 7, 2012")
	c.drawText(textobject)
	return (x,y)
    
registerType(Letter, PROJECTNAME)
# end of class Invoice

##code-section module-footer #fill in your manual code here
##/code-section module-footer

