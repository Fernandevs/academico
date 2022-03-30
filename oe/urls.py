from django.urls import path

from oe.views import login, dashboard, UserListView, UserUpdateView, UserDeleteView, logout, UserCreateView

urlpatterns = [
    path('users/', login, name='login'),
    path('users/dashboard/', dashboard, name='dashboard'),
    path('users/list/', UserListView.as_view(), name='list_users'),
    path('users/create/', UserCreateView.as_view(), name='create_user'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='update_user'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='delete_user'),
    path('users/logout/', logout, name='logout'),
]
