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




class WeeksViewSet(ModelViewSet):
	queryset = Weeks.objects.all()
	serializer_class = WeeksSerializer



# ------------------------TAARIFA ZA UJAUZITO WEEK ZOTE----------

class TaarifaZaUjauzitoWeek1ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 1")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek2ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 2")
	serializer_class = TaarifaZaUjauzitoSerializer
	
class TaarifaZaUjauzitoWeek3ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 3")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek4ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 4")
	serializer_class = TaarifaZaUjauzitoSerializer


class TaarifaZaUjauzitoWeek5ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 5")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek6ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 6")
	serializer_class = TaarifaZaUjauzitoSerializer


class TaarifaZaUjauzitoWeek7ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 7")
	serializer_class = TaarifaZaUjauzitoSerializer


class TaarifaZaUjauzitoWeek8ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 8")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek9ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 9")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek10ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 10")
	serializer_class = TaarifaZaUjauzitoSerializer


class TaarifaZaUjauzitoWeek11ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 11")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek12ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 12")
	serializer_class = TaarifaZaUjauzitoSerializer
	
class TaarifaZaUjauzitoWeek13ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 13")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek14ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 14")
	serializer_class = TaarifaZaUjauzitoSerializer


class TaarifaZaUjauzitoWeek15ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 15")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek16ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 16")
	serializer_class = TaarifaZaUjauzitoSerializer


class TaarifaZaUjauzitoWeek17ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 17")
	serializer_class = TaarifaZaUjauzitoSerializer


class TaarifaZaUjauzitoWeek18ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 18")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek19ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 19")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek20ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 20")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek21ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 21")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek22ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 22")
	serializer_class = TaarifaZaUjauzitoSerializer
	
class TaarifaZaUjauzitoWeek23ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 23")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek24ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 24")
	serializer_class = TaarifaZaUjauzitoSerializer


class TaarifaZaUjauzitoWeek25ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 25")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek26ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 26")
	serializer_class = TaarifaZaUjauzitoSerializer


class TaarifaZaUjauzitoWeek27ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 27")
	serializer_class = TaarifaZaUjauzitoSerializer


class TaarifaZaUjauzitoWeek28ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 28")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek29ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 29")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek30ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 30")
	serializer_class = TaarifaZaUjauzitoSerializer


class TaarifaZaUjauzitoWeek31ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 31")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek32ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 32")
	serializer_class = TaarifaZaUjauzitoSerializer
	
class TaarifaZaUjauzitoWeek33ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 33")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek34ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 34")
	serializer_class = TaarifaZaUjauzitoSerializer


class TaarifaZaUjauzitoWeek35ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 35")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek36ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 36")
	serializer_class = TaarifaZaUjauzitoSerializer


class TaarifaZaUjauzitoWeek37ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 37")
	serializer_class = TaarifaZaUjauzitoSerializer


class TaarifaZaUjauzitoWeek38ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 38")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek39ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 39")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek40ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 40")
	serializer_class = TaarifaZaUjauzitoSerializer


class TaarifaZaUjauzitoWeek41ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 41")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek42ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 42")
	serializer_class = TaarifaZaUjauzitoSerializer
	
class TaarifaZaUjauzitoWeek43ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 43")
	serializer_class = TaarifaZaUjauzitoSerializer

class TaarifaZaUjauzitoWeek44ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 44")
	serializer_class = TaarifaZaUjauzitoSerializer


class TaarifaZaUjauzitoWeek45ViewSet(ModelViewSet):
	queryset = TaarifaZaUjauzito.objects.filter(Week__WeekName__icontains="Wiki 45")
	serializer_class = TaarifaZaUjauzitoSerializer












# ------------------------JE WAJUA  KWA WAJAWAZITO KWA WEEK ZOTE----------

class JeWajuaWajawazitoWeek1ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 1")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek2ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 2")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek3ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 3")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek4ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 4")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek5ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 5")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek6ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 6")
	serializer_class = JeWajuaSerializer


class JeWajuaWajawazitoWeek7ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 7")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek8ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 8")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek9ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 9")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek10ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 10")
	serializer_class = JeWajuaSerializer


class JeWajuaWajawazitoWeek11ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 11")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek12ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 12")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek13ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 13")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek14ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 14")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek15ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 15")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek16ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 16")
	serializer_class = JeWajuaSerializer


class JeWajuaWajawazitoWeek17ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 17")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek18ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 18")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek19ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 19")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek20ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 20")
	serializer_class = JeWajuaSerializer


class JeWajuaWajawazitoWeek21ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 21")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek22ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 22")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek23ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 23")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek24ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 24")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek25ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 25")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek26ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 26")
	serializer_class = JeWajuaSerializer


class JeWajuaWajawazitoWeek27ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 27")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek28ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 28")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek29ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 29")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek30ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 30")
	serializer_class = JeWajuaSerializer


class JeWajuaWajawazitoWeek31ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 31")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek32ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 32")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek33ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 33")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek34ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 34")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek35ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 35")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek36ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 36")
	serializer_class = JeWajuaSerializer


class JeWajuaWajawazitoWeek37ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 37")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek38ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 38")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek39ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 39")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek40ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 40")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek41ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 41")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek42ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 42")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek43ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 43")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek44ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 44")
	serializer_class = JeWajuaSerializer

class JeWajuaWajawazitoWeek45ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WAJAWAZITO", Week__WeekName__icontains="Wiki 45")
	serializer_class = JeWajuaSerializer













# ------------------------WEEK ZOTE  KWA WAJAWAZITO ----------

class WajawazitoWeek1ViewSet(ModelViewSet):
	queryset = Week1.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 1")
	serializer_class = Week1Serializer

class WajawazitoWeek2ViewSet(ModelViewSet):
	queryset = Week2.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 2")
	serializer_class = Week2Serializer

class WajawazitoWeek3ViewSet(ModelViewSet):
	queryset = Week3.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 3")
	serializer_class = Week3Serializer

class WajawazitoWeek4ViewSet(ModelViewSet):
	queryset = Week4.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 4")
	serializer_class = Week4Serializer

class WajawazitoWeek5ViewSet(ModelViewSet):
	queryset = Week5.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 5")
	serializer_class = Week5Serializer

class WajawazitoWeek6ViewSet(ModelViewSet):
	queryset = Week6.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 6")
	serializer_class = Week6Serializer

class WajawazitoWeek7ViewSet(ModelViewSet):
	queryset = Week7.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 7")
	serializer_class = Week7Serializer

class WajawazitoWeek8ViewSet(ModelViewSet):
	queryset = Week8.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 8")
	serializer_class = Week8Serializer

class WajawazitoWeek9ViewSet(ModelViewSet):
	queryset = Week9.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 9")
	serializer_class = Week9Serializer


class WajawazitoWeek10ViewSet(ModelViewSet):
	queryset = Week10.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 10")
	serializer_class = Week10Serializer


class WajawazitoWeek11ViewSet(ModelViewSet):
	queryset = Week11.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 11")
	serializer_class = Week11Serializer

class WajawazitoWeek12ViewSet(ModelViewSet):
	queryset = Week12.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 12")
	serializer_class = Week12Serializer

class WajawazitoWeek13ViewSet(ModelViewSet):
	queryset = Week13.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 13")
	serializer_class = Week13Serializer

class WajawazitoWeek14ViewSet(ModelViewSet):
	queryset = Week14.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 14")
	serializer_class = Week14Serializer

class WajawazitoWeek15ViewSet(ModelViewSet):
	queryset = Week15.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 15")
	serializer_class = Week15Serializer

class WajawazitoWeek16ViewSet(ModelViewSet):
	queryset = Week16.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 16")
	serializer_class = Week16Serializer

class WajawazitoWeek17ViewSet(ModelViewSet):
	queryset = Week17.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 17")
	serializer_class = Week17Serializer

class WajawazitoWeek18ViewSet(ModelViewSet):
	queryset = Week18.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 18")
	serializer_class = Week18Serializer

class WajawazitoWeek19ViewSet(ModelViewSet):
	queryset = Week19.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 19")
	serializer_class = Week19Serializer

class WajawazitoWeek20ViewSet(ModelViewSet):
	queryset = Week20.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 20")
	serializer_class = Week20Serializer

class WajawazitoWeek21ViewSet(ModelViewSet):
	queryset = Week21.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 21")
	serializer_class = Week21Serializer

class WajawazitoWeek22ViewSet(ModelViewSet):
	queryset = Week22.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 22")
	serializer_class = Week22Serializer

