from django.urls import path
from goods.views import ItemsListView

app_name = 'goods'

urlpatterns = [
    path('', ItemsListView.as_view(), name='index'),
    path('<int:category_id>/', ItemsListView.as_view(), name='category'),

]