from LisheApp.models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class LisheForm(forms.ModelForm):
	
	class Meta:
		model = Lishe
		fields ='__all__'


class ElimuYaLisheForm(forms.ModelForm):
	
	class Meta:
		model = ElimuYaLishe
		fields ='__all__'


class BidhaaZetuForm(forms.ModelForm):
	
	class Meta:
		model = BidhaaZetu
		fields ='__all__'


class DaysForm(forms.ModelForm):
	
	class Meta:
		model = Days
		fields ='__all__'


class DayOneForm(forms.ModelForm):
	
	class Meta:
		model = DayOne
		fields ='__all__'

class DayTwoForm(forms.ModelForm):
	
	class Meta:
		model = DayTwo
		fields ='__all__'



class DayThreeForm(forms.ModelForm):
	
	class Meta:
		model = DayThree
		fields ='__all__'


class DayFourForm(forms.ModelForm):
	
	class Meta:
		model = DayFour
		fields ='__all__'


class DayFiveForm(forms.ModelForm):
	
	class Meta:
		model = DayFive
		fields ='__all__'


class DaySixForm(forms.ModelForm):
	
	class Meta:
		model = DaySix
		fields ='__all__'


class DaySevenForm(forms.ModelForm):
	
	class Meta:
		model = DaySeven
		fields ='__all__'

class MakundiYaChakulaForm(forms.ModelForm):
	
	class Meta:
		model = MakundiYaChakula
		fields ='__all__'


class PosterNaPichaForm(forms.ModelForm):
	
	class Meta:
		model = PosterNaPicha
		fields ='__all__'











#----------------------SEARCH FORM----------------

class LisheSearchForm(forms.ModelForm):
	
	ItemName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'item', 'placeholder' : 'Search'})

	)
	
	class Meta:
		model = Lishe
		fields =['ItemName']



class ElimuYaLisheSearchForm(forms.ModelForm):
	
	Category = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'item', 'placeholder' : 'Search'})

	)
	
	class Meta:
		model = ElimuYaLishe
		fields =['Category']



class BidhaaZetuSearchForm(forms.ModelForm):
	
	ProductName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'item', 'placeholder' : 'Search'})

	)
	
	class Meta:
		model = BidhaaZetu
		fields =['ProductName']


class DaysSearchForm(forms.ModelForm):
	
	DayName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'item', 'placeholder' : 'Search'})

	)
	
	class Meta:
		model = Days
		fields =['DayName']


class DayOneSearchForm(forms.ModelForm):
	
	# Time = forms.CharField(
	# 	required=False,
	# #label=False,
	# 	widget=forms.TextInput(attrs={'id' :'item', 'placeholder' : 'Search eg: MCHANA'})

	# )
	
	class Meta:
		model = DayOne
		fields =['Category']


class DayTwoSearchForm(forms.ModelForm):
	
	
	
	class Meta:
		model = DayTwo
		fields =['Category']

class DayThreeSearchForm(forms.ModelForm):
	
	
	
	class Meta:
		model = DayThree
		fields =['Category']


class DayFourSearchForm(forms.ModelForm):
	
		
	class Meta:
		model = DayFour
		fields =['Category']



class DayFiveSearchForm(forms.ModelForm):
	
	
	
	class Meta:
		model = DayFive
		fields =['Category']


class DaySixSearchForm(forms.ModelForm):
	
	
	
	class Meta:
		model = DaySix
		fields =['Category']


class DaySevenSearchForm(forms.ModelForm):
	
		
	class Meta:
		model = DaySeven
		fields =['Category']


class MakundiYaChakulaSearchForm(forms.ModelForm):
	
	FoodCategory = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'item', 'placeholder' : 'Search'})

	)
	
	class Meta:
		model = MakundiYaChakula
		fields =['FoodCategory']










