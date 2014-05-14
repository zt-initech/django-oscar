from django.views import generic
from django.db.models import get_model


Product = get_model('catalogue', 'Product')


class ProductListing(generic.ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 20
    template_name = 'djangocms/product-listing.html'
