from django.urls import path
from goods.views import ItemsListView

urlpatterns = [
    path('', ItemsListView.as_view()),

]