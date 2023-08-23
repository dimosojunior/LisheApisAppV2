
from django.shortcuts import render,redirect,get_object_or_404
from LisheApp.models import *
from LisheApp.forms import *
from django.http import JsonResponse
from django.db.models import Q
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):

	return render(request, 'LisheApp/home.html')



#-------------------MWANZO WA LISTS ITEMS--------------------

def LisheItems(request):
	item = Lishe.objects.all().order_by('id')
	# form ya kusearch
	form = LisheSearchForm(request.POST or None)
	if request.method =="POST":
		item = Lishe.objects.filter(ItemName__icontains=form['ItemName'].value())


	context = {
		"item":item,
		"form":form,
	}

	return render(request, 'LisheApp/Lishe/LisheItems.html', context)



def ElimuYaLisheItems(request):
	item = ElimuYaLishe.objects.all().order_by('id')
	# form ya kusearch
	form = ElimuYaLisheSearchForm(request.POST or None)
	if request.method =="POST":
		item = ElimuYaLishe.objects.filter(Category__icontains=form['Category'].value())


	context = {
		"item":item,
		"form":form,
	}

	return render(request, 'LisheApp/ElimuYaLishe/ElimuYaLisheItems.html', context)


def BidhaaZetuItems(request):
	item = BidhaaZetu.objects.all().order_by('id')
	# form ya kusearch
	form = BidhaaZetuSearchForm(request.POST or None)
	if request.method =="POST":
		item = BidhaaZetu.objects.filter(ProductName__icontains=form['ProductName'].value())


	context = {
		"item":item,
		"form":form,
	}

	return render(request, 'LisheApp/BidhaaZetu/BidhaaZetuItems.html', context)






def MakundiYaChakulaItems(request):
	item = MakundiYaChakula.objects.all().order_by('id')
	# form ya kusearch
	form = MakundiYaChakulaSearchForm(request.POST or None)
	if request.method =="POST":
		item = MakundiYaChakula.objects.filter(FoodCategory__icontains=form['FoodCategory'].value())


	context = {
		"item":item,
		"form":form,
	}

	return render(request, 'LisheApp/MakundiYaChakula/MakundiYaChakulaItems.html', context)

def PosterNaPichaItems(request):
	item = PosterNaPicha.objects.all().order_by('id')
	

	context = {
		"item":item,
		# "form":form,
	}

	return render(request, 'LisheApp/PosterNaPicha/PosterNaPichaItems.html', context)





#----------------------DAYS LIST ITEMS------------------------

def DayOneItems(request):
	queryset = DayOne.objects.all().order_by('id')
	form = DayOneSearchForm(request.POST or None)
	# # form ya kusearch
	# form = DayOneSearchForm(request.POST or None)
	# if request.method =="POST":
	# 	item = DayOne.objects.filter(Category__ItemName__icontains=form['Category'].value())


	context = {
		"queryset":queryset,
		"form":form,
	}

	#kwa ajili ya kufilter items and category ktk form
	if request.method == 'POST':
		#category__icontains=form['category'].value(),
		category = form['Category'].value()

		
#KAMA UNATAKA KUADD FIELD NYINGINE TUMIA HIYO YA CHINI
										
		# queryset = DayOne.objects.filter(
		# 								Time__icontains=form['Time'].value()
										
		# 	)
		if (category != ''):
			queryset = DayOne.objects.all()
			queryset = queryset.filter(Category_id=category)

			
			#ZINAISHIA HAPA ZA KUSEARCH ILA CONTEXT IPO KWA CHINI
		


			#HII NI CONTEXT KWA AJILI YA KUSEARCH ITEM OR CATEGORY KWENYE FORMYETU
		context ={
		#"QuerySet":QuerySet,
		"form":form,
		"queryset":queryset,
		
	}









	return render(request, 'LisheApp/DayOne/DayOneItems.html', context)










def DayTwoItems(request):
	queryset = DayTwo.objects.all().order_by('id')
	form = DayTwoSearchForm(request.POST or None)
	# # form ya kusearch
	# form = DayTwoSearchForm(request.POST or None)
	# if request.method =="POST":
	# 	item = DayTwo.objects.filter(Category__ItemName__icontains=form['Category'].value())


	context = {
		"queryset":queryset,
		"form":form,
	}

	#kwa ajili ya kufilter items and category ktk form
	if request.method == 'POST':
		#category__icontains=form['category'].value(),
		category = form['Category'].value()

		
