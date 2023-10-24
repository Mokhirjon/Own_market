from django.urls import path
from .views import (Sold_outdeleteapieview,Sold_outdetailapieview,
                    Sold_outcreateapieview,Sold_outupdateapieview,Sold_outListapieview)

urlpatterns = [
    path('list',Sold_outListapieview.as_view()),
    path('update/<int:pk>/',Sold_outupdateapieview.as_view()),
    path('create/',Sold_outcreateapieview.as_view()),
    path('delete/<int:pk>/',Sold_outdeleteapieview.as_view()),
    path('details/<int:pk>/',Sold_outdetailapieview.as_view())
]