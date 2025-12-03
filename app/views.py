from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Category, Item
from .froms import ItemForm, loginForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator


def category(request, foo):
    foo_name = foo.replace('-', ' ')
    try:        
        cat_id = int(foo)
        category_obj = get_object_or_404(Category, id=cat_id)
    except (ValueError, Category.DoesNotExist):
        category_obj = get_object_or_404(Category, name__iexact=foo_name)

    products_qs = Item.objects.filter(category=category_obj, is_available=True).order_by('-created_at')
    # paginate
    paginator = Paginator(products_qs, 12)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
        'category': category_obj,
        'products': products,
    }
    return render(request, 'app/category.html', context)


# @login_required
# @cache_page(60*15)
def test(request):
    lists = Item.objects.all().order_by('id')
    paginator = Paginator(lists,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj' : page_obj
    }
    return render(request, 'app/table.html',context)



    
def details(request,id):
    single_value = Item.objects.get(id = id)
    context = {
        'single_value' : single_value
    }
    return render(request, 'app/dashboard.html', context)

# def ProfileEdit(request,id):
#     profile = Item.objects.get(id = id)
#     context = {
#         'profile' : profile
#     }
#     return render(request, 'app/profile.html',context )



 

def create_item(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:home')
    context = {
        'form':form  
    }
    return render(request, 'app/item_form.html', context)




def update_item(request,id):
    item = Item.objects.get(id = id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('app:home' )
    context = {
        'form' : form
    }
    return render(request, 'app/item_update_form.html', context)


def delet_item(request,id):
    item = get_object_or_404(Item, id=id)
    item.delete()
    return redirect('app:home')



def search_item(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Item.objects.filter(
            product__icontains = query
        )
    context = {
        'results' : results,
        'query' : query 
    }
    return render(request, 'app/search_items.html', context)




# class base Listview
# @method_decorator(cache_page(60*15), name='dispatch')
# class Homeclassview(ListView):
#     model = Item
#     template_name = 'app/table.html'
#     context_object_name = 'lists' 
#     # paginate_by = 5

    # def get_queryset(self):
    #     query = self.request.GET.get('q')
    #     print("search query",query)
    #     if query:
    #         qs = Item.objects.filter(product__icontains=query)
    #         print('results',qs)
    #         return qs
    #     return Item.objects.all()


#class base Detailview
# class detailsview(LoginRequiredMixin,DetailView):
#     model = Item
#     template_name = 'app/dashboard.html'
#     context_object_name = 'single_value'

#cclassbased Profilepage
# class Profileview(DetailView):
#     model = Item
#     template_name = 'app/profile.html'
#     context_object_name = 'profile'
   

# create class  
# class Createclassview(LoginRequiredMixin,CreateView):
#     #createview is automatic checks the html file named (tablename_form.html)
#     model = Item
#     fields = ['image', 'product','description','price']

#     def form_valid(self,form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

#     # login_url = '/login/'
#     # redirect_field_name = 'next'


#classupdateview
# class Updateclassview(UpdateView):
#     model = Item
#     fields=['image', 'product','description','price']
#     #createview is automatic checks the html file named (tablename_update_form.html)
#     template_name_suffix ='_update_form'

    # def get_queryset(self):
    #     return Item.objects.filter(user = self.request.user)
        
# classDeletview
# class Deletclassview(DeleteView):
#     model = Item
#     success_url = reverse_lazy("app:home")
