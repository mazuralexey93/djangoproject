from django.contrib import admin

from goods.models.goodsmodel import GoodItem, Category

admin.site.register(GoodItem)
admin.site.register(Category)
