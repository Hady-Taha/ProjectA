from django.urls import path, include
from webservices.ControlAccessLayer import view
from django.conf.urls import  url
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [

    path('api-auth',  include ('rest_framework.urls') ),
    path('api/auth/token/', TokenObtainPairView.as_view() ),
    path('api/token/refresh/', TokenRefreshView.as_view() ),

    #calss based views
    path('api/profiles', view.profileListApi2.as_view(), name='profileListApi'),
    path('api/profiles/<int:id>', view.profileDetails.as_view(), name='studentprofileapi'),

    #attendence api
    path('api/attendence', view.attendenceListApi, name='attendenceListApi2'),
]