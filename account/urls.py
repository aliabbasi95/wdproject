from django.urls import path

from account.views import signup_view, signin_view, logout_view, profile_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', signin_view, name='signin'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
]
