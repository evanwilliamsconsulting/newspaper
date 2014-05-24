# -*- coding: utf-8 -*-
#
# File: Contributor.py
#
# Copyright (c) 2012 by unknown <unknown>
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

from Products.CreditsBox.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='first',
        widget=StringField._properties['widget'](
            label='First',
            label_msgid='CreditsBox_label_first',
            i18n_domain='CreditsBox',
        ),
    ),
    StringField(
        name='last',
        widget=StringField._properties['widget'](
            label='Last',
            label_msgid='CreditsBox_label_last',
            i18n_domain='CreditsBox',
        ),
    ),
    StringField(
        name='email',
        widget=StringField._properties['widget'](
            label='Email',
            label_msgid='CreditsBox_label_email',
            i18n_domain='CreditsBox',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Contributor_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Contributor(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IContributor)

    meta_type = 'Contributor'
    _at_rename_after_creation = True

    schema = Contributor_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def getWidth(self):
	    """
	    Test
	    """
	    return 280

    def getHeight(self):
	    """
	    Test
	    """
	    return 320

    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top):
	    """
	    Test
	    """
            print self.Title()
	    verbage = self.Title()
	    first= self.getFirst()
	    last = self.getLast()
	    email = self.getEmail()
            textobject = c.beginText()
            textobject.setTextOrigin(x,y)
            textobject.setFont("Times-Roman",9)
	    team = verbage + ": " + email
            textobject.textLine(team)
	    c.drawText(textobject)
	    y+=10
	    return (x,y)

registerType(Contributor, PROJECTNAME)
# end of class Contributor

##code-section module-footer #fill in your manual code here
##/code-section module-footer

