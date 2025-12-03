from rest_framework.pagination import PageNumberPagination,CursorPagination
from rest_framework.response import Response

# class CustomPagination(PageNumberPagination):
#     page_size = 3
#     page_size_query_param = 'page_size_pavan'  
#     max_page_size = 100  
#     page_query_param = 'page_num'  
#     last_page_strings = ['last', 'end']  

#     def get_paginated_response(self, data):
#         return Response ({
#             'next': self.get_next_link(),
#             'previous':self.get_previous_link(),
#             'count':self.page.paginator.count,
#             'page_size':self.page_size,
#             'results':data
#         })

class ItemCursorPagination(CursorPagination):
    page_size=5
    ordering = '-id'
    cursor_query_param = 'cursor'
