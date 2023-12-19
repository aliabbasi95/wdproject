from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import login, logout


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})


def signin_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
        else:
            form = AuthenticationForm()
            return render(request, 'account/signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'account/signin.html', {'form': form})


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            form = UserChangeForm(instance=request.user)
            return render(request, 'account/profile.html', {'form': form})
    else:
        form = UserChangeForm(instance=request.user)
        return render(request, 'account/profile.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'account/logout.html')
