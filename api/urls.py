from django.urls import path, re_path,include
from . import views 
from .views import ProductModelView,CategoryHyperView,ItemHyperView
from rest_framework.routers import DefaultRouter

app_name ='api'

router = DefaultRouter()
router.register(r'item', ItemHyperView)
router.register(r'category', CategoryHyperView)


router.register(r'products', ProductModelView, basename='product')
urlpatterns = [
    # path('product/',views.ProductView.as_view()),
    # path('product/',views.ProductView.as_view({'get':'list'})),
    # path('productdetail/<int:pk>',views.ProductDetailView.as_view(), name = 'productdetail'),




    #Function based @api_view
    path('product/',views.ProductView, name='productviewset'),
    path('productdetail/<int:pk>',views.ProductDetailView, name = 'productdetail'),

    #class based (APIView)
    # path('productclass/',views.ProductClassView.as_view(), name = 'productclassview'),
    # path('productdetailclass/',views.ProductDetailViewClass.as_view(), name = 'productdetailclass')

    #Mixins
    # path('productgeneric/',views.ProductClassGeneric.as_view(), name = 'productgeneric'),
    # path('productdetailgeneric/<int:pk>',views.ProductDetailClassgeneric.as_view(), name = 'productdetailgeneric'),

    #Generic
    path('productlistgeneric/',views.ProductListCreatGeneric.as_view(), name= 'productlistgeneric'),
    # path('product_rud_generic/<int:pk>',views.ProductRetriveGeneric.as_view(), name= 'productretrivegeneric'),
    # path('product_RUD_generic/<int:pk>',views.Product_RUD_Generic.as_view(), name= 'productretrivegeneric'),
    # path('product_RUD_generic1/',views.viewset.as_view(), name= 'productretrivegeneric'),

    #Viewset
    path('productviewset/',include(router.urls)),
]