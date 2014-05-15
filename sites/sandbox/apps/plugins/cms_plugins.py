from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool


from .models import FeaturedProduct


class FeaturedProductPlugin(CMSPluginBase):
    model = FeaturedProduct
    name = 'Featured Product'
    admin_preview = True
    render_template = ''

    def render(self, context, instance, placeholder):
        self.render_template = instance.render_template
        return context


plugin_pool.register_plugin(FeaturedProductPlugin)
