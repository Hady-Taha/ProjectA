from django.urls import path, include
from . import views
# from . import api

urlpatterns = [
    #path('admin/', admin.site.urls),attendance
    path('student/', views.student, name='student'),
    path('attendance/', views.attendance, name='attendance'),

    # #api 
    # path('api/profiles', api.profileListApi, name='profileListApi'),
    # path('api/profiles/<int:id>', api.profile_details_api, name='studentprofileapi'),

    # #calss based views
    # path('api/v2/profiles', api.profileListApi2.as_view(), name='profileListApi'),
    # path('api/v2/profiles/<int:id>', api.profileDrtails.as_view(), name='studentprofileapi'),


    # #attendence api
    #  path('api/attendence', api.attendenceListApi, name='attendenceListApi2'),

]

