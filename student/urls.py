from django.urls import path, include
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),attendance
    path('student/', views.student, name='student'),
    path('attendance/', views.attendance, name='attendance'),
]