#KAMA UNATAKA KUADD FIELD NYINGINE TUMIA HIYO YA CHINI
										
		# queryset = DayTwo.objects.filter(
		# 								Time__icontains=form['Time'].value()
										
		# 	)
		if (category != ''):
			queryset = DayTwo.objects.all()
			queryset = queryset.filter(Category_id=category)

			
			#ZINAISHIA HAPA ZA KUSEARCH ILA CONTEXT IPO KWA CHINI
		


			#HII NI CONTEXT KWA AJILI YA KUSEARCH ITEM OR CATEGORY KWENYE FORMYETU
		context ={
		#"QuerySet":QuerySet,
		"form":form,
		"queryset":queryset,
		
	}









	return render(request, 'LisheApp/DayTwo/DayTwoItems.html', context)



def DayThreeItems(request):
	queryset = DayThree.objects.all().order_by('id')
	form = DayThreeSearchForm(request.POST or None)
	# # form ya kusearch
	# form = DayThreeSearchForm(request.POST or None)
	# if request.method =="POST":
	# 	item = DayThree.objects.filter(Category__ItemName__icontains=form['Category'].value())


	context = {
		"queryset":queryset,
		"form":form,
	}

	#kwa ajili ya kufilter items and category ktk form
	if request.method == 'POST':
		#category__icontains=form['category'].value(),
		category = form['Category'].value()

		
#KAMA UNATAKA KUADD FIELD NYINGINE TUMIA HIYO YA CHINI
										
		# queryset = DayThree.objects.filter(
		# 								Time__icontains=form['Time'].value()
										
		# 	)
		if (category != ''):
			queryset = DayThree.objects.all()
			queryset = queryset.filter(Category_id=category)

			
			#ZINAISHIA HAPA ZA KUSEARCH ILA CONTEXT IPO KWA CHINI
		


			#HII NI CONTEXT KWA AJILI YA KUSEARCH ITEM OR CATEGORY KWENYE FORMYETU
		context ={
		#"QuerySet":QuerySet,
		"form":form,
		"queryset":queryset,
		
	}









	return render(request, 'LisheApp/DayThree/DayThreeItems.html', context)




def DayFourItems(request):
	queryset = DayFour.objects.all().order_by('id')
	form = DayFourSearchForm(request.POST or None)
	# # form ya kusearch
	# form = DayFourSearchForm(request.POST or None)
	# if request.method =="POST":
	# 	item = DayFour.objects.filter(Category__ItemName__icontains=form['Category'].value())


	context = {
		"queryset":queryset,
		"form":form,
	}

	#kwa ajili ya kufilter items and category ktk form
	if request.method == 'POST':
		#category__icontains=form['category'].value(),
		category = form['Category'].value()

		
#KAMA UNATAKA KUADD FIELD NYINGINE TUMIA HIYO YA CHINI
										
		# queryset = DayFour.objects.filter(
		# 								Time__icontains=form['Time'].value()
										
		# 	)
		if (category != ''):
			queryset = DayFour.objects.all()
			queryset = queryset.filter(Category_id=category)

			
			#ZINAISHIA HAPA ZA KUSEARCH ILA CONTEXT IPO KWA CHINI
		


			#HII NI CONTEXT KWA AJILI YA KUSEARCH ITEM OR CATEGORY KWENYE FORMYETU
		context ={
		#"QuerySet":QuerySet,
		"form":form,
		"queryset":queryset,
		
	}









	return render(request, 'LisheApp/DayFour/DayFourItems.html', context)





def DayFiveItems(request):
	queryset = DayFive.objects.all().order_by('id')
	form = DayFiveSearchForm(request.POST or None)
	# # form ya kusearch
	# form = DayFiveSearchForm(request.POST or None)
	# if request.method =="POST":
	# 	item = DayFive.objects.filter(Category__ItemName__icontains=form['Category'].value())


	context = {
		"queryset":queryset,
		"form":form,
	}

	#kwa ajili ya kufilter items and category ktk form
	if request.method == 'POST':
		#category__icontains=form['category'].value(),
		category = form['Category'].value()

		
