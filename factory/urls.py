from django.urls import path
from factory.views import FactoryOwnerDetail, FactoryOwnerView, FactoryView, FactoryDetail

urlpatterns = [
    path('factory/', FactoryView.as_view()),
    path('factory/<int:pk>', FactoryDetail.as_view()),
    # factory owner url
    path('factoryOwner/', FactoryOwnerView.as_view()),
    path('factoryOwner/<int:pk>/', FactoryOwnerDetail.as_view())
]
