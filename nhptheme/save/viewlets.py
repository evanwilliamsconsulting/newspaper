from plone.app.portlets.browser.manage import ManageContextualPortletsViewlet as base
from zope.component import getMultiAdapter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.utils import getToolByName


from zope.component import adapts
from zope.interface import Interface
from zope.publisher.interfaces.browser import IBrowserView
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.app.portlets.manager import ColumnPortletManagerRenderer
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from quintagroup.theme.schools.browser.interfaces import IThemeSchoolsPortlets

from Acquisition import aq_inner
from plone.app.customerize import registration
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.viewlet.interfaces import IViewlet



class TopPortletRenderer(ColumnPortletManagerRenderer):
    """
    A renderer for the content-well portlets
    """
    adapts(Interface, IDefaultBrowserLayer, IBrowserView, IThemeSchoolsPortlets)
    template = ViewPageTemplateFile('templates/renderer.pt')


class ManageContextualPortletsViewlet(base):
    """Viewlet for @@manage-portlets view to make portlets inserted via this
    viewlet editable.

    And this viewlet fix problem with kss edit. It just add __name__ attribute
    which is required for ajax functionality.
    """

    def __init__(self, context, request, view, manager):
        super(ManageContextualPortletsViewlet, self).__init__(context, request, view, manager)
        self.__name__ = view.__name__


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
