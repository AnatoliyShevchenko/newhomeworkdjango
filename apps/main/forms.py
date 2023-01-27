from django import forms

from main.models import Button, Keyboard


class ButtonForm(forms.ModelForm):
    class Meta:
        model = Button
        fields = '__all__'


class KeyboardForm(forms.ModelForm):
    class Meta:
        model = Keyboard
        fields = '__all__'