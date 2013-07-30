# -*- coding: utf-8 -*-
#
# File: Widget.py
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
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate
from Products.CMFCore.utils import getToolByName

from Products.Five.browser import BrowserView

from interfaces import IWidget
import interfaces

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    IntegerField(
	name='left',
	widget=IntegerField._properties['widget'](
	    label='left',
	    label_msgid='Newspaper_label_left',
	    i18n_domain='Newspaper',
	),
    ),
    IntegerField(
	name='top',
	widget=IntegerField._properties['widget'](
	    label='top',
	    label_msgid='Newspaper_label_top',
	    i18n_domain='Newspaper',
	),
    ),
    StringField(
        name='divid',
        widget=StringField._properties['widget'](
            label='Divid',
            label_msgid='Newspaper_label_divid',
            i18n_domain='Newspaper',
        ),
    ),
    StringField(
        name='class',
        widget=StringField._properties['widget'](
            label='Class',
            label_msgid='Newspaper_label_class',
            i18n_domain='Newspaper',
        ),
    ),
    TextField(
        name='markup',
        widget=TextAreaWidget(
            label='Markup',
            label_msgid='Newspaper_label_markup',
            i18n_domain='Newspaper',
        ),
    ),
    ReferenceField(
        name='containers',
        widget=ReferenceBrowserWidget(
            label='Containers',
            label_msgid='Newspaper_label_containers',
            i18n_domain='Newspaper',
        ),
        allowed_types=('Container','YouCanBox','CreditsBox','Puzzle',),
        multiValued=1,
        relationship='containerLocation',
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Widget_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class WidgetView(BrowserView):
    """ A View of the Widget """

class Widget(OrderedBaseFolder,  BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IWidget)

    meta_type = 'Widget'
    _at_rename_after_creation = True

    schema = Widget_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    security.declarePublic('ttbird')
    def ttbird(self):
	    """
	    TTBird
	    """
	    top = self.getTop()
	    return top + 300

    security.declarePublic('llbird')
    def llbird(self):
	    """
	    llbird
	    """
	    left = self.getLeft()
	    return left + 100

    security.declarePublic('show')
    def show(self): 
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    showTemplate=skin.showWidget
	    return showTemplate()

    security.declarePublic('listContainers')
    def listContainers(self):
	    """
	    """
	    return self.returnInput()

    def returnInput(self):
	    """
	    Test
	    """
	    #stringValue = ""
	    #$items = self.listFolderContents(contentFilter={"portal_type":"Container"})
	    #items=self.contentItems()
	    items=self.getContainers()
	    return items

    def WidgetView(self):
	   """
	   Test
	   """
	   skin = self.portal_skins.newspaper_templates
	   widgetTemplate = skin.showWidget
	   return widgetTemplate()

registerType(Widget, PROJECTNAME)
# end of class Widget

##code-section module-footer #fill in your manual code here
##/code-section module-footer

