from django.urls import path
from . import views

# MWANZO IN ORDER TO USE MODEL VIEW SET
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Weeks', views.WeeksViewSet)

router.register('TaarifaZaUjauzitoWeek1', views.TaarifaZaUjauzitoWeek1ViewSet)
router.register('TaarifaZaUjauzitoWeek2', views.TaarifaZaUjauzitoWeek2ViewSet)
router.register('TaarifaZaUjauzitoWeek3', views.TaarifaZaUjauzitoWeek3ViewSet)
router.register('TaarifaZaUjauzitoWeek4', views.TaarifaZaUjauzitoWeek4ViewSet)
router.register('TaarifaZaUjauzitoWeek5', views.TaarifaZaUjauzitoWeek5ViewSet)
router.register('TaarifaZaUjauzitoWeek6', views.TaarifaZaUjauzitoWeek6ViewSet)
router.register('TaarifaZaUjauzitoWeek7', views.TaarifaZaUjauzitoWeek7ViewSet)
router.register('TaarifaZaUjauzitoWeek8', views.TaarifaZaUjauzitoWeek8ViewSet)
router.register('TaarifaZaUjauzitoWeek9', views.TaarifaZaUjauzitoWeek9ViewSet)
router.register('TaarifaZaUjauzitoWeek10', views.TaarifaZaUjauzitoWeek10ViewSet)

router.register('TaarifaZaUjauzitoWeek11', views.TaarifaZaUjauzitoWeek11ViewSet)
router.register('TaarifaZaUjauzitoWeek12', views.TaarifaZaUjauzitoWeek12ViewSet)
router.register('TaarifaZaUjauzitoWeek13', views.TaarifaZaUjauzitoWeek13ViewSet)
router.register('TaarifaZaUjauzitoWeek14', views.TaarifaZaUjauzitoWeek14ViewSet)
router.register('TaarifaZaUjauzitoWeek15', views.TaarifaZaUjauzitoWeek15ViewSet)
router.register('TaarifaZaUjauzitoWeek16', views.TaarifaZaUjauzitoWeek16ViewSet)
router.register('TaarifaZaUjauzitoWeek17', views.TaarifaZaUjauzitoWeek17ViewSet)
router.register('TaarifaZaUjauzitoWeek18', views.TaarifaZaUjauzitoWeek18ViewSet)
router.register('TaarifaZaUjauzitoWeek19', views.TaarifaZaUjauzitoWeek19ViewSet)
router.register('TaarifaZaUjauzitoWeek20', views.TaarifaZaUjauzitoWeek20ViewSet)

router.register('TaarifaZaUjauzitoWeek21', views.TaarifaZaUjauzitoWeek21ViewSet)
router.register('TaarifaZaUjauzitoWeek22', views.TaarifaZaUjauzitoWeek22ViewSet)
router.register('TaarifaZaUjauzitoWeek23', views.TaarifaZaUjauzitoWeek23ViewSet)
router.register('TaarifaZaUjauzitoWeek24', views.TaarifaZaUjauzitoWeek24ViewSet)
router.register('TaarifaZaUjauzitoWeek25', views.TaarifaZaUjauzitoWeek25ViewSet)
router.register('TaarifaZaUjauzitoWeek26', views.TaarifaZaUjauzitoWeek26ViewSet)
router.register('TaarifaZaUjauzitoWeek27', views.TaarifaZaUjauzitoWeek27ViewSet)
router.register('TaarifaZaUjauzitoWeek28', views.TaarifaZaUjauzitoWeek28ViewSet)
router.register('TaarifaZaUjauzitoWeek29', views.TaarifaZaUjauzitoWeek29ViewSet)
router.register('TaarifaZaUjauzitoWeek30', views.TaarifaZaUjauzitoWeek30ViewSet)

router.register('TaarifaZaUjauzitoWeek31', views.TaarifaZaUjauzitoWeek31ViewSet)
router.register('TaarifaZaUjauzitoWeek32', views.TaarifaZaUjauzitoWeek32ViewSet)
router.register('TaarifaZaUjauzitoWeek33', views.TaarifaZaUjauzitoWeek33ViewSet)
router.register('TaarifaZaUjauzitoWeek34', views.TaarifaZaUjauzitoWeek34ViewSet)
router.register('TaarifaZaUjauzitoWeek35', views.TaarifaZaUjauzitoWeek35ViewSet)
router.register('TaarifaZaUjauzitoWeek36', views.TaarifaZaUjauzitoWeek36ViewSet)
router.register('TaarifaZaUjauzitoWeek37', views.TaarifaZaUjauzitoWeek37ViewSet)
router.register('TaarifaZaUjauzitoWeek38', views.TaarifaZaUjauzitoWeek38ViewSet)
router.register('TaarifaZaUjauzitoWeek39', views.TaarifaZaUjauzitoWeek39ViewSet)
router.register('TaarifaZaUjauzitoWeek40', views.TaarifaZaUjauzitoWeek40ViewSet)

router.register('TaarifaZaUjauzitoWeek41', views.TaarifaZaUjauzitoWeek41ViewSet)
router.register('TaarifaZaUjauzitoWeek42', views.TaarifaZaUjauzitoWeek42ViewSet)
router.register('TaarifaZaUjauzitoWeek43', views.TaarifaZaUjauzitoWeek43ViewSet)
router.register('TaarifaZaUjauzitoWeek44', views.TaarifaZaUjauzitoWeek44ViewSet)
router.register('TaarifaZaUjauzitoWeek45', views.TaarifaZaUjauzitoWeek45ViewSet)



router.register('JeWajuaWajawazitoWeek1', views.JeWajuaWajawazitoWeek1ViewSet)
router.register('JeWajuaWajawazitoWeek2', views.JeWajuaWajawazitoWeek2ViewSet)
router.register('JeWajuaWajawazitoWeek3', views.JeWajuaWajawazitoWeek3ViewSet)
router.register('JeWajuaWajawazitoWeek4', views.JeWajuaWajawazitoWeek4ViewSet)
router.register('JeWajuaWajawazitoWeek5', views.JeWajuaWajawazitoWeek5ViewSet)
router.register('JeWajuaWajawazitoWeek6', views.JeWajuaWajawazitoWeek6ViewSet)
router.register('JeWajuaWajawazitoWeek7', views.JeWajuaWajawazitoWeek7ViewSet)
router.register('JeWajuaWajawazitoWeek8', views.JeWajuaWajawazitoWeek8ViewSet)
router.register('JeWajuaWajawazitoWeek9', views.JeWajuaWajawazitoWeek9ViewSet)
router.register('JeWajuaWajawazitoWeek10', views.JeWajuaWajawazitoWeek10ViewSet)

router.register('JeWajuaWajawazitoWeek11', views.JeWajuaWajawazitoWeek11ViewSet)
router.register('JeWajuaWajawazitoWeek12', views.JeWajuaWajawazitoWeek12ViewSet)
router.register('JeWajuaWajawazitoWeek13', views.JeWajuaWajawazitoWeek13ViewSet)
router.register('JeWajuaWajawazitoWeek14', views.JeWajuaWajawazitoWeek14ViewSet)
router.register('JeWajuaWajawazitoWeek15', views.JeWajuaWajawazitoWeek15ViewSet)
router.register('JeWajuaWajawazitoWeek16', views.JeWajuaWajawazitoWeek16ViewSet)
router.register('JeWajuaWajawazitoWeek17', views.JeWajuaWajawazitoWeek17ViewSet)
router.register('JeWajuaWajawazitoWeek18', views.JeWajuaWajawazitoWeek18ViewSet)
router.register('JeWajuaWajawazitoWeek19', views.JeWajuaWajawazitoWeek19ViewSet)
router.register('JeWajuaWajawazitoWeek20', views.JeWajuaWajawazitoWeek20ViewSet)

router.register('JeWajuaWajawazitoWeek21', views.JeWajuaWajawazitoWeek21ViewSet)
router.register('JeWajuaWajawazitoWeek22', views.JeWajuaWajawazitoWeek22ViewSet)
router.register('JeWajuaWajawazitoWeek23', views.JeWajuaWajawazitoWeek23ViewSet)
router.register('JeWajuaWajawazitoWeek24', views.JeWajuaWajawazitoWeek24ViewSet)
router.register('JeWajuaWajawazitoWeek25', views.JeWajuaWajawazitoWeek25ViewSet)
router.register('JeWajuaWajawazitoWeek26', views.JeWajuaWajawazitoWeek26ViewSet)
router.register('JeWajuaWajawazitoWeek27', views.JeWajuaWajawazitoWeek27ViewSet)
router.register('JeWajuaWajawazitoWeek28', views.JeWajuaWajawazitoWeek28ViewSet)
router.register('JeWajuaWajawazitoWeek29', views.JeWajuaWajawazitoWeek29ViewSet)
router.register('JeWajuaWajawazitoWeek30', views.JeWajuaWajawazitoWeek30ViewSet)

router.register('JeWajuaWajawazitoWeek31', views.JeWajuaWajawazitoWeek31ViewSet)
router.register('JeWajuaWajawazitoWeek32', views.JeWajuaWajawazitoWeek32ViewSet)
router.register('JeWajuaWajawazitoWeek33', views.JeWajuaWajawazitoWeek33ViewSet)
router.register('JeWajuaWajawazitoWeek34', views.JeWajuaWajawazitoWeek34ViewSet)
router.register('JeWajuaWajawazitoWeek35', views.JeWajuaWajawazitoWeek35ViewSet)
router.register('JeWajuaWajawazitoWeek36', views.JeWajuaWajawazitoWeek36ViewSet)
router.register('JeWajuaWajawazitoWeek37', views.JeWajuaWajawazitoWeek37ViewSet)
router.register('JeWajuaWajawazitoWeek38', views.JeWajuaWajawazitoWeek38ViewSet)
router.register('JeWajuaWajawazitoWeek39', views.JeWajuaWajawazitoWeek39ViewSet)
router.register('JeWajuaWajawazitoWeek40', views.JeWajuaWajawazitoWeek40ViewSet)

