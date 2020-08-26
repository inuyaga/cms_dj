from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from app.cucm import views as ViewCucm


app_name = 'cucm'

urlpatterns = [
    path('', ViewCucm.Inicio.as_view(), name="index"),
    path('inscripcion/', ViewCucm.InscripcionCucmView.as_view(), name="inscribir"),
    path('sie/',include('app.sie.urls')),
    path('admincms/', admin.site.urls),    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
