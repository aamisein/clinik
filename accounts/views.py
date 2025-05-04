from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.urls import reverse
from django.views import View
from .forms import LoginForm

# Create your views here.
class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {'form': login_form}
        return render(request, 'accounts/login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('visits:home'))  # یا هر صفحه‌ای که می‌خواهید
                else:
                    login_form.add_error(None, 'حساب کاربری شما فعال نیست.')
            else:
                login_form.add_error(None, 'نام کاربری یا رمز عبور اشتباه است.')
        context = {'form': login_form}
        return render(request, 'accounts/login.html', context)



class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('accounts:login_page'))   