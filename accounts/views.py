from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView
from django.contrib.auth.models import User
from .forms import UserForm

from django.urls import reverse, reverse_lazy 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class RegistrationView(CreateView):
    form_class = UserForm
    success_url = reverse_lazy('user_login')
    template_name = 'registration.html'

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Account Not active!")
        else:
            print("someone tried to login and failed!")
            print("username: {} password: {}".format(username, password))
            return render(request, 'error.html', {})

    else:
        return render(request, 'login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))