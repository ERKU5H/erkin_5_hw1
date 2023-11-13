from django.urls import path

from product.views import product_view, product_detail_view, category_list_api_view, category_detail_api_view, review_list_api_view, review_detail_api_view, review_product_view

urlpatterns = [
    path('products/', product_view),
    path('products/<int:id>/', product_detail_view),
    path('category/', category_list_api_view),
    path('category/<int:id>/', category_detail_api_view),
    path('review/', review_list_api_view),
    path('review/<int:id>/', review_detail_api_view),
    path('review/product/', review_product_view)
]
