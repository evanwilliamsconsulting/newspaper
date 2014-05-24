#
__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'


import logging
logger = logging.getLogger('nhptheme')
logger.debug('Installing Product')

import os
import os.path
from Globals import package_home
import Products.CMFCore.interfaces
from Products.Archetypes import listTypes
from Products.Archetypes.atapi import *
from Products.Archetypes.utils import capitalize
from Products.CMFCore import DirectoryView
from Products.CMFCore import permissions as cmfpermissions
from Products.CMFCore import utils as cmfutils
from Products.CMFPlone.utils import ToolInit
from config import *

DirectoryView.registerDirectory('skins', product_globals)

from AccessControl.SecurityInfo import ModuleSecurityInfo
from Products.CMFCore.permissions import setDefaultRoles

##code-section custom-init-head #fill in your manual code here
##/code-section custom-init-head

from Products.CMFCore.utils import getToolByName

def initialize(context):
    """initialize product (called by zope)"""
    ##code-section custom-init-top #fill in your manual code here
    ##/code-section custom-init-top

    # imports packages and types for registration

    ##code-section custom-init-bottom #fill in your manual code here
    ##/code-section custom-init-bottom
