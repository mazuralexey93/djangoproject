from django.views.generic.list import ListView

from goods.models.goodsmodel import GoodItem


class ItemsListView(ListView):
    model = GoodItem
    template_name = "goods_list.html"

    def get_queryset(self):
        queryset  = GoodItem.objects.select_related('category').prefetch_related('new_category').all()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset
