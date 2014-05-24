# -*- coding: utf-8 -*-
#
# File: Clue.py
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

from Products.Crossword.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='Clue',
        widget=StringField._properties['widget'](
            label='Clue',
            label_msgid='Crossword_label_Clue',
            i18n_domain='Crossword',
        ),
    ),
    StringField(
        name='Answer',
        widget=StringField._properties['widget'](
            label='Answer',
            label_msgid='Crossword_label_Answer',
            i18n_domain='Crossword',
        ),
    ),
    IntegerField(
        name='X',
        widget=IntegerField._properties['widget'](
            label='X',
            label_msgid='Crossword_label_X',
            i18n_domain='Crossword',
        ),
    ),
    IntegerField(
        name='Y',
        widget=IntegerField._properties['widget'](
            label='Y',
            label_msgid='Crossword_label_Y',
            i18n_domain='Crossword',
        ),
    ),
    BooleanField(
        name='Orientation',
        widget=BooleanField._properties['widget'](
            label='Orientation',
            label_msgid='Crossword_label_Orientation',
            i18n_domain='Crossword',
        ),
    ),
    IntegerField(
        name='ItemNo',
        widget=IntegerField._properties['widget'](
            label='Itemno',
            label_msgid='Crossword_label_ItemNo',
            i18n_domain='Crossword',
        ),
    ),
    StringField(
        name='AnswerLanguage',
        widget=StringField._properties['widget'](
            label='Answerlanguage',
            label_msgid='Crossword_label_AnswerLanguage',
            i18n_domain='Crossword',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Clue_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Clue(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IClue)

    meta_type = 'Clue'
    _at_rename_after_creation = True

    schema = Clue_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(Clue, PROJECTNAME)
# end of class Clue

##code-section module-footer #fill in your manual code here
##/code-section module-footer

