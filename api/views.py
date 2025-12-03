from django.shortcuts import render,get_object_or_404
from app.models import Item,Category
from .serialization import ItemSerialization,CategotySerialization,CategoryHyperSerialization,ItemHyperSerialization
from rest_framework import viewsets,filters,permissions
from rest_framework.decorators import throttle_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics,mixins
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .paginator import ItemCursorPagination
# from .paginator import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CustomFilter
from rest_framework.filters import SearchFilter
from rest_framework.throttling import UserRateThrottle
from .permissions import IsOwnerOrReadOnly
# from .renderers import CustomJsonRender
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from rest_framework.parsers import MultiPartParser,FormParser


# Create your views here.

class CategoryHyperView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryHyperSerialization
  
    # pagination_class = None

class ItemHyperView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemHyperSerialization
    # renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    parser_classes = [MultiPartParser,FormParser]




# #Model VIEWSET
class ProductModelView(viewsets.ModelViewSet):
    # throttle_classes = [UserRateThrottle]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    queryset = Item.objects.all()
    serializer_class = ItemSerialization
    
    pagination_class = ItemCursorPagination
    filterset_class = CustomFilter
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter,
                       filters.SearchFilter,]
    filterset_fields = ['price']
    ordering_fields = ['price']
    search_fields = ['product']
    
    
#FUNCTION BASED CRUD

@api_view(['GET', 'POST'])
@throttle_classes([UserRateThrottle])
# @renderer_classes([JSONRenderer])
def ProductView(request):
    if request.method == 'GET':
        items = Item.objects.all()

        paginator= ItemCursorPagination()

        pagination_items=paginator.paginate_queryset(items,request)

        serialization = ItemSerialization(pagination_items, many = True)
        return Response(serialization.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serialization = ItemSerialization(data = request.data)
        if serialization.is_valid():
            serialization.save()
            return Response(serialization.data,status=status.HTTP_201_CREATED)
        else:
            print(serialization.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT','PATCH', 'DELETE'])
def ProductDetailView(request,pk):
    try:
        productdetail = Item.objects.get(pk = pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serialization = ItemSerialization(productdetail)
        return Response(serialization.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serialization = ItemSerialization(productdetail, data=request.data)
        if serialization.is_valid():
            serialization.save()
            return Response(serialization.data, status=status.HTTP_200_OK)
        else:
            print(serialization.error_messages)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serialization = ItemSerialization(
        productdetail,
        data=request.data,
        partial=True
    )
        if serialization.is_valid():
            serialization.save()
            return Response(serialization.data, status=status.HTTP_200_OK)
        else:
            return Response(serialization.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'Delete':
        productdetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



#CLASS BASED APIView
'''class ProductView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        lists = Item.objects.all()
        serialization = ItemSerialization(lists, many = True)
        return Response(serialization.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serialization = ItemSerialization(data=request.data)
        if serialization.is_valid():
            serialization.save()
            return Response(serialization.data, status=status.HTTP_201_CREATED)
        else:
            print(serialization.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self,request,pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Http404
    
    def get(self,request,pk):
        item_detail = self.get_object(pk)
        serialization = ItemSerialization(item_detail)
        return Response(serialization.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        item_detail = self.get_object(pk)
        serialization = ItemSerialization(item_detail,data=request.data)
        if serialization.is_valid():
            serialization.save()
            return Response(serialization.data, status=status.HTTP_200_OK)
        else:
            print(serialization.errors)
            return Response({'errors':'update is failed'} ,tatus=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        item_detail = self.get_object(pk)
        item_detail.delete()
        return Response({'message':'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


'''

'''
#MIXINS
class ProductView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerialization

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
class ProductDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerialization

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    '''



#GENERICS LIST, CREATE
'''
class ProductView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerialization

class ProductCreatGeneric(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerialization
'''
class ProductListCreatGeneric(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerialization
    pagination_class = ItemCursorPagination
    filter_backends = [SearchFilter]

'''
#GENERICS RETRIVE UPDATE DELETE
class ProductDetailView(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerialization
    lookup_field = 'pk'
'''
'''class ProductView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerialization
    pagination_class = CustomPagination

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerialization
    lookup_field = 'pk'
    pagination_class = CustomPagination
'''


#VIEWSET
'''
class ProductView(viewsets.ViewSet):
    def list(self,request):
        lists = Item.objects.all()
        serialization = ItemSerialization(lists, many = True)
        return Response(serialization.data,status=status.HTTP_200_OK)
    
    def create(self,request ):
        serialization = ItemSerialization(data=request.data)
        if serialization.is_valid():
            serialization.save()
            return Response(serialization.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialization.errors)
    
    def retrieve(self,request, pk=None):
        lists = get_object_or_404(Item,pk=pk)
        serialization = ItemSerialization(lists)
        return Response(serialization.data, status=status.HTTP_200_OK)
    
    def update(self,request,pk=None):
        lists = get_object_or_404(Item,pk=pk)
        serialization = ItemSerialization(lists, data=request.data)
        if serialization.is_valid():
            serialization.save()
            return Response(serialization.data,status=status.HTTP_200_OK)
        else:
            return Response(serialization.errors)
        
    def destroy(self,request,pk=None):
        lists = get_object_or_404(Item,pk=pk)
        lists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        '''