from django.urls import path

from .views import *

urlpatterns = [
    path('', login),
    path('home/', home),
    path('allemp/', allemp),
    path('addemp/', addemp),
    path('removeemp/', removeemp),
    path('removeemp/<int:id>', removeemp),
    path('filteremp/', filteremp),
    path('navbar/', navbar),
    path('removesuccess/', removesuccess),

]
