"""This file contains the cart related forms

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.2.0-alpha
@since: 2015-06-22
"""

from django.forms import ModelForm
from djangocart.models import Cart


class VoucherUpdateForm(ModelForm):
    """This class provides a simple form
    for applying vouchers on carts
    @since: 2015-06-22
    """
    class Meta:
        model = Cart
        fields = ['voucher_code']