router.register('JeWajuaWajawazitoWeek41', views.JeWajuaWajawazitoWeek41ViewSet)
router.register('JeWajuaWajawazitoWeek42', views.JeWajuaWajawazitoWeek42ViewSet)
router.register('JeWajuaWajawazitoWeek43', views.JeWajuaWajawazitoWeek43ViewSet)
router.register('JeWajuaWajawazitoWeek44', views.JeWajuaWajawazitoWeek44ViewSet)
router.register('JeWajuaWajawazitoWeek45', views.JeWajuaWajawazitoWeek45ViewSet)



router.register('WajawazitoWeek1', views.WajawazitoWeek1ViewSet)
router.register('WajawazitoWeek2', views.WajawazitoWeek2ViewSet)
router.register('WajawazitoWeek3', views.WajawazitoWeek3ViewSet)
router.register('WajawazitoWeek4', views.WajawazitoWeek4ViewSet)
router.register('WajawazitoWeek5', views.WajawazitoWeek5ViewSet)
router.register('WajawazitoWeek6', views.WajawazitoWeek6ViewSet)
router.register('WajawazitoWeek7', views.WajawazitoWeek7ViewSet)
router.register('WajawazitoWeek8', views.WajawazitoWeek8ViewSet)
router.register('WajawazitoWeek9', views.WajawazitoWeek9ViewSet)
router.register('WajawazitoWeek10', views.WajawazitoWeek10ViewSet)

router.register('WajawazitoWeek11', views.WajawazitoWeek11ViewSet)
router.register('WajawazitoWeek12', views.WajawazitoWeek12ViewSet)
router.register('WajawazitoWeek13', views.WajawazitoWeek13ViewSet)
router.register('WajawazitoWeek14', views.WajawazitoWeek14ViewSet)
router.register('WajawazitoWeek15', views.WajawazitoWeek15ViewSet)
router.register('WajawazitoWeek16', views.WajawazitoWeek16ViewSet)
router.register('WajawazitoWeek17', views.WajawazitoWeek17ViewSet)
router.register('WajawazitoWeek18', views.WajawazitoWeek18ViewSet)
router.register('WajawazitoWeek19', views.WajawazitoWeek19ViewSet)
router.register('WajawazitoWeek20', views.WajawazitoWeek20ViewSet)

router.register('WajawazitoWeek21', views.WajawazitoWeek21ViewSet)
router.register('WajawazitoWeek22', views.WajawazitoWeek22ViewSet)
router.register('WajawazitoWeek23', views.WajawazitoWeek23ViewSet)
router.register('WajawazitoWeek24', views.WajawazitoWeek24ViewSet)
router.register('WajawazitoWeek25', views.WajawazitoWeek25ViewSet)
router.register('WajawazitoWeek26', views.WajawazitoWeek26ViewSet)
router.register('WajawazitoWeek27', views.WajawazitoWeek27ViewSet)
router.register('WajawazitoWeek28', views.WajawazitoWeek28ViewSet)
router.register('WajawazitoWeek29', views.WajawazitoWeek29ViewSet)
router.register('WajawazitoWeek30', views.WajawazitoWeek30ViewSet)

router.register('WajawazitoWeek31', views.WajawazitoWeek31ViewSet)
router.register('WajawazitoWeek32', views.WajawazitoWeek32ViewSet)
router.register('WajawazitoWeek33', views.WajawazitoWeek33ViewSet)
router.register('WajawazitoWeek34', views.WajawazitoWeek34ViewSet)
router.register('WajawazitoWeek35', views.WajawazitoWeek35ViewSet)
router.register('WajawazitoWeek36', views.WajawazitoWeek36ViewSet)
router.register('WajawazitoWeek37', views.WajawazitoWeek37ViewSet)
router.register('WajawazitoWeek38', views.WajawazitoWeek38ViewSet)
router.register('WajawazitoWeek39', views.WajawazitoWeek39ViewSet)
router.register('WajawazitoWeek40', views.WajawazitoWeek40ViewSet)

router.register('WajawazitoWeek41', views.WajawazitoWeek41ViewSet)
router.register('WajawazitoWeek42', views.WajawazitoWeek42ViewSet)
router.register('WajawazitoWeek43', views.WajawazitoWeek43ViewSet)
router.register('WajawazitoWeek44', views.WajawazitoWeek44ViewSet)
router.register('WajawazitoWeek45', views.WajawazitoWeek45ViewSet)





















#--------------------------------------UZITO ZAIDI----------------------------


router.register('TaarifaZaUzitoZaidiWeek1', views.TaarifaZaUzitoZaidiWeek1ViewSet)
router.register('TaarifaZaUzitoZaidiWeek2', views.TaarifaZaUzitoZaidiWeek2ViewSet)
router.register('TaarifaZaUzitoZaidiWeek3', views.TaarifaZaUzitoZaidiWeek3ViewSet)
router.register('TaarifaZaUzitoZaidiWeek4', views.TaarifaZaUzitoZaidiWeek4ViewSet)
router.register('TaarifaZaUzitoZaidiWeek5', views.TaarifaZaUzitoZaidiWeek5ViewSet)
router.register('TaarifaZaUzitoZaidiWeek6', views.TaarifaZaUzitoZaidiWeek6ViewSet)
router.register('TaarifaZaUzitoZaidiWeek7', views.TaarifaZaUzitoZaidiWeek7ViewSet)
router.register('TaarifaZaUzitoZaidiWeek8', views.TaarifaZaUzitoZaidiWeek8ViewSet)
router.register('TaarifaZaUzitoZaidiWeek9', views.TaarifaZaUzitoZaidiWeek9ViewSet)
router.register('TaarifaZaUzitoZaidiWeek10', views.TaarifaZaUzitoZaidiWeek10ViewSet)

router.register('TaarifaZaUzitoZaidiWeek11', views.TaarifaZaUzitoZaidiWeek11ViewSet)
router.register('TaarifaZaUzitoZaidiWeek12', views.TaarifaZaUzitoZaidiWeek12ViewSet)
router.register('TaarifaZaUzitoZaidiWeek13', views.TaarifaZaUzitoZaidiWeek13ViewSet)
router.register('TaarifaZaUzitoZaidiWeek14', views.TaarifaZaUzitoZaidiWeek14ViewSet)
router.register('TaarifaZaUzitoZaidiWeek15', views.TaarifaZaUzitoZaidiWeek15ViewSet)
router.register('TaarifaZaUzitoZaidiWeek16', views.TaarifaZaUzitoZaidiWeek16ViewSet)
router.register('TaarifaZaUzitoZaidiWeek17', views.TaarifaZaUzitoZaidiWeek17ViewSet)
router.register('TaarifaZaUzitoZaidiWeek18', views.TaarifaZaUzitoZaidiWeek18ViewSet)
router.register('TaarifaZaUzitoZaidiWeek19', views.TaarifaZaUzitoZaidiWeek19ViewSet)
router.register('TaarifaZaUzitoZaidiWeek20', views.TaarifaZaUzitoZaidiWeek20ViewSet)

router.register('TaarifaZaUzitoZaidiWeek21', views.TaarifaZaUzitoZaidiWeek21ViewSet)
router.register('TaarifaZaUzitoZaidiWeek22', views.TaarifaZaUzitoZaidiWeek22ViewSet)
router.register('TaarifaZaUzitoZaidiWeek23', views.TaarifaZaUzitoZaidiWeek23ViewSet)
router.register('TaarifaZaUzitoZaidiWeek24', views.TaarifaZaUzitoZaidiWeek24ViewSet)
router.register('TaarifaZaUzitoZaidiWeek25', views.TaarifaZaUzitoZaidiWeek25ViewSet)
router.register('TaarifaZaUzitoZaidiWeek26', views.TaarifaZaUzitoZaidiWeek26ViewSet)
router.register('TaarifaZaUzitoZaidiWeek27', views.TaarifaZaUzitoZaidiWeek27ViewSet)
router.register('TaarifaZaUzitoZaidiWeek28', views.TaarifaZaUzitoZaidiWeek28ViewSet)
router.register('TaarifaZaUzitoZaidiWeek29', views.TaarifaZaUzitoZaidiWeek29ViewSet)
router.register('TaarifaZaUzitoZaidiWeek30', views.TaarifaZaUzitoZaidiWeek30ViewSet)

router.register('TaarifaZaUzitoZaidiWeek31', views.TaarifaZaUzitoZaidiWeek31ViewSet)
router.register('TaarifaZaUzitoZaidiWeek32', views.TaarifaZaUzitoZaidiWeek32ViewSet)
router.register('TaarifaZaUzitoZaidiWeek33', views.TaarifaZaUzitoZaidiWeek33ViewSet)
router.register('TaarifaZaUzitoZaidiWeek34', views.TaarifaZaUzitoZaidiWeek34ViewSet)
router.register('TaarifaZaUzitoZaidiWeek35', views.TaarifaZaUzitoZaidiWeek35ViewSet)
router.register('TaarifaZaUzitoZaidiWeek36', views.TaarifaZaUzitoZaidiWeek36ViewSet)
router.register('TaarifaZaUzitoZaidiWeek37', views.TaarifaZaUzitoZaidiWeek37ViewSet)
router.register('TaarifaZaUzitoZaidiWeek38', views.TaarifaZaUzitoZaidiWeek38ViewSet)
router.register('TaarifaZaUzitoZaidiWeek39', views.TaarifaZaUzitoZaidiWeek39ViewSet)
router.register('TaarifaZaUzitoZaidiWeek40', views.TaarifaZaUzitoZaidiWeek40ViewSet)

router.register('TaarifaZaUzitoZaidiWeek41', views.TaarifaZaUzitoZaidiWeek41ViewSet)
router.register('TaarifaZaUzitoZaidiWeek42', views.TaarifaZaUzitoZaidiWeek42ViewSet)
router.register('TaarifaZaUzitoZaidiWeek43', views.TaarifaZaUzitoZaidiWeek43ViewSet)
router.register('TaarifaZaUzitoZaidiWeek44', views.TaarifaZaUzitoZaidiWeek44ViewSet)
router.register('TaarifaZaUzitoZaidiWeek45', views.TaarifaZaUzitoZaidiWeek45ViewSet)








