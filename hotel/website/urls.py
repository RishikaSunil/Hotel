from django.urls import path
from website.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('log',LoginView.as_view(),name="log"),
    path('reg',Regview.as_view(),name="reg"),
    path('logout',LogoutView.as_view(),name="out")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
