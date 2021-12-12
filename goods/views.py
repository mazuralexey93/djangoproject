from django.views.generic.list import ListView
from goods.models import GoodItem


class ItemsListView(ListView):
    model = GoodItem
    template_name = "items_index.html"

    def get_queryset(self):
        items = GoodItem.objects.all()
        return items