class WajawazitoWeek23ViewSet(ModelViewSet):
	queryset = Week23.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 23")
	serializer_class = Week23Serializer


class WajawazitoWeek24ViewSet(ModelViewSet):
	queryset = Week24.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 24")
	serializer_class = Week24Serializer


class WajawazitoWeek25ViewSet(ModelViewSet):
	queryset = Week25.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 25")
	serializer_class = Week25Serializer

class WajawazitoWeek26ViewSet(ModelViewSet):
	queryset = Week26.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 26")
	serializer_class = Week26Serializer

class WajawazitoWeek27ViewSet(ModelViewSet):
	queryset = Week27.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 27")
	serializer_class = Week27Serializer

class WajawazitoWeek28ViewSet(ModelViewSet):
	queryset = Week28.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 28")
	serializer_class = Week28Serializer

class WajawazitoWeek29ViewSet(ModelViewSet):
	queryset = Week29.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 29")
	serializer_class = Week29Serializer

class WajawazitoWeek30ViewSet(ModelViewSet):
	queryset = Week30.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 30")
	serializer_class = Week30Serializer

class WajawazitoWeek31ViewSet(ModelViewSet):
	queryset = Week31.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 31")
	serializer_class = Week31Serializer


class WajawazitoWeek32ViewSet(ModelViewSet):
	queryset = Week32.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 32")
	serializer_class = Week32Serializer

class WajawazitoWeek33ViewSet(ModelViewSet):
	queryset = Week33.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 33")
	serializer_class = Week33Serializer

class WajawazitoWeek34ViewSet(ModelViewSet):
	queryset = Week34.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 34")
	serializer_class = Week34Serializer

class WajawazitoWeek35ViewSet(ModelViewSet):
	queryset = Week35.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 35")
	serializer_class = Week35Serializer

class WajawazitoWeek36ViewSet(ModelViewSet):
	queryset = Week36.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 36")
	serializer_class = Week36Serializer


class WajawazitoWeek37ViewSet(ModelViewSet):
	queryset = Week37.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 37")
	serializer_class = Week37Serializer

class WajawazitoWeek38ViewSet(ModelViewSet):
	queryset = Week38.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 38")
	serializer_class = Week38Serializer

class WajawazitoWeek39ViewSet(ModelViewSet):
	queryset = Week39.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 39")
	serializer_class = Week39Serializer


class WajawazitoWeek40ViewSet(ModelViewSet):
	queryset = Week40.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 40")
	serializer_class = Week40Serializer

class WajawazitoWeek41ViewSet(ModelViewSet):
	queryset = Week41.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 41")
	serializer_class = Week41Serializer


class WajawazitoWeek42ViewSet(ModelViewSet):
	queryset = Week42.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 42")
	serializer_class = Week42Serializer


class WajawazitoWeek43ViewSet(ModelViewSet):
	queryset = Week43.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 43")
	serializer_class = Week43Serializer

class WajawazitoWeek44ViewSet(ModelViewSet):
	queryset = Week44.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 44")
	serializer_class = Week44Serializer

class WajawazitoWeek45ViewSet(ModelViewSet):
	queryset = Week45.objects.filter(Category__ItemName__icontains="WAJAWAZITO", WeekName__icontains="Wiki 45")
	serializer_class = Week45Serializer

















	#---------------------UZITO ZAIDI------------------------------


# ------------------------TAARIFA ZA UZITO ZAIDI WEEK ZOTE----------

class TaarifaZaUzitoZaidiWeek1ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 1")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek2ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 2")
	serializer_class = TaarifaZaUzitoZaidiSerializer
	
class TaarifaZaUzitoZaidiWeek3ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 3")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek4ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 4")
	serializer_class = TaarifaZaUzitoZaidiSerializer


class TaarifaZaUzitoZaidiWeek5ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 5")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek6ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 6")
	serializer_class = TaarifaZaUzitoZaidiSerializer


class TaarifaZaUzitoZaidiWeek7ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 7")
	serializer_class = TaarifaZaUzitoZaidiSerializer


class TaarifaZaUzitoZaidiWeek8ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 8")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek9ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 9")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek10ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 10")
	serializer_class = TaarifaZaUzitoZaidiSerializer


class TaarifaZaUzitoZaidiWeek11ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 11")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek12ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 12")
	serializer_class = TaarifaZaUzitoZaidiSerializer
	
class TaarifaZaUzitoZaidiWeek13ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 13")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek14ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 14")
	serializer_class = TaarifaZaUzitoZaidiSerializer


class TaarifaZaUzitoZaidiWeek15ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 15")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek16ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 16")
	serializer_class = TaarifaZaUzitoZaidiSerializer


class TaarifaZaUzitoZaidiWeek17ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 17")
	serializer_class = TaarifaZaUzitoZaidiSerializer


class TaarifaZaUzitoZaidiWeek18ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 18")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek19ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 19")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek20ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 20")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek21ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 21")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek22ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 22")
	serializer_class = TaarifaZaUzitoZaidiSerializer
	
class TaarifaZaUzitoZaidiWeek23ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 23")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek24ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 24")
	serializer_class = TaarifaZaUzitoZaidiSerializer


class TaarifaZaUzitoZaidiWeek25ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 25")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek26ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 26")
	serializer_class = TaarifaZaUzitoZaidiSerializer


class TaarifaZaUzitoZaidiWeek27ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 27")
	serializer_class = TaarifaZaUzitoZaidiSerializer


class TaarifaZaUzitoZaidiWeek28ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 28")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek29ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 29")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek30ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 30")
	serializer_class = TaarifaZaUzitoZaidiSerializer


class TaarifaZaUzitoZaidiWeek31ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 31")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek32ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 32")
	serializer_class = TaarifaZaUzitoZaidiSerializer
	
class TaarifaZaUzitoZaidiWeek33ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 33")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek34ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 34")
	serializer_class = TaarifaZaUzitoZaidiSerializer


class TaarifaZaUzitoZaidiWeek35ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 35")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek36ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 36")
	serializer_class = TaarifaZaUzitoZaidiSerializer


class TaarifaZaUzitoZaidiWeek37ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 37")
	serializer_class = TaarifaZaUzitoZaidiSerializer


class TaarifaZaUzitoZaidiWeek38ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 38")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek39ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 39")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek40ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 40")
	serializer_class = TaarifaZaUzitoZaidiSerializer


class TaarifaZaUzitoZaidiWeek41ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 41")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek42ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 42")
	serializer_class = TaarifaZaUzitoZaidiSerializer
	
class TaarifaZaUzitoZaidiWeek43ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 43")
	serializer_class = TaarifaZaUzitoZaidiSerializer

class TaarifaZaUzitoZaidiWeek44ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 44")
	serializer_class = TaarifaZaUzitoZaidiSerializer


class TaarifaZaUzitoZaidiWeek45ViewSet(ModelViewSet):
	queryset = TaarifaZaUzitoZaidi.objects.filter(Week__WeekName__icontains="Wiki 45")
	serializer_class = TaarifaZaUzitoZaidiSerializer










# ------------------------JE WAJUA  KWA UZITO ZAIDI KWA WEEK ZOTE----------

class JeWajuaUzitoZaidiWeek1ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 1")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek2ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 2")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek3ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 3")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek4ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 4")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek5ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 5")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek6ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 6")
	serializer_class = JeWajuaSerializer


class JeWajuaUzitoZaidiWeek7ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 7")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek8ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 8")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek9ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 9")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek10ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 10")
	serializer_class = JeWajuaSerializer


class JeWajuaUzitoZaidiWeek11ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 11")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek12ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 12")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek13ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 13")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek14ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 14")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek15ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 15")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek16ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 16")
	serializer_class = JeWajuaSerializer


class JeWajuaUzitoZaidiWeek17ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 17")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek18ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 18")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek19ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 19")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek20ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 20")
	serializer_class = JeWajuaSerializer


class JeWajuaUzitoZaidiWeek21ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 21")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek22ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 22")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek23ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 23")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek24ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 24")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek25ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 25")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek26ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 26")
	serializer_class = JeWajuaSerializer


class JeWajuaUzitoZaidiWeek27ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 27")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek28ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 28")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek29ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 29")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek30ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 30")
	serializer_class = JeWajuaSerializer


class JeWajuaUzitoZaidiWeek31ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 31")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek32ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 32")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek33ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 33")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek34ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 34")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek35ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 35")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek36ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 36")
	serializer_class = JeWajuaSerializer


class JeWajuaUzitoZaidiWeek37ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 37")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek38ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 38")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek39ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 39")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek40ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 40")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek41ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 41")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek42ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 42")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek43ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 43")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek44ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 44")
	serializer_class = JeWajuaSerializer

