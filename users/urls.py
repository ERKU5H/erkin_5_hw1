from django.urls import path
from users.views import user_register, login_user, confirm_user

urlpatterns = [
    path('user/register/', user_register),
    path('confirm/', confirm_user),
    path('login/', login_user),
]
