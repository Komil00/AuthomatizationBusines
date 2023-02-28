from django.urls import path, include
from .views import UsersViewList, UsersVerifyApiView, CreateUserViewSet, MeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'me', MeViewSet, basename='me')
router.register(r'registration', CreateUserViewSet, basename='registration')
router.register(r'verify_code', UsersVerifyApiView, basename='verify_code')

urlpatterns = [
    path('all_users', UsersViewList.as_view()),
    path('', include(router.urls))
]