class JeWajuaUzitoZaidiWeek45ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", Week__WeekName__icontains="Wiki 45")
	serializer_class = JeWajuaSerializer








# ------------------------WEEK ZOTE  KWA UZITO ZAIDI ----------

class UzitoZaidiWeek1ViewSet(ModelViewSet):
	queryset = Week1.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 1")
	serializer_class = Week1Serializer

class UzitoZaidiWeek2ViewSet(ModelViewSet):
	queryset = Week2.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 2")
	serializer_class = Week2Serializer

class UzitoZaidiWeek3ViewSet(ModelViewSet):
	queryset = Week3.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 3")
	serializer_class = Week3Serializer

class UzitoZaidiWeek4ViewSet(ModelViewSet):
	queryset = Week4.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 4")
	serializer_class = Week4Serializer

class UzitoZaidiWeek5ViewSet(ModelViewSet):
	queryset = Week5.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 5")
	serializer_class = Week5Serializer

class UzitoZaidiWeek6ViewSet(ModelViewSet):
	queryset = Week6.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 6")
	serializer_class = Week6Serializer

class UzitoZaidiWeek7ViewSet(ModelViewSet):
	queryset = Week7.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 7")
	serializer_class = Week7Serializer

class UzitoZaidiWeek8ViewSet(ModelViewSet):
	queryset = Week8.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 8")
	serializer_class = Week8Serializer

class UzitoZaidiWeek9ViewSet(ModelViewSet):
	queryset = Week9.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 9")
	serializer_class = Week9Serializer


class UzitoZaidiWeek10ViewSet(ModelViewSet):
	queryset = Week10.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 10")
	serializer_class = Week10Serializer


class UzitoZaidiWeek11ViewSet(ModelViewSet):
	queryset = Week11.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 11")
	serializer_class = Week11Serializer

class UzitoZaidiWeek12ViewSet(ModelViewSet):
	queryset = Week12.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 12")
	serializer_class = Week12Serializer

class UzitoZaidiWeek13ViewSet(ModelViewSet):
	queryset = Week13.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 13")
	serializer_class = Week13Serializer

class UzitoZaidiWeek14ViewSet(ModelViewSet):
	queryset = Week14.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 14")
	serializer_class = Week14Serializer

class UzitoZaidiWeek15ViewSet(ModelViewSet):
	queryset = Week15.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 15")
	serializer_class = Week15Serializer

class UzitoZaidiWeek16ViewSet(ModelViewSet):
	queryset = Week16.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 16")
	serializer_class = Week16Serializer

class UzitoZaidiWeek17ViewSet(ModelViewSet):
	queryset = Week17.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 17")
	serializer_class = Week17Serializer

class UzitoZaidiWeek18ViewSet(ModelViewSet):
	queryset = Week18.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 18")
	serializer_class = Week18Serializer

class UzitoZaidiWeek19ViewSet(ModelViewSet):
	queryset = Week19.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 19")
	serializer_class = Week19Serializer

class UzitoZaidiWeek20ViewSet(ModelViewSet):
	queryset = Week20.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 20")
	serializer_class = Week20Serializer

class UzitoZaidiWeek21ViewSet(ModelViewSet):
	queryset = Week21.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 21")
	serializer_class = Week21Serializer

class UzitoZaidiWeek22ViewSet(ModelViewSet):
	queryset = Week22.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 22")
	serializer_class = Week22Serializer

class UzitoZaidiWeek23ViewSet(ModelViewSet):
	queryset = Week23.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 23")
	serializer_class = Week23Serializer


class UzitoZaidiWeek24ViewSet(ModelViewSet):
	queryset = Week24.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 24")
	serializer_class = Week24Serializer


class UzitoZaidiWeek25ViewSet(ModelViewSet):
	queryset = Week25.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 25")
	serializer_class = Week25Serializer

class UzitoZaidiWeek26ViewSet(ModelViewSet):
	queryset = Week26.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 26")
	serializer_class = Week26Serializer

class UzitoZaidiWeek27ViewSet(ModelViewSet):
	queryset = Week27.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 27")
	serializer_class = Week27Serializer

class UzitoZaidiWeek28ViewSet(ModelViewSet):
	queryset = Week28.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 28")
	serializer_class = Week28Serializer

class UzitoZaidiWeek29ViewSet(ModelViewSet):
	queryset = Week29.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 29")
	serializer_class = Week29Serializer

class UzitoZaidiWeek30ViewSet(ModelViewSet):
	queryset = Week30.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 30")
	serializer_class = Week30Serializer

class UzitoZaidiWeek31ViewSet(ModelViewSet):
	queryset = Week31.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 31")
	serializer_class = Week31Serializer


class UzitoZaidiWeek32ViewSet(ModelViewSet):
	queryset = Week32.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 32")
	serializer_class = Week32Serializer

class UzitoZaidiWeek33ViewSet(ModelViewSet):
	queryset = Week33.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 33")
	serializer_class = Week33Serializer

class UzitoZaidiWeek34ViewSet(ModelViewSet):
	queryset = Week34.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 34")
	serializer_class = Week34Serializer

class UzitoZaidiWeek35ViewSet(ModelViewSet):
	queryset = Week35.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 35")
	serializer_class = Week35Serializer

class UzitoZaidiWeek36ViewSet(ModelViewSet):
	queryset = Week36.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 36")
	serializer_class = Week36Serializer


class UzitoZaidiWeek37ViewSet(ModelViewSet):
	queryset = Week37.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 37")
	serializer_class = Week37Serializer

class UzitoZaidiWeek38ViewSet(ModelViewSet):
	queryset = Week38.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 38")
	serializer_class = Week38Serializer

class UzitoZaidiWeek39ViewSet(ModelViewSet):
	queryset = Week39.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 39")
	serializer_class = Week39Serializer


class UzitoZaidiWeek40ViewSet(ModelViewSet):
	queryset = Week40.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 40")
	serializer_class = Week40Serializer

class UzitoZaidiWeek41ViewSet(ModelViewSet):
	queryset = Week41.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 41")
	serializer_class = Week41Serializer


class UzitoZaidiWeek42ViewSet(ModelViewSet):
	queryset = Week42.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 42")
	serializer_class = Week42Serializer


class UzitoZaidiWeek43ViewSet(ModelViewSet):
	queryset = Week43.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 43")
	serializer_class = Week43Serializer

class UzitoZaidiWeek44ViewSet(ModelViewSet):
	queryset = Week44.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 44")
	serializer_class = Week44Serializer

class UzitoZaidiWeek45ViewSet(ModelViewSet):
	queryset = Week45.objects.filter(Category__ItemName__icontains="UZITO ZAIDI", WeekName__icontains="Wiki 45")
	serializer_class = Week45Serializer




























#---------------------WATOTO------------------------------


# ------------------------TAARIFA ZA WATOTO WEEK ZOTE----------

class TaarifaZaWatotoWeek1ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 1")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek2ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 2")
	serializer_class = TaarifaZaWatotoSerializer
	
class TaarifaZaWatotoWeek3ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 3")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek4ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 4")
	serializer_class = TaarifaZaWatotoSerializer


class TaarifaZaWatotoWeek5ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 5")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek6ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 6")
	serializer_class = TaarifaZaWatotoSerializer


class TaarifaZaWatotoWeek7ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 7")
	serializer_class = TaarifaZaWatotoSerializer


class TaarifaZaWatotoWeek8ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 8")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek9ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 9")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek10ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 10")
	serializer_class = TaarifaZaWatotoSerializer


class TaarifaZaWatotoWeek11ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 11")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek12ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 12")
	serializer_class = TaarifaZaWatotoSerializer
	
class TaarifaZaWatotoWeek13ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 13")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek14ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 14")
	serializer_class = TaarifaZaWatotoSerializer


class TaarifaZaWatotoWeek15ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 15")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek16ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 16")
	serializer_class = TaarifaZaWatotoSerializer


class TaarifaZaWatotoWeek17ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 17")
	serializer_class = TaarifaZaWatotoSerializer


class TaarifaZaWatotoWeek18ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 18")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek19ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 19")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek20ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 20")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek21ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 21")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek22ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 22")
	serializer_class = TaarifaZaWatotoSerializer
	
class TaarifaZaWatotoWeek23ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 23")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek24ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 24")
	serializer_class = TaarifaZaWatotoSerializer


class TaarifaZaWatotoWeek25ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 25")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek26ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 26")
	serializer_class = TaarifaZaWatotoSerializer


