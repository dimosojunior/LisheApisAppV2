from django.urls import path
from . import views

# MWANZO IN ORDER TO USE MODEL VIEW SET
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Lishe', views.LisheViewSet)
router.register('ElimuYaLishe', views.ElimuYaLisheViewSet)
router.register('BidhaaZetu', views.BidhaaZetuViewSet)
router.register('MakundiYaChakula', views.MakundiYaChakulaViewSet)
router.register('PosterNaPicha', views.PosterNaPichaViewSet)

router.register('Days', views.DaysViewSet)


#WATOTO DAYS URLS
router.register('WatotoDayOne', views.WatotoDayOneViewSet)
router.register('WatotoDayTwo', views.WatotoDayTwoViewSet)
router.register('WatotoDayThree', views.WatotoDayThreeViewSet)
router.register('WatotoDayFour', views.WatotoDayFourViewSet)
router.register('WatotoDayFive', views.WatotoDayFiveViewSet)
router.register('WatotoDaySix', views.WatotoDaySixViewSet)
router.register('WatotoDaySeven', views.WatotoDaySevenViewSet)



#FAMILIA DAYS URLS
router.register('FamiliaDayOne', views.FamiliaDayOneViewSet)
router.register('FamiliaDayTwo', views.FamiliaDayTwoViewSet)
router.register('FamiliaDayThree', views.FamiliaDayThreeViewSet)
router.register('FamiliaDayFour', views.FamiliaDayFourViewSet)
router.register('FamiliaDayFive', views.FamiliaDayFiveViewSet)
router.register('FamiliaDaySix', views.FamiliaDaySixViewSet)
router.register('FamiliaDaySeven', views.FamiliaDaySevenViewSet)



#KISUKARI DAYS URLS
router.register('KisukariDayOne', views.KisukariDayOneViewSet)
router.register('KisukariDayTwo', views.KisukariDayTwoViewSet)
router.register('KisukariDayThree', views.KisukariDayThreeViewSet)
router.register('KisukariDayFour', views.KisukariDayFourViewSet)
router.register('KisukariDayFive', views.KisukariDayFiveViewSet)
router.register('KisukariDaySix', views.KisukariDaySixViewSet)
router.register('KisukariDaySeven', views.KisukariDaySevenViewSet)




#HIV DAYS URLS
router.register('HivDayOne', views.HivDayOneViewSet)
router.register('HivDayTwo', views.HivDayTwoViewSet)
router.register('HivDayThree', views.HivDayThreeViewSet)
router.register('HivDayFour', views.HivDayFourViewSet)
router.register('HivDayFive', views.HivDayFiveViewSet)
router.register('HivDaySix', views.HivDaySixViewSet)
router.register('HivDaySeven', views.HivDaySevenViewSet)







#WAJAWAZITO DAYS URLS
router.register('WajawazitoDayOne', views.WajawazitoDayOneViewSet)
router.register('WajawazitoDayTwo', views.WajawazitoDayTwoViewSet)
router.register('WajawazitoDayThree', views.WajawazitoDayThreeViewSet)
router.register('WajawazitoDayFour', views.WajawazitoDayFourViewSet)
router.register('WajawazitoDayFive', views.WajawazitoDayFiveViewSet)
router.register('WajawazitoDaySix', views.WajawazitoDaySixViewSet)
router.register('WajawazitoDaySeven', views.WajawazitoDaySevenViewSet)




#UZITO ZAIDI DAYS URLS
router.register('UzitoZaidiDayOne', views.UzitoZaidiDayOneViewSet)
router.register('UzitoZaidiDayTwo', views.UzitoZaidiDayTwoViewSet)
router.register('UzitoZaidiDayThree', views.UzitoZaidiDayThreeViewSet)
router.register('UzitoZaidiDayFour', views.UzitoZaidiDayFourViewSet)
router.register('UzitoZaidiDayFive', views.UzitoZaidiDayFiveViewSet)
router.register('UzitoZaidiDaySix', views.UzitoZaidiDaySixViewSet)
router.register('UzitoZaidiDaySeven', views.UzitoZaidiDaySevenViewSet)





# WATOTO DAYS

# WATOTO DAY ONE
router.register('WatotoDayOne', views.WatotoDayOneViewSet)











urlpatterns = router.urls