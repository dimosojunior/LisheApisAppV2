from django.shortcuts import render,redirect


# Create your views here.
from django.shortcuts import render,get_object_or_404
from LisheApis.serializers import *
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

from LisheApis.serializers import *
from drf_yasg.utils import swagger_auto_schema

from rest_framework import generics,status
from rest_framework.decorators import api_view

# Create your views here.

# class UserView(APIView):

# 	def get(self,request, format=None):
# 		return Response("User Account View", status=200)

# 	def post(self,request, format=None):

# 		return Response("Creating User", status=200)



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



import jwt, datetime
from rest_framework.exceptions import AuthenticationFailed



# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail

# import uuid
# import hashlib

from LisheApp.models import Token


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         token['username'] = user.username
#         # ...

#         return token


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer



# # SIGNIN YA KAWAIDA SIO YA APIS
# def signin(request):

#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         user = auth.authenticate(email=email, password=password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect('home')
#         else:
#             messages.info(request, 'Credentials Invalid, Username or Password is incorrect')
#             return redirect('home')

#     else:
#         return render(request, 'LisheApp/home.html')


# def logout(request):
#     auth.logout(request)
#     return redirect('home')


# # SIGNUP YA KAWAIDA SIO YA APIS
# def signup(request):

#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password1']
#         password2 = request.POST['password2']

#         if password == password2:
#             if User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email Already Taken')
#                 return redirect('home')
#             elif User.objects.filter(username=username).exists():
#                 messages.info(request, 'Username Already Taken')
#                 return redirect('home')
#             else:
#                 user = User.objects.create_user(username=username, email=email, password=password)
#                 user.save()



#                 #log user in and redirect to settings page
#                 user_login = auth.authenticate(email=email, password=password)
#                 auth.login(request, user_login)

#                 messages.success(request, f'You have registered successfully as {username} ')
#                 return redirect('home')

                
#         else:
#             messages.info(request, 'Password Not Matching')
#             return redirect('home')

#     # else:
#     #     return render(request, 'LisheApis/home.html')



# # SIGNUP YA APIS
# class user_create_view(generics.GenericAPIView):
#     serializer_class=UserCreationSerializer

#     @swagger_auto_schema(operation_summary="User Registration Form")
#     def post(self,request):
#         data=request.data
#         serializer=self.serializer_class(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data,status=status.HTTP_201_CREATED)

#         return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)









# #------------------DJANGO REACT AUTHENTICATION----------------

# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# class LoginView(APIView):
#     def post(self, request):
#         email = request.data['email']
#         password = request.data['password']

#         user = User.objects.filter(email=email).first()

#         if user is None:
#             raise AuthenticationFailed('User not found!')

#         if not user.check_password(password):
#             raise AuthenticationFailed('Incorrect password!')

#         payload = {
#             'id': user.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             'iat': datetime.datetime.utcnow()
#         }

#         token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

#         response = Response()

#         response.set_cookie(key='jwt', value=token, httponly=True)
#         response.data = {
#             'jwt': token
#         }
#         return response


# class UserView(APIView):

#     def get(self, request):
#         token = request.COOKIES.get('jwt')

#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')

#         try:
#             payload = jwt.decode(token, 'secret', algorithm=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')

#         user = User.objects.filter(id=payload['id']).first()
#         serializer = UserSerializer(user)
#         return Response(serializer.data)


# class LogoutView(APIView):
#     def post(self, request):
#         response = Response()
#         response.delete_cookie('jwt')
#         response.data = {
#             'message': 'success'
#         }
#         return response





















#----------------------TUTORIAL NYINGINE----------------------



class TestView(APIView):
    def get(self, request, format=None):
        print("API Was Called")
        return Response("You Made It", status=200)


class UserView(APIView):
    def post(self, request, format=None):
        print("Creating a user")

        user_data = request.data
        user_data['is_active'] = False

        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=False):
            user_serializer.save()
            print("DATA UPLOADED SUCCESFULLY")

            # salt = uuid.uuid4().hex
            # hash_object = hashlib.sha256(salt.encode() + str(user_serializer.data['id']).encode())
            # token = hash_object.hexdigest() + ':' + salt

            # token_serializer=TokenSerializer(data={"user":user_serializer.data['id'], "token":token})
            # if token_serializer.is_valid(raise_exception=False):
            #     token_serializer.save()


            #     message = Mail(
            #         from_email="tim@poieo-dev.com",
            #         to_emails=user_data['email'],
            #         subject='Please Confirm your Email Address',
            #         html_content=f"\
            #         Hi {user_data['first_name']},\
            #         <br><br>Thank you for signing up. To confirm your email address, please click <a href='http://localhost:8000/api/v1.0/user/verify-user/{token}'>HERE</a>\
            #         "
            #         )

            #     try:
            #         sg = SendGridAPIClient("<<SENDGRID API KEY>>")
            #         response = sg.send(message)

            #         return Response(user_serializer.data, status=200)

            #     except Exception as e:
            #         print("ERROR", e)

        else:
            print(user_serializer.errors)

        return Response(user_serializer.data, status=400)

class UserVerificationView(APIView):

    def get(self, request, pk, format=None):
        print("VERIFYING USER", pk)

        tokenObj = Token.objects.filter(token=pk).first()


        user = User.objects.filter(id=tokenObj.user.id).first()

        if user:
            user_serializer = UserSerializer(user, data={'is_active':True}, partial=True)
            if user_serializer.is_valid(raise_exception=False):
                user_serializer.save()

                return Response(status=200)

        return Response(status=404)



class UserLoginView(APIView):
    # Convert a user token into user data
    def get(self, request, format=None):

        if request.user.is_authenticated == False or request.user.is_active == False:
            return Response("Invalid Credentials", status=403)

        user = UserSerializer(request.user)
        return Response(user.data, status=200)

    def post(self, request, format=None):
        print("Login Class")

        user_obj = User.objects.filter(email=request.data['username']).first() or User.objects.filter(username=request.data['username']).first()

        if user_obj is not None:
            credentials = {
                'email': user_obj.email,
                'password': request.data['password']
            }
            user = authenticate(**credentials)

            if user and user.is_active:
                user_serializer = UserSerializer(user)
                return Response(user_serializer.data, status=200)

        return Response("Invalid Credentials", status=403)






class SettingsView(APIView):
    def get(self, request, format=None):
        settingsDict = {}
        #{"NAME":"VALUE", "NAME2":"VALUE2"}

        try:
            settingObjects = Setting.objects.all()

            for setting in settingObjects:
                settingsDict[setting.name] = setting.value

            return Response(settingsDict, status=200)

        except:
            return Response(status=404)

    def post(self, request, format=None):

        #This view we are going to create new settings in the DB

        #JSON Object: {"setings": [{"NAME":NAME, "VALUE":VALUE}, {"NAME":NAME, "VALUE":VALUE}]}
        settings = request.data['settings']
        bad_settings = []
        for setting in settings:
            try:
                new_setting = Setting(name=setting['NAME'], value=setting['VALUE'])
                new_setting.save()
            except:
                bad_settings.append(setting)

        if len(bad_settings) > 0:
            return Response({"INVALID SETTINGS": bad_settings}, status=200)

        else:
            return Response(status=200)
