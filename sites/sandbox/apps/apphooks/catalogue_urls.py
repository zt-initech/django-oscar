from django.conf.urls import patterns

from .catalogue_views import ProductListing


urlpatterns = patterns(
    '',
    (r'^$', ProductListing.as_view()),
)
