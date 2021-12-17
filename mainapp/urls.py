from django.urls import path
from rest_framework import routers

from mainapp import views

urlpatterns = [
    path('category-list/', views.BookCategoryListView.as_view()),
    path('category-create/', views.BookCategoryCreateView.as_view()),
    path('category-list-create/', views.BookCategoryListCreateView.as_view()),
    path('category-retrieve/<int:pk>', views. BookCategoryRetrieveView.as_view()),
    path('category-update/<int:pk>', views.BookCategoryUpdetaView.as_view()),
    path('category-retrieve-update/<int:pk>', views.BookCategoryUpdetaRetrieveView.as_view()),
    path('category-destroy/<int:pk>', views.BookCategoryDestroyView.as_view())
]
