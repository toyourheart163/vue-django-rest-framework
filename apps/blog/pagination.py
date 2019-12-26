from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter

class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(
            {'code': 20000,
             'data': {
                 'total': self.page.paginator.count,
                 'items': data
             }
            })

