from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,FormView
from .forms import RegForm,LogForm
from django.urls import reverse_lazy
from django.forms import BaseModelForm
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate,login,logout




# Create your views here.

class LandingView(TemplateView):
    template_name="landing.html"

# class LoginView(TemplateView):
#     template_name="log.html"


class LoginView(FormView):
    template_name="log.html"
    form_class=LogForm
    def post(self,request):
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get('username')
            pswd=form_data.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                print(user)
                login(request,user)
                messages.success(request,"login successfull!")
                return redirect('home')
            else:
                print(user,"login failed")
                messages.error(request,"LOGIN FAILED")
                return redirect('log')
        return render(request,"log.html",{"form":form_data}) 


class Regview(CreateView):
    form_class=RegForm
    template_name='reg.html'
    success_url=reverse_lazy("log")
    def from_valid(self, form: BaseModelForm):
        messages.success(self.request,"registration success")
        return super().from_valid(form)
    def from_invalid(self, form: BaseModelForm):
        messages.error(self.request,"registration failed")
        return super().from_invalid(form)

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('landing')
    

    