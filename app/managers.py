from django.db import  models

# class Itemmanager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_deleted = False)
    
#     def deleted(self):
#         return super().get_queryset().filter(is_deleted = True)

    # def cheap_items(self):
    #     return self.filter(price__lt=200)
    
    # def expensive_items(self):
    #     return self.filter(price__gt=150)
    
    # def search(self,keyword):
    #     return self.filter(product__icontains=keyword)