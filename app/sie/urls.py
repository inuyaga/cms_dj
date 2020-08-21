from django.urls import path
from app.sie import views as Vistas


app_name = 'sie'

urlpatterns = [
    path('', Vistas.index.as_view(), name="index"),
    path('Admision', Vistas.CreateAdmisiones.as_view(), name="CreateAdmision"),
    path('ListaAdmision', Vistas.AdmisionesListView.as_view(), name="VerAdmision"),
    path('DetalleAdmision/<int:pk>', Vistas.AdmisionesDetailView.as_view(), name="DetalleAdmision"),
]
