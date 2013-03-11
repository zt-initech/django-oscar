from django.conf.urls.defaults import patterns, include

from . import api, views

product_resource = api.ProductResource()


urlpatterns = patterns('',
    (r'^$', views.IndexView.as_view()),
    (r'', include(product_resource.urls)),
)