#KAMA UNATAKA KUADD FIELD NYINGINE TUMIA HIYO YA CHINI
										
		# queryset = DayFive.objects.filter(
		# 								Time__icontains=form['Time'].value()
										
		# 	)
		if (category != ''):
			queryset = DayFive.objects.all()
			queryset = queryset.filter(Category_id=category)

			
			#ZINAISHIA HAPA ZA KUSEARCH ILA CONTEXT IPO KWA CHINI
		


			#HII NI CONTEXT KWA AJILI YA KUSEARCH ITEM OR CATEGORY KWENYE FORMYETU
		context ={
		#"QuerySet":QuerySet,
		"form":form,
		"queryset":queryset,
		
	}









	return render(request, 'LisheApp/DayFive/DayFiveItems.html', context)





def DaySixItems(request):
	queryset = DaySix.objects.all().order_by('id')
	form = DaySixSearchForm(request.POST or None)
	# # form ya kusearch
	# form = DaySixSearchForm(request.POST or None)
	# if request.method =="POST":
	# 	item = DaySix.objects.filter(Category__ItemName__icontains=form['Category'].value())


	context = {
		"queryset":queryset,
		"form":form,
	}

	#kwa ajili ya kufilter items and category ktk form
	if request.method == 'POST':
		#category__icontains=form['category'].value(),
		category = form['Category'].value()

		
#KAMA UNATAKA KUADD FIELD NYINGINE TUMIA HIYO YA CHINI
										
		# queryset = DaySix.objects.filter(
		# 								Time__icontains=form['Time'].value()
										
		# 	)
		if (category != ''):
			queryset = DaySix.objects.all()
			queryset = queryset.filter(Category_id=category)

			
			#ZINAISHIA HAPA ZA KUSEARCH ILA CONTEXT IPO KWA CHINI
		


			#HII NI CONTEXT KWA AJILI YA KUSEARCH ITEM OR CATEGORY KWENYE FORMYETU
		context ={
		#"QuerySet":QuerySet,
		"form":form,
		"queryset":queryset,
		
	}









	return render(request, 'LisheApp/DaySix/DaySixItems.html', context)







def DaySevenItems(request):
	queryset = DaySeven.objects.all().order_by('id')
	form = DaySevenSearchForm(request.POST or None)
	# # form ya kusearch
	# form = DaySevenSearchForm(request.POST or None)
	# if request.method =="POST":
	# 	item = DaySeven.objects.filter(Category__ItemName__icontains=form['Category'].value())


	context = {
		"queryset":queryset,
		"form":form,
	}

	#kwa ajili ya kufilter items and category ktk form
	if request.method == 'POST':
		#category__icontains=form['category'].value(),
		category = form['Category'].value()

		
#KAMA UNATAKA KUADD FIELD NYINGINE TUMIA HIYO YA CHINI
										
		# queryset = DaySeven.objects.filter(
		# 								Time__icontains=form['Time'].value()
										
		# 	)
		if (category != ''):
			queryset = DaySeven.objects.all()
			queryset = queryset.filter(Category_id=category)

			
			#ZINAISHIA HAPA ZA KUSEARCH ILA CONTEXT IPO KWA CHINI
		


			#HII NI CONTEXT KWA AJILI YA KUSEARCH ITEM OR CATEGORY KWENYE FORMYETU
		context ={
		#"QuerySet":QuerySet,
		"form":form,
		"queryset":queryset,
		
	}









	return render(request, 'LisheApp/DaySeven/DaySevenItems.html', context)




























#-----------------------------MWANZO WA ADD------------------------


#-----------------------------ADD LISHE ITEMS------------------------------

def AddLishe(request):
	form = LisheForm()


	if request.method == "POST":
		ItemName = request.POST.get('ItemName')
		form = LisheForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ItemName} Added Successfuly")
			return redirect('LisheItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('AddLishe')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/Lishe/AddLishe.html',context)



#-----------------------------ADD ELIMU YA LISHE ITEMS------------------------------

def AddElimuYaLishe(request):
	form = ElimuYaLisheForm()


	if request.method == "POST":
		Category = request.POST.get('Category')
		form = ElimuYaLisheForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{Category} Added Successfuly")
			return redirect('ElimuYaLisheItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('AddElimuYaLishe')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/ElimuYaLishe/AddElimuYaLishe.html',context)




