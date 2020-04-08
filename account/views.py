from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserLoginForm

# Login
class UserLogin(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'
    # Display blank form
    def get(self, request):
        context = {
            "form":self.form_class()
        }
        return render(request, self.template_name, context)

    # process form data
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        # returns User objects if credentials are correct
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect("dashboard:index")
        context = {
            "form":form_class(),
            'message': 'Wrong password or username, please check and try and again.',
        }
        return render(request, self.template_name, context)

def logout_user(request):
    logout(request)
    # Redirect to a success page.
    return redirect('account:login')