class TaarifaZaWatotoWeek27ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 27")
	serializer_class = TaarifaZaWatotoSerializer


class TaarifaZaWatotoWeek28ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 28")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek29ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 29")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek30ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 30")
	serializer_class = TaarifaZaWatotoSerializer


class TaarifaZaWatotoWeek31ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 31")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek32ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 32")
	serializer_class = TaarifaZaWatotoSerializer
	
class TaarifaZaWatotoWeek33ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 33")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek34ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 34")
	serializer_class = TaarifaZaWatotoSerializer


class TaarifaZaWatotoWeek35ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 35")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek36ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 36")
	serializer_class = TaarifaZaWatotoSerializer


class TaarifaZaWatotoWeek37ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 37")
	serializer_class = TaarifaZaWatotoSerializer


class TaarifaZaWatotoWeek38ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 38")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek39ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 39")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek40ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 40")
	serializer_class = TaarifaZaWatotoSerializer


class TaarifaZaWatotoWeek41ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 41")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek42ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 42")
	serializer_class = TaarifaZaWatotoSerializer
	
class TaarifaZaWatotoWeek43ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 43")
	serializer_class = TaarifaZaWatotoSerializer

class TaarifaZaWatotoWeek44ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 44")
	serializer_class = TaarifaZaWatotoSerializer


class TaarifaZaWatotoWeek45ViewSet(ModelViewSet):
	queryset = TaarifaZaWatoto.objects.filter(Week__WeekName__icontains="Wiki 45")
	serializer_class = TaarifaZaWatotoSerializer











# ------------------------JE WAJUA  KWA WATOTO KWA WEEK ZOTE----------

class JeWajuaWatotoWeek1ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 1")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek2ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 2")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek3ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 3")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek4ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 4")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek5ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 5")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek6ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 6")
	serializer_class = JeWajuaSerializer


class JeWajuaWatotoWeek7ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 7")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek8ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 8")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek9ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 9")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek10ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 10")
	serializer_class = JeWajuaSerializer


class JeWajuaWatotoWeek11ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 11")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek12ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 12")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek13ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 13")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek14ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 14")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek15ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 15")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek16ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 16")
	serializer_class = JeWajuaSerializer


class JeWajuaWatotoWeek17ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 17")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek18ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 18")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek19ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 19")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek20ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 20")
	serializer_class = JeWajuaSerializer


class JeWajuaWatotoWeek21ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 21")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek22ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 22")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek23ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 23")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek24ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 24")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek25ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 25")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek26ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 26")
	serializer_class = JeWajuaSerializer


class JeWajuaWatotoWeek27ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 27")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek28ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 28")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek29ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 29")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek30ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 30")
	serializer_class = JeWajuaSerializer


class JeWajuaWatotoWeek31ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 31")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek32ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 32")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek33ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 33")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek34ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 34")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek35ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 35")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek36ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 36")
	serializer_class = JeWajuaSerializer


class JeWajuaWatotoWeek37ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 37")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek38ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 38")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek39ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 39")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek40ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 40")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek41ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 41")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek42ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 42")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek43ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 43")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek44ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 44")
	serializer_class = JeWajuaSerializer

class JeWajuaWatotoWeek45ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="WATOTO", Week__WeekName__icontains="Wiki 45")
	serializer_class = JeWajuaSerializer









# ------------------------WEEK ZOTE  KWA WATOTO  ----------

class WatotoWeek1ViewSet(ModelViewSet):
	queryset = Week1.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 1")
	serializer_class = Week1Serializer

class WatotoWeek2ViewSet(ModelViewSet):
	queryset = Week2.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 2")
	serializer_class = Week2Serializer

class WatotoWeek3ViewSet(ModelViewSet):
	queryset = Week3.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 3")
	serializer_class = Week3Serializer

class WatotoWeek4ViewSet(ModelViewSet):
	queryset = Week4.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 4")
	serializer_class = Week4Serializer

class WatotoWeek5ViewSet(ModelViewSet):
	queryset = Week5.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 5")
	serializer_class = Week5Serializer

class WatotoWeek6ViewSet(ModelViewSet):
	queryset = Week6.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 6")
	serializer_class = Week6Serializer

class WatotoWeek7ViewSet(ModelViewSet):
	queryset = Week7.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 7")
	serializer_class = Week7Serializer

class WatotoWeek8ViewSet(ModelViewSet):
	queryset = Week8.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 8")
	serializer_class = Week8Serializer

class WatotoWeek9ViewSet(ModelViewSet):
	queryset = Week9.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 9")
	serializer_class = Week9Serializer


class WatotoWeek10ViewSet(ModelViewSet):
	queryset = Week10.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 10")
	serializer_class = Week10Serializer


class WatotoWeek11ViewSet(ModelViewSet):
	queryset = Week11.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 11")
	serializer_class = Week11Serializer

class WatotoWeek12ViewSet(ModelViewSet):
	queryset = Week12.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 12")
	serializer_class = Week12Serializer

class WatotoWeek13ViewSet(ModelViewSet):
	queryset = Week13.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 13")
	serializer_class = Week13Serializer

class WatotoWeek14ViewSet(ModelViewSet):
	queryset = Week14.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 14")
	serializer_class = Week14Serializer

class WatotoWeek15ViewSet(ModelViewSet):
	queryset = Week15.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 15")
	serializer_class = Week15Serializer

class WatotoWeek16ViewSet(ModelViewSet):
	queryset = Week16.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 16")
	serializer_class = Week16Serializer

class WatotoWeek17ViewSet(ModelViewSet):
	queryset = Week17.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 17")
	serializer_class = Week17Serializer

class WatotoWeek18ViewSet(ModelViewSet):
	queryset = Week18.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 18")
	serializer_class = Week18Serializer

class WatotoWeek19ViewSet(ModelViewSet):
	queryset = Week19.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 19")
	serializer_class = Week19Serializer

class WatotoWeek20ViewSet(ModelViewSet):
	queryset = Week20.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 20")
	serializer_class = Week20Serializer

class WatotoWeek21ViewSet(ModelViewSet):
	queryset = Week21.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 21")
	serializer_class = Week21Serializer

class WatotoWeek22ViewSet(ModelViewSet):
	queryset = Week22.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 22")
	serializer_class = Week22Serializer

class WatotoWeek23ViewSet(ModelViewSet):
	queryset = Week23.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 23")
	serializer_class = Week23Serializer


class WatotoWeek24ViewSet(ModelViewSet):
	queryset = Week24.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 24")
	serializer_class = Week24Serializer


class WatotoWeek25ViewSet(ModelViewSet):
	queryset = Week25.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 25")
	serializer_class = Week25Serializer

class WatotoWeek26ViewSet(ModelViewSet):
	queryset = Week26.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 26")
	serializer_class = Week26Serializer

class WatotoWeek27ViewSet(ModelViewSet):
	queryset = Week27.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 27")
	serializer_class = Week27Serializer

class WatotoWeek28ViewSet(ModelViewSet):
	queryset = Week28.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 28")
	serializer_class = Week28Serializer

class WatotoWeek29ViewSet(ModelViewSet):
	queryset = Week29.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 29")
	serializer_class = Week29Serializer

class WatotoWeek30ViewSet(ModelViewSet):
	queryset = Week30.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 30")
	serializer_class = Week30Serializer

class WatotoWeek31ViewSet(ModelViewSet):
	queryset = Week31.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 31")
	serializer_class = Week31Serializer


class WatotoWeek32ViewSet(ModelViewSet):
	queryset = Week32.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 32")
	serializer_class = Week32Serializer

class WatotoWeek33ViewSet(ModelViewSet):
	queryset = Week33.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 33")
	serializer_class = Week33Serializer

class WatotoWeek34ViewSet(ModelViewSet):
	queryset = Week34.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 34")
	serializer_class = Week34Serializer

class WatotoWeek35ViewSet(ModelViewSet):
	queryset = Week35.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 35")
	serializer_class = Week35Serializer

class WatotoWeek36ViewSet(ModelViewSet):
	queryset = Week36.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 36")
	serializer_class = Week36Serializer


class WatotoWeek37ViewSet(ModelViewSet):
	queryset = Week37.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 37")
	serializer_class = Week37Serializer

class WatotoWeek38ViewSet(ModelViewSet):
	queryset = Week38.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 38")
	serializer_class = Week38Serializer

class WatotoWeek39ViewSet(ModelViewSet):
	queryset = Week39.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 39")
	serializer_class = Week39Serializer


