from django.contrib import admin
from django.urls import path, include

from employee.urls import router

from .views import index


urlpatterns = [
    path('', index, name='index'),
    path('employee/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth', include('rest_framework.urls')),
]
