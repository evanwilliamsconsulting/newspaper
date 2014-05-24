"""Mixin class for selectable views

This module contains a mixin-class to support selecting default layout
templates and/or default pages (in the style of default_page/index_html).
The implementation extends TemplateMixin from Archetypes, and implements
the ISelectableBrowserDefault interface from CMFPlone.
"""

from zope.interface import implements
import zope.component

#from zope.publisher.interfaces.browser import IBrowserMenu

from ExtensionClass import Base
from AccessControl import ClassSecurityInfo
from App.class_init import InitializeClass
from Acquisition import aq_base
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.permissions import View

from Products.CMFDynamicViewFTI.permissions import ModifyViewTemplate
from Products.CMFDynamicViewFTI.fti import DynamicViewTypeInformation

from Products.CMFDynamicViewFTI.interfaces import ISelectableBrowserDefault


from urllib import quote

from Acquisition import Acquired
from Acquisition import aq_acquire
from Acquisition import aq_base
from Acquisition import aq_inner
from Acquisition import aq_parent
from Acquisition.interfaces import IAcquirer
from OFS.interfaces import ITraversable
from zExceptions import NotFound
from ZODB.POSException import ConflictError

from zope.interface import implements
from zope.interface import Interface
from zope.component import queryMultiAdapter
from zope.location.interfaces import LocationError
from zope.traversing.namespace import namespaceLookup
from zope.traversing.namespace import nsParse

_marker = object()
fti_meta_type = DynamicViewTypeInformation.meta_type

class UseTraversalDefault(Exception):
	"""
	"""

