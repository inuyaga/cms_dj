from django.urls import path
from app.cucm import views as ViewCucm


app_name = 'cucm'

urlpatterns = [
    path('', ViewCucm.Inicio.as_view(), name="index"),
    
]
