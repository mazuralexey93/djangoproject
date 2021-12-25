from django.views.generic.list import ListView

from goods.models.goodsmodel import GoodItem


class ItemsListView(ListView):
    model = GoodItem
    template_name = "goods_list.html"
    # queryset = GoodItem.objects.select_related('category').prefetch_related('new_category').all()

    def get_queryset(self):
        queryset = GoodItem.on_site.select_related('category').prefetch_related('new_category').all()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'site': self.request.site
        })
        return context
