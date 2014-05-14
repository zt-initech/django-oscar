from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin


class FeaturedProduct(CMSPlugin):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    product = models.ForeignKey('catalogue.Product')
    TEMPLATE_CHOICES = (
        ('djangocms/plugins/product-sidebar.html', _('Sidebar')),
        ('djangocms/plugins/product-main.html', _('Main')),
    )
    render_template = models.CharField(
        max_length=255, choices=TEMPLATE_CHOICES)