router.register('JeWajuaUzitoZaidiWeek1', views.JeWajuaUzitoZaidiWeek1ViewSet)
router.register('JeWajuaUzitoZaidiWeek2', views.JeWajuaUzitoZaidiWeek2ViewSet)
router.register('JeWajuaUzitoZaidiWeek3', views.JeWajuaUzitoZaidiWeek3ViewSet)
router.register('JeWajuaUzitoZaidiWeek4', views.JeWajuaUzitoZaidiWeek4ViewSet)
router.register('JeWajuaUzitoZaidiWeek5', views.JeWajuaUzitoZaidiWeek5ViewSet)
router.register('JeWajuaUzitoZaidiWeek6', views.JeWajuaUzitoZaidiWeek6ViewSet)
router.register('JeWajuaUzitoZaidiWeek7', views.JeWajuaUzitoZaidiWeek7ViewSet)
router.register('JeWajuaUzitoZaidiWeek8', views.JeWajuaUzitoZaidiWeek8ViewSet)
router.register('JeWajuaUzitoZaidiWeek9', views.JeWajuaUzitoZaidiWeek9ViewSet)
router.register('JeWajuaUzitoZaidiWeek10', views.JeWajuaUzitoZaidiWeek10ViewSet)

router.register('JeWajuaUzitoZaidiWeek11', views.JeWajuaUzitoZaidiWeek11ViewSet)
router.register('JeWajuaUzitoZaidiWeek12', views.JeWajuaUzitoZaidiWeek12ViewSet)
router.register('JeWajuaUzitoZaidiWeek13', views.JeWajuaUzitoZaidiWeek13ViewSet)
router.register('JeWajuaUzitoZaidiWeek14', views.JeWajuaUzitoZaidiWeek14ViewSet)
router.register('JeWajuaUzitoZaidiWeek15', views.JeWajuaUzitoZaidiWeek15ViewSet)
router.register('JeWajuaUzitoZaidiWeek16', views.JeWajuaUzitoZaidiWeek16ViewSet)
router.register('JeWajuaUzitoZaidiWeek17', views.JeWajuaUzitoZaidiWeek17ViewSet)
router.register('JeWajuaUzitoZaidiWeek18', views.JeWajuaUzitoZaidiWeek18ViewSet)
router.register('JeWajuaUzitoZaidiWeek19', views.JeWajuaUzitoZaidiWeek19ViewSet)
router.register('JeWajuaUzitoZaidiWeek20', views.JeWajuaUzitoZaidiWeek20ViewSet)

router.register('JeWajuaUzitoZaidiWeek21', views.JeWajuaUzitoZaidiWeek21ViewSet)
router.register('JeWajuaUzitoZaidiWeek22', views.JeWajuaUzitoZaidiWeek22ViewSet)
router.register('JeWajuaUzitoZaidiWeek23', views.JeWajuaUzitoZaidiWeek23ViewSet)
router.register('JeWajuaUzitoZaidiWeek24', views.JeWajuaUzitoZaidiWeek24ViewSet)
router.register('JeWajuaUzitoZaidiWeek25', views.JeWajuaUzitoZaidiWeek25ViewSet)
router.register('JeWajuaUzitoZaidiWeek26', views.JeWajuaUzitoZaidiWeek26ViewSet)
router.register('JeWajuaUzitoZaidiWeek27', views.JeWajuaUzitoZaidiWeek27ViewSet)
router.register('JeWajuaUzitoZaidiWeek28', views.JeWajuaUzitoZaidiWeek28ViewSet)
router.register('JeWajuaUzitoZaidiWeek29', views.JeWajuaUzitoZaidiWeek29ViewSet)
router.register('JeWajuaUzitoZaidiWeek30', views.JeWajuaUzitoZaidiWeek30ViewSet)

router.register('JeWajuaUzitoZaidiWeek31', views.JeWajuaUzitoZaidiWeek31ViewSet)
router.register('JeWajuaUzitoZaidiWeek32', views.JeWajuaUzitoZaidiWeek32ViewSet)
router.register('JeWajuaUzitoZaidiWeek33', views.JeWajuaUzitoZaidiWeek33ViewSet)
router.register('JeWajuaUzitoZaidiWeek34', views.JeWajuaUzitoZaidiWeek34ViewSet)
router.register('JeWajuaUzitoZaidiWeek35', views.JeWajuaUzitoZaidiWeek35ViewSet)
router.register('JeWajuaUzitoZaidiWeek36', views.JeWajuaUzitoZaidiWeek36ViewSet)
router.register('JeWajuaUzitoZaidiWeek37', views.JeWajuaUzitoZaidiWeek37ViewSet)
router.register('JeWajuaUzitoZaidiWeek38', views.JeWajuaUzitoZaidiWeek38ViewSet)
router.register('JeWajuaUzitoZaidiWeek39', views.JeWajuaUzitoZaidiWeek39ViewSet)
router.register('JeWajuaUzitoZaidiWeek40', views.JeWajuaUzitoZaidiWeek40ViewSet)

router.register('JeWajuaUzitoZaidiWeek41', views.JeWajuaUzitoZaidiWeek41ViewSet)
router.register('JeWajuaUzitoZaidiWeek42', views.JeWajuaUzitoZaidiWeek42ViewSet)
router.register('JeWajuaUzitoZaidiWeek43', views.JeWajuaUzitoZaidiWeek43ViewSet)
router.register('JeWajuaUzitoZaidiWeek44', views.JeWajuaUzitoZaidiWeek44ViewSet)
router.register('JeWajuaUzitoZaidiWeek45', views.JeWajuaUzitoZaidiWeek45ViewSet)









router.register('UzitoZaidiWeek1', views.UzitoZaidiWeek1ViewSet)
router.register('UzitoZaidiWeek2', views.UzitoZaidiWeek2ViewSet)
router.register('UzitoZaidiWeek3', views.UzitoZaidiWeek3ViewSet)
router.register('UzitoZaidiWeek4', views.UzitoZaidiWeek4ViewSet)
router.register('UzitoZaidiWeek5', views.UzitoZaidiWeek5ViewSet)
router.register('UzitoZaidiWeek6', views.UzitoZaidiWeek6ViewSet)
router.register('UzitoZaidiWeek7', views.UzitoZaidiWeek7ViewSet)
router.register('UzitoZaidiWeek8', views.UzitoZaidiWeek8ViewSet)
router.register('UzitoZaidiWeek9', views.UzitoZaidiWeek9ViewSet)
router.register('UzitoZaidiWeek10', views.UzitoZaidiWeek10ViewSet)

router.register('UzitoZaidiWeek11', views.UzitoZaidiWeek11ViewSet)
router.register('UzitoZaidiWeek12', views.UzitoZaidiWeek12ViewSet)
router.register('UzitoZaidiWeek13', views.UzitoZaidiWeek13ViewSet)
router.register('UzitoZaidiWeek14', views.UzitoZaidiWeek14ViewSet)
router.register('UzitoZaidiWeek15', views.UzitoZaidiWeek15ViewSet)
router.register('UzitoZaidiWeek16', views.UzitoZaidiWeek16ViewSet)
router.register('UzitoZaidiWeek17', views.UzitoZaidiWeek17ViewSet)
router.register('UzitoZaidiWeek18', views.UzitoZaidiWeek18ViewSet)
router.register('UzitoZaidiWeek19', views.UzitoZaidiWeek19ViewSet)
router.register('UzitoZaidiWeek20', views.UzitoZaidiWeek20ViewSet)

router.register('UzitoZaidiWeek21', views.UzitoZaidiWeek21ViewSet)
router.register('UzitoZaidiWeek22', views.UzitoZaidiWeek22ViewSet)
router.register('UzitoZaidiWeek23', views.UzitoZaidiWeek23ViewSet)
router.register('UzitoZaidiWeek24', views.UzitoZaidiWeek24ViewSet)
router.register('UzitoZaidiWeek25', views.UzitoZaidiWeek25ViewSet)
router.register('UzitoZaidiWeek26', views.UzitoZaidiWeek26ViewSet)
router.register('UzitoZaidiWeek27', views.UzitoZaidiWeek27ViewSet)
router.register('UzitoZaidiWeek28', views.UzitoZaidiWeek28ViewSet)
router.register('UzitoZaidiWeek29', views.UzitoZaidiWeek29ViewSet)
router.register('UzitoZaidiWeek30', views.UzitoZaidiWeek30ViewSet)

router.register('UzitoZaidiWeek31', views.UzitoZaidiWeek31ViewSet)
router.register('UzitoZaidiWeek32', views.UzitoZaidiWeek32ViewSet)
router.register('UzitoZaidiWeek33', views.UzitoZaidiWeek33ViewSet)
router.register('UzitoZaidiWeek34', views.UzitoZaidiWeek34ViewSet)
router.register('UzitoZaidiWeek35', views.UzitoZaidiWeek35ViewSet)
router.register('UzitoZaidiWeek36', views.UzitoZaidiWeek36ViewSet)
router.register('UzitoZaidiWeek37', views.UzitoZaidiWeek37ViewSet)
router.register('UzitoZaidiWeek38', views.UzitoZaidiWeek38ViewSet)
router.register('UzitoZaidiWeek39', views.UzitoZaidiWeek39ViewSet)
router.register('UzitoZaidiWeek40', views.UzitoZaidiWeek40ViewSet)

router.register('UzitoZaidiWeek41', views.UzitoZaidiWeek41ViewSet)
router.register('UzitoZaidiWeek42', views.UzitoZaidiWeek42ViewSet)
router.register('UzitoZaidiWeek43', views.UzitoZaidiWeek43ViewSet)
router.register('UzitoZaidiWeek44', views.UzitoZaidiWeek44ViewSet)
router.register('UzitoZaidiWeek45', views.UzitoZaidiWeek45ViewSet)













#----------------------------------WATOTO-------------------------




