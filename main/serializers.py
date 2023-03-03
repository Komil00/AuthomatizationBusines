from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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
    # ishlab_chiqarilgan_korxona = serializers.PrimaryKeyRelatedField(many=True, queryset=Zavod.objects.filter(diller=))

    class Meta:
        model = Mahsulot
        fields = ['name', 'image', 'ishlab_chiqarilgan_korxona', 'ishlab_chiqarilgan_sana']


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
        fields = ['diller', 'zavod_nomi', 'mahsulot_nomi', 'mahsulot_soni', 'bitta_mahsulot_narxi', 'olgan_vaqt']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['total_price'] = instance.mahsulot_soni * instance.bitta_mahsulot_narxi
        return representation


class ZavoddanOlganMahsulotCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = ZavoddanOlganMahsulot
        fields = ['zavod_nomi', 'mahsulot_nomi', 'mahsulot_soni', 'bitta_mahsulot_narxi', 'olgan_vaqt']


class TarqatishListSerializers(serializers.ModelSerializer):
    # diller = CustomUserListSerializer()

    class Meta:
        model = Tarqatish
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['total_price'] = instance.mahsulot_soni * instance.bitta_mahsulot_narxi
        return representation


class TarqatishCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tarqatish
        fields = ['client', 'mahsulot_nomi', 'mahsulot_soni', 'bitta_mahsulot_narxi', 'tarqatgan_vaqti']

    def validate_mahsulot_soni(self, value):
        if value < 1:
            raise ValidationError("mahsulot soni 0 dan kop bolishi kerak")
        return value


class TarqatishPutSerializers(serializers.ModelSerializer):
    diller = CustomUserListSerializer(read_only=True)
    mahsulot_nomi = MahsulotListSerializers(read_only=True)

    class Meta:
        model = Tarqatish
        fields = '__all__'

    def validate_mahsulot_soni(self, value):
        if value < 1:
            raise ValidationError("mahsulot soni 0 dan kop bolishi kerak")
        return value


class ClientQarzlariListSerializers(serializers.ModelSerializer):
    diller = CustomUserListSerializer()

    class Meta:
        model = ClientQarzlari
        fields = '__all__'


class ClientQarzlariCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClientQarzlari
        fields = ['client', 'mahsulot_nomi', 'mahsulot_soni', 'bitta_mahsulot_narxi', 'qarz_berish_vaqti']
