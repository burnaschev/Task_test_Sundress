from rest_framework.pagination import PageNumberPagination


class CategoryPaginator(PageNumberPagination):
    page_size = 4
    page_query_param = 'page_size'
    max_page_size = 15


class ProductPaginator(PageNumberPagination):
    page_size = 4
    page_query_param = 'page_size'
    max_page_size = 50
