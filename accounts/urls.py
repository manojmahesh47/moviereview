from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/', views.view_profile, name='view_profile'),  # Corrected line
]
