"""

    Zope 3 schema vocabulary factory for making multiple choices between installed content types of Plone site.

    http://mfabrik.com

"""

__license__ = "GPL 2"
__copyright__ = "2010 mFabrik Research Oy"
__author__ = "Mikko Ohtamaa <mikko@mfabrik.com>"
__docformat__ = "epytext"

from Acquisition import aq_inner
from zope.app.component.hooks import getSite
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from Products.CMFCore.utils import getToolByName

def make_terms(items):
    """ Create zope.schema terms for vocab from tuples,

    @return: Generator of SimpleTerm objects
    """
    terms = [ SimpleTerm(value=pair[0], token=pair[0], title=pair[1]) for pair in items ]
    return terms

def friendly_types(site):
    """ List user selectable content types.

    Note that there exist a method in IPortalState utility view for this, but we cannot
    use it, because vocabulary factory must be available in contexts where there is
    no HTTP request (e.g. installing add-on product).

    This code is copy-pasted from https://svn.plone.org/svn/plone/plone.app.layout/trunk/plone/app/layout/globals/portal.py

    @return: Generator for (id, type_info title) tuples
    """
    context = aq_inner(site)
    site_properties = getToolByName(context, "portal_properties").site_properties
    not_searched = site_properties.getProperty('types_not_searched', [])

    portal_types = getToolByName(context, "portal_types")
    types = portal_types.listContentTypes()

    # Get list of content type ids which are not filtered out
    prepared_types = [t for t in types if t not in not_searched]

    # Return (id, title) pairs
    return [ (id, portal_types[id].title) for id in prepared_types ]

def content_types_vocabulary(context):
    """
    A vocabulary factory for making a choice of a portal type.

    @param context: Assume Plone site.

    @return: SimpleVocabulary containing (portal type id, portal type title) pairs.
    """

    # This special case must be handled by plone.app.registry quick installing registry.xml
    # which refers to zope.schema refering to this vocabulary
    # site information is *not* available

    try:
        import plone.registry.record
        import plone.registry.recordsproxy
        if isinstance(context, plone.registry.record.Record) or isinstance(context, plone.registry.recordsproxy.RecordsProxy):
            context = getSite()
    except ImportError:
        pass

    items = friendly_types(context)

    return SimpleVocabulary(make_terms(items))
