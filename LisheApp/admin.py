from django.contrib import admin
from LisheApp.models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# class MyUserAdmin(BaseUserAdmin):
#     list_display=('username', 'email', 'company_name', 'date_joined', 'last_login', 'is_admin', 'is_active')
#     search_fields=('email', 'first_name', 'last_name')
#     readonly_fields=('date_joined', 'last_login')
#     filter_horizontal=()
#     list_filter=('last_login',)
#     fieldsets=()

#     add_fieldsets=(
#         (None,{
#             'classes':('wide'),
#             'fields':('email', 'username', 'first_name', 'middle_name', 'last_name', 'company_name', 'phone', 'password1', 'password2'),
#         }),
#     )

#     ordering=('email',)



# admin.site.register(MyUser, MyUserAdmin)


class LisheAdmin(admin.ModelAdmin):

    list_display = ["ItemName","status","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["ItemName"]

class ElimuYaLisheAdmin(admin.ModelAdmin):

    list_display = ["Category","status","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["Category"]


class BidhaaZetuAdmin(admin.ModelAdmin):

    list_display = ["ProductName","status","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["ProductName"]


class DaysAdmin(admin.ModelAdmin):

    list_display = ["DayName","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["DayName"]

#WATOTO DAYS
class DayOneAdmin(admin.ModelAdmin):

    list_display = ["Time", "Category", "DayName", "Created","Updated"]
    list_filter =["Category"]
    search_fields = ["DayName"]

class DayTwoAdmin(admin.ModelAdmin):

    list_display = ["Time", "Category", "DayName", "Created","Updated"]
    list_filter =["Category"]
    search_fields = ["DayName"]

class DayThreeAdmin(admin.ModelAdmin):

    list_display = ["Time", "Category", "DayName", "Created","Updated"]
    list_filter =["Category"]
    search_fields = ["DayName"]


class DayFourAdmin(admin.ModelAdmin):

    list_display = ["Time", "Category", "DayName", "Created","Updated"]
    list_filter =["Category"]
    search_fields = ["DayName"]


class DayFiveAdmin(admin.ModelAdmin):

    list_display = ["Time", "Category", "DayName", "Created","Updated"]
    list_filter =["Category"]
    search_fields = ["DayName"]

class DaySixAdmin(admin.ModelAdmin):

    list_display = ["Time", "Category", "DayName", "Created","Updated"]
    list_filter =["Category"]
    search_fields = ["DayName"]


class DaySevenAdmin(admin.ModelAdmin):

    list_display = ["Time", "Category", "DayName", "Created","Updated"]
    list_filter =["Category"]
    search_fields = ["DayName"]




class MakundiYaChakulaAdmin(admin.ModelAdmin):

    list_display = ["FoodCategory","status","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["FoodCategory"]

# class VyakulaAdmin(admin.ModelAdmin):

#     list_display = ["Name","Created","Updated"]
#     list_filter =["Created","Updated"]
#     search_fields = ["Name"]


class PosterNaPichaAdmin(admin.ModelAdmin):

    list_display = ["Image","status","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["Created"]





class TaarifaZaUjauzitoAdmin(admin.ModelAdmin):
    list_display = ["Title","Week","Created","Updated"]
    list_filter =["Created","Updated","Week"]
    search_fields = ["Created"]

class TaarifaZaUzitoZaidiAdmin(admin.ModelAdmin):
    list_display = ["Title","Week","Created","Updated"]
    list_filter =["Created","Updated","Week"]
    search_fields = ["Created"]

class TaarifaZaWatotoAdmin(admin.ModelAdmin):
    list_display = ["Title","Week","Created","Updated"]
    list_filter =["Created","Updated","Week"]
    search_fields = ["Created"]

class TaarifaZaKisukariAdmin(admin.ModelAdmin):
    list_display = ["Title","Week","Created","Updated"]
    list_filter =["Created","Updated","Week"]
    search_fields = ["Created"]

class TaarifaZaHivAdmin(admin.ModelAdmin):
    list_display = ["Title","Week","Created","Updated"]
    list_filter =["Created","Updated","Week"]
    search_fields = ["Created"]

class TaarifaZaFamiliaAdmin(admin.ModelAdmin):
    list_display = ["Title","Week","Created","Updated"]
    list_filter =["Created","Updated","Week"]
    search_fields = ["Created"]

class WeeksAdmin(admin.ModelAdmin):

    list_display = ["WeekName","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["Created"]

class JeWajuaAdmin(admin.ModelAdmin):

    list_display = ["Title","Category","Week","Created","Updated"]
    list_filter =["Created","Category","Week"]
    search_fields = ["Created"]

class Week1Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week2Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week3Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]


class Week4Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week5Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]


class Week6Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week7Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week8Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]



class Week9Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week10Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]


class Week11Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week12Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week13Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]


class Week14Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week15Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]


class Week16Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week17Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week18Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]