class BrowserDefaultMixin(Base):
    """Mixin class for content types using the dynamic view FTI

    Allow the user to select a layout template (in the same way as
    TemplateMixin in Archetypes does), and/or to set a contained
    object's id as a default_page (acting in the same way as index_html)

    Note: folderish content types should overwrite HEAD like ATContentTypes
    """
    implements(ISelectableBrowserDefault)

    _at_fti_meta_type = fti_meta_type
    aliases = {
        '(Default)'  : '(dynamic view)',
        'view'       : '(selected layout)',
        'edit'       : 'base_edit',
        'properties' : 'base_metadata',
        'sharing'    : 'folder_localrole_form',
        'gethtml'    : '',
        'mkdir'      : '',
        }

    default_view = "base_view"
    suppl_views = ()

    security = ClassSecurityInfo()

    security.declareProtected(View, 'defaultView')
    def defaultView(self, request=None):
        """
        Get the actual view to use. If a default page is set, its id will
        be returned. Else, the current layout's page template id is returned.
        """
	print 'self'
	print self
        fti = self.getTypeInfo()
	print 'fti'
	print fti
        if fti is None:
            return self.default_view
        else:
	    print 'default_view'
	    print fti.defaultView(self)
            return fti.defaultView(self)

    security.declareProtected(View, '__call__')
    def __call__(self):
        """
        Resolve and return the selected view template applied to the object.
        This should not consider the default page.
        """
        template = self.unrestrictedTraverse(self.getLayout())
        return template()

    security.declareProtected(View, 'getDefaultPage')
    def getDefaultPage(self):
        """Return the id of the default page, or None if none is set.

        The default page must be contained within this (folderish) item.
        """
        fti = self.getTypeInfo()
        if fti is None:
            return None
        else:
            plone_utils = getToolByName(self, 'plone_utils', None)
            if plone_utils is not None:
                return plone_utils.getDefaultPage(self)
            else:
                return fti.getDefaultPage(self, check_exists=True)

    security.declareProtected(View, 'getLayout')
    def getLayout(self, **kw):
        """Get the selected view method.

        Note that a selected default page will override the view method.
        """
        fti = self.getTypeInfo()
        if fti is None:
            return None
        else:
            return fti.getViewMethod(self)

    security.declarePublic(View, 'getPDF')
    def getPDF(self):
        """Get the selected view method.

        Note that a selected default page will override the view method.
        """
        fti = self.getTypeInfo()
	baseview = fti.getViewMethod(self)
	return baseview
        #if fti is None:
        #    return None
        #else:
        #    return fti.getViewMethod(self)

    security.declarePublic(View, 'pdf')
    def pdf(self):
        """
        Resolve and return the selected view template applied to the object.
        This should not consider the default page.
        """
        template = self.traverseIT(self.getLayout())
        return template

    security.declarePublic('traverseIT')
    def traverseIT(self, path, default=_marker, restricted=False):
        """Lookup an object by path.

        path -- The path to the object. May be a sequence of strings or a slash
        separated string. If the path begins with an empty path element
        (i.e., an empty string or a slash) then the lookup is performed
        from the application root. Otherwise, the lookup is relative to
        self. Two dots (..) as a path element indicates an upward traversal
        to the acquisition parent.

        default -- If provided, this is the value returned if the path cannot
        be traversed for any reason (i.e., no object exists at that path or
        the object is inaccessible).

        restricted -- If false (default) then no security checking is performed.
        If true, then all of the objects along the path are validated with
        the security machinery. Usually invoked using restrictedTraverse().
        """
        from webdav.NullResource import NullResource
	print "enter traversal"
        if not path:
            print "Not path return self"
            return self

        if isinstance(path, str):
            # Unicode paths are not allowed
            path = path.split('/')
	    print "is instance split paths %s" % path
        else:
            path = list(path)
	    print "is not instance path is %s" % path

        REQUEST = {'TraversalRequestNameStack': path}
        path.reverse()
        path_pop = path.pop

        if len(path) > 1 and not path[0]:
            # Remove trailing slash
            path_pop(0)

        if restricted:
            validate = getSecurityManager().validate

        if not path[-1]:
            # If the path starts with an empty string, go to the root first.
            path_pop()
            obj = self.getPhysicalRoot()
            if restricted:
                validate(None, None, None, obj) # may raise Unauthorized
        else:
            obj = self

        resource = _marker
        try:
            while path:
                name = path_pop()
		print "name is %s" % name
                __traceback_info__ = path, name

                if name[0] == '_':
                    # Never allowed in a URL.
                    raise NotFound, name

                if name == '..':
                    next = aq_parent(obj)
                    if next is not None:
                        if restricted and not validate(obj, obj, name, next):
                            raise Unauthorized(name)
                        obj = next
                        continue

                bobo_traverse = getattr(obj, '__bobo_traverse__', None)
                try:
                    if name and name[:1] in '@+' and name != '+' and nsParse(name)[1]:
                        # Process URI segment parameters.
                        ns, nm = nsParse(name)
			print "the result %s %s" % (ns,nm)
                        try:
                            next = namespaceLookup(
                                ns, nm, obj, aq_acquire(self, 'REQUEST'))
			    print "next is %s" % next
                            if IAcquirer.providedBy(next):
                                next = next.__of__(obj)
                            if restricted and not validate(
                                obj, obj, name, next):
                                raise Unauthorized(name)
                        except LocationError:
                            raise AttributeError(name)

                    else:
                        next = UseTraversalDefault # indicator
                        try:
                            if bobo_traverse is not None:
                                next = bobo_traverse(REQUEST, name)
				print "bobo %s" % next
                                if restricted:
                                    if aq_base(next) is not next:
                                        # The object is wrapped, so the acquisition
                                        # context is the container.
                                        container = aq_parent(aq_inner(next))
                                    elif getattr(next, 'im_self', None) is not None:
                                        # Bound method, the bound instance
                                        # is the container
                                        container = next.im_self
                                    elif getattr(aq_base(obj), name, _marker) is next:
                                        # Unwrapped direct attribute of the object so
                                        # object is the container
                                        container = obj
                                    else:
                                        # Can't determine container
                                        container = None
                                    # If next is a simple unwrapped property, its
                                    # parentage is indeterminate, but it may have
                                    # been acquired safely. In this case validate
                                    # will raise an error, and we can explicitly
                                    # check that our value was acquired safely.
                                    try:
                                        ok = validate(obj, container, name, next)
                                    except Unauthorized:
                                        ok = False
                                    if not ok:
                                        if (container is not None or
                                            guarded_getattr(obj, name, _marker)
                                                is not next):
                                            raise Unauthorized(name)
                        except UseTraversalDefault:
                            # behave as if there had been no '__bobo_traverse__'
                            bobo_traverse = None
                        if next is UseTraversalDefault:
                            if getattr(aq_base(obj), name, _marker) is not _marker:
                                if restricted:
                                    next = guarded_getattr(obj, name)
                                else:
                                    next = getattr(obj, name)
                            else:
                                try:
                                    next = obj[name]
                                    # The item lookup may return a NullResource,
                                    # if this is the case we save it and return it
                                    # if all other lookups fail.
                                    if isinstance(next, NullResource):
                                        resource = next
                                        raise KeyError(name)
                                except AttributeError:
                                    # Raise NotFound for easier debugging
                                    # instead of AttributeError: __getitem__
                                    raise NotFound(name)
                                if restricted and not validate(
                                    obj, obj, None, next):
                                    raise Unauthorized(name)

                except (AttributeError, NotFound, KeyError), e:
                    # Try to look for a view
                    next = queryMultiAdapter((obj, aq_acquire(self, 'REQUEST')),
                                             Interface, name)

                    if next is not None:
                        if IAcquirer.providedBy(next):
                            next = next.__of__(obj)
                        if restricted and not validate(obj, obj, name, next):
                            raise Unauthorized(name)
                    elif bobo_traverse is not None:
                        # Attribute lookup should not be done after
                        # __bobo_traverse__:
                        raise e
                    else:
                        # No view, try acquired attributes
                        try:
                            if restricted:
                                next = guarded_getattr(obj, name, _marker)
                            else:
                                next = getattr(obj, name, _marker)
                        except AttributeError:
                            raise e
                        if next is _marker:
                            # If we have a NullResource from earlier use it.
                            next = resource
                            if next is _marker:
                                # Nothing found re-raise error
                                raise e

                obj = next

            return obj

        except ConflictError:
            raise
        except:
            if default is not _marker:
                return default
            else:
                raise

    security.declareProtected(View, 'getDefaultPage')
    security.declarePublic('canSetDefaultPage')
    def canSetDefaultPage(self):
        """Check if the user has permission to select a default page on this
        (folderish) item, and the item is folderish.
        """
        if not self.isPrincipiaFolderish:
            return False
        mtool = getToolByName(self, 'portal_membership')
        member = mtool.getAuthenticatedMember()
        return member.has_permission(ModifyViewTemplate, self)

    security.declareProtected(ModifyViewTemplate, 'setDefaultPage')
    def setDefaultPage(self, objectId):
        """Set the default page to display in this (folderish) object.

        The objectId must be a value found in self.objectIds() (i.e. a contained
        object). This object will be displayed as the default_page/index_html object
        of this (folderish) object. This will override the current layout
        template returned by getLayout(). Pass None for objectId to turn off
        the default page and return to using the selected layout template.
        """
        new_page = old_page = None
        if objectId is not None:
            new_page = getattr(self, objectId, None)
        if self.hasProperty('default_page'):
            pages = self.getProperty('default_page','')
            if isinstance(pages, (list, tuple)):
                for page in pages:
                    old_page = getattr(self, page, None)
                    if page is not None: break
            elif isinstance(pages, str):
                old_page = getattr(self, pages, None)

            if objectId is None:
                self.manage_delProperties(['default_page'])
            else:
                self.manage_changeProperties(default_page = objectId)
        else:
            if objectId is not None:
                self.manage_addProperty('default_page', objectId, 'string')
        if new_page != old_page:
            if new_page is not None:
                new_page.reindexObject(['is_default_page'])
            if old_page is not None:
                old_page.reindexObject(['is_default_page'])

    security.declareProtected(ModifyViewTemplate, 'setLayout')
    def setLayout(self, layout):
        """Set the layout as the current view.

        'layout' should be one of the list returned by getAvailableLayouts(), but it
        is not enforced. If a default page has been set with setDefaultPage(), it is
        turned off by calling setDefaultPage(None).
        """
        if not (layout and isinstance(layout, basestring)):
            raise ValueError, ("layout must be a non empty string, got %s(%s)" %
                               (layout, type(layout)))

        defaultPage = self.getDefaultPage()
        if defaultPage is None and layout == self.getLayout():
            return

        if self.hasProperty('layout'):
            self.manage_changeProperties(layout = layout)
        else:
            if getattr(aq_base(self), 'layout', _marker) is not _marker:
                # Archetypes remains? clean up
                old = self.layout
                if old and not isinstance(old, basestring):
                    raise RuntimeError, ("layout attribute exists on %s and is"
                                         "no string: %s" % (self, type(old)))
                delattr(self, 'layout')

            self.manage_addProperty('layout', layout, 'string')

        self.setDefaultPage(None)

    security.declareProtected(View, 'getDefaultLayout')
    def getDefaultLayout(self):
        """Get the default layout method.
        """
        fti = self.getTypeInfo()
        if fti is None:
            return "base_view" # XXX
        else:
            return fti.getDefaultViewMethod(self)

    security.declarePublic('canSetLayout')
    def canSetLayout(self):
        """Check if the current authenticated user is permitted to select a layout.
        """
        mtool = getToolByName(self, 'portal_membership')
        member = mtool.getAuthenticatedMember()
        return member.has_permission(ModifyViewTemplate, self)

    security.declareProtected(View, 'getAvailableLayouts')
    def getAvailableLayouts(self):
        """Get the layouts registered for this object from its FTI.
        """
        fti = self.getTypeInfo()
        if fti is None:
            return ()
        result = []
        method_ids = fti.getAvailableViewMethods(self)
        for mid in method_ids:
            view = zope.component.queryMultiAdapter((self, self.REQUEST),
                                                    zope.interface.Interface,
                                                    name=mid)

            if view is not None:
                menu = zope.component.getUtility(
                    IBrowserMenu, 'plone_displayviews')
                item = menu.getMenuItemByAction(self, self.REQUEST, mid)
                title = item and item.title or mid
                result.append((mid, title))
            else:
                method = getattr(self, mid, None)
                if method is not None:
                    # a method might be a template, script or method
                    try:
                        title = method.aq_inner.aq_explicit.title_or_id()
                    except AttributeError:
                        title = mid
                    result.append((mid, title))
        return result

InitializeClass(BrowserDefaultMixin)