class WatotoWeek40ViewSet(ModelViewSet):
	queryset = Week40.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 40")
	serializer_class = Week40Serializer

class WatotoWeek41ViewSet(ModelViewSet):
	queryset = Week41.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 41")
	serializer_class = Week41Serializer


class WatotoWeek42ViewSet(ModelViewSet):
	queryset = Week42.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 42")
	serializer_class = Week42Serializer


class WatotoWeek43ViewSet(ModelViewSet):
	queryset = Week43.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 43")
	serializer_class = Week43Serializer

class WatotoWeek44ViewSet(ModelViewSet):
	queryset = Week44.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 44")
	serializer_class = Week44Serializer

class WatotoWeek45ViewSet(ModelViewSet):
	queryset = Week45.objects.filter(Category__ItemName__icontains="WATOTO", WeekName__icontains="Wiki 45")
	serializer_class = Week45Serializer

























#----------------------KISUKARI--------------------------------------


# ------------------------JE WAJUA  KWA KISUKARI KWA WEEK ZOTE----------

class JeWajuaKisukariWeek1ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 1")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek2ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 2")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek3ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 3")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek4ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 4")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek5ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 5")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek6ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 6")
	serializer_class = JeWajuaSerializer


class JeWajuaKisukariWeek7ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 7")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek8ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 8")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek9ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 9")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek10ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 10")
	serializer_class = JeWajuaSerializer


class JeWajuaKisukariWeek11ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 11")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek12ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 12")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek13ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 13")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek14ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 14")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek15ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 15")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek16ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 16")
	serializer_class = JeWajuaSerializer


class JeWajuaKisukariWeek17ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 17")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek18ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 18")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek19ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 19")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek20ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 20")
	serializer_class = JeWajuaSerializer


class JeWajuaKisukariWeek21ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 21")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek22ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 22")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek23ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 23")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek24ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 24")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek25ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 25")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek26ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 26")
	serializer_class = JeWajuaSerializer


class JeWajuaKisukariWeek27ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 27")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek28ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 28")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek29ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 29")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek30ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 30")
	serializer_class = JeWajuaSerializer


class JeWajuaKisukariWeek31ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 31")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek32ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 32")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek33ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 33")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek34ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 34")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek35ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 35")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek36ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 36")
	serializer_class = JeWajuaSerializer


class JeWajuaKisukariWeek37ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 37")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek38ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 38")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek39ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 39")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek40ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 40")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek41ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 41")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek42ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 42")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek43ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 43")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek44ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 44")
	serializer_class = JeWajuaSerializer

class JeWajuaKisukariWeek45ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="KISUKARI", Week__WeekName__icontains="Wiki 45")
	serializer_class = JeWajuaSerializer






























#---------------------KISUKARI------------------------------


# ------------------------TAARIFA ZA KISUKARI WEEK ZOTE----------

class TaarifaZaKisukariWeek1ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 1")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek2ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 2")
	serializer_class = TaarifaZaKisukariSerializer
	
class TaarifaZaKisukariWeek3ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 3")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek4ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 4")
	serializer_class = TaarifaZaKisukariSerializer


class TaarifaZaKisukariWeek5ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 5")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek6ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 6")
	serializer_class = TaarifaZaKisukariSerializer


class TaarifaZaKisukariWeek7ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 7")
	serializer_class = TaarifaZaKisukariSerializer


class TaarifaZaKisukariWeek8ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 8")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek9ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 9")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek10ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 10")
	serializer_class = TaarifaZaKisukariSerializer


class TaarifaZaKisukariWeek11ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 11")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek12ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 12")
	serializer_class = TaarifaZaKisukariSerializer
	
class TaarifaZaKisukariWeek13ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 13")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek14ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 14")
	serializer_class = TaarifaZaKisukariSerializer


class TaarifaZaKisukariWeek15ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 15")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek16ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 16")
	serializer_class = TaarifaZaKisukariSerializer


class TaarifaZaKisukariWeek17ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 17")
	serializer_class = TaarifaZaKisukariSerializer


class TaarifaZaKisukariWeek18ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 18")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek19ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 19")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek20ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 20")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek21ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 21")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek22ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 22")
	serializer_class = TaarifaZaKisukariSerializer
	
class TaarifaZaKisukariWeek23ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 23")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek24ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 24")
	serializer_class = TaarifaZaKisukariSerializer


class TaarifaZaKisukariWeek25ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 25")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek26ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 26")
	serializer_class = TaarifaZaKisukariSerializer


class TaarifaZaKisukariWeek27ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 27")
	serializer_class = TaarifaZaKisukariSerializer


class TaarifaZaKisukariWeek28ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 28")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek29ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 29")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek30ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 30")
	serializer_class = TaarifaZaKisukariSerializer


class TaarifaZaKisukariWeek31ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 31")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek32ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 32")
	serializer_class = TaarifaZaKisukariSerializer
	
class TaarifaZaKisukariWeek33ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 33")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek34ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 34")
	serializer_class = TaarifaZaKisukariSerializer


class TaarifaZaKisukariWeek35ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 35")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek36ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 36")
	serializer_class = TaarifaZaKisukariSerializer


class TaarifaZaKisukariWeek37ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 37")
	serializer_class = TaarifaZaKisukariSerializer


class TaarifaZaKisukariWeek38ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 38")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek39ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 39")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek40ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 40")
	serializer_class = TaarifaZaKisukariSerializer


class TaarifaZaKisukariWeek41ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 41")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek42ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 42")
	serializer_class = TaarifaZaKisukariSerializer
	
class TaarifaZaKisukariWeek43ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 43")
	serializer_class = TaarifaZaKisukariSerializer

class TaarifaZaKisukariWeek44ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 44")
	serializer_class = TaarifaZaKisukariSerializer


class TaarifaZaKisukariWeek45ViewSet(ModelViewSet):
	queryset = TaarifaZaKisukari.objects.filter(Week__WeekName__icontains="Wiki 45")
	serializer_class = TaarifaZaKisukariSerializer











# ------------------------WEEK ZOTE  KWA KISUKARI  ----------

class KisukariWeek1ViewSet(ModelViewSet):
	queryset = Week1.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 1")
	serializer_class = Week1Serializer

class KisukariWeek2ViewSet(ModelViewSet):
	queryset = Week2.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 2")
	serializer_class = Week2Serializer

class KisukariWeek3ViewSet(ModelViewSet):
	queryset = Week3.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 3")
	serializer_class = Week3Serializer

class KisukariWeek4ViewSet(ModelViewSet):
	queryset = Week4.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 4")
	serializer_class = Week4Serializer

class KisukariWeek5ViewSet(ModelViewSet):
	queryset = Week5.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 5")
	serializer_class = Week5Serializer

class KisukariWeek6ViewSet(ModelViewSet):
	queryset = Week6.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 6")
	serializer_class = Week6Serializer

class KisukariWeek7ViewSet(ModelViewSet):
	queryset = Week7.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 7")
	serializer_class = Week7Serializer

class KisukariWeek8ViewSet(ModelViewSet):
	queryset = Week8.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 8")
	serializer_class = Week8Serializer

class KisukariWeek9ViewSet(ModelViewSet):
	queryset = Week9.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 9")
	serializer_class = Week9Serializer


class KisukariWeek10ViewSet(ModelViewSet):
	queryset = Week10.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 10")
	serializer_class = Week10Serializer


class KisukariWeek11ViewSet(ModelViewSet):
	queryset = Week11.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 11")
	serializer_class = Week11Serializer

class KisukariWeek12ViewSet(ModelViewSet):
	queryset = Week12.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 12")
	serializer_class = Week12Serializer

class KisukariWeek13ViewSet(ModelViewSet):
	queryset = Week13.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 13")
	serializer_class = Week13Serializer

class KisukariWeek14ViewSet(ModelViewSet):
	queryset = Week14.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 14")
	serializer_class = Week14Serializer

class KisukariWeek15ViewSet(ModelViewSet):
	queryset = Week15.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 15")
	serializer_class = Week15Serializer

class KisukariWeek16ViewSet(ModelViewSet):
	queryset = Week16.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 16")
	serializer_class = Week16Serializer

class KisukariWeek17ViewSet(ModelViewSet):
	queryset = Week17.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 17")
	serializer_class = Week17Serializer

class KisukariWeek18ViewSet(ModelViewSet):
	queryset = Week18.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 18")
	serializer_class = Week18Serializer

class KisukariWeek19ViewSet(ModelViewSet):
	queryset = Week19.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 19")
	serializer_class = Week19Serializer

