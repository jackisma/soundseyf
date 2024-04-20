from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import UserCreationForm
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render
import sweetify


# Login View Function
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                # Extract username and password from the form
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                email = form.cleaned_data.get('email')

                # Check if email is provided, if so, set username to email
                if email:
                    username = email

                # Authenticate the user
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    # Login the user
                    login(request, user)
                    sweetify.success(request, 'Login successful!', persistent = 'ok')
                    return redirect('/')
            else:
                sweetify.error(request, 'Login failed. Please check your username and password.', persistent=':(')
                return redirect('/')  # Redirect back to the login page
        else:
            form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')




# Signup View Function
def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                # Check if username or email already exists
                if User.objects.filter(email=email).exists():
                    sweetify.error(request, 'Signup not successful. Email address already registered.', persistent=':(')
                    return render(request, 'accounts/register.html', {'form': form})
                else:
                    form.save()
                    sweetify.success(request, 'Signup successful', persistent='OK')
                    return redirect('/')
            else:
                sweetify.error(request, 'Signup not successful. Please Check your Email , Password and Username!', persistent=':(')
                return render(request, 'accounts/register.html', {'form': form})
        else:
            form = UserCreationForm()
            context = {'form': form}
            return render(request, 'accounts/register.html', context)
    else:
        return redirect('/')
         
                    



# Logout View Class 
class LogoutView(TemplateView, View):
    template_name = 'accounts/logout.html'

    def post(self, request, *args, **kwargs):
        return self.log_out_user(request)

    def log_out_user(self, request):
        # Perform the actual logout logic here
        # For example, you can use Django's built-in logout function
        logout(request)
        sweetify.success(request,'logout successful',persistent = 'OK')
          # Redirect to the desired page after logout with a Sweetify notification
        return render(request, 'website/index.html')

