from django.urls import path
from .views import *

urlpatterns = [
    path('pay/',home,name='home'),
    path('success/',success,name='success'),
    path('',tt,name='home22'),
    path('about/',about_page, name='about'),
    path('contact/',contact_page, name='contact'),
    path('refund/',refund,name='refund'),
    path('soon/',soon,name='soon'),

]