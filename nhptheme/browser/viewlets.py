from datetime import date
from zope.component import getMultiAdapter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

from zope.interface import implements, alsoProvides
from zope.component import getMultiAdapter
from zope.viewlet.interfaces import IViewlet
from zope.deprecation.deprecation import deprecate

from Products.nhptheme.portlets import topimage

from zope.component import adapts

from zope.interface import Interface
from zope.publisher.interfaces.browser import IBrowserView
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.nhptheme.browser.interfaces import INHPTheme


from plone.app.layout.globals.interfaces import IViewView 

from AccessControl import getSecurityManager
from Acquisition import aq_base, aq_inner
from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.portlets.manager import ColumnPortletManagerRenderer
from Products.CMFCore.utils import getToolByName
from cgi import escape
from urllib import quote_plus


from zope.interface import implements, alsoProvides
from zope.component import getMultiAdapter
from zope.viewlet.interfaces import IViewlet
from zope.deprecation.deprecation import deprecate

from plone.app.layout.globals.interfaces import IViewView 

from AccessControl import getSecurityManager
from Acquisition import aq_base, aq_inner
from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from cgi import escape
from urllib import quote_plus

import viewlets as thistheme
from plone.app.layout.viewlets import common as base


class TopPortletRenderer(ColumnPortletManagerRenderer):
    """
    A renderer for the content-well portlets
    """
    adapts(Interface, IDefaultBrowserLayer, IBrowserView, INHPTheme)
    template = ViewPageTemplateFile('templates/renderer.pt')

def render_viewlet(factory,context,request):
	context = aq_inner(context)
	viewlet = factory(context, request, None, None).__of__(context)
	viewlet.update()
	return viewlet.render()

class NhpmastheadViewlet(ViewletBase):

    def theDate(self):
	today = date.today()
	return today.strftime("%A %d %B %Y")

    def update(self):
    	base.ViewletBase.update(self)
    	self.subviewlets = {}

    def renderViewlet(self,viewlet_class):
    	return render_viewlet(viewlet_class,self.context,self.request)

    def render(self):
        self.subviewlets['masthead'] = self.renderViewlet(thistheme.MastheadViewlet)
        self.subviewlets['windmill'] = self.renderViewlet(thistheme.WindmillViewlet)
        self.subviewlets['volumenum'] = self.renderViewlet(thistheme.VolumenumViewlet)
        self.subviewlets['motto'] = self.renderViewlet(thistheme.MottoViewlet)
        self.subviewlets['price'] = self.renderViewlet(thistheme.PriceViewlet)
        self.subviewlets['publicationdate'] = self.renderViewlet(thistheme.PublicationDateViewlet)
        self.bigdeal = ViewPageTemplateFile('../skins/nhptheme_templates/nhpmasthead.pt')
	return self.bigdeal(self)

class MastheadViewlet(ViewletBase):
    render = ViewPageTemplateFile('../skins/nhptheme_templates/masthead.pt')

    def update(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                            name=u'plone_portal_state')

        self.navigation_root_url = portal_state.navigation_root_url()


class PriceViewlet(ViewletBase):
    render = ViewPageTemplateFile('../skins/nhptheme_templates/price.pt')

class VolumenumViewlet(ViewletBase):
    render = ViewPageTemplateFile('../skins/nhptheme_templates/volumenum.pt')

class PublicationDateViewlet(ViewletBase):
    render = ViewPageTemplateFile('../skins/nhptheme_templates/publicationdate.pt')

class MottoViewlet(ViewletBase):
    render = ViewPageTemplateFile('../skins/nhptheme_templates/motto.pt')

class WindmillViewlet(ViewletBase):
    render = ViewPageTemplateFile('../skins/nhptheme_templates/windmill.pt')


class TopPortletsViewlet(ViewletBase):
    render = ViewPageTemplateFile('templates/top_portlets.pt')
        
    def update(self):
        """
        Define everything we want to call in the template
        """
        context_state = getMultiAdapter((self.context, self.request), name=u'plone_context_state')
        self.manageUrl =  '%s/@@manage-topportlets' % context_state.view_url()
        
        ## This is the way it's done in plone.app.portlets.manager, so we'll do the same
        mt = getToolByName(self.context, 'portal_membership')
        self.canManagePortlets = mt.checkPermission('Portlets: Manage portlets', self.context)


class PathBarViewlet(ViewletBase):
    index = ViewPageTemplateFile('path_bar.pt')

    def update(self):
        super(PathBarViewlet, self).update()

        self.is_rtl = self.portal_state.is_rtl()

        breadcrumbs_view = getMultiAdapter((self.context, self.request),
                                           name='breadcrumbs_view')
        self.breadcrumbs = breadcrumbs_view.breadcrumbs()

class PageNumbersViewlet(ViewletBase):
    index = ViewPageTemplateFile('pagenumbers.pt')
    
    def update(self):
        super(PageNumbersViewlet, self).update()

	pagenumbers_view = getMultiAdapter((self.context, self.request),
					   name='pagenumbers_view')

        self.pages = pagenumbers_view.pages() 


class SchoolsGlobalSections(ViewletBase):

    def getViewletByName(self, name):
        views = registration.getViews(IBrowserRequest)
        found = None

        # Get active layers on the currest request object
        wanted_layers = list(self.request.__provides__.__iro__)
                
        # List of all viewlet registration with the name
        # Note: several registrations possible due to layers
        possible = []
        for v in views:
            if v.provided == IViewlet:
                # Note that we might have conflicting BrowserView with the same name,
                # thus we need to check for provided
                if v.name == name:
                    possible.append(v)

        wanted_layers = wanted_layers[:]
        for layer in wanted_layers:
            for viewlet_registration in possible:
                theme_layer = viewlet_registration.required[1]
                if theme_layer == layer:
                    return viewlet_registration
        return None

    def setupViewletByName(self, name):
        context = aq_inner(self.context)
        request = self.request

        # Perform viewlet regisration look-up
        # from adapters registry
        reg = self.getViewletByName(name)
        if reg == None:
            return None

        # factory method is responsible for creating the viewlet instance
        factory = reg.factory

        # Create viewlet and put it to the acquisition chain
        # Viewlet need initialization parameters: context, request, view
        
        from Shared.DC.Scripts.Bindings import UnauthorizedBinding

        if isinstance(context, UnauthorizedBinding):
            # Viewlets cannot be constructed on Unauthorized error pages, so we try to reconstruct them using the site root
            context = context.portal_url.getPortalObject()
        
        viewlet = factory(context, request, self, None)

        if hasattr(viewlet, "__of__"):
            # Plone 3 viewlets with implicit acquisiton
            viewlet = viewlet.__of__(context)

        return viewlet

    def render(self):
        viewlet = self.setupViewletByName("plone.global_sections")
        viewlet.update()
        result = viewlet.render()
        return result
