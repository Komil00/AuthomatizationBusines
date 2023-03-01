from rest_framework import serializers
from .models import Zavod, Mahsulot, Client, ClientQarzlari, ZavoddanOlganMahsulot, Tarqatish
from customuser.serializers import CustomUserListSerializer


class ZavodListSerializers(serializers.ModelSerializer):
    diller = CustomUserListSerializer()
    class Meta:
        model = Zavod
        fields = '__all__'

class ZavodCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Zavod
        fields = ['name', 'phone_number']

class MahsulotListSerializers(serializers.ModelSerializer):
    diller = CustomUserListSerializer()
    ishlab_chiqarilgan_korxona = ZavodCreateSerializers()
    class Meta:
        model = Mahsulot
        fields = '__all__'

class MahsulotCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = ['name', 'ishlab_chiqarilgan_korxona', 'ishlab_chiqarilgan_sana']

class ClientListSerializers(serializers.ModelSerializer):
    diller = CustomUserListSerializer()
    class Meta:
        model = Client
        fields = '__all__'

class ClientCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'phone_number']

class ZavoddanOlganMahsulotListSerializers(serializers.ModelSerializer):
    diller = CustomUserListSerializer()
    class Meta:
        model = ZavoddanOlganMahsulot
        fields = '__all__'

class ZavoddanOlganMahsulotCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = ZavoddanOlganMahsulot
        fields = ['zavod_nomi', 'mahsulot_nomi', 'mahsulot_soni', 'bitta_mahsulot_narxi', 'olgan_vaqt']

class TarqatishListSerializers(serializers.ModelSerializer):
    diller = CustomUserListSerializer()
    class Meta:
        model = Tarqatish
        fields = '__all__'

class TarqatishCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tarqatish
        fields = ['client', 'mahsulot_nomi', 'mahsulot_soni', 'bitta_mahsulot_narxi', 'tarqatgan_vaqti']


class ClientQarzlariListSerializers(serializers.ModelSerializer):
    diller = CustomUserListSerializer()
    class Meta:
        model = ClientQarzlari
        fields = '__all__'

class ClientQarzlariCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClientQarzlari
        fields = ['client', 'mahsulot_nomi', 'mahsulot_soni', 'bitta_mahsulot_narxi', 'qarz_berish_vaqti']