"""This file contains the admin classes for djangocart related
models

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.4.2-alpha
@since: 2015-07-13
"""

from django.contrib import admin

from .models import Cart

admin.site.register(Cart)
