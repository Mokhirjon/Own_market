from django.urls import path
from .views import (ShoesListAPiviews,ShoesCreateAPiviews,ShoesDeleteAPiviews,ShoesUpdateAPiviews,
                    ShoesDetailsAPiviews,Shopping_centerListCreateAPiviews)

urlpatterns = [
    path('shopping_center_list/', Shopping_centerListCreateAPiviews.as_view()),
    path('shoes_list/',ShoesListAPiviews.as_view()),
    path('shoes_create/',ShoesCreateAPiviews.as_view()),
    path('shoes_update/<int:pk>/',ShoesUpdateAPiviews.as_view()),
    path('shoes_delete/<int:pk>/',ShoesDeleteAPiviews.as_view()),
    path('shoes_details/<int:pk>/',ShoesDetailsAPiviews.as_view())

]