class KisukariWeek20ViewSet(ModelViewSet):
	queryset = Week20.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 20")
	serializer_class = Week20Serializer

class KisukariWeek21ViewSet(ModelViewSet):
	queryset = Week21.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 21")
	serializer_class = Week21Serializer

class KisukariWeek22ViewSet(ModelViewSet):
	queryset = Week22.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 22")
	serializer_class = Week22Serializer

class KisukariWeek23ViewSet(ModelViewSet):
	queryset = Week23.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 23")
	serializer_class = Week23Serializer


class KisukariWeek24ViewSet(ModelViewSet):
	queryset = Week24.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 24")
	serializer_class = Week24Serializer


class KisukariWeek25ViewSet(ModelViewSet):
	queryset = Week25.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 25")
	serializer_class = Week25Serializer

class KisukariWeek26ViewSet(ModelViewSet):
	queryset = Week26.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 26")
	serializer_class = Week26Serializer

class KisukariWeek27ViewSet(ModelViewSet):
	queryset = Week27.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 27")
	serializer_class = Week27Serializer

class KisukariWeek28ViewSet(ModelViewSet):
	queryset = Week28.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 28")
	serializer_class = Week28Serializer

class KisukariWeek29ViewSet(ModelViewSet):
	queryset = Week29.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 29")
	serializer_class = Week29Serializer

class KisukariWeek30ViewSet(ModelViewSet):
	queryset = Week30.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 30")
	serializer_class = Week30Serializer

class KisukariWeek31ViewSet(ModelViewSet):
	queryset = Week31.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 31")
	serializer_class = Week31Serializer


class KisukariWeek32ViewSet(ModelViewSet):
	queryset = Week32.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 32")
	serializer_class = Week32Serializer

class KisukariWeek33ViewSet(ModelViewSet):
	queryset = Week33.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 33")
	serializer_class = Week33Serializer

class KisukariWeek34ViewSet(ModelViewSet):
	queryset = Week34.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 34")
	serializer_class = Week34Serializer

class KisukariWeek35ViewSet(ModelViewSet):
	queryset = Week35.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 35")
	serializer_class = Week35Serializer

class KisukariWeek36ViewSet(ModelViewSet):
	queryset = Week36.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 36")
	serializer_class = Week36Serializer


class KisukariWeek37ViewSet(ModelViewSet):
	queryset = Week37.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 37")
	serializer_class = Week37Serializer

class KisukariWeek38ViewSet(ModelViewSet):
	queryset = Week38.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 38")
	serializer_class = Week38Serializer

class KisukariWeek39ViewSet(ModelViewSet):
	queryset = Week39.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 39")
	serializer_class = Week39Serializer


class KisukariWeek40ViewSet(ModelViewSet):
	queryset = Week40.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 40")
	serializer_class = Week40Serializer

class KisukariWeek41ViewSet(ModelViewSet):
	queryset = Week41.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 41")
	serializer_class = Week41Serializer


class KisukariWeek42ViewSet(ModelViewSet):
	queryset = Week42.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 42")
	serializer_class = Week42Serializer


class KisukariWeek43ViewSet(ModelViewSet):
	queryset = Week43.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 43")
	serializer_class = Week43Serializer

class KisukariWeek44ViewSet(ModelViewSet):
	queryset = Week44.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 44")
	serializer_class = Week44Serializer

class KisukariWeek45ViewSet(ModelViewSet):
	queryset = Week45.objects.filter(Category__ItemName__icontains="KISUKARI", WeekName__icontains="Wiki 45")
	serializer_class = Week45Serializer
































#---------------------HIV------------------------------


# ------------------------TAARIFA ZA HIV WEEK ZOTE----------

class TaarifaZaHivWeek1ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 1")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek2ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 2")
	serializer_class = TaarifaZaHivSerializer
	
class TaarifaZaHivWeek3ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 3")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek4ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 4")
	serializer_class = TaarifaZaHivSerializer


class TaarifaZaHivWeek5ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 5")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek6ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 6")
	serializer_class = TaarifaZaHivSerializer


class TaarifaZaHivWeek7ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 7")
	serializer_class = TaarifaZaHivSerializer


class TaarifaZaHivWeek8ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 8")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek9ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 9")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek10ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 10")
	serializer_class = TaarifaZaHivSerializer


class TaarifaZaHivWeek11ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 11")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek12ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 12")
	serializer_class = TaarifaZaHivSerializer
	
class TaarifaZaHivWeek13ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 13")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek14ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 14")
	serializer_class = TaarifaZaHivSerializer


class TaarifaZaHivWeek15ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 15")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek16ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 16")
	serializer_class = TaarifaZaHivSerializer


class TaarifaZaHivWeek17ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 17")
	serializer_class = TaarifaZaHivSerializer


class TaarifaZaHivWeek18ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 18")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek19ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 19")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek20ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 20")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek21ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 21")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek22ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 22")
	serializer_class = TaarifaZaHivSerializer
	
class TaarifaZaHivWeek23ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 23")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek24ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 24")
	serializer_class = TaarifaZaHivSerializer


class TaarifaZaHivWeek25ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 25")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek26ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 26")
	serializer_class = TaarifaZaHivSerializer


class TaarifaZaHivWeek27ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 27")
	serializer_class = TaarifaZaHivSerializer


class TaarifaZaHivWeek28ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 28")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek29ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 29")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek30ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 30")
	serializer_class = TaarifaZaHivSerializer


class TaarifaZaHivWeek31ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 31")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek32ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 32")
	serializer_class = TaarifaZaHivSerializer
	
class TaarifaZaHivWeek33ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 33")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek34ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 34")
	serializer_class = TaarifaZaHivSerializer


class TaarifaZaHivWeek35ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 35")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek36ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 36")
	serializer_class = TaarifaZaHivSerializer


class TaarifaZaHivWeek37ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 37")
	serializer_class = TaarifaZaHivSerializer


class TaarifaZaHivWeek38ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 38")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek39ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 39")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek40ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 40")
	serializer_class = TaarifaZaHivSerializer


class TaarifaZaHivWeek41ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 41")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek42ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 42")
	serializer_class = TaarifaZaHivSerializer
	
class TaarifaZaHivWeek43ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 43")
	serializer_class = TaarifaZaHivSerializer

class TaarifaZaHivWeek44ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 44")
	serializer_class = TaarifaZaHivSerializer


class TaarifaZaHivWeek45ViewSet(ModelViewSet):
	queryset = TaarifaZaHiv.objects.filter(Week__WeekName__icontains="Wiki 45")
	serializer_class = TaarifaZaHivSerializer












# ------------------------JE WAJUA  KWA HIV KWA WEEK ZOTE----------

class JeWajuaHivWeek1ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 1")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek2ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 2")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek3ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 3")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek4ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 4")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek5ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 5")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek6ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 6")
	serializer_class = JeWajuaSerializer


class JeWajuaHivWeek7ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 7")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek8ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 8")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek9ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 9")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek10ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 10")
	serializer_class = JeWajuaSerializer


class JeWajuaHivWeek11ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 11")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek12ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 12")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek13ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 13")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek14ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 14")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek15ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 15")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek16ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 16")
	serializer_class = JeWajuaSerializer


class JeWajuaHivWeek17ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 17")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek18ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 18")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek19ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 19")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek20ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 20")
	serializer_class = JeWajuaSerializer


class JeWajuaHivWeek21ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 21")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek22ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 22")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek23ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 23")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek24ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 24")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek25ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 25")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek26ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 26")
	serializer_class = JeWajuaSerializer


class JeWajuaHivWeek27ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 27")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek28ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 28")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek29ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 29")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek30ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 30")
	serializer_class = JeWajuaSerializer


class JeWajuaHivWeek31ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 31")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek32ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 32")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek33ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 33")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek34ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 34")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek35ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 35")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek36ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 36")
	serializer_class = JeWajuaSerializer


class JeWajuaHivWeek37ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 37")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek38ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 38")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek39ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 39")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek40ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 40")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek41ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 41")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek42ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 42")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek43ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 43")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek44ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 44")
	serializer_class = JeWajuaSerializer

class JeWajuaHivWeek45ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="HIV", Week__WeekName__icontains="Wiki 45")
	serializer_class = JeWajuaSerializer












# ------------------------WEEK ZOTE  KWA HIV  ----------

class HivWeek1ViewSet(ModelViewSet):
	queryset = Week1.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 1")
	serializer_class = Week1Serializer

class HivWeek2ViewSet(ModelViewSet):
	queryset = Week2.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 2")
	serializer_class = Week2Serializer

