from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
from .serializers import *
from LisheApis.models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#REST FRAMEWORK
from rest_framework import status
from rest_framework.response import Response

#---------------------FUNCTION VIEW-------------------------
from rest_framework.decorators import api_view

#------------------------CLASS BASED VIEW-------------------
from rest_framework.views import APIView


#------------------------GENERIC VIEWs-------------------
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


#------------------------ VIEW SETS-------------------
from rest_framework.viewsets import ModelViewSet


#------FILTERS, SEARCH AND ORDERING
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter,OrderingFilter

#------PAGINATION-------------
from rest_framework.pagination import PageNumberPagination




#----------------CREATING A CART------------------------
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet


from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser



# ALL LISHE OPTIONS APIS

class LisheViewSet(ModelViewSet):
	queryset = Lishe.objects.all()
	serializer_class = LisheSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['ItemName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination





# ALL ELIMU YA LISHE OPTIONS APIS

class ElimuYaLisheViewSet(ModelViewSet):
	queryset = ElimuYaLishe.objects.all()
	serializer_class = ElimuYaLisheSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['Category']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination





# ALL BIDHAA ZETU OPTIONS APIS

class BidhaaZetuViewSet(ModelViewSet):
	queryset = BidhaaZetu.objects.all()
	serializer_class = BidhaaZetuSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['ProductName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination


class MakundiYaChakulaViewSet(ModelViewSet):
	queryset = MakundiYaChakula.objects.all()
	serializer_class = MakundiYaChakulaSerializer
	
class PosterNaPichaViewSet(ModelViewSet):
	queryset = PosterNaPicha.objects.all()
	serializer_class = PosterNaPichaSerializer
	


#  DAYS OPTIONS APIS

class DaysViewSet(ModelViewSet):
	queryset = Days.objects.all()
	serializer_class = DaysSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination









# MWANZO WA WATOTO DAYS

#  WATOTO DAY ONE

class WatotoDayOneViewSet(ModelViewSet):
	queryset = DayOne.objects.filter(Category__ItemName__icontains="WATOTO", DayName__icontains="Day one")
	serializer_class = DayOneSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination





#  WATOTO DAY TWO

class WatotoDayTwoViewSet(ModelViewSet):
	queryset = DayTwo.objects.filter(Category__ItemName__icontains="WATOTO", DayName__icontains="Day two")
	serializer_class = DayTwoSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination



#  WATOTO DAY Three

class WatotoDayThreeViewSet(ModelViewSet):
	queryset = DayThree.objects.filter(Category__ItemName__icontains="WATOTO", DayName__icontains="Day three")
	serializer_class = DayThreeSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination



#  WATOTO DAY Four

class WatotoDayFourViewSet(ModelViewSet):
	queryset = DayFour.objects.filter(Category__ItemName__icontains="WATOTO", DayName__icontains="Day four")
	serializer_class = DayFourSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination



#  WATOTO DAY Five

class WatotoDayFiveViewSet(ModelViewSet):
	queryset = DayFive.objects.filter(Category__ItemName__icontains="WATOTO", DayName__icontains="Day five")
	serializer_class = DayFiveSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination




#  WATOTO DAY SIX

class WatotoDaySixViewSet(ModelViewSet):
	queryset = DaySix.objects.filter(Category__ItemName__icontains="WATOTO", DayName__icontains="Day six")
	serializer_class = DaySixSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination




#  WATOTO DAY Seven

class WatotoDaySevenViewSet(ModelViewSet):
	queryset = DaySeven.objects.filter(Category__ItemName__icontains="WATOTO", DayName__icontains="Day seven")
	serializer_class = DaySevenSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination






# MWISHO WA WATOTO DAYS















# KISUKARI DAYS


#  KISUKARI DAY ONE

class KisukariDayOneViewSet(ModelViewSet):
	queryset = DayOne.objects.filter(Category__ItemName__icontains="KISUKARI", DayName__icontains="Day one")
	serializer_class = DayOneSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination




#  KISUKARI DAY TWO

class KisukariDayTwoViewSet(ModelViewSet):
	queryset = DayTwo.objects.filter(Category__ItemName__icontains="KISUKARI", DayName__icontains="Day two")
	serializer_class = DayTwoSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination



#  KISUKARI DAY Three

class KisukariDayThreeViewSet(ModelViewSet):
	queryset = DayThree.objects.filter(Category__ItemName__icontains="KISUKARI", DayName__icontains="Day three")
	serializer_class = DayThreeSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination



#  KISUKARI DAY Four

class KisukariDayFourViewSet(ModelViewSet):
	queryset = DayFour.objects.filter(Category__ItemName__icontains="KISUKARI", DayName__icontains="Day four")
	serializer_class = DayFourSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination



#  KISUKARI DAY Five

class KisukariDayFiveViewSet(ModelViewSet):
	queryset = DayFive.objects.filter(Category__ItemName__icontains="KISUKARI", DayName__icontains="Day five")
	serializer_class = DayFiveSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination




#  KISUKARI DAY SIX

class KisukariDaySixViewSet(ModelViewSet):
	queryset = DaySix.objects.filter(Category__ItemName__icontains="KISUKARI", DayName__icontains="Day six")
	serializer_class = DaySixSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination




#  KISUKARI DAY Seven

class KisukariDaySevenViewSet(ModelViewSet):
	queryset = DaySeven.objects.filter(Category__ItemName__icontains="KISUKARI", DayName__icontains="Day seven")
	serializer_class = DaySevenSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination

# MWISHO WA KISUKARI DAYS













# FAMILIA DAYS


#  FAMILIA DAY ONE

class FamiliaDayOneViewSet(ModelViewSet):
	queryset = DayOne.objects.filter(Category__ItemName__icontains="FAMILIA", DayName__icontains="Day one")
	serializer_class = DayOneSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination




#  FAMILIA DAY TWO

class FamiliaDayTwoViewSet(ModelViewSet):
	queryset = DayTwo.objects.filter(Category__ItemName__icontains="FAMILIA", DayName__icontains="Day two")
	serializer_class = DayTwoSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination



#  FAMILIA DAY Three

class FamiliaDayThreeViewSet(ModelViewSet):
	queryset = DayThree.objects.filter(Category__ItemName__icontains="FAMILIA", DayName__icontains="Day three")
	serializer_class = DayThreeSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination



#  FAMILIA DAY Four

class FamiliaDayFourViewSet(ModelViewSet):
	queryset = DayFour.objects.filter(Category__ItemName__icontains="FAMILIA", DayName__icontains="Day four")
	serializer_class = DayFourSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination



#  FAMILIA DAY Five

class FamiliaDayFiveViewSet(ModelViewSet):
	queryset = DayFive.objects.filter(Category__ItemName__icontains="FAMILIA", DayName__icontains="Day five")
	serializer_class = DayFiveSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination




#  FAMILIA DAY SIX

class FamiliaDaySixViewSet(ModelViewSet):
	queryset = DaySix.objects.filter(Category__ItemName__icontains="FAMILIA", DayName__icontains="Day six")
	serializer_class = DaySixSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination




#  FAMILIA DAY Seven

class FamiliaDaySevenViewSet(ModelViewSet):
	queryset = DaySeven.objects.filter(Category__ItemName__icontains="FAMILIA", DayName__icontains="Day seven")
	serializer_class = DaySevenSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination

# MWISHO WA FAMILIA DAYS













# HIV DAYS


#  HIV DAY ONE

class HivDayOneViewSet(ModelViewSet):
	queryset = DayOne.objects.filter(Category__ItemName__icontains="HIV", DayName__icontains="Day one")
	serializer_class = DayOneSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination




#  HIV DAY TWO

class HivDayTwoViewSet(ModelViewSet):
	queryset = DayTwo.objects.filter(Category__ItemName__icontains="HIV", DayName__icontains="Day two")
	serializer_class = DayTwoSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination



#  HIV DAY Three

class HivDayThreeViewSet(ModelViewSet):
	queryset = DayThree.objects.filter(Category__ItemName__icontains="HIV", DayName__icontains="Day three")
	serializer_class = DayThreeSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination



#  HIV DAY Four

class HivDayFourViewSet(ModelViewSet):
	queryset = DayFour.objects.filter(Category__ItemName__icontains="HIV", DayName__icontains="Day four")
	serializer_class = DayFourSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination



#  HIV DAY Five

class HivDayFiveViewSet(ModelViewSet):
	queryset = DayFive.objects.filter(Category__ItemName__icontains="HIV", DayName__icontains="Day five")
	serializer_class = DayFiveSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination




#  HIV DAY SIX

class HivDaySixViewSet(ModelViewSet):
	queryset = DaySix.objects.filter(Category__ItemName__icontains="HIV", DayName__icontains="Day six")
	serializer_class = DaySixSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination




#  HIV DAY Seven

class HivDaySevenViewSet(ModelViewSet):
	queryset = DaySeven.objects.filter(Category__ItemName__icontains="HIV", DayName__icontains="Day seven")
	serializer_class = DaySevenSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination


# MWISHO WA HIV DAYS













# WAJAWAZITO DAYS


#  WAJAWAZITO DAY ONE

class WajawazitoDayOneViewSet(ModelViewSet):
	queryset = DayOne.objects.filter(Category__ItemName__icontains="WAJAWAZITO", DayName__icontains="Day one")
	serializer_class = DayOneSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination




#  WAJAWAZITO DAY TWO

class WajawazitoDayTwoViewSet(ModelViewSet):
	queryset = DayTwo.objects.filter(Category__ItemName__icontains="WAJAWAZITO", DayName__icontains="Day two")
	serializer_class = DayTwoSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination



#  WAJAWAZITO DAY Three

class WajawazitoDayThreeViewSet(ModelViewSet):
	queryset = DayThree.objects.filter(Category__ItemName__icontains="WAJAWAZITO", DayName__icontains="Day three")
	serializer_class = DayThreeSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination



#  WAJAWAZITO DAY Four

class WajawazitoDayFourViewSet(ModelViewSet):
	queryset = DayFour.objects.filter(Category__ItemName__icontains="WAJAWAZITO", DayName__icontains="Day four")
	serializer_class = DayFourSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination



#  WAJAWAZITO DAY Five

class WajawazitoDayFiveViewSet(ModelViewSet):
	queryset = DayFive.objects.filter(Category__ItemName__icontains="WAJAWAZITO", DayName__icontains="Day five")
	serializer_class = DayFiveSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination




#  WAJAWAZITO DAY SIX

class WajawazitoDaySixViewSet(ModelViewSet):
	queryset = DaySix.objects.filter(Category__ItemName__icontains="WAJAWAZITO", DayName__icontains="Day six")
	serializer_class = DaySixSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination




#  WAJAWAZITO DAY Seven

class WajawazitoDaySevenViewSet(ModelViewSet):
	queryset = DaySeven.objects.filter(Category__ItemName__icontains="WAJAWAZITO", DayName__icontains="Day seven")
	serializer_class = DaySevenSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination


# MWISHO WA WAJAWAZITO DAYS










# UZITO ZAIDI DAYS


#  UZITO ZAIDI DAY ONE

class UzitoZaidiDayOneViewSet(ModelViewSet):
	queryset = DayOne.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", DayName__icontains="Day one")
	serializer_class = DayOneSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination




#  UZITO ZAIDI DAY TWO

class UzitoZaidiDayTwoViewSet(ModelViewSet):
	queryset = DayTwo.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", DayName__icontains="Day two")
	serializer_class = DayTwoSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination



#  UZITO ZAIDI DAY Three

class UzitoZaidiDayThreeViewSet(ModelViewSet):
	queryset = DayThree.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", DayName__icontains="Day three")
	serializer_class = DayThreeSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination



#  UZITO ZAIDI DAY Four

class UzitoZaidiDayFourViewSet(ModelViewSet):
	queryset = DayFour.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", DayName__icontains="Day four")
	serializer_class = DayFourSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination



#  UZITO ZAIDI DAY Five

class UzitoZaidiDayFiveViewSet(ModelViewSet):
	queryset = DayFive.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", DayName__icontains="Day five")
	serializer_class = DayFiveSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination




#  UZITO ZAIDI DAY SIX

class UzitoZaidiDaySixViewSet(ModelViewSet):
	queryset = DaySix.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", DayName__icontains="Day six")
	serializer_class = DaySixSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination




#  UZITO ZAIDI DAY Seven

class UzitoZaidiDaySevenViewSet(ModelViewSet):
	queryset = DaySeven.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", DayName__icontains="Day seven")
	serializer_class = DaySevenSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['DayName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination


# MWISHO WA UZITO ZAIDI DAYS