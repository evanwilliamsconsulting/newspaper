# -*- coding: utf-8 -*-
#
# File: Correspondant.py
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
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate

from Products.Five.browser import BrowserView


from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics

from reportlab.pdfbase.ttfonts import TTFont

import json
##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='library',
        widget=StringField._properties['widget'](
            label='Library',
            label_msgid='Newspaper_label_library',
            i18n_domain='Newspaper',
        ),
    ),
    StringField(
        name='description',
        widget=StringField._properties['widget'](
            label='Description',
            label_msgid='Newspaper_label_description',
            i18n_domain='Newspaper',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Library_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema
#class M_Correspondant(NewsFolder.__class__): pass
class LibraryJSON(BrowserView):
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
   	self.request.response.setHeader("Content-encoding","utf8")
	json_item = {}
	title = self.context.getId()
	json_item['Library']=title
	json_item['Description']=self.context.getDescription()
	#self.context.orderObjects(key="dateOfPublication")
	allIssues = self.context.listFolderContents()
	json_issue = {}
	for issue in allIssues:
		issueId = issue.getId()
		issueDate = str(issue.getDateOfPublication())
		issueD = issue.getDateOfPublication()
		year = issueD.year()
		month = issueD.month()
		day = issueD.day()
		theDate = "%s" % ( issueD )
		json_issue[theDate]=issueId
	json_item['Issues']=json_issue
	pretty = json.dumps(json_item)    
	self.request.response.setBody(pretty)

class LibraryView(BrowserView):
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

class Library(OrderedBaseFolder,ExtensibleMetadata,BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ILibrary)

    meta_type = 'Library'
    _at_rename_after_creation = True

    schema = Library_schema

    def firstissue(self):
	"""
	show the issue view of the page one broadsheet
	"""
	for issue in self.listFolderContents(contentFilter={"portal_type":"Issue"}):
	    return issue 
    ##code-section class-header #fill in your manual code here
    ##/code-section class-header
registerType(Library, PROJECTNAME)
# end of class Correspondant

##code-section module-footer #fill in your manual code here
##/code-section module-footer

