from rest_framework.generics import ListAPIView
from restaurants.models import Restaurant
from .serializers import RestaurantsSerializer


class RestaurantListView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantsSerializer
	