router.register('TaarifaZaWatotoWeek1', views.TaarifaZaWatotoWeek1ViewSet)
router.register('TaarifaZaWatotoWeek2', views.TaarifaZaWatotoWeek2ViewSet)
router.register('TaarifaZaWatotoWeek3', views.TaarifaZaWatotoWeek3ViewSet)
router.register('TaarifaZaWatotoWeek4', views.TaarifaZaWatotoWeek4ViewSet)
router.register('TaarifaZaWatotoWeek5', views.TaarifaZaWatotoWeek5ViewSet)
router.register('TaarifaZaWatotoWeek6', views.TaarifaZaWatotoWeek6ViewSet)
router.register('TaarifaZaWatotoWeek7', views.TaarifaZaWatotoWeek7ViewSet)
router.register('TaarifaZaWatotoWeek8', views.TaarifaZaWatotoWeek8ViewSet)
router.register('TaarifaZaWatotoWeek9', views.TaarifaZaWatotoWeek9ViewSet)
router.register('TaarifaZaWatotoWeek10', views.TaarifaZaWatotoWeek10ViewSet)

router.register('TaarifaZaWatotoWeek11', views.TaarifaZaWatotoWeek11ViewSet)
router.register('TaarifaZaWatotoWeek12', views.TaarifaZaWatotoWeek12ViewSet)
router.register('TaarifaZaWatotoWeek13', views.TaarifaZaWatotoWeek13ViewSet)
router.register('TaarifaZaWatotoWeek14', views.TaarifaZaWatotoWeek14ViewSet)
router.register('TaarifaZaWatotoWeek15', views.TaarifaZaWatotoWeek15ViewSet)
router.register('TaarifaZaWatotoWeek16', views.TaarifaZaWatotoWeek16ViewSet)
router.register('TaarifaZaWatotoWeek17', views.TaarifaZaWatotoWeek17ViewSet)
router.register('TaarifaZaWatotoWeek18', views.TaarifaZaWatotoWeek18ViewSet)
router.register('TaarifaZaWatotoWeek19', views.TaarifaZaWatotoWeek19ViewSet)
router.register('TaarifaZaWatotoWeek20', views.TaarifaZaWatotoWeek20ViewSet)

router.register('TaarifaZaWatotoWeek21', views.TaarifaZaWatotoWeek21ViewSet)
router.register('TaarifaZaWatotoWeek22', views.TaarifaZaWatotoWeek22ViewSet)
router.register('TaarifaZaWatotoWeek23', views.TaarifaZaWatotoWeek23ViewSet)
router.register('TaarifaZaWatotoWeek24', views.TaarifaZaWatotoWeek24ViewSet)
router.register('TaarifaZaWatotoWeek25', views.TaarifaZaWatotoWeek25ViewSet)
router.register('TaarifaZaWatotoWeek26', views.TaarifaZaWatotoWeek26ViewSet)
router.register('TaarifaZaWatotoWeek27', views.TaarifaZaWatotoWeek27ViewSet)
router.register('TaarifaZaWatotoWeek28', views.TaarifaZaWatotoWeek28ViewSet)
router.register('TaarifaZaWatotoWeek29', views.TaarifaZaWatotoWeek29ViewSet)
router.register('TaarifaZaWatotoWeek30', views.TaarifaZaWatotoWeek30ViewSet)

router.register('TaarifaZaWatotoWeek31', views.TaarifaZaWatotoWeek31ViewSet)
router.register('TaarifaZaWatotoWeek32', views.TaarifaZaWatotoWeek32ViewSet)
router.register('TaarifaZaWatotoWeek33', views.TaarifaZaWatotoWeek33ViewSet)
router.register('TaarifaZaWatotoWeek34', views.TaarifaZaWatotoWeek34ViewSet)
router.register('TaarifaZaWatotoWeek35', views.TaarifaZaWatotoWeek35ViewSet)
router.register('TaarifaZaWatotoWeek36', views.TaarifaZaWatotoWeek36ViewSet)
router.register('TaarifaZaWatotoWeek37', views.TaarifaZaWatotoWeek37ViewSet)
router.register('TaarifaZaWatotoWeek38', views.TaarifaZaWatotoWeek38ViewSet)
router.register('TaarifaZaWatotoWeek39', views.TaarifaZaWatotoWeek39ViewSet)
router.register('TaarifaZaWatotoWeek40', views.TaarifaZaWatotoWeek40ViewSet)

router.register('TaarifaZaWatotoWeek41', views.TaarifaZaWatotoWeek41ViewSet)
router.register('TaarifaZaWatotoWeek42', views.TaarifaZaWatotoWeek42ViewSet)
router.register('TaarifaZaWatotoWeek43', views.TaarifaZaWatotoWeek43ViewSet)
router.register('TaarifaZaWatotoWeek44', views.TaarifaZaWatotoWeek44ViewSet)
router.register('TaarifaZaWatotoWeek45', views.TaarifaZaWatotoWeek45ViewSet)








router.register('JeWajuaWatotoWeek1', views.JeWajuaWatotoWeek1ViewSet)
router.register('JeWajuaWatotoWeek2', views.JeWajuaWatotoWeek2ViewSet)
router.register('JeWajuaWatotoWeek3', views.JeWajuaWatotoWeek3ViewSet)
router.register('JeWajuaWatotoWeek4', views.JeWajuaWatotoWeek4ViewSet)
router.register('JeWajuaWatotoWeek5', views.JeWajuaWatotoWeek5ViewSet)
router.register('JeWajuaWatotoWeek6', views.JeWajuaWatotoWeek6ViewSet)
router.register('JeWajuaWatotoWeek7', views.JeWajuaWatotoWeek7ViewSet)
router.register('JeWajuaWatotoWeek8', views.JeWajuaWatotoWeek8ViewSet)
router.register('JeWajuaWatotoWeek9', views.JeWajuaWatotoWeek9ViewSet)
router.register('JeWajuaWatotoWeek10', views.JeWajuaWatotoWeek10ViewSet)

router.register('JeWajuaWatotoWeek11', views.JeWajuaWatotoWeek11ViewSet)
router.register('JeWajuaWatotoWeek12', views.JeWajuaWatotoWeek12ViewSet)
router.register('JeWajuaWatotoWeek13', views.JeWajuaWatotoWeek13ViewSet)
router.register('JeWajuaWatotoWeek14', views.JeWajuaWatotoWeek14ViewSet)
router.register('JeWajuaWatotoWeek15', views.JeWajuaWatotoWeek15ViewSet)
router.register('JeWajuaWatotoWeek16', views.JeWajuaWatotoWeek16ViewSet)
router.register('JeWajuaWatotoWeek17', views.JeWajuaWatotoWeek17ViewSet)
router.register('JeWajuaWatotoWeek18', views.JeWajuaWatotoWeek18ViewSet)
router.register('JeWajuaWatotoWeek19', views.JeWajuaWatotoWeek19ViewSet)
router.register('JeWajuaWatotoWeek20', views.JeWajuaWatotoWeek20ViewSet)

router.register('JeWajuaWatotoWeek21', views.JeWajuaWatotoWeek21ViewSet)
router.register('JeWajuaWatotoWeek22', views.JeWajuaWatotoWeek22ViewSet)
router.register('JeWajuaWatotoWeek23', views.JeWajuaWatotoWeek23ViewSet)
router.register('JeWajuaWatotoWeek24', views.JeWajuaWatotoWeek24ViewSet)
router.register('JeWajuaWatotoWeek25', views.JeWajuaWatotoWeek25ViewSet)
router.register('JeWajuaWatotoWeek26', views.JeWajuaWatotoWeek26ViewSet)
router.register('JeWajuaWatotoWeek27', views.JeWajuaWatotoWeek27ViewSet)
router.register('JeWajuaWatotoWeek28', views.JeWajuaWatotoWeek28ViewSet)
router.register('JeWajuaWatotoWeek29', views.JeWajuaWatotoWeek29ViewSet)
router.register('JeWajuaWatotoWeek30', views.JeWajuaWatotoWeek30ViewSet)

router.register('JeWajuaWatotoWeek31', views.JeWajuaWatotoWeek31ViewSet)
router.register('JeWajuaWatotoWeek32', views.JeWajuaWatotoWeek32ViewSet)
router.register('JeWajuaWatotoWeek33', views.JeWajuaWatotoWeek33ViewSet)
router.register('JeWajuaWatotoWeek34', views.JeWajuaWatotoWeek34ViewSet)
router.register('JeWajuaWatotoWeek35', views.JeWajuaWatotoWeek35ViewSet)
router.register('JeWajuaWatotoWeek36', views.JeWajuaWatotoWeek36ViewSet)
router.register('JeWajuaWatotoWeek37', views.JeWajuaWatotoWeek37ViewSet)
router.register('JeWajuaWatotoWeek38', views.JeWajuaWatotoWeek38ViewSet)
router.register('JeWajuaWatotoWeek39', views.JeWajuaWatotoWeek39ViewSet)
router.register('JeWajuaWatotoWeek40', views.JeWajuaWatotoWeek40ViewSet)

router.register('JeWajuaWatotoWeek41', views.JeWajuaWatotoWeek41ViewSet)
router.register('JeWajuaWatotoWeek42', views.JeWajuaWatotoWeek42ViewSet)
router.register('JeWajuaWatotoWeek43', views.JeWajuaWatotoWeek43ViewSet)
router.register('JeWajuaWatotoWeek44', views.JeWajuaWatotoWeek44ViewSet)
router.register('JeWajuaWatotoWeek45', views.JeWajuaWatotoWeek45ViewSet)









router.register('WatotoWeek1', views.WatotoWeek1ViewSet)
router.register('WatotoWeek2', views.WatotoWeek2ViewSet)
router.register('WatotoWeek3', views.WatotoWeek3ViewSet)
router.register('WatotoWeek4', views.WatotoWeek4ViewSet)
router.register('WatotoWeek5', views.WatotoWeek5ViewSet)
router.register('WatotoWeek6', views.WatotoWeek6ViewSet)
router.register('WatotoWeek7', views.WatotoWeek7ViewSet)
router.register('WatotoWeek8', views.WatotoWeek8ViewSet)
router.register('WatotoWeek9', views.WatotoWeek9ViewSet)
router.register('WatotoWeek10', views.WatotoWeek10ViewSet)

