# -*- coding: utf-8 -*-
#
# File: Section.py
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

Section_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Section(OrderedBaseFolder,  BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ISection)

    meta_type = 'Section'
    _at_rename_after_creation = True

    schema = Section_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

##code-section module-footer #fill in your manual code here
##/code-section module-footer
