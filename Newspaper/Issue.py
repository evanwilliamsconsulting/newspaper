# -*- coding: utf-8 -*-
#
# File: Issue.py
#
# Copyright (c) 2011 by unknown <unknown>
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
from Products.CMFCore import permissions
from zope.interface import implements
from zope.component import getMultiAdapter
import interfaces

from Products.Newspaper.PDFPageTemplate import PDFPageTemplate

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Newspaper.config import *
from Products.Newspaper import Form

from Products.Five.browser import BrowserView

import json

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    DateTimeField(
        name='dateOfPublication',
        widget=DateTimeField._properties['widget'](
            label='Dateofpublication',
            label_msgid='Newspaper_label_dateOfPublication',
            i18n_domain='Newspaper',
        ),
    ),
    BooleanField(
	name='toggleDivTagsOn',
        widget=BooleanField._properties['widget'](
	    label='Display Div Tags',
	    label_msgid='Newspaper_label_toggleDivTagsOn',
	    i18n_domain='Newspaper',
	),
    ),
    FixedPointField(
        name='priceOfCopy',
        widget=FixedPointField._properties['widget'](
            label='Priceofcopy',
            label_msgid='Newspaper_label_priceOfCopy',
            i18n_domain='Newspaper',
        ),
    ),
    StringField(
        name='tagLine',
        widget=StringField._properties['widget'](
            label='Tagline',
            label_msgid='Newspaper_label_tagLine',
            i18n_domain='Newspaper',
        ),
    ),
    ImageField(
        name='QRImage',
        widget=ImageField._properties['widget'](
            label='Qrimage',
            label_msgid='Newspaper_label_QRImage',
            i18n_domain='Newspaper',
        ),
        storage=AnnotationStorage(),
    ),
    StringField(
        name='headingTheme',
        widget=StringField._properties['widget'](
            label='Headingtheme',
            label_msgid='Newspaper_label_headingTheme',
            i18n_domain='Newspaper',
        ),
    ),
    StringField(
        name='secondTheme',
        widget=StringField._properties['widget'](
            label='Secondtheme',
            label_msgid='Newspaper_label_secondTheme',
            i18n_domain='Newspaper',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Issue_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema
class IssueJSON(BrowserView):
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
	json_item['Issue']=title
	self.context.orderObjects(key="dateOfPublication")
	pages = self.context.listFolderContents()
	json_pages = {}
	for page in pages:
		pageId = page.getId()
		pageNo = page.getPageNo()
		json_pages[pageId]=pageNo
	json_item['Pages']=json_pages
	pretty = json.dumps(json_item)    
	return pretty 

class IssueView(BrowserView):
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
    def __call__(self):
	"""
	TEST
	"""


class Issue(BaseFolder,BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IIssue)

    meta_type = 'Issue'
    _at_rename_after_creation = True

    schema = Issue_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    aliases = {
        '(Default)'	:	'base_view',
	'view'		:	'base_view',
	'edit'		:	'base_edit',
	'base'	        :       'base_view',
	'pdf'		:	'pdf_view',
	'form'		:	'form_view',
	}

    # Methods
    def listBroadsheets(self):
	    """
	    hey!
	    """
	    items = self.listFolderContents(contentFilter={"portal_type":"Broadsheet"})
	    return items

    def pageNumbers(self):
	    """
	    use the pageNumber method in each contained Broadsheet to return
	    a list of links to pageNumbers.
	    """
	    pages = self.listFolderContents(contentFilter={"portal_type":"Broadsheet"})
	    linkPages = []
	    for page in pages:
		linkPages.append(page.pageNumber())

	    return linkPages

    def firstpage(self):
	"""
	show the issue view of the page one broadsheet
	"""
	for broadsheet in self.listFolderContents(contentFilter={"portal_type":"Broadsheet"}):
	    return broadsheet
		
    def pages(self):
	    """
	    links
	    """
	    items = self.listFolderContents(contentFilter={"portal_type":"Broadsheet"})
	    pages = []
	    for item in items:
		page = {}
		page['name'] = item.getId()
	        page['link'] = item.absolute_url()
		pages.append(page)
	    return pages

    def returnInput(self):
	    """
	    Test
	    """
	    stringValue = ""
	    items = self.listFolderContents(contentFilter={"portal_type":"Broadsheet"})
	    return items[0]

    def listItems(self):
	"""
	hey
	"""
	items = self.listFolderContents(contentFilter={"portal_type":"Broadsheet"})
	return items

    def show(self,REQUEST):
	"""
	test 
	"""
	skin = self.portal_skins.newspaper_templates
	theIssue = skin.showIssue
	parent = self.aq_inner
        return theIssue(parent)

    def nhp_template(self): 
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    return skin.nhp_template

    def web(self): 
        """
        Test
        """
	pagetwo = self.pagetwo
	pagetwo.web()
    
    security.declareProtected(permissions.View,'view')
    def view(self,REQUEST):
	"""
	Test
	"""
        skin = self.portal_skins.newspaper_templates
        showTemplate=skin.showIssue
	parent = self.aq_inner.aq_parent
	for broadsheet in parent.listFolderContents(contentFilter={"portal_type":"Issue"}):
        	return showTemplate.pt_render(REQUEST,broadsheet)

    security.declareProtected(permissions.View,'the_issues')
    def the_issues(self):
        """
        Here is a list of the issues.
        """
	parent=self.aq_inner.aq_parent
	return parent.listFolderContents(contentFilter={"portal_type":"Issue"})


    security.declareProtected(permissions.View,'the_stories')
    def the_stories(self):
	"""
	We will return the Ads separately
	"""
	return self.listFolderContents(contentFilter={"portal_type":"Container"})
	
    def just(self): 
        """
        Test
        """
        skin = self.portal_skins.newspaper_templates
        showTemplate=skin.showIssue
        return showTemplate()
    
    def pdfshow(self,REQUEST): 
        """
        pdf
        """
	theTemplate = PDFPageTemplate('issue','var/issue.pd')
	parent = self.aq_inner
        return theTemplate.pt_render(REQUEST,parent)
    
    def webfetch(self,REQUEST): 
        """
        web 
        """
	theTemplate = PDFPageTemplate('issue','products/Newspaper/issue.pd')
	parent = self.aq_inner
	return theTemplate.web(REQUEST,parent)

    def webshow2(self,REQUEST): 
        """
        web 
        """
        someTemplate = "<div tal:define='contents python:webfetch(REQUEST)'><div tal:replace='structure contents' style='position:absolute;clear:both;'>SomeTemplate</div></div>"
        return someTemplate
    
    def hello(self, c):
	c.translate(inch,inch)
	c.setFont("Helvetica", 14)
	c.setStrokeColorRGB(0.2,0.5,0.3)
	c.setFillColorRGB(1,0,1)
	c.line(0,0,0,1.7*inch)
	c.line(0,0,1*inch,0)
	c.rect(0.2*inch,0.2*inch,1*inch,1.5*inch, fill=1)
	c.rotate(90)
	c.setFillColorRGB(0,0,0.77)
	c.drawString(0.3*inch, -inch, "Hello World")

    def pdfview(self):
        c = canvas.Canvas('/tmp/hello.pdf')
        self.hello(c)
        c.showPage()
        c.save()
        return "saved"

    def form(self):
	return wrap_form(MyForm)

    def getTitle(self):
	return self.Title

    def breadcrumbs(self,REQUEST):
        # We do this here do maintain the rule that we must be wrapped
        container = self.aq_inner

        base = tuple(getMultiAdapter((container, REQUEST),
                                     name='absolute_url').breadcrumbs())

        return base

registerType(Issue, PROJECTNAME)
# end of class Issue

##code-section module-footer #fill in your manual code here
##/code-section module-footer

