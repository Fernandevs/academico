from django.urls import path

from oe.views import login, dashboard, UserListView, UserUpdateView, UserDeleteView, logout, \
    UserCreateView, CareerListView, CareerCreateView, CareerUpdateView, CareerDeleteView, StudentListView, \
    StudentCreateView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    path('users/', login, name='login'),
    path('users/dashboard/', dashboard, name='dashboard'),
    path('users/list/', UserListView.as_view(), name='list_users'),
    path('users/create/', UserCreateView.as_view(), name='create_user'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='update_user'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='delete_user'),
    path('careers/list/', CareerListView.as_view(), name='list_careers'),
    path('careers/create/', CareerCreateView.as_view(), name='create_career'),
    path('careers/update/<int:pk>/', CareerUpdateView.as_view(), name='update_career'),
    path('careers/delete/<int:pk>/', CareerDeleteView.as_view(), name='delete_career'),
    path('students/list/', StudentListView.as_view(), name='list_students'),
    path('students/create/', StudentCreateView.as_view(), name='create_student'),
    path('students/update/<int:pk>/', StudentUpdateView.as_view(), name='update_student'),
    path('students/delete/<int:pk>/', StudentDeleteView.as_view(), name='delete_student'),
    path('users/logout/', logout, name='logout'),
]
