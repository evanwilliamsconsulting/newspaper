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
import interfaces

from Products.Newspaper.BookTemplate import BookTemplate

from Products.Newspaper.config import *
from Products.Newspaper import Form

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
    FixedPointField(
        name='priceOfCopy',
        widget=FixedPointField._properties['widget'](
            label='Priceofcopy',
            label_msgid='Newspaper_label_priceOfCopy',
            i18n_domain='Newspaper',
        ),
    ),
    TextField(
        name='Synopsis',
        widget=TextField._properties['widget'](
            label='Synopsis',
            label_msgid='Newspaper_label_synopsis',
            i18n_domain='Newspaper',
        ),
    ),
    ImageField(
        name='CoverImage',
        widget=ImageField._properties['widget'](
            label='CoverImage',
            label_msgid='Newspaper_label_CoverImage',
            i18n_domain='Newspaper',
        ),
        storage=AnnotationStorage(),
    ),
    ImageField(
        name='BackImage',
        widget=ImageField._properties['widget'](
            label='BackImage',
            label_msgid='Newspaper_label_BackImage',
            i18n_domain='Newspaper',
        ),
        storage=AnnotationStorage(),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Book_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Book(OrderedBaseFolder):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IBook)

    meta_type = 'Book'
    _at_rename_after_creation = True

    schema = Book_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    aliases = {
        '(Default)'	:	PROJECTNAME.lower() + '_view',
	'view'		:	PROJECTNAME.lower() + '_view',
	'edit'		:	'base_edit',
	'base'	        :       'base_view',
	'pdf'		:	'pdf_view',
	'form'		:	'form_view',
	}

    # Methods
    def pdfshow(self,REQUEST): 
        """
        pdf
        """
	theTemplate = BookTemplate('book','/opt/newhol/press/products/Newspaper/skins/newspaper_templates/book.pd')
	theTemplate.setWidth(8.5)
	theTemplate.setHeight(11)
	parent = self.aq_inner
        return theTemplate.pt_render(REQUEST,parent)

registerType(Book, PROJECTNAME)
# end of class Book

##code-section module-footer #fill in your manual code here
##/code-section module-footer

