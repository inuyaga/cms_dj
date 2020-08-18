from django.urls import path
from app.web import views as Vistas


app_name = 'web'

urlpatterns = [
    path('', Vistas.webindex.as_view(), name="index"),
    path('Historia/', Vistas.historia.as_view(), name="Historia"),
]
