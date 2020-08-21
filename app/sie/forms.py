from django import forms
from app.sie.models import Prospecto

class createAdmisionForm(forms.ModelForm):
    class Meta: 
        model = Prospecto
        exclude = ['p_estatus']
        # fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        




    