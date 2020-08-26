from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from app.web import views as Vistas


app_name = 'web'

urlpatterns = [
    path('', Vistas.webindex.as_view(), name="index"),
    path('Historia/', Vistas.historia.as_view(), name="Historia"),
    path('sie/',include('app.sie.urls')),
    path('admincms/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
