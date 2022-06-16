from rest_framework.pagination import PageNumberPagination

class WatchListPagination(PageNumberPagination):
    """Defining a pagination"""
    page_size = 7
    page_query_param = 'p'
    page_size_query_param = 'size'