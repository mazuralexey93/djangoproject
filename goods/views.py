from django.views.generic.list import ListView

from goods.models.goodsmodel import GoodItem


class ItemsListView(ListView):
    model = GoodItem
    template_name = "goods_list.html"

    def get_queryset(self):
        items = GoodItem.objects.all()
        return items