router.register('WatotoWeek11', views.WatotoWeek11ViewSet)
router.register('WatotoWeek12', views.WatotoWeek12ViewSet)
router.register('WatotoWeek13', views.WatotoWeek13ViewSet)
router.register('WatotoWeek14', views.WatotoWeek14ViewSet)
router.register('WatotoWeek15', views.WatotoWeek15ViewSet)
router.register('WatotoWeek16', views.WatotoWeek16ViewSet)
router.register('WatotoWeek17', views.WatotoWeek17ViewSet)
router.register('WatotoWeek18', views.WatotoWeek18ViewSet)
router.register('WatotoWeek19', views.WatotoWeek19ViewSet)
router.register('WatotoWeek20', views.WatotoWeek20ViewSet)

router.register('WatotoWeek21', views.WatotoWeek21ViewSet)
router.register('WatotoWeek22', views.WatotoWeek22ViewSet)
router.register('WatotoWeek23', views.WatotoWeek23ViewSet)
router.register('WatotoWeek24', views.WatotoWeek24ViewSet)
router.register('WatotoWeek25', views.WatotoWeek25ViewSet)
router.register('WatotoWeek26', views.WatotoWeek26ViewSet)
router.register('WatotoWeek27', views.WatotoWeek27ViewSet)
router.register('WatotoWeek28', views.WatotoWeek28ViewSet)
router.register('WatotoWeek29', views.WatotoWeek29ViewSet)
router.register('WatotoWeek30', views.WatotoWeek30ViewSet)

router.register('WatotoWeek31', views.WatotoWeek31ViewSet)
router.register('WatotoWeek32', views.WatotoWeek32ViewSet)
router.register('WatotoWeek33', views.WatotoWeek33ViewSet)
router.register('WatotoWeek34', views.WatotoWeek34ViewSet)
router.register('WatotoWeek35', views.WatotoWeek35ViewSet)
router.register('WatotoWeek36', views.WatotoWeek36ViewSet)
router.register('WatotoWeek37', views.WatotoWeek37ViewSet)
router.register('WatotoWeek38', views.WatotoWeek38ViewSet)
router.register('WatotoWeek39', views.WatotoWeek39ViewSet)
router.register('WatotoWeek40', views.WatotoWeek40ViewSet)

router.register('WatotoWeek41', views.WatotoWeek41ViewSet)
router.register('WatotoWeek42', views.WatotoWeek42ViewSet)
router.register('WatotoWeek43', views.WatotoWeek43ViewSet)
router.register('WatotoWeek44', views.WatotoWeek44ViewSet)
router.register('WatotoWeek45', views.WatotoWeek45ViewSet)













#----------------------------------KISUKARI-------------------------




router.register('TaarifaZaKisukariWeek1', views.TaarifaZaKisukariWeek1ViewSet)
router.register('TaarifaZaKisukariWeek2', views.TaarifaZaKisukariWeek2ViewSet)
router.register('TaarifaZaKisukariWeek3', views.TaarifaZaKisukariWeek3ViewSet)
router.register('TaarifaZaKisukariWeek4', views.TaarifaZaKisukariWeek4ViewSet)
router.register('TaarifaZaKisukariWeek5', views.TaarifaZaKisukariWeek5ViewSet)
router.register('TaarifaZaKisukariWeek6', views.TaarifaZaKisukariWeek6ViewSet)
router.register('TaarifaZaKisukariWeek7', views.TaarifaZaKisukariWeek7ViewSet)
router.register('TaarifaZaKisukariWeek8', views.TaarifaZaKisukariWeek8ViewSet)
router.register('TaarifaZaKisukariWeek9', views.TaarifaZaKisukariWeek9ViewSet)
router.register('TaarifaZaKisukariWeek10', views.TaarifaZaKisukariWeek10ViewSet)

router.register('TaarifaZaKisukariWeek11', views.TaarifaZaKisukariWeek11ViewSet)
router.register('TaarifaZaKisukariWeek12', views.TaarifaZaKisukariWeek12ViewSet)
router.register('TaarifaZaKisukariWeek13', views.TaarifaZaKisukariWeek13ViewSet)
router.register('TaarifaZaKisukariWeek14', views.TaarifaZaKisukariWeek14ViewSet)
router.register('TaarifaZaKisukariWeek15', views.TaarifaZaKisukariWeek15ViewSet)
router.register('TaarifaZaKisukariWeek16', views.TaarifaZaKisukariWeek16ViewSet)
router.register('TaarifaZaKisukariWeek17', views.TaarifaZaKisukariWeek17ViewSet)
router.register('TaarifaZaKisukariWeek18', views.TaarifaZaKisukariWeek18ViewSet)
router.register('TaarifaZaKisukariWeek19', views.TaarifaZaKisukariWeek19ViewSet)
router.register('TaarifaZaKisukariWeek20', views.TaarifaZaKisukariWeek20ViewSet)

router.register('TaarifaZaKisukariWeek21', views.TaarifaZaKisukariWeek21ViewSet)
router.register('TaarifaZaKisukariWeek22', views.TaarifaZaKisukariWeek22ViewSet)
router.register('TaarifaZaKisukariWeek23', views.TaarifaZaKisukariWeek23ViewSet)
router.register('TaarifaZaKisukariWeek24', views.TaarifaZaKisukariWeek24ViewSet)
router.register('TaarifaZaKisukariWeek25', views.TaarifaZaKisukariWeek25ViewSet)
router.register('TaarifaZaKisukariWeek26', views.TaarifaZaKisukariWeek26ViewSet)
router.register('TaarifaZaKisukariWeek27', views.TaarifaZaKisukariWeek27ViewSet)
router.register('TaarifaZaKisukariWeek28', views.TaarifaZaKisukariWeek28ViewSet)
router.register('TaarifaZaKisukariWeek29', views.TaarifaZaKisukariWeek29ViewSet)
router.register('TaarifaZaKisukariWeek30', views.TaarifaZaKisukariWeek30ViewSet)

router.register('TaarifaZaKisukariWeek31', views.TaarifaZaKisukariWeek31ViewSet)
router.register('TaarifaZaKisukariWeek32', views.TaarifaZaKisukariWeek32ViewSet)
router.register('TaarifaZaKisukariWeek33', views.TaarifaZaKisukariWeek33ViewSet)
router.register('TaarifaZaKisukariWeek34', views.TaarifaZaKisukariWeek34ViewSet)
router.register('TaarifaZaKisukariWeek35', views.TaarifaZaKisukariWeek35ViewSet)
router.register('TaarifaZaKisukariWeek36', views.TaarifaZaKisukariWeek36ViewSet)
router.register('TaarifaZaKisukariWeek37', views.TaarifaZaKisukariWeek37ViewSet)
router.register('TaarifaZaKisukariWeek38', views.TaarifaZaKisukariWeek38ViewSet)
router.register('TaarifaZaKisukariWeek39', views.TaarifaZaKisukariWeek39ViewSet)
router.register('TaarifaZaKisukariWeek40', views.TaarifaZaKisukariWeek40ViewSet)

router.register('TaarifaZaKisukariWeek41', views.TaarifaZaKisukariWeek41ViewSet)
router.register('TaarifaZaKisukariWeek42', views.TaarifaZaKisukariWeek42ViewSet)
router.register('TaarifaZaKisukariWeek43', views.TaarifaZaKisukariWeek43ViewSet)
router.register('TaarifaZaKisukariWeek44', views.TaarifaZaKisukariWeek44ViewSet)
router.register('TaarifaZaKisukariWeek45', views.TaarifaZaKisukariWeek45ViewSet)








router.register('JeWajuaKisukariWeek1', views.JeWajuaKisukariWeek1ViewSet)
router.register('JeWajuaKisukariWeek2', views.JeWajuaKisukariWeek2ViewSet)
router.register('JeWajuaKisukariWeek3', views.JeWajuaKisukariWeek3ViewSet)
router.register('JeWajuaKisukariWeek4', views.JeWajuaKisukariWeek4ViewSet)
router.register('JeWajuaKisukariWeek5', views.JeWajuaKisukariWeek5ViewSet)
router.register('JeWajuaKisukariWeek6', views.JeWajuaKisukariWeek6ViewSet)
router.register('JeWajuaKisukariWeek7', views.JeWajuaKisukariWeek7ViewSet)
router.register('JeWajuaKisukariWeek8', views.JeWajuaKisukariWeek8ViewSet)
router.register('JeWajuaKisukariWeek9', views.JeWajuaKisukariWeek9ViewSet)
router.register('JeWajuaKisukariWeek10', views.JeWajuaKisukariWeek10ViewSet)

router.register('JeWajuaKisukariWeek11', views.JeWajuaKisukariWeek11ViewSet)
router.register('JeWajuaKisukariWeek12', views.JeWajuaKisukariWeek12ViewSet)
router.register('JeWajuaKisukariWeek13', views.JeWajuaKisukariWeek13ViewSet)
router.register('JeWajuaKisukariWeek14', views.JeWajuaKisukariWeek14ViewSet)
router.register('JeWajuaKisukariWeek15', views.JeWajuaKisukariWeek15ViewSet)
router.register('JeWajuaKisukariWeek16', views.JeWajuaKisukariWeek16ViewSet)
router.register('JeWajuaKisukariWeek17', views.JeWajuaKisukariWeek17ViewSet)
router.register('JeWajuaKisukariWeek18', views.JeWajuaKisukariWeek18ViewSet)
router.register('JeWajuaKisukariWeek19', views.JeWajuaKisukariWeek19ViewSet)
router.register('JeWajuaKisukariWeek20', views.JeWajuaKisukariWeek20ViewSet)

router.register('JeWajuaKisukariWeek21', views.JeWajuaKisukariWeek21ViewSet)
router.register('JeWajuaKisukariWeek22', views.JeWajuaKisukariWeek22ViewSet)
router.register('JeWajuaKisukariWeek23', views.JeWajuaKisukariWeek23ViewSet)
router.register('JeWajuaKisukariWeek24', views.JeWajuaKisukariWeek24ViewSet)
router.register('JeWajuaKisukariWeek25', views.JeWajuaKisukariWeek25ViewSet)
router.register('JeWajuaKisukariWeek26', views.JeWajuaKisukariWeek26ViewSet)
router.register('JeWajuaKisukariWeek27', views.JeWajuaKisukariWeek27ViewSet)
router.register('JeWajuaKisukariWeek28', views.JeWajuaKisukariWeek28ViewSet)
router.register('JeWajuaKisukariWeek29', views.JeWajuaKisukariWeek29ViewSet)
router.register('JeWajuaKisukariWeek30', views.JeWajuaKisukariWeek30ViewSet)

