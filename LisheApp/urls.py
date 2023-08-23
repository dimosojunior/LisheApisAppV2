
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('LisheItems/', views.LisheItems, name="LisheItems"),
    path('ElimuYaLisheItems/', views.ElimuYaLisheItems, name="ElimuYaLisheItems"),
    path('BidhaaZetuItems/', views.BidhaaZetuItems, name="BidhaaZetuItems"),
    path('MakundiYaChakulaItems/', views.MakundiYaChakulaItems, name="MakundiYaChakulaItems"),
    path('PosterNaPichaItems/', views.PosterNaPichaItems, name="PosterNaPichaItems"),

    path('DayOneItems/', views.DayOneItems, name="DayOneItems"),
    path('DayTwoItems/', views.DayTwoItems, name="DayTwoItems"),
    path('DayThreeItems/', views.DayThreeItems, name="DayThreeItems"),
    path('DayFourItems/', views.DayFourItems, name="DayFourItems"),
    path('DayFiveItems/', views.DayFiveItems, name="DayFiveItems"),
    path('DaySixItems/', views.DaySixItems, name="DaySixItems"),
    path('DaySevenItems/', views.DaySevenItems, name="DaySevenItems"),






    path('AddLishe/', views.AddLishe, name="AddLishe"),
    path('AddElimuYaLishe/', views.AddElimuYaLishe, name="AddElimuYaLishe"),
    path('AddBidhaaZetu/', views.AddBidhaaZetu, name="AddBidhaaZetu"),
    path('AddDays/', views.AddDays, name="AddDays"),
    path('AddDayOne/', views.AddDayOne, name="AddDayOne"),
    path('AddDayTwo/', views.AddDayTwo, name="AddDayTwo"),
    path('AddDayThree/', views.AddDayThree, name="AddDayThree"),
    path('AddDayFour/', views.AddDayFour, name="AddDayFour"),
    path('AddDayFive/', views.AddDayFive, name="AddDayFive"),
    path('AddDaySix/', views.AddDaySix, name="AddDaySix"),
    path('AddDaySeven/', views.AddDaySeven, name="AddDaySeven"),
    path('AddMakundiYaChakula/', views.AddMakundiYaChakula, name="AddMakundiYaChakula"),
    path('AddPosterNaPicha/', views.AddPosterNaPicha, name="AddPosterNaPicha"),




    path('UpdateLishe/<int:id>/', views.UpdateLishe, name="UpdateLishe"),
    path('UpdateElimuYaLishe/<int:id>/', views.UpdateElimuYaLishe, name="UpdateElimuYaLishe"),
    path('UpdateBidhaaZetu/<int:id>/', views.UpdateBidhaaZetu, name="UpdateBidhaaZetu"),
    path('UpdateDays/<int:id>/', views.UpdateDays, name="UpdateDays"),
    path('UpdateDayOne/<int:id>/', views.UpdateDayOne, name="UpdateDayOne"),
    path('UpdateDayTwo/<int:id>/', views.UpdateDayTwo, name="UpdateDayTwo"),
    path('UpdateDayThree/<int:id>/', views.UpdateDayThree, name="UpdateDayThree"),
    path('UpdateDayFour/<int:id>/', views.UpdateDayFour, name="UpdateDayFour"),
    path('UpdateDayFive/<int:id>/', views.UpdateDayFive, name="UpdateDayFive"),
    path('UpdateDaySix/<int:id>/', views.UpdateDaySix, name="UpdateDaySix"),
    path('UpdateDaySeven/<int:id>/', views.UpdateDaySeven, name="UpdateDaySeven"),
    path('UpdateMakundiYaChakula/<int:id>/', views.UpdateMakundiYaChakula, name="UpdateMakundiYaChakula"),
    path('UpdatePosterNaPicha/<int:id>/', views.UpdatePosterNaPicha, name="UpdatePosterNaPicha"),
    



    path('DeleteLishe/<int:id>/', views.DeleteLishe, name="DeleteLishe"),
    path('DeleteElimuYaLishe/<int:id>/', views.DeleteElimuYaLishe, name="DeleteElimuYaLishe"),
    path('DeleteBidhaaZetu/<int:id>/', views.DeleteBidhaaZetu, name="DeleteBidhaaZetu"),
    path('DeleteDays/<int:id>/', views.DeleteDays, name="DeleteDays"),
    path('DeleteDayOne/<int:id>/', views.DeleteDayOne, name="DeleteDayOne"),
    path('DeleteDayTwo/<int:id>/', views.DeleteDayTwo, name="DeleteDayTwo"),
    path('DeleteDayThree/<int:id>/', views.DeleteDayThree, name="DeleteDayThree"),
    path('DeleteDayFour/<int:id>/', views.DeleteDayFour, name="DeleteDayFour"),
    path('DeleteDayFive/<int:id>/', views.DeleteDayFive, name="DeleteDayFive"),
    path('DeleteDaySix/<int:id>/', views.DeleteDaySix, name="DeleteDaySix"),
    path('DeleteDaySeven/<int:id>/', views.DeleteDaySeven, name="DeleteDaySeven"),
    path('DeleteMakundiYaChakula/<int:id>/', views.DeleteMakundiYaChakula, name="DeleteMakundiYaChakula"),
    path('DeletePosterNaPicha/<int:id>/', views.DeletePosterNaPicha, name="DeletePosterNaPicha"),









    path('Lishe_search_autocomplete/', views.Lishe_search_autocomplete, name="Lishe_search_autocomplete"),
    path('ElimuYaLishe_search_autocomplete/', views.ElimuYaLishe_search_autocomplete, name="ElimuYaLishe_search_autocomplete"),
    path('BidhaaZetu_search_autocomplete/', views.BidhaaZetu_search_autocomplete, name="BidhaaZetu_search_autocomplete"),
    path('Days_search_autocomplete/', views.Days_search_autocomplete, name="Days_search_autocomplete"),
    path('DayOne_search_autocomplete/', views.DayOne_search_autocomplete, name="DayOne_search_autocomplete"),
    path('DayTwo_search_autocomplete/', views.DayTwo_search_autocomplete, name="DayTwo_search_autocomplete"),
    path('DayThree_search_autocomplete/', views.DayThree_search_autocomplete, name="DayThree_search_autocomplete"),
    path('DayFour_search_autocomplete/', views.DayFour_search_autocomplete, name="DayFour_search_autocomplete"),
    path('DayFive_search_autocomplete/', views.DayFive_search_autocomplete, name="DayFive_search_autocomplete"),
    path('DaySix_search_autocomplete/', views.DaySix_search_autocomplete, name="DaySix_search_autocomplete"),
    path('DaySeven_search_autocomplete/', views.DaySeven_search_autocomplete, name="DaySeven_search_autocomplete"),
    path('MakundiYaChakula_search_autocomplete/', views.MakundiYaChakula_search_autocomplete, name="MakundiYaChakula_search_autocomplete"),




]
