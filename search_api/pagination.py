from rest_framework.pagination import CursorPagination

# Paginations class with CursorPagination method querying upto 10 results per page
class ResultsPagination(CursorPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100