#-----------------------ADD BIDHAA ZETU ITEMS---------------
def AddBidhaaZetu(request):
	form = BidhaaZetuForm()


	if request.method == "POST":
		ProductName = request.POST.get('ProductName')
		form = BidhaaZetuForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ProductName} Added Successfuly")
			return redirect('BidhaaZetuItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('AddBidhaaZetu')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/BidhaaZetu/AddBidhaaZetu.html',context)




#-----------------------ADD DAYS  ITEMS---------------
def AddDays(request):
	form = DaysForm()


	if request.method == "POST":
		DayName = request.POST.get('DayName')
		form = DaysForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{DayName} Added Successfuly")
			return redirect('DaysItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('AddDays')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/Days/AddDays.html',context)



#-----------------------ADD DAY oNE  ---------------
def AddDayOne(request):
	form = DayOneForm()


	if request.method == "POST":
		DayName = request.POST.get('DayName')
		form = DayOneForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"item for {DayName} Added Successfuly")
			return redirect('DayOneItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('AddDayOne')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/DayOne/AddDayOne.html',context)





#-----------------------ADD DAY TWO  ---------------
def AddDayTwo(request):
	form = DayTwoForm()


	if request.method == "POST":
		DayName = request.POST.get('DayName')
		form = DayTwoForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"item for {DayName} Added Successfuly")
			return redirect('DayTwoItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('AddDayTwo')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/DayTwo/AddDayTwo.html',context)


#-----------------------ADD DAY THREE  ---------------
def AddDayThree(request):
	form = DayThreeForm()


	if request.method == "POST":
		DayName = request.POST.get('DayName')
		form = DayThreeForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"item for {DayName} Added Successfuly")
			return redirect('DayThreeItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('AddDayThree')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/DayThree/AddDayThree.html',context)




#-----------------------ADD DAY FOUR  ---------------
def AddDayFour(request):
	form = DayFourForm()


	if request.method == "POST":
		DayName = request.POST.get('DayName')
		form = DayFourForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"item for {DayName} Added Successfuly")
			return redirect('DayFourItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('AddDayFour')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/DayFour/AddDayFour.html',context)


#-----------------------ADD DAY FIVE  ---------------
def AddDayFive(request):
	form = DayFiveForm()


	if request.method == "POST":
		DayName = request.POST.get('DayName')
		form = DayFiveForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"item for {DayName} Added Successfuly")
			return redirect('DayFiveItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('AddDayFive')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/DayFive/AddDayFive.html',context)




#-----------------------ADD DAY SIX  ---------------
def AddDaySix(request):
	form = DaySixForm()


	if request.method == "POST":
		DayName = request.POST.get('DayName')
		form = DaySixForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"item for {DayName} Added Successfuly")
			return redirect('DaySixItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('AddDaySix')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/DaySix/AddDaySix.html',context)


#-----------------------ADD DAY SEVEN  ---------------
def AddDaySeven(request):
	form = DaySevenForm()


	if request.method == "POST":
		DayName = request.POST.get('DayName')
		form = DaySevenForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"item for {DayName} Added Successfuly")
			return redirect('DaySevenItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('AddDaySeven')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/DaySeven/AddDaySeven.html',context)



#-----------------------ADD MAKUNDI YA CHAKULA  ---------------
def AddMakundiYaChakula(request):
	form = MakundiYaChakulaForm()


	if request.method == "POST":
		FoodCategory = request.POST.get('FoodCategory')
		form = MakundiYaChakulaForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{FoodCategory} Added Successfuly")
			return redirect('MakundiYaChakulaItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('AddMakundiYaChakula')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/MakundiYaChakula/AddMakundiYaChakula.html',context)





#-----------------------ADD POSTER NA PICHA  ---------------
def AddPosterNaPicha(request):
	form = PosterNaPichaForm()


	if request.method == "POST":
		
		form = PosterNaPichaForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"Item Added Successfuly")
			return redirect('PosterNaPichaItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('AddPosterNaPicha')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/PosterNaPicha/AddPosterNaPicha.html',context)























#-----------------------------MWANZO WA UPDATE------------------------