router.register('JeWajuaKisukariWeek31', views.JeWajuaKisukariWeek31ViewSet)
router.register('JeWajuaKisukariWeek32', views.JeWajuaKisukariWeek32ViewSet)
router.register('JeWajuaKisukariWeek33', views.JeWajuaKisukariWeek33ViewSet)
router.register('JeWajuaKisukariWeek34', views.JeWajuaKisukariWeek34ViewSet)
router.register('JeWajuaKisukariWeek35', views.JeWajuaKisukariWeek35ViewSet)
router.register('JeWajuaKisukariWeek36', views.JeWajuaKisukariWeek36ViewSet)
router.register('JeWajuaKisukariWeek37', views.JeWajuaKisukariWeek37ViewSet)
router.register('JeWajuaKisukariWeek38', views.JeWajuaKisukariWeek38ViewSet)
router.register('JeWajuaKisukariWeek39', views.JeWajuaKisukariWeek39ViewSet)
router.register('JeWajuaKisukariWeek40', views.JeWajuaKisukariWeek40ViewSet)

router.register('JeWajuaKisukariWeek41', views.JeWajuaKisukariWeek41ViewSet)
router.register('JeWajuaKisukariWeek42', views.JeWajuaKisukariWeek42ViewSet)
router.register('JeWajuaKisukariWeek43', views.JeWajuaKisukariWeek43ViewSet)
router.register('JeWajuaKisukariWeek44', views.JeWajuaKisukariWeek44ViewSet)
router.register('JeWajuaKisukariWeek45', views.JeWajuaKisukariWeek45ViewSet)









router.register('KisukariWeek1', views.KisukariWeek1ViewSet)
router.register('KisukariWeek2', views.KisukariWeek2ViewSet)
router.register('KisukariWeek3', views.KisukariWeek3ViewSet)
router.register('KisukariWeek4', views.KisukariWeek4ViewSet)
router.register('KisukariWeek5', views.KisukariWeek5ViewSet)
router.register('KisukariWeek6', views.KisukariWeek6ViewSet)
router.register('KisukariWeek7', views.KisukariWeek7ViewSet)
router.register('KisukariWeek8', views.KisukariWeek8ViewSet)
router.register('KisukariWeek9', views.KisukariWeek9ViewSet)
router.register('KisukariWeek10', views.KisukariWeek10ViewSet)

router.register('KisukariWeek11', views.KisukariWeek11ViewSet)
router.register('KisukariWeek12', views.KisukariWeek12ViewSet)
router.register('KisukariWeek13', views.KisukariWeek13ViewSet)
router.register('KisukariWeek14', views.KisukariWeek14ViewSet)
router.register('KisukariWeek15', views.KisukariWeek15ViewSet)
router.register('KisukariWeek16', views.KisukariWeek16ViewSet)
router.register('KisukariWeek17', views.KisukariWeek17ViewSet)
router.register('KisukariWeek18', views.KisukariWeek18ViewSet)
router.register('KisukariWeek19', views.KisukariWeek19ViewSet)
router.register('KisukariWeek20', views.KisukariWeek20ViewSet)

router.register('KisukariWeek21', views.KisukariWeek21ViewSet)
router.register('KisukariWeek22', views.KisukariWeek22ViewSet)
router.register('KisukariWeek23', views.KisukariWeek23ViewSet)
router.register('KisukariWeek24', views.KisukariWeek24ViewSet)
router.register('KisukariWeek25', views.KisukariWeek25ViewSet)
router.register('KisukariWeek26', views.KisukariWeek26ViewSet)
router.register('KisukariWeek27', views.KisukariWeek27ViewSet)
router.register('KisukariWeek28', views.KisukariWeek28ViewSet)
router.register('KisukariWeek29', views.KisukariWeek29ViewSet)
router.register('KisukariWeek30', views.KisukariWeek30ViewSet)

router.register('KisukariWeek31', views.KisukariWeek31ViewSet)
router.register('KisukariWeek32', views.KisukariWeek32ViewSet)
router.register('KisukariWeek33', views.KisukariWeek33ViewSet)
router.register('KisukariWeek34', views.KisukariWeek34ViewSet)
router.register('KisukariWeek35', views.KisukariWeek35ViewSet)
router.register('KisukariWeek36', views.KisukariWeek36ViewSet)
router.register('KisukariWeek37', views.KisukariWeek37ViewSet)
router.register('KisukariWeek38', views.KisukariWeek38ViewSet)
router.register('KisukariWeek39', views.KisukariWeek39ViewSet)
router.register('KisukariWeek40', views.KisukariWeek40ViewSet)

router.register('KisukariWeek41', views.KisukariWeek41ViewSet)
router.register('KisukariWeek42', views.KisukariWeek42ViewSet)
router.register('KisukariWeek43', views.KisukariWeek43ViewSet)
router.register('KisukariWeek44', views.KisukariWeek44ViewSet)
router.register('KisukariWeek45', views.KisukariWeek45ViewSet)
















#----------------------------------HIV-------------------------




router.register('TaarifaZaHivWeek1', views.TaarifaZaHivWeek1ViewSet)
router.register('TaarifaZaHivWeek2', views.TaarifaZaHivWeek2ViewSet)
router.register('TaarifaZaHivWeek3', views.TaarifaZaHivWeek3ViewSet)
router.register('TaarifaZaHivWeek4', views.TaarifaZaHivWeek4ViewSet)
router.register('TaarifaZaHivWeek5', views.TaarifaZaHivWeek5ViewSet)
router.register('TaarifaZaHivWeek6', views.TaarifaZaHivWeek6ViewSet)
router.register('TaarifaZaHivWeek7', views.TaarifaZaHivWeek7ViewSet)
router.register('TaarifaZaHivWeek8', views.TaarifaZaHivWeek8ViewSet)
router.register('TaarifaZaHivWeek9', views.TaarifaZaHivWeek9ViewSet)
router.register('TaarifaZaHivWeek10', views.TaarifaZaHivWeek10ViewSet)

router.register('TaarifaZaHivWeek11', views.TaarifaZaHivWeek11ViewSet)
router.register('TaarifaZaHivWeek12', views.TaarifaZaHivWeek12ViewSet)
router.register('TaarifaZaHivWeek13', views.TaarifaZaHivWeek13ViewSet)
router.register('TaarifaZaHivWeek14', views.TaarifaZaHivWeek14ViewSet)
router.register('TaarifaZaHivWeek15', views.TaarifaZaHivWeek15ViewSet)
router.register('TaarifaZaHivWeek16', views.TaarifaZaHivWeek16ViewSet)
router.register('TaarifaZaHivWeek17', views.TaarifaZaHivWeek17ViewSet)
router.register('TaarifaZaHivWeek18', views.TaarifaZaHivWeek18ViewSet)
router.register('TaarifaZaHivWeek19', views.TaarifaZaHivWeek19ViewSet)
router.register('TaarifaZaHivWeek20', views.TaarifaZaHivWeek20ViewSet)

router.register('TaarifaZaHivWeek21', views.TaarifaZaHivWeek21ViewSet)
router.register('TaarifaZaHivWeek22', views.TaarifaZaHivWeek22ViewSet)
router.register('TaarifaZaHivWeek23', views.TaarifaZaHivWeek23ViewSet)
router.register('TaarifaZaHivWeek24', views.TaarifaZaHivWeek24ViewSet)
router.register('TaarifaZaHivWeek25', views.TaarifaZaHivWeek25ViewSet)
router.register('TaarifaZaHivWeek26', views.TaarifaZaHivWeek26ViewSet)
router.register('TaarifaZaHivWeek27', views.TaarifaZaHivWeek27ViewSet)
router.register('TaarifaZaHivWeek28', views.TaarifaZaHivWeek28ViewSet)
router.register('TaarifaZaHivWeek29', views.TaarifaZaHivWeek29ViewSet)
router.register('TaarifaZaHivWeek30', views.TaarifaZaHivWeek30ViewSet)

router.register('TaarifaZaHivWeek31', views.TaarifaZaHivWeek31ViewSet)
router.register('TaarifaZaHivWeek32', views.TaarifaZaHivWeek32ViewSet)
router.register('TaarifaZaHivWeek33', views.TaarifaZaHivWeek33ViewSet)
router.register('TaarifaZaHivWeek34', views.TaarifaZaHivWeek34ViewSet)
router.register('TaarifaZaHivWeek35', views.TaarifaZaHivWeek35ViewSet)
router.register('TaarifaZaHivWeek36', views.TaarifaZaHivWeek36ViewSet)
router.register('TaarifaZaHivWeek37', views.TaarifaZaHivWeek37ViewSet)
router.register('TaarifaZaHivWeek38', views.TaarifaZaHivWeek38ViewSet)
router.register('TaarifaZaHivWeek39', views.TaarifaZaHivWeek39ViewSet)
router.register('TaarifaZaHivWeek40', views.TaarifaZaHivWeek40ViewSet)

router.register('TaarifaZaHivWeek41', views.TaarifaZaHivWeek41ViewSet)
router.register('TaarifaZaHivWeek42', views.TaarifaZaHivWeek42ViewSet)
router.register('TaarifaZaHivWeek43', views.TaarifaZaHivWeek43ViewSet)
router.register('TaarifaZaHivWeek44', views.TaarifaZaHivWeek44ViewSet)
router.register('TaarifaZaHivWeek45', views.TaarifaZaHivWeek45ViewSet)








router.register('JeWajuaHivWeek1', views.JeWajuaHivWeek1ViewSet)
router.register('JeWajuaHivWeek2', views.JeWajuaHivWeek2ViewSet)
router.register('JeWajuaHivWeek3', views.JeWajuaHivWeek3ViewSet)
router.register('JeWajuaHivWeek4', views.JeWajuaHivWeek4ViewSet)
router.register('JeWajuaHivWeek5', views.JeWajuaHivWeek5ViewSet)
router.register('JeWajuaHivWeek6', views.JeWajuaHivWeek6ViewSet)
router.register('JeWajuaHivWeek7', views.JeWajuaHivWeek7ViewSet)
router.register('JeWajuaHivWeek8', views.JeWajuaHivWeek8ViewSet)
router.register('JeWajuaHivWeek9', views.JeWajuaHivWeek9ViewSet)
router.register('JeWajuaHivWeek10', views.JeWajuaHivWeek10ViewSet)

