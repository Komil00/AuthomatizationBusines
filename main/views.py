from django.shortcuts import render, get_object_or_404
from .models import Zavod, Mahsulot, Client, ClientQarzlari, ZavoddanOlganMahsulot, Tarqatish
from .serializers import ZavodListSerializers, ZavodCreateSerializers, MahsulotListSerializers, \
    MahsulotCreateSerializers, ClientListSerializers, ClientCreateSerializers, \
    ZavoddanOlganMahsulotListSerializers, ZavoddanOlganMahsulotCreateSerializers, \
    TarqatishCreateSerializers, TarqatishListSerializers, \
    ClientQarzlariListSerializers, ClientQarzlariCreateSerializers, TarqatishPutSerializers
from rest_framework import status, views, generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ZavodViewSets(viewsets.ModelViewSet):
    queryset = Zavod.objects.all()
    serializer_class = ZavodListSerializers
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = ZavodCreateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(diller=request.user)
        serializer.save()
        return Response('Zavod yratildi', status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.action in ['list']:
            return ZavodListSerializers
        else:
            return ZavodCreateSerializers

    def get_queryset(self):
        return Zavod.objects.filter(diller=self.request.user)


class MahsulotViewSets(viewsets.ModelViewSet):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotListSerializers
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = MahsulotCreateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(diller=request.user)
        serializer.save()
        return Response('Mahsulot yratildi', status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.action in ['list']:
            return MahsulotListSerializers
        else:
            return MahsulotCreateSerializers

    def get_queryset(self):
        return Mahsulot.objects.filter(diller=self.request.user)


class ClientViewSets(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializers
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = ClientCreateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(diller=request.user)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.action in ['list']:
            return ClientListSerializers
        else:
            return ClientCreateSerializers

    def get_queryset(self):
        return Client.objects.filter(diller=self.request.user)


class ZavoddanOlganMahsulotViewSets(viewsets.ModelViewSet):
    queryset = ZavoddanOlganMahsulot.objects.all()
    serializer_class = ZavoddanOlganMahsulotListSerializers()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = ZavoddanOlganMahsulotCreateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(diller=request.user)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.action in ['list']:
            return ZavoddanOlganMahsulotListSerializers
        else:
            return ZavoddanOlganMahsulotCreateSerializers

    def get_queryset(self):
        return ZavoddanOlganMahsulot.objects.filter(diller=self.request.user)


class TarqatishViewSets(viewsets.ModelViewSet):
    queryset = Tarqatish.objects.all()
    serializer_class = TarqatishListSerializers()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = TarqatishCreateSerializers(data=request.data)
        mahsulot_nomi = ZavoddanOlganMahsulot.objects.get(id=request.data['mahsulot_nomi'])
        try:
            order_mahsulot_nomi = int(request.data['mahsulot_soni'])
            if mahsulot_nomi.mahsulot_soni < order_mahsulot_nomi:
                return Response("buncha mahsulot yo'q", status=status.HTTP_400_BAD_REQUEST)
            serializer.is_valid(raise_exception=True)
            mahsulot_nomi.mahsulot_soni -= order_mahsulot_nomi
            mahsulot_nomi.save()
            serializer.save(diller=request.user)  # user pole ni zapros berayotgan user bn tuldiradi
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError:
            return Response('Butun son kiriting', status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request, pk=None, *args, **kwargs):
    #     serializer = TarqatishPutSerializers(data=request.data)
    #     serializer.is_valid()
    #     set_zakaz = set()
    #     zakaz = get_object_or_404(self.queryset, pk=pk)
    #     set_zakaz.add(zakaz)
    #     zak = set_zakaz.pop()
    #     mahsulot_son = serializer.validated_data.get('mahsulot_soni')
    #     mahsulot_nomi = zak.mahsulot_nomi
    #     if mahsulot_son:
    #         if mahsulot_son >= zak.mahsulot_soni:
    #             if mahsulot_nomi.mahsulot_soni < mahsulot_son - zak.mahsulot_soni:
    #                 return Response("do'konda buncha mahsulot yo'q", status=status.HTTP_400_BAD_REQUEST)
    #             mahsulot_nomi.mahsulot_soni -= mahsulot_son - zak.mahsulot_soni
    #         else:
    #             mahsulot_nomi.productquantity += zak.productquantity - mahsulot_son
    #         mahsulot_nomi.save()
    #         zak.productquantity = mahsulot_son
    #         zak.save()
    #         return Response({"success": "mahsulotingiz soni muvafaqiyatli o'zgartirildi"})
    #     return Response("mahsulot sonini to'gri kiriting", status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.action in ['list']:
            return TarqatishListSerializers
        elif self.action in ['create']:
            return TarqatishCreateSerializers
        else:
            return TarqatishPutSerializers

    def get_queryset(self):
        return Tarqatish.objects.filter(diller=self.request.user)


class ClientQarzlariViewSets(viewsets.ModelViewSet):
    queryset = ClientQarzlari.objects.all()
    serializer_class = ClientQarzlariListSerializers()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = ClientQarzlariCreateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(diller=request.user)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.action in ['list']:
            return ClientQarzlariListSerializers
        else:
            return ClientQarzlariCreateSerializers

    def get_queryset(self):
        return ClientQarzlari.objects.filter(diller=self.request.user)
