from rest_framework.routers import DefaultRouter
from django.urls import path

from api.apps import ApiConfig
from api.views import *

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('referrals', ReferralModelViewSet)


app_name = ApiConfig.name

urlpatterns = ([
                   path('user/<int:pk>', UsersIdListAPIView.as_view(), name='user_id'),
                   path('user/<str:email>', UsersCodeRetrieveAPIView.as_view(), name='user_code'),
               ]
               + router.urls)