router.register('JeWajuaHivWeek11', views.JeWajuaHivWeek11ViewSet)
router.register('JeWajuaHivWeek12', views.JeWajuaHivWeek12ViewSet)
router.register('JeWajuaHivWeek13', views.JeWajuaHivWeek13ViewSet)
router.register('JeWajuaHivWeek14', views.JeWajuaHivWeek14ViewSet)
router.register('JeWajuaHivWeek15', views.JeWajuaHivWeek15ViewSet)
router.register('JeWajuaHivWeek16', views.JeWajuaHivWeek16ViewSet)
router.register('JeWajuaHivWeek17', views.JeWajuaHivWeek17ViewSet)
router.register('JeWajuaHivWeek18', views.JeWajuaHivWeek18ViewSet)
router.register('JeWajuaHivWeek19', views.JeWajuaHivWeek19ViewSet)
router.register('JeWajuaHivWeek20', views.JeWajuaHivWeek20ViewSet)

router.register('JeWajuaHivWeek21', views.JeWajuaHivWeek21ViewSet)
router.register('JeWajuaHivWeek22', views.JeWajuaHivWeek22ViewSet)
router.register('JeWajuaHivWeek23', views.JeWajuaHivWeek23ViewSet)
router.register('JeWajuaHivWeek24', views.JeWajuaHivWeek24ViewSet)
router.register('JeWajuaHivWeek25', views.JeWajuaHivWeek25ViewSet)
router.register('JeWajuaHivWeek26', views.JeWajuaHivWeek26ViewSet)
router.register('JeWajuaHivWeek27', views.JeWajuaHivWeek27ViewSet)
router.register('JeWajuaHivWeek28', views.JeWajuaHivWeek28ViewSet)
router.register('JeWajuaHivWeek29', views.JeWajuaHivWeek29ViewSet)
router.register('JeWajuaHivWeek30', views.JeWajuaHivWeek30ViewSet)

router.register('JeWajuaHivWeek31', views.JeWajuaHivWeek31ViewSet)
router.register('JeWajuaHivWeek32', views.JeWajuaHivWeek32ViewSet)
router.register('JeWajuaHivWeek33', views.JeWajuaHivWeek33ViewSet)
router.register('JeWajuaHivWeek34', views.JeWajuaHivWeek34ViewSet)
router.register('JeWajuaHivWeek35', views.JeWajuaHivWeek35ViewSet)
router.register('JeWajuaHivWeek36', views.JeWajuaHivWeek36ViewSet)
router.register('JeWajuaHivWeek37', views.JeWajuaHivWeek37ViewSet)
router.register('JeWajuaHivWeek38', views.JeWajuaHivWeek38ViewSet)
router.register('JeWajuaHivWeek39', views.JeWajuaHivWeek39ViewSet)
router.register('JeWajuaHivWeek40', views.JeWajuaHivWeek40ViewSet)

router.register('JeWajuaHivWeek41', views.JeWajuaHivWeek41ViewSet)
router.register('JeWajuaHivWeek42', views.JeWajuaHivWeek42ViewSet)
router.register('JeWajuaHivWeek43', views.JeWajuaHivWeek43ViewSet)
router.register('JeWajuaHivWeek44', views.JeWajuaHivWeek44ViewSet)
router.register('JeWajuaHivWeek45', views.JeWajuaHivWeek45ViewSet)









router.register('HivWeek1', views.HivWeek1ViewSet)
router.register('HivWeek2', views.HivWeek2ViewSet)
router.register('HivWeek3', views.HivWeek3ViewSet)
router.register('HivWeek4', views.HivWeek4ViewSet)
router.register('HivWeek5', views.HivWeek5ViewSet)
router.register('HivWeek6', views.HivWeek6ViewSet)
router.register('HivWeek7', views.HivWeek7ViewSet)
router.register('HivWeek8', views.HivWeek8ViewSet)
router.register('HivWeek9', views.HivWeek9ViewSet)
router.register('HivWeek10', views.HivWeek10ViewSet)

router.register('HivWeek11', views.HivWeek11ViewSet)
router.register('HivWeek12', views.HivWeek12ViewSet)
router.register('HivWeek13', views.HivWeek13ViewSet)
router.register('HivWeek14', views.HivWeek14ViewSet)
router.register('HivWeek15', views.HivWeek15ViewSet)
router.register('HivWeek16', views.HivWeek16ViewSet)
router.register('HivWeek17', views.HivWeek17ViewSet)
router.register('HivWeek18', views.HivWeek18ViewSet)
router.register('HivWeek19', views.HivWeek19ViewSet)
router.register('HivWeek20', views.HivWeek20ViewSet)

router.register('HivWeek21', views.HivWeek21ViewSet)
router.register('HivWeek22', views.HivWeek22ViewSet)
router.register('HivWeek23', views.HivWeek23ViewSet)
router.register('HivWeek24', views.HivWeek24ViewSet)
router.register('HivWeek25', views.HivWeek25ViewSet)
router.register('HivWeek26', views.HivWeek26ViewSet)
router.register('HivWeek27', views.HivWeek27ViewSet)
router.register('HivWeek28', views.HivWeek28ViewSet)
router.register('HivWeek29', views.HivWeek29ViewSet)
router.register('HivWeek30', views.HivWeek30ViewSet)

router.register('HivWeek31', views.HivWeek31ViewSet)
router.register('HivWeek32', views.HivWeek32ViewSet)
router.register('HivWeek33', views.HivWeek33ViewSet)
router.register('HivWeek34', views.HivWeek34ViewSet)
router.register('HivWeek35', views.HivWeek35ViewSet)
router.register('HivWeek36', views.HivWeek36ViewSet)
router.register('HivWeek37', views.HivWeek37ViewSet)
router.register('HivWeek38', views.HivWeek38ViewSet)
router.register('HivWeek39', views.HivWeek39ViewSet)
router.register('HivWeek40', views.HivWeek40ViewSet)

router.register('HivWeek41', views.HivWeek41ViewSet)
router.register('HivWeek42', views.HivWeek42ViewSet)
router.register('HivWeek43', views.HivWeek43ViewSet)
router.register('HivWeek44', views.HivWeek44ViewSet)
router.register('HivWeek45', views.HivWeek45ViewSet)















#----------------------------------FAMILIA-------------------------




router.register('TaarifaZaFamiliaWeek1', views.TaarifaZaFamiliaWeek1ViewSet)
router.register('TaarifaZaFamiliaWeek2', views.TaarifaZaFamiliaWeek2ViewSet)
router.register('TaarifaZaFamiliaWeek3', views.TaarifaZaFamiliaWeek3ViewSet)
router.register('TaarifaZaFamiliaWeek4', views.TaarifaZaFamiliaWeek4ViewSet)
router.register('TaarifaZaFamiliaWeek5', views.TaarifaZaFamiliaWeek5ViewSet)
router.register('TaarifaZaFamiliaWeek6', views.TaarifaZaFamiliaWeek6ViewSet)
router.register('TaarifaZaFamiliaWeek7', views.TaarifaZaFamiliaWeek7ViewSet)
router.register('TaarifaZaFamiliaWeek8', views.TaarifaZaFamiliaWeek8ViewSet)
router.register('TaarifaZaFamiliaWeek9', views.TaarifaZaFamiliaWeek9ViewSet)
router.register('TaarifaZaFamiliaWeek10', views.TaarifaZaFamiliaWeek10ViewSet)

router.register('TaarifaZaFamiliaWeek11', views.TaarifaZaFamiliaWeek11ViewSet)
router.register('TaarifaZaFamiliaWeek12', views.TaarifaZaFamiliaWeek12ViewSet)
router.register('TaarifaZaFamiliaWeek13', views.TaarifaZaFamiliaWeek13ViewSet)
router.register('TaarifaZaFamiliaWeek14', views.TaarifaZaFamiliaWeek14ViewSet)
router.register('TaarifaZaFamiliaWeek15', views.TaarifaZaFamiliaWeek15ViewSet)
router.register('TaarifaZaFamiliaWeek16', views.TaarifaZaFamiliaWeek16ViewSet)
router.register('TaarifaZaFamiliaWeek17', views.TaarifaZaFamiliaWeek17ViewSet)
router.register('TaarifaZaFamiliaWeek18', views.TaarifaZaFamiliaWeek18ViewSet)
router.register('TaarifaZaFamiliaWeek19', views.TaarifaZaFamiliaWeek19ViewSet)
router.register('TaarifaZaFamiliaWeek20', views.TaarifaZaFamiliaWeek20ViewSet)

router.register('TaarifaZaFamiliaWeek21', views.TaarifaZaFamiliaWeek21ViewSet)
router.register('TaarifaZaFamiliaWeek22', views.TaarifaZaFamiliaWeek22ViewSet)
router.register('TaarifaZaFamiliaWeek23', views.TaarifaZaFamiliaWeek23ViewSet)
router.register('TaarifaZaFamiliaWeek24', views.TaarifaZaFamiliaWeek24ViewSet)
router.register('TaarifaZaFamiliaWeek25', views.TaarifaZaFamiliaWeek25ViewSet)
router.register('TaarifaZaFamiliaWeek26', views.TaarifaZaFamiliaWeek26ViewSet)
router.register('TaarifaZaFamiliaWeek27', views.TaarifaZaFamiliaWeek27ViewSet)
router.register('TaarifaZaFamiliaWeek28', views.TaarifaZaFamiliaWeek28ViewSet)
router.register('TaarifaZaFamiliaWeek29', views.TaarifaZaFamiliaWeek29ViewSet)
router.register('TaarifaZaFamiliaWeek30', views.TaarifaZaFamiliaWeek30ViewSet)