class HivWeek3ViewSet(ModelViewSet):
	queryset = Week3.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 3")
	serializer_class = Week3Serializer

class HivWeek4ViewSet(ModelViewSet):
	queryset = Week4.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 4")
	serializer_class = Week4Serializer

class HivWeek5ViewSet(ModelViewSet):
	queryset = Week5.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 5")
	serializer_class = Week5Serializer

class HivWeek6ViewSet(ModelViewSet):
	queryset = Week6.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 6")
	serializer_class = Week6Serializer

class HivWeek7ViewSet(ModelViewSet):
	queryset = Week7.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 7")
	serializer_class = Week7Serializer

class HivWeek8ViewSet(ModelViewSet):
	queryset = Week8.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 8")
	serializer_class = Week8Serializer

class HivWeek9ViewSet(ModelViewSet):
	queryset = Week9.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 9")
	serializer_class = Week9Serializer


class HivWeek10ViewSet(ModelViewSet):
	queryset = Week10.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 10")
	serializer_class = Week10Serializer


class HivWeek11ViewSet(ModelViewSet):
	queryset = Week11.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 11")
	serializer_class = Week11Serializer

class HivWeek12ViewSet(ModelViewSet):
	queryset = Week12.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 12")
	serializer_class = Week12Serializer

class HivWeek13ViewSet(ModelViewSet):
	queryset = Week13.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 13")
	serializer_class = Week13Serializer

class HivWeek14ViewSet(ModelViewSet):
	queryset = Week14.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 14")
	serializer_class = Week14Serializer

class HivWeek15ViewSet(ModelViewSet):
	queryset = Week15.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 15")
	serializer_class = Week15Serializer

class HivWeek16ViewSet(ModelViewSet):
	queryset = Week16.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 16")
	serializer_class = Week16Serializer

class HivWeek17ViewSet(ModelViewSet):
	queryset = Week17.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 17")
	serializer_class = Week17Serializer

class HivWeek18ViewSet(ModelViewSet):
	queryset = Week18.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 18")
	serializer_class = Week18Serializer

class HivWeek19ViewSet(ModelViewSet):
	queryset = Week19.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 19")
	serializer_class = Week19Serializer

class HivWeek20ViewSet(ModelViewSet):
	queryset = Week20.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 20")
	serializer_class = Week20Serializer

class HivWeek21ViewSet(ModelViewSet):
	queryset = Week21.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 21")
	serializer_class = Week21Serializer

class HivWeek22ViewSet(ModelViewSet):
	queryset = Week22.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 22")
	serializer_class = Week22Serializer

class HivWeek23ViewSet(ModelViewSet):
	queryset = Week23.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 23")
	serializer_class = Week23Serializer


class HivWeek24ViewSet(ModelViewSet):
	queryset = Week24.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 24")
	serializer_class = Week24Serializer


class HivWeek25ViewSet(ModelViewSet):
	queryset = Week25.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 25")
	serializer_class = Week25Serializer

class HivWeek26ViewSet(ModelViewSet):
	queryset = Week26.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 26")
	serializer_class = Week26Serializer

class HivWeek27ViewSet(ModelViewSet):
	queryset = Week27.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 27")
	serializer_class = Week27Serializer

class HivWeek28ViewSet(ModelViewSet):
	queryset = Week28.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 28")
	serializer_class = Week28Serializer

class HivWeek29ViewSet(ModelViewSet):
	queryset = Week29.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 29")
	serializer_class = Week29Serializer

class HivWeek30ViewSet(ModelViewSet):
	queryset = Week30.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 30")
	serializer_class = Week30Serializer

class HivWeek31ViewSet(ModelViewSet):
	queryset = Week31.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 31")
	serializer_class = Week31Serializer


class HivWeek32ViewSet(ModelViewSet):
	queryset = Week32.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 32")
	serializer_class = Week32Serializer

class HivWeek33ViewSet(ModelViewSet):
	queryset = Week33.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 33")
	serializer_class = Week33Serializer

class HivWeek34ViewSet(ModelViewSet):
	queryset = Week34.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 34")
	serializer_class = Week34Serializer

class HivWeek35ViewSet(ModelViewSet):
	queryset = Week35.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 35")
	serializer_class = Week35Serializer

class HivWeek36ViewSet(ModelViewSet):
	queryset = Week36.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 36")
	serializer_class = Week36Serializer


class HivWeek37ViewSet(ModelViewSet):
	queryset = Week37.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 37")
	serializer_class = Week37Serializer

class HivWeek38ViewSet(ModelViewSet):
	queryset = Week38.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 38")
	serializer_class = Week38Serializer

class HivWeek39ViewSet(ModelViewSet):
	queryset = Week39.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 39")
	serializer_class = Week39Serializer


class HivWeek40ViewSet(ModelViewSet):
	queryset = Week40.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 40")
	serializer_class = Week40Serializer

class HivWeek41ViewSet(ModelViewSet):
	queryset = Week41.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 41")
	serializer_class = Week41Serializer


class HivWeek42ViewSet(ModelViewSet):
	queryset = Week42.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 42")
	serializer_class = Week42Serializer


class HivWeek43ViewSet(ModelViewSet):
	queryset = Week43.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 43")
	serializer_class = Week43Serializer

class HivWeek44ViewSet(ModelViewSet):
	queryset = Week44.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 44")
	serializer_class = Week44Serializer

class HivWeek45ViewSet(ModelViewSet):
	queryset = Week45.objects.filter(Category__ItemName__icontains="HIV", WeekName__icontains="Wiki 45")
	serializer_class = Week45Serializer





















#---------------------FAMILIA------------------------------


# ------------------------TAARIFA ZA FAMILIA WEEK ZOTE----------

class TaarifaZaFamiliaWeek1ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 1")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek2ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 2")
	serializer_class = TaarifaZaFamiliaSerializer
	
class TaarifaZaFamiliaWeek3ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 3")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek4ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 4")
	serializer_class = TaarifaZaFamiliaSerializer


class TaarifaZaFamiliaWeek5ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 5")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek6ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 6")
	serializer_class = TaarifaZaFamiliaSerializer


class TaarifaZaFamiliaWeek7ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 7")
	serializer_class = TaarifaZaFamiliaSerializer


class TaarifaZaFamiliaWeek8ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 8")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek9ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 9")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek10ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 10")
	serializer_class = TaarifaZaFamiliaSerializer


class TaarifaZaFamiliaWeek11ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 11")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek12ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 12")
	serializer_class = TaarifaZaFamiliaSerializer
	
class TaarifaZaFamiliaWeek13ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 13")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek14ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 14")
	serializer_class = TaarifaZaFamiliaSerializer


class TaarifaZaFamiliaWeek15ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 15")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek16ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 16")
	serializer_class = TaarifaZaFamiliaSerializer


class TaarifaZaFamiliaWeek17ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 17")
	serializer_class = TaarifaZaFamiliaSerializer


class TaarifaZaFamiliaWeek18ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 18")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek19ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 19")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek20ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 20")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek21ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 21")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek22ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 22")
	serializer_class = TaarifaZaFamiliaSerializer
	
class TaarifaZaFamiliaWeek23ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 23")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek24ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 24")
	serializer_class = TaarifaZaFamiliaSerializer


class TaarifaZaFamiliaWeek25ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 25")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek26ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 26")
	serializer_class = TaarifaZaFamiliaSerializer


class TaarifaZaFamiliaWeek27ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 27")
	serializer_class = TaarifaZaFamiliaSerializer


class TaarifaZaFamiliaWeek28ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 28")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek29ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 29")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek30ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 30")
	serializer_class = TaarifaZaFamiliaSerializer


class TaarifaZaFamiliaWeek31ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 31")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek32ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 32")
	serializer_class = TaarifaZaFamiliaSerializer
	
class TaarifaZaFamiliaWeek33ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 33")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek34ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 34")
	serializer_class = TaarifaZaFamiliaSerializer


class TaarifaZaFamiliaWeek35ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 35")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek36ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 36")
	serializer_class = TaarifaZaFamiliaSerializer


class TaarifaZaFamiliaWeek37ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 37")
	serializer_class = TaarifaZaFamiliaSerializer


class TaarifaZaFamiliaWeek38ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 38")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek39ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 39")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek40ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 40")
	serializer_class = TaarifaZaFamiliaSerializer


class TaarifaZaFamiliaWeek41ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 41")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek42ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 42")
	serializer_class = TaarifaZaFamiliaSerializer
	
