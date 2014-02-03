from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

from oscar.app import shop

# These simply need to be imported into this namespace.  Ignore the PEP8
# warning that they aren't used.
from oscar.views import handler500, handler404, handler403

admin.autodiscover()

urlpatterns = i18n_patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    (r'^gateway/', include('apps.gateway.urls')),
    (r'^shop/', include(shop.urls)),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    import debug_toolbar

    # Server statics and uploaded media
    debug_patterns = static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
    # Allow error pages to be tested
    debug_patterns += patterns('',
        url(r'^403$', handler403),
        url(r'^404$', handler404),
        url(r'^500$', handler500),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
    urlpatterns = debug_patterns + urlpatterns