def UpdateLishe(request, id):
	x = get_object_or_404(Lishe, id=id)
	form = LisheForm(instance=x)


	if request.method == "POST":
		ItemName = request.POST.get('ItemName')
		form = LisheForm(request.POST or None, files=request.FILES, instance=x)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ItemName} Updated Successfuly")
			return redirect('LisheItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('UpdateLishe')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/Lishe/UpdateLishe.html',context)





#-----------------------------Update ELIMU YA LISHE ITEMS------------------------------

def UpdateElimuYaLishe(request,id):
	x = get_object_or_404(ElimuYaLishe, id=id)
	form = ElimuYaLisheForm(instance=x)
	



	if request.method == "POST":
		Category = request.POST.get('Category')
		form = ElimuYaLisheForm(request.POST or None, files=request.FILES,instance=x)
		if form.is_valid():
			form.save()
			messages.success(request, f"{Category} Updated Successfuly")
			return redirect('ElimuYaLisheItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('UpdateElimuYaLishe')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/ElimuYaLishe/UpdateElimuYaLishe.html',context)




#-----------------------Update BIDHAA ZETU ITEMS---------------
def UpdateBidhaaZetu(request, id):
	x = get_object_or_404(BidhaaZetu, id=id)
	form = BidhaaZetuForm(instance=x)

	


	if request.method == "POST":
		ProductName = request.POST.get('ProductName')
		form = BidhaaZetuForm(request.POST or None, files=request.FILES,instance=x)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ProductName} Updated Successfuly")
			return redirect('BidhaaZetuItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('UpdateBidhaaZetu')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/BidhaaZetu/UpdateBidhaaZetu.html',context)




#-----------------------Update DAYS  ITEMS---------------
def UpdateDays(request,id):
	x = get_object_or_404(Days, id=id)
	form = DaysForm(instance=x)
	


	if request.method == "POST":
		DayName = request.POST.get('DayName')
		form = DaysForm(request.POST or None, files=request.FILES,instance=x)
		if form.is_valid():
			form.save()
			messages.success(request, f"{DayName} Updated Successfuly")
			return redirect('DaysItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('UpdateDays')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/Days/UpdateDays.html',context)



#-----------------------Update DAY oNE  ---------------
def UpdateDayOne(request, id):
	x = get_object_or_404(DayOne, id=id)
	form = DayOneForm(instance=x)
	


	if request.method == "POST":
		DayName = request.POST.get('DayName')
		form = DayOneForm(request.POST or None, files=request.FILES,instance=x)
		if form.is_valid():
			form.save()
			messages.success(request, f"item for {DayName} Updated Successfuly")
			return redirect('DayOneItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('UpdateDayOne')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/DayOne/UpdateDayOne.html',context)





#-----------------------Update DAY TWO  ---------------
def UpdateDayTwo(request,id):
	x = get_object_or_404(DayTwo, id=id)
	form = DayTwoForm(instance=x)
	


	if request.method == "POST":
		DayName = request.POST.get('DayName')
		form = DayTwoForm(request.POST or None, files=request.FILES,instance=x)
		if form.is_valid():
			form.save()
			messages.success(request, f"item for {DayName} Updated Successfuly")
			return redirect('DayTwoItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('UpdateDayTwo')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/DayTwo/UpdateDayTwo.html',context)


#-----------------------Update DAY THREE  ---------------
def UpdateDayThree(request,id):
	x = get_object_or_404(DayThree, id=id)
	form = DayThreeForm(instance=x)
	


	if request.method == "POST":
		DayName = request.POST.get('DayName')
		form = DayThreeForm(request.POST or None, files=request.FILES,instance=x)
		if form.is_valid():
			form.save()
			messages.success(request, f"item for {DayName} Updated Successfuly")
			return redirect('DayThreeItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('UpdateDayThree')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/DayThree/UpdateDayThree.html',context)




#-----------------------Update DAY FOUR  ---------------
def UpdateDayFour(request,id):
	x = get_object_or_404(DayFour, id=id)
	form = DayFourForm(instance=x)
	


	if request.method == "POST":
		DayName = request.POST.get('DayName')
		form = DayFourForm(request.POST or None, files=request.FILES,instance=x)
		if form.is_valid():
			form.save()
			messages.success(request, f"item for {DayName} Updated Successfuly")
			return redirect('DayFourItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('UpdateDayFour')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/DayFour/UpdateDayFour.html',context)


