from django.conf.urls import patterns, url
from django.views import generic

from apps.foobar import models

model_classes = (models.MyNewModel,)

urlpatterns = []
for model in model_classes:
    name = model._meta.object_name.lower()
    urlpatterns += patterns('',
        url(r'%s/' % name,
            generic.ListView.as_view(model=model)),
        url(r'%s/(?P<pk>\d+)/$' % name,
            generic.DetailView.as_view(model=model)),
        url(r'%s/(?P<pk>\d+)/delete/$' % name,
            generic.DeleteView.as_view(model=model)))
