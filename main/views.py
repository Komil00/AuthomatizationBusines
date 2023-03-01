from django.shortcuts import render
from .models import Zavod, Mahsulot, Client, ClientQarzlari, ZavoddanOlganMahsulot, Tarqatish
from .serializers import ZavodListSerializers, ZavodCreateSerializers , MahsulotListSerializers,\
MahsulotCreateSerializers, ClientListSerializers, ClientCreateSerializers,\
ZavoddanOlganMahsulotListSerializers, ZavoddanOlganMahsulotCreateSerializers,\
TarqatishCreateSerializers, TarqatishListSerializers,\
ClientQarzlariListSerializers, ClientQarzlariCreateSerializers
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
        serializer.is_valid(raise_exception=True)
        serializer.save(diller=request.user)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get_serializer_class(self):
        if self.action in ['list']:
            return TarqatishListSerializers
        else:
            return TarqatishCreateSerializers
        
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
    
