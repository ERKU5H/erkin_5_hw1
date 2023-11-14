from django.urls import path

from product.views import ProductView, ProductDetailView, CategoryView, CategoryDetailView, ReviewView, ReviewDetailView, ReviewProductView

urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/<int:id>/', ProductDetailView.as_view()),
    path('category/', CategoryView.as_view()),
    path('category/<int:id>/', CategoryDetailView.as_view()),
    path('review/', ReviewView.as_view()),
    path('review/<int:id>/', ReviewDetailView.as_view()),
    path('review/product/', ReviewProductView.as_view())
]
