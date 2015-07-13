import datetime
from djangocart import models

CART_ID = 'CART-ID'


class ItemAlreadyExists(Exception):
    pass


class ItemDoesNotExist(Exception):
    pass


class SessionCart:
    """@change: Rename Cart to SessionCart to avoid clashes"""
    def __init__(self, request):
        cart_id = request.session.get(CART_ID)
        if cart_id:
            try:
                cart = models.Cart.objects.get(id=cart_id, checked_out=False)
            except models.Cart.DoesNotExist:
                cart = self.new(request)
        else:
            cart = self.new(request)
        self.cart = cart

    def __iter__(self):
        for item in self.cart.item_set.all():
            yield item

    def new(self, request):
        cart = models.Cart(creation_date=datetime.datetime.now())
        cart.save()
        request.session[CART_ID] = cart.id
        return cart

    def add(self, product, unit_price, quantity=1):
        try:
            item = models.Item.objects.get(
                cart=self.cart,
                product=product,
            )
        except models.Item.DoesNotExist:
            item = models.Item()
            item.cart = self.cart
            item.product = product
            item.unit_price = unit_price
            item.quantity = quantity
            item.save()
        else: #ItemAlreadyExists
            item.unit_price = unit_price
            item.quantity = item.quantity + int(quantity)
            item.save()

    def remove(self, product):
        try:
            item = models.Item.objects.get(
                cart=self.cart,
                product=product,
            )
        except models.Item.DoesNotExist:
            raise ItemDoesNotExist
        else:
            item.delete()

    def update(self, product, quantity, unit_price=None):
        try:
            item = models.Item.objects.get(
                cart=self.cart,
                product=product,
            )
        except models.Item.DoesNotExist:
            raise ItemDoesNotExist

    def count(self):
        result = 0
        for item in self.cart.item_set.all():
            result += 1 * item.quantity
        return result

    def summary(self):
        """@change: Implement discount logic"""
        result = 0
        is_footwear = False
        for item in self.cart.item_set.all():
            item_product = item.get_product()
            if 'Footwear' in item_product.product_category.category_name:
                is_footwear = True
            result += item.total_price
        if self.cart.has_voucher and self.cart.voucher_code:
            if self.cart.voucher_code == "vou5":
                result -= 5
            if 50 < result < 75 and self.cart.voucher_code == "vou10":
                result -= 10
            if result > 75 and is_footwear and self.cart.voucher_code == "vou15":
                result -= 15
        return result

    def clear(self):
        """@change: Remove voucher code and voucher status"""
        for item in self.cart.item_set.all():
            item.delete()
        self.cart.voucher_code = ""
        self.cart.has_voucher = False
        self.cart.save()
