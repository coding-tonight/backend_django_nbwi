from django.urls import path
from group.views import GroupView, GroupDetail


urlpatterns = [
    path('group/', GroupView.as_view()),
    path('group/<int:pk>/', GroupDetail.as_view())
]
