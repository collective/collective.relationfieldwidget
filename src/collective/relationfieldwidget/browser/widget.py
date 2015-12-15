# -*- coding: utf-8 -*-
from Acquisition import ImplicitAcquisitionWrapper
from Acquisition import aq_inner
from UserDict import UserDict
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import base_hasattr
from lxml import etree
from plone.app.widgets.base import TextareaWidget
from plone.app.widgets.base import dict_merge
from plone.app.widgets.utils import NotImplemented
from plone.app.widgets.utils import get_ajaxselect_options
from plone.app.widgets.utils import get_date_options
from plone.app.widgets.utils import get_datetime_options
from plone.app.widgets.utils import get_querystring_options
from plone.app.widgets.utils import get_relateditems_options
from plone.app.widgets.utils import get_tinymce_options
from plone.registry.interfaces import IRegistry
from plone.app.z3cform.utils import closest_content
from z3c.form.browser.text import TextWidget as z3cform_TextWidget
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import NO_VALUE
from z3c.form.widget import FieldWidget
from z3c.form.widget import Widget
from zope.component import getUtility
from zope.component import ComponentLookupError
from zope.i18n import translate
from zope.interface import implementer
from plone.app.z3cform.interfaces import IRelatedItemsWidget
from plone.app.z3cform.widget import RelatedItemsWidget as plonez3cform_RelatedItemsWidget

class RelatedItemsWidget(plonez3cform_RelatedItemsWidget):
    """RelatedItems widget for z3c.form with clickable list of URLs as output"""

    def related_items(self):
        context = aq_inner(self.context)
        res = ()
        # Dexterity
        catalog = getToolByName(context, 'portal_catalog')
        separator = self.separator
        related = self.value.split(separator)
        if not related:
            return ()
        res = catalog(UID=related)
        return res


@implementer(IFieldWidget)
def RelatedItemsFieldWidget(field, request, extra=None):
    if extra is not None:
        request = extra
    return FieldWidget(field, RelatedItemsWidget(request))


