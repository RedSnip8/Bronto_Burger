from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check for a password match
    if password == password2:
        # check username is availible
        if User.objects.filter(username=username).exists():
            messages.error(request, 'That user name is already in use')
            return redirect('register')
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'That Email address is already linked to an account')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email, first_name=first_name, last_name=last_name,
                )
                auth.login(request, user)
                messages.success(request, 'Your account has been registered')
                return redirect('index')
    else:
      messages.error(request, 'Those passwords do not match')
      return redirect('register')
  else:
      return render(request, 'account/register.html')

def login(request):
    if request.method == 'POST':
        # Login User
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you have been logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'that is an invalid password/username.')
            return redirect('login')
    else:
        return render(request, 'account/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('index')
