from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name="profile"),
    path('edit_profile/', views.profile_edit, name="edit_profile"),
    path('change_password/', views.change_password, name="change_password"),
    path('apply/', views.apply, name="apply"),
]
