from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import RegisterForm


class RegisterView(View):
    form_class = RegisterForm
    template_name = 'app_users/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(to='quotes:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f"Wellcome, {username}! Your account has been created.")
            return redirect(to="app_users:signin")
        return render(request, self.template_name, {'form': form})