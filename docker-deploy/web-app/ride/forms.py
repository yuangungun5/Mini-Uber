from django import forms
from .models import Ride, DriverSearch, SharerSearch, ShareOrder

class DriverSearchForm(forms.ModelForm):
    class Meta:
        model = DriverSearch
        fields = ['arrival_after', 'arrival_before']
  
class SharerSearchForm(forms.ModelForm):
    class Meta:
        model = SharerSearch
        fields = ['destination', 'passenger_num', 'arrival_after', 'arrival_before']

class ShareCreateForm(forms.ModelForm):
    class Meta:
        model = ShareOrder
        fields = ['passenger_num']
