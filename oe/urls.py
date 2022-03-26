from django.urls import path

from oe.views import create_user, UserListView, dashboard

urlpatterns = [
    path('users/list/', UserListView.as_view(), name='list_users'),
    path('users/create/', create_user, name='create_user'),
    path('users/dashboard/', dashboard, name='dashboard'),
]
