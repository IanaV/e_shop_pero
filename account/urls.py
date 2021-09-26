from django.urls import path

from .views import *

urlpatterns = [
    # path('', profile, name='profile'),
    # path('register', register, name='register'),

    path('', login, name='login'),
    path('register', register, name='register'),
    path('logout', user_logout, name='logout'),
    path('profile-edit', profile_edit, name='profile_edit'),
    path('profile', profile, name='profile'),
]