router.register('TaarifaZaFamiliaWeek31', views.TaarifaZaFamiliaWeek31ViewSet)
router.register('TaarifaZaFamiliaWeek32', views.TaarifaZaFamiliaWeek32ViewSet)
router.register('TaarifaZaFamiliaWeek33', views.TaarifaZaFamiliaWeek33ViewSet)
router.register('TaarifaZaFamiliaWeek34', views.TaarifaZaFamiliaWeek34ViewSet)
router.register('TaarifaZaFamiliaWeek35', views.TaarifaZaFamiliaWeek35ViewSet)
router.register('TaarifaZaFamiliaWeek36', views.TaarifaZaFamiliaWeek36ViewSet)
router.register('TaarifaZaFamiliaWeek37', views.TaarifaZaFamiliaWeek37ViewSet)
router.register('TaarifaZaFamiliaWeek38', views.TaarifaZaFamiliaWeek38ViewSet)
router.register('TaarifaZaFamiliaWeek39', views.TaarifaZaFamiliaWeek39ViewSet)
router.register('TaarifaZaFamiliaWeek40', views.TaarifaZaFamiliaWeek40ViewSet)

router.register('TaarifaZaFamiliaWeek41', views.TaarifaZaFamiliaWeek41ViewSet)
router.register('TaarifaZaFamiliaWeek42', views.TaarifaZaFamiliaWeek42ViewSet)
router.register('TaarifaZaFamiliaWeek43', views.TaarifaZaFamiliaWeek43ViewSet)
router.register('TaarifaZaFamiliaWeek44', views.TaarifaZaFamiliaWeek44ViewSet)
router.register('TaarifaZaFamiliaWeek45', views.TaarifaZaFamiliaWeek45ViewSet)








router.register('JeWajuaFamiliaWeek1', views.JeWajuaFamiliaWeek1ViewSet)
router.register('JeWajuaFamiliaWeek2', views.JeWajuaFamiliaWeek2ViewSet)
router.register('JeWajuaFamiliaWeek3', views.JeWajuaFamiliaWeek3ViewSet)
router.register('JeWajuaFamiliaWeek4', views.JeWajuaFamiliaWeek4ViewSet)
router.register('JeWajuaFamiliaWeek5', views.JeWajuaFamiliaWeek5ViewSet)
router.register('JeWajuaFamiliaWeek6', views.JeWajuaFamiliaWeek6ViewSet)
router.register('JeWajuaFamiliaWeek7', views.JeWajuaFamiliaWeek7ViewSet)
router.register('JeWajuaFamiliaWeek8', views.JeWajuaFamiliaWeek8ViewSet)
router.register('JeWajuaFamiliaWeek9', views.JeWajuaFamiliaWeek9ViewSet)
router.register('JeWajuaFamiliaWeek10', views.JeWajuaFamiliaWeek10ViewSet)

router.register('JeWajuaFamiliaWeek11', views.JeWajuaFamiliaWeek11ViewSet)
router.register('JeWajuaFamiliaWeek12', views.JeWajuaFamiliaWeek12ViewSet)
router.register('JeWajuaFamiliaWeek13', views.JeWajuaFamiliaWeek13ViewSet)
router.register('JeWajuaFamiliaWeek14', views.JeWajuaFamiliaWeek14ViewSet)
router.register('JeWajuaFamiliaWeek15', views.JeWajuaFamiliaWeek15ViewSet)
router.register('JeWajuaFamiliaWeek16', views.JeWajuaFamiliaWeek16ViewSet)
router.register('JeWajuaFamiliaWeek17', views.JeWajuaFamiliaWeek17ViewSet)
router.register('JeWajuaFamiliaWeek18', views.JeWajuaFamiliaWeek18ViewSet)
router.register('JeWajuaFamiliaWeek19', views.JeWajuaFamiliaWeek19ViewSet)
router.register('JeWajuaFamiliaWeek20', views.JeWajuaFamiliaWeek20ViewSet)

router.register('JeWajuaFamiliaWeek21', views.JeWajuaFamiliaWeek21ViewSet)
router.register('JeWajuaFamiliaWeek22', views.JeWajuaFamiliaWeek22ViewSet)
router.register('JeWajuaFamiliaWeek23', views.JeWajuaFamiliaWeek23ViewSet)
router.register('JeWajuaFamiliaWeek24', views.JeWajuaFamiliaWeek24ViewSet)
router.register('JeWajuaFamiliaWeek25', views.JeWajuaFamiliaWeek25ViewSet)
router.register('JeWajuaFamiliaWeek26', views.JeWajuaFamiliaWeek26ViewSet)
router.register('JeWajuaFamiliaWeek27', views.JeWajuaFamiliaWeek27ViewSet)
router.register('JeWajuaFamiliaWeek28', views.JeWajuaFamiliaWeek28ViewSet)
router.register('JeWajuaFamiliaWeek29', views.JeWajuaFamiliaWeek29ViewSet)
router.register('JeWajuaFamiliaWeek30', views.JeWajuaFamiliaWeek30ViewSet)

router.register('JeWajuaFamiliaWeek31', views.JeWajuaFamiliaWeek31ViewSet)
router.register('JeWajuaFamiliaWeek32', views.JeWajuaFamiliaWeek32ViewSet)
router.register('JeWajuaFamiliaWeek33', views.JeWajuaFamiliaWeek33ViewSet)
router.register('JeWajuaFamiliaWeek34', views.JeWajuaFamiliaWeek34ViewSet)
router.register('JeWajuaFamiliaWeek35', views.JeWajuaFamiliaWeek35ViewSet)
router.register('JeWajuaFamiliaWeek36', views.JeWajuaFamiliaWeek36ViewSet)
router.register('JeWajuaFamiliaWeek37', views.JeWajuaFamiliaWeek37ViewSet)
router.register('JeWajuaFamiliaWeek38', views.JeWajuaFamiliaWeek38ViewSet)
router.register('JeWajuaFamiliaWeek39', views.JeWajuaFamiliaWeek39ViewSet)
router.register('JeWajuaFamiliaWeek40', views.JeWajuaFamiliaWeek40ViewSet)

router.register('JeWajuaFamiliaWeek41', views.JeWajuaFamiliaWeek41ViewSet)
router.register('JeWajuaFamiliaWeek42', views.JeWajuaFamiliaWeek42ViewSet)
router.register('JeWajuaFamiliaWeek43', views.JeWajuaFamiliaWeek43ViewSet)
router.register('JeWajuaFamiliaWeek44', views.JeWajuaFamiliaWeek44ViewSet)
router.register('JeWajuaFamiliaWeek45', views.JeWajuaFamiliaWeek45ViewSet)









router.register('FamiliaWeek1', views.FamiliaWeek1ViewSet)
router.register('FamiliaWeek2', views.FamiliaWeek2ViewSet)
router.register('FamiliaWeek3', views.FamiliaWeek3ViewSet)
router.register('FamiliaWeek4', views.FamiliaWeek4ViewSet)
router.register('FamiliaWeek5', views.FamiliaWeek5ViewSet)
router.register('FamiliaWeek6', views.FamiliaWeek6ViewSet)
router.register('FamiliaWeek7', views.FamiliaWeek7ViewSet)
router.register('FamiliaWeek8', views.FamiliaWeek8ViewSet)
router.register('FamiliaWeek9', views.FamiliaWeek9ViewSet)
router.register('FamiliaWeek10', views.FamiliaWeek10ViewSet)

router.register('FamiliaWeek11', views.FamiliaWeek11ViewSet)
router.register('FamiliaWeek12', views.FamiliaWeek12ViewSet)
router.register('FamiliaWeek13', views.FamiliaWeek13ViewSet)
router.register('FamiliaWeek14', views.FamiliaWeek14ViewSet)
router.register('FamiliaWeek15', views.FamiliaWeek15ViewSet)
router.register('FamiliaWeek16', views.FamiliaWeek16ViewSet)
router.register('FamiliaWeek17', views.FamiliaWeek17ViewSet)
router.register('FamiliaWeek18', views.FamiliaWeek18ViewSet)
router.register('FamiliaWeek19', views.FamiliaWeek19ViewSet)
router.register('FamiliaWeek20', views.FamiliaWeek20ViewSet)

router.register('FamiliaWeek21', views.FamiliaWeek21ViewSet)
router.register('FamiliaWeek22', views.FamiliaWeek22ViewSet)
router.register('FamiliaWeek23', views.FamiliaWeek23ViewSet)
router.register('FamiliaWeek24', views.FamiliaWeek24ViewSet)
router.register('FamiliaWeek25', views.FamiliaWeek25ViewSet)
router.register('FamiliaWeek26', views.FamiliaWeek26ViewSet)
router.register('FamiliaWeek27', views.FamiliaWeek27ViewSet)
router.register('FamiliaWeek28', views.FamiliaWeek28ViewSet)
router.register('FamiliaWeek29', views.FamiliaWeek29ViewSet)
router.register('FamiliaWeek30', views.FamiliaWeek30ViewSet)

router.register('FamiliaWeek31', views.FamiliaWeek31ViewSet)
router.register('FamiliaWeek32', views.FamiliaWeek32ViewSet)
router.register('FamiliaWeek33', views.FamiliaWeek33ViewSet)
router.register('FamiliaWeek34', views.FamiliaWeek34ViewSet)
router.register('FamiliaWeek35', views.FamiliaWeek35ViewSet)
router.register('FamiliaWeek36', views.FamiliaWeek36ViewSet)
router.register('FamiliaWeek37', views.FamiliaWeek37ViewSet)
router.register('FamiliaWeek38', views.FamiliaWeek38ViewSet)
router.register('FamiliaWeek39', views.FamiliaWeek39ViewSet)
router.register('FamiliaWeek40', views.FamiliaWeek40ViewSet)

router.register('FamiliaWeek41', views.FamiliaWeek41ViewSet)
router.register('FamiliaWeek42', views.FamiliaWeek42ViewSet)
router.register('FamiliaWeek43', views.FamiliaWeek43ViewSet)
router.register('FamiliaWeek44', views.FamiliaWeek44ViewSet)
router.register('FamiliaWeek45', views.FamiliaWeek45ViewSet)







urlpatterns = router.urls