#-----------------------Update DAY FIVE  ---------------
def UpdateDayFive(request,id):
	x = get_object_or_404(DayFive, id=id)
	form = DayFiveForm(instance=x)
	

	if request.method == "POST":
		DayName = request.POST.get('DayName')
		form = DayFiveForm(request.POST or None, files=request.FILES,instance=x)
		if form.is_valid():
			form.save()
			messages.success(request, f"item for {DayName} Updated Successfuly")
			return redirect('DayFiveItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('UpdateDayFive')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/DayFive/UpdateDayFive.html',context)




#-----------------------Update DAY SIX  ---------------
def UpdateDaySix(request,id):
	x = get_object_or_404(DaySix, id=id)
	form = DaySixForm(instance=x)
	


	if request.method == "POST":
		DayName = request.POST.get('DayName')
		form = DaySixForm(request.POST or None, files=request.FILES,instance=x)
		if form.is_valid():
			form.save()
			messages.success(request, f"item for {DayName} Updated Successfuly")
			return redirect('DaySixItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('UpdateDaySix')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/DaySix/UpdateDaySix.html',context)


#-----------------------Update DAY SEVEN  ---------------
def UpdateDaySeven(request,id):
	x = get_object_or_404(DaySeven, id=id)
	form = DaySevenForm(instance=x)
	

	if request.method == "POST":
		DayName = request.POST.get('DayName')
		form = DaySevenForm(request.POST or None, files=request.FILES,instance=x)
		if form.is_valid():
			form.save()
			messages.success(request, f"item for {DayName} Updated Successfuly")
			return redirect('DaySevenItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('UpdateDaySeven')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/DaySeven/UpdateDaySeven.html',context)



#-----------------------Update MAKUNDI YA CHAKULA  ---------------
def UpdateMakundiYaChakula(request,id):
	x = get_object_or_404(MakundiYaChakula, id=id)
	form = MakundiYaChakulaForm(instance=x)

	

	if request.method == "POST":
		FoodCategory = request.POST.get('FoodCategory')
		form = MakundiYaChakulaForm(request.POST or None, files=request.FILES,instance=x)
		if form.is_valid():
			form.save()
			messages.success(request, f"{FoodCategory} Updated Successfuly")
			return redirect('MakundiYaChakulaItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('UpdateMakundiYaChakula')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/MakundiYaChakula/UpdateMakundiYaChakula.html',context)





#-----------------------Update POSTER NA PICHA  ---------------
def UpdatePosterNaPicha(request,id):
	x = get_object_or_404(PosterNaPicha, id=id)
	form = PosterNaPichaForm(instance=x)
	


	if request.method == "POST":
		
		form = PosterNaPichaForm(request.POST or None, files=request.FILES,instance=x)
		if form.is_valid():
			form.save()
			messages.success(request, f"Item Updated Successfuly")
			return redirect('PosterNaPichaItems')

		messages.info(request, "There is a problem when you are creating a new item")
		return redirect('UpdatePosterNaPicha')


	context = {
		"form":form,
	}

	return render(request, 'LisheApp/PosterNaPicha/UpdatePosterNaPicha.html',context)






















#-----------------------SEARCH AUTOCOMPLETE--------------------------

