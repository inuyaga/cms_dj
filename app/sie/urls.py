from django.urls import path
from app.sie import views as Vistas


app_name = 'sie'

urlpatterns = [
    path('', Vistas.index.as_view(), name="index"),
]
