from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('pay/',home,name='home'),
    path('success/',success,name='success'),
    path('',tt,name='home22'),
    path('about/',about_page, name='about'),
    path('contact/',contact_page, name='contact'),
    path('refund/',refund,name='refund'),
    path('soon/',soon,name='soon'),
    path('ladmin/',ladmin,name="ladmin"),
    path('edit/',edit,name="edit"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)