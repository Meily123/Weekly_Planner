from django import forms
from task.models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 100%; margin-top:5px', 'class': 'form-control'}))
    date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 100%; margin-top:5px', 'class': 'form-control'}))
    initial = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 100%; margin-top:5px', 'class': 'form-control'}))
    target = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 100%; margin-top:5px', 'class': 'form-control'}))
    weight = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 100%; margin-top:5px', 'class': 'form-control'}))
    class Meta:
        model = Task
        fields = '__all__'