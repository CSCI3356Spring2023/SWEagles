from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import CustomUser
from django.contrib.auth import login

class registerForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    
    class Meta:
        model = CustomUser
        fields = ('username','role','email', 'password1', 'password2')
        
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(registerForm, self).form_valid(form)