def Lishe_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(ItemName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    item = Lishe.objects.filter(search)
    mylist= []
    mylist += [x.ItemName for x in item]
    return JsonResponse(mylist, safe=False)


def ElimuYaLishe_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(Category__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    item = ElimuYaLishe.objects.filter(search)
    mylist= []
    mylist += [x.Category for x in item]
    return JsonResponse(mylist, safe=False)


def BidhaaZetu_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(ProductName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    item = BidhaaZetu.objects.filter(search)
    mylist= []
    mylist += [x.ProductName for x in item]
    return JsonResponse(mylist, safe=False)


def Days_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(DayName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    item = Days.objects.filter(search)
    mylist= []
    mylist += [x.DayName for x in item]
    return JsonResponse(mylist, safe=False)


def DayOne_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(DayName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    item = DayOne.objects.filter(search)
    mylist= []
    mylist += [x.DayName for x in item]
    return JsonResponse(mylist, safe=False)

def DayTwo_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(DayName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    item = DayTwo.objects.filter(search)
    mylist= []
    mylist += [x.DayName for x in item]
    return JsonResponse(mylist, safe=False)


def DayThree_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(DayName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    item = DayThree.objects.filter(search)
    mylist= []
    mylist += [x.DayName for x in item]
    return JsonResponse(mylist, safe=False)


def DayFour_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(DayName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    item = DayFour.objects.filter(search)
    mylist= []
    mylist += [x.DayName for x in item]
    return JsonResponse(mylist, safe=False)


def DayFive_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(DayName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    item = DayFive.objects.filter(search)
    mylist= []
    mylist += [x.DayName for x in item]
    return JsonResponse(mylist, safe=False)


def DaySix_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(DayName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    item = DaySix.objects.filter(search)
    mylist= []
    mylist += [x.DayName for x in item]
    return JsonResponse(mylist, safe=False)


def DaySeven_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(DayName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    item = DaySeven.objects.filter(search)
    mylist= []
    mylist += [x.DayName for x in item]
    return JsonResponse(mylist, safe=False)


def MakundiYaChakula_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(FoodCategory__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    item = MakundiYaChakula.objects.filter(search)
    mylist= []
    mylist += [x.FoodCategory for x in item]
    return JsonResponse(mylist, safe=False)






















#----------------------MWANZO WA DELETE------------------------------------

def DeleteLishe(request,id):
	item = get_object_or_404(Lishe, id=id)
	item.delete()
	messages.success(request, f"Item Deleted Successfuly")
	return redirect('LisheItems')
		
def DeleteElimuYaLishe(request,id):
	item = get_object_or_404(ElimuYaLishe, id=id)
	item.delete()
	messages.success(request, f"Item Deleted Successfuly")
	return redirect('ElimuYaLisheItems')

def DeleteBidhaaZetu(request,id):
	item = get_object_or_404(BidhaaZetu, id=id)
	item.delete()
	messages.success(request, f"Item Deleted Successfuly")
	return redirect('BidhaaZetuItems')


def DeleteDays(request,id):
	item = get_object_or_404(Days, id=id)
	item.delete()
	messages.success(request, f"Item Deleted Successfuly")
	return redirect('DaysItems')

def DeleteDayOne(request,id):
	item = get_object_or_404(DayOne, id=id)
	item.delete()
	messages.success(request, f"Item Deleted Successfuly")
	return redirect('DayOneItems')


def DeleteDayTwo(request,id):
	item = get_object_or_404(DayTwo, id=id)
	item.delete()
	messages.success(request, f"Item Deleted Successfuly")
	return redirect('DayTwoItems')

def DeleteDayThree(request,id):
	item = get_object_or_404(DayThree, id=id)
	item.delete()
	messages.success(request, f"Item Deleted Successfuly")
	return redirect('DayThreeItems')

def DeleteDayFour(request,id):
	item = get_object_or_404(DayFour, id=id)
	item.delete()
	messages.success(request, f"Item Deleted Successfuly")
	return redirect('DayFourItems')

def DeleteDayFive(request,id):
	item = get_object_or_404(DayFive, id=id)
	item.delete()
	messages.success(request, f"Item Deleted Successfuly")
	return redirect('DayFiveItems')

def DeleteDaySix(request,id):
	item = get_object_or_404(DaySix, id=id)
	item.delete()
	messages.success(request, f"Item Deleted Successfuly")
	return redirect('DaySixItems')

def DeleteDaySeven(request,id):
	item = get_object_or_404(DaySeven, id=id)
	item.delete()
	messages.success(request, f"Item Deleted Successfuly")
	return redirect('DaySevenItems')


def DeleteMakundiYaChakula(request,id):
	item = get_object_or_404(MakundiYaChakula, id=id)
	item.delete()
	messages.success(request, f"Item Deleted Successfuly")
	return redirect('MakundiYaChakulaItems')


def DeletePosterNaPicha(request,id):
	item = get_object_or_404(PosterNaPicha, id=id)
	item.delete()
	messages.success(request, f"Item Deleted Successfuly")
	return redirect('PosterNaPichaItems')






