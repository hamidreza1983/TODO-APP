from django.shortcuts import render, redirect, HttpResponse, HttpResponsePermanentRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib import messages
from django.urls import reverse



#================= Login CBV ==================
class LoginView(View):

    template_name ='registration/login.html'
    #post method override
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect ('/')
            else:
                return HttpResponse("Inactive user.")
        else:
            return redirect ('/')   

    #get method override
    def get(self, request):
        return render(request, self.template_name)
        

#=================Logout FBV ====================
@login_required
def Logout(request):
    logout(request)
    return redirect('/')




#==================Register CBV ====================
class RegisterView(View):

    template_name ='registration/signup.html'
    #post method override
    # if registration complete LOGIN AUTOMATICALLY
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect ('/')
        else :
            messages.add_message(request, messages.ERROR, 'Use a strong password')
            return HttpResponsePermanentRedirect(reverse('accounts:login'))
        

    #get method override
    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})