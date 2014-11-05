from oscar.apps.address import abstract_models


class ShippingAddress(abstract_models.AbstractShippingAddress):
    # Adjust the regex for France
    POSTCODES_REGEX = abstract_models.AbstractAddress.POSTCODES_REGEX.copy()
    POSTCODES_REGEX['FR'] = r'^[0-9]{4}$'


from oscar.apps.order.models import *  # noqa
