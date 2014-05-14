from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool


from .models import FeaturedProduct


class FeaturedProductPlugin(CMSPluginBase):
    model = FeaturedProduct
    name = 'Featured Product'
    admin_preview = True

    def render(self, context, instance, placeholder):
        # self.render_template = instance.template
        # print 'self render template', self.render_template
        # print 'prod'
        print 'product', instance.product
        print instance
        return context


plugin_pool.register_plugin(FeaturedProductPlugin)
