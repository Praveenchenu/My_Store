from django.urls import path
from . import views
app_name = 'users'

urlpatterns = [
    path('signup/',views.Signup, name= 'signup'),
    path('login/',views.login_view, name = 'login'),
    path('logout/',views.log_out, name = 'logout'),
    path('profile/',views.profile, name = 'profile')
]