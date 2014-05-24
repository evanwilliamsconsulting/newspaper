# -*- coding: utf-8 -*-
#
# File: setuphandlers.py
#
# Copyright (c) 2012 by unknown <unknown>
# Generator: ArchGenXML Version 2.6
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'


import logging
logger = logging.getLogger('Invoicing: setuphandlers')
from Products.Invoicing.config import PROJECTNAME
from Products.Invoicing.config import DEPENDENCIES
import os
from Products.CMFCore.utils import getToolByName
import transaction
##code-section HEAD
##/code-section HEAD

def isNotInvoicingProfile(context):
    return context.readDataFile("Invoicing_marker.txt") is None


from Products.remember.utils import getAdderUtility

def setupMemberTypes(context):
    """Adds our member types to MemberDataContainer.allowed_content_types."""
    if isNotInvoicingProfile(context): return 
    site = context.getSite()
    types_tool = getToolByName(site, 'portal_types')
    act = types_tool.MemberDataContainer.allowed_content_types
    types_tool.MemberDataContainer.manage_changeProperties(allowed_content_types=act+('Contact', ))
    # registers with membrane tool ...
    membrane_tool = getToolByName(site, 'membrane_tool')


def updateRoleMappings(context):
    """after workflow changed update the roles mapping. this is like pressing
    the button 'Update Security Setting' and portal_workflow"""
    if isNotInvoicingProfile(context): return
    wft = getToolByName(context.getSite(), 'portal_workflow')
    wft.updateRoleMappings()


def postInstall(context):
    """Called as at the end of the setup process. """
    # the right place for your custom code
    if isNotInvoicingProfile(context): return 
    site = context.getSite()


##code-section FOOT
##/code-section FOOT
