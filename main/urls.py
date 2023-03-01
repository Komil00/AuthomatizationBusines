from django.urls import path, include
from .views import ZavodViewSets, MahsulotViewSets, ClientViewSets, ZavoddanOlganMahsulotViewSets,\
TarqatishViewSets, ClientQarzlariViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'zavod', ZavodViewSets, basename='zavod')
router.register(r'mahsulot', MahsulotViewSets, basename='mahsulot')
router.register(r'zavoddan_olgan_mahsulot', ZavoddanOlganMahsulotViewSets, basename='zavoddan_olgan_mahsulot')
router.register(r'client', ClientViewSets, basename='client')
router.register(r'client_qarzlari', ClientQarzlariViewSets, basename='client_qarzlari')
router.register(r'tarqatish', TarqatishViewSets, basename='tarqatish')



urlpatterns = [
    path('', include(router.urls)),
]
