from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from rest_framework.decorators import action
from rest_framework import status

from .serializers import CustomUserSerializers, CustomUserListSerializer, \
    CustomUserVerifyCodeSerializer, MeSerializers, MePutPatchDeleteSerializers
from .models import CustomUser

from rest_framework import permissions

from rest_framework import permissions
from customuser.emails import send_code_to_email
from AuthomatizationBusines import settings


class AuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    # def has_object_permission(self, request, view, obj):
    #     if obj.author == request.user:
    #         return True
    #     return False


class UsersViewList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['email', 'username']
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserListSerializer


# class UserView(generics.RetrieveUpdateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#
#     def perform_update(self, serializer):
#         if self.request.user.is_staff:
#             instance = self.get_object()
#             serializer.save(instance=instance)
#         if self.request.user.role == 'MANAGER':
#             user = CustomUser.objects.get(pk=self.kwargs['pk'])
#             if user.role == 'OPERATOR':
#                 instance = self.get_object()
#                 serializer.save(instance=instance)
#             else:
#                 return None


class CreateUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializers
    queryset = CustomUser.objects.all()
    http_method_names = ['post']

    def perform_create(self, serializer):
        serializer.save()
        send_code_to_email(serializer.data['email'])


class MeViewSet(viewsets.ModelViewSet):
    serializer_class = MeSerializers
    queryset = CustomUser.objects.all()
    http_method_names = ['get', 'put', 'delete']

    @action(detail=False, methods=['get', 'put', 'patch', 'delete'])
    def me(self, request, pk=None, *args, **kwargs):
        self.kwargs['pk'] = request.user.pk
        if request.method == "GET":
            return super().list(request, *args, **kwargs)
        elif request.method in ["PUT", "PATCH"]:
            return super().update(request, *args, **kwargs)
        elif request.method == "DELETE":
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(status=405)

    def get_serializer_class(self):
        if self.action in ['list']:
            return MeSerializers
        else:
            return MePutPatchDeleteSerializers

    def get_queryset(self):
        return CustomUser.objects.filter(username=self.request.user.username)


class UsersVerifyApiView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserVerifyCodeSerializer
    http_method_names = ['post']

    def create(self, request):
        data = request.data
        serializer = CustomUserVerifyCodeSerializer(data=data)
        if serializer.is_valid():
            email = serializer.data['email']
            code = serializer.data['code']
            user = CustomUser.objects.filter(email=email)
            if not user.exists():
                return Response({
                    'status': 400,
                    'message': 'something went wrong',
                    'data': 'invalid email'
                })
            if user.first().code != code:
                return Response({
                    'status': 400,
                    'message': 'something went wrong',
                    'data': 'invalid code'
                })
            user = user.first()
            user.is_verify = True
            user.save()

            return Response({
                'status': 200,
                'message': 'account verified',
                'data': {}
            })
