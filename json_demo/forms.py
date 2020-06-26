from django.forms import ModelForm
from json_demo.models import UserDetails

class UserModelForm(ModelForm):
    class Meta:
        model = UserDetails
        fields = ['real_name', 'tz', 'start_time', 'end_time']