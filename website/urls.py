from django.urls import path
from .import views

app_name = "user_account"


urlpatterns = [
    path('home/',views.home, name="home"),
    path('',views.register_view, name="register"),
    path('login/',views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('password-reset/', views.request_password_reset_view, name="request_password_reset"),
    path('verify-email/<str:email>/', views.verify_email_view, name="verify_email"),
    path('reset-password/<str:email>/', views.reset_password, name="reset_password"),

]