class Week19Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week20Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week21Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week22Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week23Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]


class Week24Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week25Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]


class Week26Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week27Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week28Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]



class Week29Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week30Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week31Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week32Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week33Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]


class Week34Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week35Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]


class Week36Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week37Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week38Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]



class Week39Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week40Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week41Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week42Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week43Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]


class Week44Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]

class Week45Admin(admin.ModelAdmin):

    list_display = ["Time","Category","WeekName","Created","Updated"]
    list_filter =["Created","Category","Time"]
    search_fields = ["Created"]



admin.site.register(Token)
admin.site.register(Setting)

admin.site.register(Lishe, LisheAdmin)
admin.site.register(ElimuYaLishe, ElimuYaLisheAdmin)
admin.site.register(BidhaaZetu, BidhaaZetuAdmin)
admin.site.register(Days, DaysAdmin)


#WATOTO DAYS
admin.site.register(DayOne, DayOneAdmin)
admin.site.register(DayTwo, DayTwoAdmin)
admin.site.register(DayThree, DayThreeAdmin)
admin.site.register(DayFour, DayFourAdmin)
admin.site.register(DayFive, DayFiveAdmin)
admin.site.register(DaySix, DaySixAdmin)
admin.site.register(DaySeven, DaySevenAdmin)


admin.site.register(MakundiYaChakula, MakundiYaChakulaAdmin)
# admin.site.register(Vyakula, VyakulaAdmin)


admin.site.register(PosterNaPicha, PosterNaPichaAdmin)





admin.site.register(TaarifaZaUjauzito, TaarifaZaUjauzitoAdmin)
admin.site.register(TaarifaZaUzitoZaidi, TaarifaZaUzitoZaidiAdmin)
admin.site.register(TaarifaZaWatoto, TaarifaZaWatotoAdmin)
admin.site.register(TaarifaZaKisukari, TaarifaZaKisukariAdmin)
admin.site.register(TaarifaZaHiv, TaarifaZaHivAdmin)
admin.site.register(TaarifaZaFamilia, TaarifaZaFamiliaAdmin)

admin.site.register(Weeks, WeeksAdmin)
admin.site.register(JeWajua, JeWajuaAdmin)


admin.site.register(Week1, Week1Admin)
admin.site.register(Week2, Week2Admin)
admin.site.register(Week3, Week3Admin)
admin.site.register(Week4, Week4Admin)
admin.site.register(Week5, Week5Admin)
admin.site.register(Week6, Week6Admin)
admin.site.register(Week7, Week7Admin)
admin.site.register(Week8, Week8Admin)
admin.site.register(Week9, Week9Admin)
admin.site.register(Week10, Week10Admin)

admin.site.register(Week11, Week11Admin)
admin.site.register(Week12, Week12Admin)
admin.site.register(Week13, Week13Admin)
admin.site.register(Week14, Week14Admin)
admin.site.register(Week15, Week15Admin)
admin.site.register(Week16, Week16Admin)
admin.site.register(Week17, Week17Admin)
admin.site.register(Week18, Week18Admin)
admin.site.register(Week19, Week19Admin)
admin.site.register(Week20, Week20Admin)

admin.site.register(Week21, Week21Admin)
admin.site.register(Week22, Week22Admin)
admin.site.register(Week23, Week23Admin)
admin.site.register(Week24, Week24Admin)
admin.site.register(Week25, Week25Admin)
admin.site.register(Week26, Week26Admin)
admin.site.register(Week27, Week27Admin)
admin.site.register(Week28, Week28Admin)
admin.site.register(Week29, Week29Admin)
admin.site.register(Week30, Week30Admin)

admin.site.register(Week31, Week31Admin)
admin.site.register(Week32, Week32Admin)
admin.site.register(Week33, Week33Admin)
admin.site.register(Week34, Week34Admin)
admin.site.register(Week35, Week35Admin)
admin.site.register(Week36, Week36Admin)
admin.site.register(Week37, Week37Admin)
admin.site.register(Week38, Week38Admin)
admin.site.register(Week39, Week39Admin)
admin.site.register(Week40, Week40Admin)

admin.site.register(Week41, Week41Admin)
admin.site.register(Week42, Week42Admin)
admin.site.register(Week43, Week43Admin)
admin.site.register(Week44, Week44Admin)
admin.site.register(Week45, Week45Admin)