class TaarifaZaFamiliaWeek43ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 43")
	serializer_class = TaarifaZaFamiliaSerializer

class TaarifaZaFamiliaWeek44ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 44")
	serializer_class = TaarifaZaFamiliaSerializer


class TaarifaZaFamiliaWeek45ViewSet(ModelViewSet):
	queryset = TaarifaZaFamilia.objects.filter(Week__WeekName__icontains="Wiki 45")
	serializer_class = TaarifaZaFamiliaSerializer













# ------------------------WEEK ZOTE  KWA FAMILIA  ----------

class FamiliaWeek1ViewSet(ModelViewSet):
	queryset = Week1.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 1")
	serializer_class = Week1Serializer

class FamiliaWeek2ViewSet(ModelViewSet):
	queryset = Week2.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 2")
	serializer_class = Week2Serializer

class FamiliaWeek3ViewSet(ModelViewSet):
	queryset = Week3.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 3")
	serializer_class = Week3Serializer

class FamiliaWeek4ViewSet(ModelViewSet):
	queryset = Week4.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 4")
	serializer_class = Week4Serializer

class FamiliaWeek5ViewSet(ModelViewSet):
	queryset = Week5.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 5")
	serializer_class = Week5Serializer

class FamiliaWeek6ViewSet(ModelViewSet):
	queryset = Week6.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 6")
	serializer_class = Week6Serializer

class FamiliaWeek7ViewSet(ModelViewSet):
	queryset = Week7.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 7")
	serializer_class = Week7Serializer

class FamiliaWeek8ViewSet(ModelViewSet):
	queryset = Week8.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 8")
	serializer_class = Week8Serializer

class FamiliaWeek9ViewSet(ModelViewSet):
	queryset = Week9.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 9")
	serializer_class = Week9Serializer


class FamiliaWeek10ViewSet(ModelViewSet):
	queryset = Week10.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 10")
	serializer_class = Week10Serializer


class FamiliaWeek11ViewSet(ModelViewSet):
	queryset = Week11.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 11")
	serializer_class = Week11Serializer

class FamiliaWeek12ViewSet(ModelViewSet):
	queryset = Week12.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 12")
	serializer_class = Week12Serializer

class FamiliaWeek13ViewSet(ModelViewSet):
	queryset = Week13.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 13")
	serializer_class = Week13Serializer

class FamiliaWeek14ViewSet(ModelViewSet):
	queryset = Week14.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 14")
	serializer_class = Week14Serializer

class FamiliaWeek15ViewSet(ModelViewSet):
	queryset = Week15.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 15")
	serializer_class = Week15Serializer

class FamiliaWeek16ViewSet(ModelViewSet):
	queryset = Week16.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 16")
	serializer_class = Week16Serializer

class FamiliaWeek17ViewSet(ModelViewSet):
	queryset = Week17.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 17")
	serializer_class = Week17Serializer

class FamiliaWeek18ViewSet(ModelViewSet):
	queryset = Week18.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 18")
	serializer_class = Week18Serializer

class FamiliaWeek19ViewSet(ModelViewSet):
	queryset = Week19.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 19")
	serializer_class = Week19Serializer

class FamiliaWeek20ViewSet(ModelViewSet):
	queryset = Week20.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 20")
	serializer_class = Week20Serializer

class FamiliaWeek21ViewSet(ModelViewSet):
	queryset = Week21.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 21")
	serializer_class = Week21Serializer

class FamiliaWeek22ViewSet(ModelViewSet):
	queryset = Week22.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 22")
	serializer_class = Week22Serializer

class FamiliaWeek23ViewSet(ModelViewSet):
	queryset = Week23.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 23")
	serializer_class = Week23Serializer


class FamiliaWeek24ViewSet(ModelViewSet):
	queryset = Week24.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 24")
	serializer_class = Week24Serializer


class FamiliaWeek25ViewSet(ModelViewSet):
	queryset = Week25.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 25")
	serializer_class = Week25Serializer

class FamiliaWeek26ViewSet(ModelViewSet):
	queryset = Week26.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 26")
	serializer_class = Week26Serializer

class FamiliaWeek27ViewSet(ModelViewSet):
	queryset = Week27.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 27")
	serializer_class = Week27Serializer

class FamiliaWeek28ViewSet(ModelViewSet):
	queryset = Week28.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 28")
	serializer_class = Week28Serializer

class FamiliaWeek29ViewSet(ModelViewSet):
	queryset = Week29.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 29")
	serializer_class = Week29Serializer

class FamiliaWeek30ViewSet(ModelViewSet):
	queryset = Week30.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 30")
	serializer_class = Week30Serializer

class FamiliaWeek31ViewSet(ModelViewSet):
	queryset = Week31.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 31")
	serializer_class = Week31Serializer


class FamiliaWeek32ViewSet(ModelViewSet):
	queryset = Week32.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 32")
	serializer_class = Week32Serializer

class FamiliaWeek33ViewSet(ModelViewSet):
	queryset = Week33.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 33")
	serializer_class = Week33Serializer

class FamiliaWeek34ViewSet(ModelViewSet):
	queryset = Week34.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 34")
	serializer_class = Week34Serializer

class FamiliaWeek35ViewSet(ModelViewSet):
	queryset = Week35.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 35")
	serializer_class = Week35Serializer

class FamiliaWeek36ViewSet(ModelViewSet):
	queryset = Week36.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 36")
	serializer_class = Week36Serializer


class FamiliaWeek37ViewSet(ModelViewSet):
	queryset = Week37.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 37")
	serializer_class = Week37Serializer

class FamiliaWeek38ViewSet(ModelViewSet):
	queryset = Week38.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 38")
	serializer_class = Week38Serializer

class FamiliaWeek39ViewSet(ModelViewSet):
	queryset = Week39.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 39")
	serializer_class = Week39Serializer


class FamiliaWeek40ViewSet(ModelViewSet):
	queryset = Week40.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 40")
	serializer_class = Week40Serializer

class FamiliaWeek41ViewSet(ModelViewSet):
	queryset = Week41.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 41")
	serializer_class = Week41Serializer


class FamiliaWeek42ViewSet(ModelViewSet):
	queryset = Week42.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 42")
	serializer_class = Week42Serializer


class FamiliaWeek43ViewSet(ModelViewSet):
	queryset = Week43.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 43")
	serializer_class = Week43Serializer

class FamiliaWeek44ViewSet(ModelViewSet):
	queryset = Week44.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 44")
	serializer_class = Week44Serializer

class FamiliaWeek45ViewSet(ModelViewSet):
	queryset = Week45.objects.filter(Category__ItemName__icontains="FAMILIA", WeekName__icontains="Wiki 45")
	serializer_class = Week45Serializer















# ------------------------JE WAJUA  KWA FAMILIA KWA WEEK ZOTE----------

class JeWajuaFamiliaWeek1ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 1")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek2ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 2")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek3ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 3")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek4ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 4")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek5ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 5")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek6ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 6")
	serializer_class = JeWajuaSerializer


class JeWajuaFamiliaWeek7ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 7")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek8ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 8")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek9ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 9")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek10ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 10")
	serializer_class = JeWajuaSerializer


class JeWajuaFamiliaWeek11ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 11")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek12ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 12")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek13ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 13")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek14ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 14")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek15ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 15")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek16ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 16")
	serializer_class = JeWajuaSerializer


class JeWajuaFamiliaWeek17ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 17")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek18ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 18")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek19ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 19")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek20ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 20")
	serializer_class = JeWajuaSerializer


class JeWajuaFamiliaWeek21ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 21")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek22ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 22")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek23ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 23")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek24ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 24")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek25ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 25")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek26ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 26")
	serializer_class = JeWajuaSerializer


class JeWajuaFamiliaWeek27ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 27")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek28ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 28")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek29ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 29")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek30ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 30")
	serializer_class = JeWajuaSerializer


class JeWajuaFamiliaWeek31ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 31")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek32ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 32")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek33ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 33")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek34ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 34")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek35ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 35")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek36ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 36")
	serializer_class = JeWajuaSerializer


class JeWajuaFamiliaWeek37ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 37")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek38ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 38")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek39ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 39")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek40ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 40")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek41ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 41")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek42ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 42")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek43ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 43")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek44ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 44")
	serializer_class = JeWajuaSerializer

class JeWajuaFamiliaWeek45ViewSet(ModelViewSet):
	queryset = JeWajua.objects.filter(Category__ItemName__icontains="FAMILIA", Week__WeekName__icontains="Wiki 45")
	serializer_class = JeWajuaSerializer

