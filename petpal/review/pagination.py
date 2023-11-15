from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10  # Set the number of items per page
    page_size_query_param = 'page_size'  # Allow client to override, e.g., ?page_size=4
    max_page_size = 100
