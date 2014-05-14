from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class CatalogueApphook(CMSApp):
    name = _("Product Catalogue")
    urls = ["apps.apphooks.catalogue_urls"]
    app_name = 'catalogue'


apphook_pool.register(CatalogueApphook)
