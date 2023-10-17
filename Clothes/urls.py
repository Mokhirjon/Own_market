from django.urls import path
from .views import (ClothesDeleteAPiviews,ClothesListAPiviews,
                    ClothesCreateAPiviews,ClothesUpdateAPiviews,ClothesDetailsAPiviews)

urlpatterns = [
    path('Clothes_list/',ClothesListAPiviews.as_view()),
    path('Clothes_create/',ClothesCreateAPiviews.as_view()),
    path('Clothes_update/<int:pk>/',ClothesUpdateAPiviews.as_view()),
    path('Clothes_delete/<int:pk>/',ClothesDeleteAPiviews.as_view()),
    path('Clothes_details/<int:pk>/',ClothesDetailsAPiviews.as_view())

]