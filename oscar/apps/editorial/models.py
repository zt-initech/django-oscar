from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.template import loader

from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent
from feincms.content.medialibrary.models import MediaFileContent

Page.register_extensions(
    'feincms.module.extensions.datepublisher',
    'feincms.module.extensions.translations')

Page.register_templates({
    'title': _('Standard template'),
    'path': 'editorial/layout_2_col.html',
    'regions': (
        ('main', _('Main content area')),
        ('sidebar', _('Sidebar'), 'inherited'),
    ),
})

# Register standard content types
Page.create_content_type(RichTextContent)
Page.create_content_type(MediaFileContent, TYPE_CHOICES=(
    ('default', _('default')),
    ('lightbox', _('lightbox')),
))


# Custom content types
class HeroProduct(models.Model):
    name = models.CharField(max_length="255")
    product = models.ForeignKey('catalogue.Product')
    description = models.TextField()

    class Meta:
        abstract = True

    def render(self, **kwargs):
        # Use the promotion template so we arrange our data like a promotion
        # object.
        ctx = {
            'promotion': {'name': self.name,
                          'description': self.description},
            'product': self.product,
        }
        return loader.render_to_string(
            'promotions/singleproduct.html', ctx)

Page.create_content_type(HeroProduct)
