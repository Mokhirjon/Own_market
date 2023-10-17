from django.urls import path
from .views import (PantsDetailsAPiviews,PantsListAPiviews,PantsCreateAPiviews,
                    PantsDeleteAPiviews,PantsUpdateAPiviews)

urlpatterns = [
    path('Pants_list/',PantsListAPiviews.as_view()),
    path('Pants_create/',PantsCreateAPiviews.as_view()),
    path('Pants_update/<int:pk>/',PantsUpdateAPiviews.as_view()),
    path('Pants_delete/<int:pk>/',PantsDeleteAPiviews.as_view()),
    path('Pants_details/<int:pk>/',PantsDetailsAPiviews.as_view())

]