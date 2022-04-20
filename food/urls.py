from django.urls import path
from .views import FoodList


urlpatterns = [
    path('', view=FoodList.as_view(), name='foodList')
]