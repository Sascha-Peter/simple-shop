"""This file contains the cart related forms

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.3.0-alpha
@since: 2015-06-22
"""

from django.forms import ModelForm, ValidationError
from django.utils.translation import gettext as _

from djangocart.models import Cart


class VoucherUpdateForm(ModelForm):
    """This class provides a simple form
    for applying vouchers on carts
    @since: 2015-06-22
    """
    class Meta:
        model = Cart
        fields = ['voucher_code']

    def clean_voucher_code(self):
        """@since: 2015-07-13"""
        vouchers = ["vou5", "vou10", "vou15"]
        data = self.cleaned_data["voucher_code"]
        result = 0
        is_footwear = False
        for item in self.instance.item_set.all():
            item_product = item.get_product()
            if 'Footwear' in item_product.product_category.category_name:
                is_footwear = True
            result += item.total_price
        if data not in vouchers:
            raise ValidationError(_('This voucher is invalid'))
        else:
            if data == "vou5":
                return data
            if data == "vou10" and not 50 < result < 75:
                raise ValidationError(_('This voucher does not apply'))
            if data == "vou15":
                if not is_footwear:
                    raise ValidationError(_('This voucher only applies for footwear'))
                else:
                    if result < 75:
                        raise ValidationError(_('This voucher does not apply'))
            return data
