from LisheApp.models import *
from rest_framework import serializers
from django.contrib.auth.models import User




#______________DJANGO REACT AUTHENTICATION_________________

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['username','email','password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

#______________MWISHO HAPA DJANGO REACT AUTHENTICATION_________________


# kwa ajili ya kumregister mtu bila kutumia token
class UserCreationSerializer(serializers.ModelSerializer):
	username=serializers.CharField(max_length=25)
	email=serializers.EmailField(max_length=50)
	password=serializers.CharField(max_length=50)


	class Meta:
		model= User
		fields= ['username','email','password']
		#fields='__all__'

	def validate(self,attrs):
		username_exists = User.objects.filter(username=attrs['username']).exists()
		if username_exists:
			raise serializers.ValidationError(detail="User with username already exists")


		email_exists = User.objects.filter(email=attrs['email']).exists()
		if email_exists:
			raise serializers.ValidationError(detail="User with email already exists")

		return super().validate(attrs)








class LisheSerializer(serializers.ModelSerializer):

	class Meta:
		model = Lishe
		fields = '__all__'

class ElimuYaLisheSerializer(serializers.ModelSerializer):

	class Meta:
		model = ElimuYaLishe
		fields = '__all__'

class BidhaaZetuSerializer(serializers.ModelSerializer):

	class Meta:
		model = BidhaaZetu
		fields = '__all__'

class DaysSerializer(serializers.ModelSerializer):

	class Meta:
		model = Days
		fields = '__all__'






# MWANZO WA  DAYS SERIALIZERS

#  DAY ONE
class DayOneSerializer(serializers.ModelSerializer):

	class Meta:
		model = DayOne
		fields = '__all__'


#  DAY Two
class DayTwoSerializer(serializers.ModelSerializer):

	class Meta:
		model = DayTwo
		fields = '__all__'

#  DAY Three
class DayThreeSerializer(serializers.ModelSerializer):

	class Meta:
		model = DayThree
		fields = '__all__'

#  DAY Four
class DayFourSerializer(serializers.ModelSerializer):

	class Meta:
		model = DayFour
		fields = '__all__'


#  DAY Five
class DayFiveSerializer(serializers.ModelSerializer):

	class Meta:
		model = DayFive
		fields = '__all__'


#  DAY Six
class DaySixSerializer(serializers.ModelSerializer):

	class Meta:
		model = DaySix
		fields = '__all__'


#  DAY Seven
class DaySevenSerializer(serializers.ModelSerializer):

	class Meta:
		model = DaySeven
		fields = '__all__'


class MakundiYaChakulaSerializer(serializers.ModelSerializer):

	class Meta:
		model = MakundiYaChakula
		fields = '__all__'

class PosterNaPichaSerializer(serializers.ModelSerializer):

	class Meta:
		model = PosterNaPicha
		fields = '__all__'