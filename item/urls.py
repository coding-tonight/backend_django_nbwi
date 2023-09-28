from django.urls import path
from item.views import ItemView, ItemDetail

urlpatterns = [
    path('item/', ItemView.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view())
]
