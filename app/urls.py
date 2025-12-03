from app import views
from django.urls import path
from django.views.decorators.cache import cache_page

app_name = 'app'

urlpatterns = [
    # path('', views.login_add, name='home'),
    path('',views.test, name='home'),
    path('app/<int:id>',views.details, name='details'),
    path('add/',views.create_item, name='create_item'),
    path('update/<int:id>',views.update_item, name = 'update_item'),
    path('delet/<int:id>',views.delet_item, name = 'delet_item'),
    path('search/',views.search_item, name = 'search'),
    path('category/<str:foo>',views.category, name='category'),


    # path('profile/',views.ProfileEdit, name = 'profile'),


    # path('',views.Homeclassview.as_view(), name='home'),
    # path('app/<int:pk>',views.detailsview.as_view(), name='details'),
    # path('add/',views.Createclassview.as_view(), name='create_item'),
    # path('update/<int:pk>',views.Updateclassview.as_view(), name = 'update_item'),
    # path('delet/<int:pk>',views.Deletclassview.as_view(), name = 'delet_item'),
    # path('profile/<int:pk>',views.Profileview.as_view(), name = 'user_profile'),
]
