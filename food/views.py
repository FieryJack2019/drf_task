from rest_framework.generics import ListAPIView
from .models import FoodCategory, Food
from .serializers import FoodListSerializer
from django.db.models import Prefetch, Count, Q


class FoodList(ListAPIView):
    model = FoodCategory
    serializer_class = FoodListSerializer

    def get_queryset(self):
        notEmptyCategory = FoodCategory.objects.all().annotate(max_foods=Count('food', filter=Q(food__is_publish=True))).filter(max_foods__gte=1)
        return notEmptyCategory.prefetch_related(Prefetch('food', queryset=Food.objects.filter(is_publish=True)))